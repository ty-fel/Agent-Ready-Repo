"""Render each pi-mono session as a readable markdown file + build index.md."""
from pathlib import Path
import json, glob, html, re

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path.home() / ".cache/huggingface/hub/datasets--badlogicgames--pi-mono/snapshots"
OUT = ROOT / "sessions"
OUT.mkdir(exist_ok=True)

files = sorted(f for f in glob.glob(str(CACHE / "*/*.jsonl")) if not Path(f).name.startswith("manifest"))

def text_of(content):
    if isinstance(content, str): return content
    if not isinstance(content, list): return ""
    parts = []
    for x in content:
        if not isinstance(x, dict): continue
        t = x.get("type")
        if t == "text": parts.append(x.get("text",""))
        elif t == "thinking":
            th = x.get("thinking","")
            if th: parts.append(f"<thinking>\n{th}\n</thinking>")
        elif t == "tool_use":
            inp = x.get("input") or {}
            parts.append(f"[tool_use: {x.get('name')}]\n```json\n{json.dumps(inp, indent=2)[:2000]}\n```")
        elif t == "tool_result":
            r = x.get("content")
            parts.append(f"[tool_result]\n{text_of(r) if isinstance(r,list) else str(r)[:2000]}")
    return "\n\n".join(parts)

def truncate(s, n=4000):
    if s is None: return ""
    s = str(s)
    return s if len(s) <= n else s[:n] + f"\n... [truncated {len(s)-n} chars]"

def render_event(e):
    t = e.get("type")
    if t == "session":
        return f"### session start\ncwd: `{e.get('cwd','?')}`  model: `{e.get('modelId','?')}`  provider: `{e.get('provider','?')}`"
    if t == "model_change":
        return f"### model_change → `{e.get('modelId') or e.get('model') or '?'}`"
    if t == "thinking_level_change":
        return f"### thinking_level_change → `{e.get('thinkingLevel') or e.get('to') or e.get('level') or '?'}`"
    if t == "compaction":
        return f"### compaction"
    if t == "label":
        return f"### label: {e.get('label','?')}"
    if t != "message":
        return f"### {t}\n```json\n{truncate(json.dumps(e, indent=2), 800)}\n```"
    m = e.get("message") or {}
    r = m.get("role")
    if r == "user":
        return f"## 👤 user\n\n{truncate(text_of(m.get('content')))}"
    if r == "assistant":
        usage = m.get("usage") or {}
        tok = usage.get("totalTokens")
        cost = (usage.get("cost") or {}).get("total")
        meta = f"  _(model={m.get('model','?')}, tokens={tok}, cost=${cost})_" if tok else ""
        stop = m.get("stopReason")
        stop_s = f"  stop=`{stop}`" if stop else ""
        return f"## 🤖 assistant{meta}{stop_s}\n\n{truncate(text_of(m.get('content')))}"
    if r == "toolResult":
        name = m.get("toolName") or m.get("name") or "?"
        out = m.get("output") or m.get("content") or ""
        return f"### 🔧 toolResult: `{name}`\n```\n{truncate(text_of(out) if isinstance(out,list) else str(out), 3000)}\n```"
    if r == "bashExecution":
        return f"### 🐚 bash\n```\n$ {m.get('command','')}\n{truncate(m.get('output',''), 2000)}\n```  exit={m.get('exitCode')}"
    return f"### {r}\n```json\n{truncate(json.dumps(m, indent=2), 800)}\n```"

def summarize(lines, fname):
    session = next((l for l in lines if l.get("type")=="session"), {})
    msgs = [l for l in lines if l.get("type")=="message"]
    first_user = ""
    for l in msgs:
        m = l.get("message") or {}
        if m.get("role") == "user":
            first_user = text_of(m.get("content"))
            break
    total_cost = 0.0; total_tokens = 0; n_asst = 0; n_user = 0; n_tool = 0
    models = set(); stop_counts = {}
    model_changes = sum(1 for l in lines if l.get("type")=="model_change")
    think_changes = sum(1 for l in lines if l.get("type")=="thinking_level_change")
    for l in msgs:
        m = l.get("message") or {}
        r = m.get("role")
        if r == "assistant":
            n_asst += 1
            if m.get("model"): models.add(m["model"])
            u = m.get("usage") or {}
            total_tokens += u.get("totalTokens") or 0
            total_cost += (u.get("cost") or {}).get("total") or 0
            if m.get("stopReason"): stop_counts[m["stopReason"]] = stop_counts.get(m["stopReason"],0)+1
        elif r == "user": n_user += 1
        elif r in ("toolResult","bashExecution"): n_tool += 1
    ts = session.get("timestamp","") or (msgs[0].get("timestamp","") if msgs else "")
    return {
        "file": fname,
        "timestamp": ts,
        "first_user": first_user,
        "cost": total_cost, "tokens": total_tokens,
        "n_user": n_user, "n_asst": n_asst, "n_tool": n_tool,
        "models": sorted(models), "stop_counts": stop_counts,
        "model_changes": model_changes, "think_changes": think_changes,
        "session_id": session.get("id",""),
    }

summaries = []
for f in files:
    try:
        lines = [json.loads(l) for l in open(f) if l.strip()]
    except Exception as ex:
        print("skip", f, ex); continue
    s = summarize(lines, Path(f).name)
    summaries.append(s)
    out = OUT / (Path(f).stem + ".md")
    parts = [f"# {Path(f).name}",
             f"- timestamp: `{s['timestamp']}`",
             f"- session_id: `{s['session_id']}`",
             f"- models: {', '.join(s['models']) or '?'}",
             f"- turns: user={s['n_user']} assistant={s['n_asst']} tool={s['n_tool']}",
             f"- model_changes={s['model_changes']}  thinking_level_changes={s['think_changes']}",
             f"- tokens={s['tokens']:,}  cost=${s['cost']:.3f}",
             f"- stop_reasons: {s['stop_counts']}",
             "", "---", ""]
    for e in lines:
        parts.append(render_event(e))
        parts.append("")
    out.write_text("\n".join(parts))

# index.md
summaries.sort(key=lambda s: s["timestamp"])
idx = ["# pi-mono session index", "",
       f"{len(summaries)} sessions. Sorted by timestamp.", "",
       "| date | file | user | asst | tool | tokens | cost | models | first prompt |",
       "|---|---|---:|---:|---:|---:|---:|---|---|"]
for s in summaries:
    fp = (s["first_user"] or "").replace("|","\\|").replace("\n"," ")[:160]
    stem = Path(s["file"]).stem
    date = s["timestamp"][:10]
    models = ",".join(m[:18] for m in s["models"])[:40]
    idx.append(f"| {date} | [{stem[:32]}](sessions/{stem}.md) | {s['n_user']} | {s['n_asst']} | {s['n_tool']} | {s['tokens']:,} | ${s['cost']:.2f} | {models} | {fp} |")
(ROOT / "index.md").write_text("\n".join(idx))

print(f"wrote {len(summaries)} session markdowns → {OUT}")
print(f"wrote index → {ROOT/'index.md'}")
