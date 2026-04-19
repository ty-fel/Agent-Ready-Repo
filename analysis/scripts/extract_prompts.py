"""Cluster first-user-messages into reusable prompt templates.

Strategy: take the first user message of every session, strip URLs / issue numbers /
trailing commentary, hash the prefix (first ~400 chars of normalized text) and
group sessions by that hash. Any cluster with >=3 sessions is a probable template.
Write the longest example per cluster to analysis/artifacts/prompts/.
"""
from pathlib import Path
from collections import defaultdict
import json, glob, re, hashlib

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path.home() / ".cache/huggingface/hub/datasets--badlogicgames--pi-mono/snapshots"
OUT = ROOT / "artifacts" / "prompts"
OUT.mkdir(parents=True, exist_ok=True)

files = sorted(f for f in glob.glob(str(CACHE / "*/*.jsonl")) if not Path(f).name.startswith("manifest"))

def first_user_text(lines):
    for l in lines:
        if l.get("type") != "message": continue
        m = l.get("message") or {}
        if m.get("role") != "user": continue
        c = m.get("content")
        if isinstance(c, list):
            return " ".join(x.get("text","") for x in c if isinstance(x,dict) and x.get("type")=="text")
        if isinstance(c, str): return c
    return ""

def normalize(t):
    t = re.sub(r"https?://\S+", "<URL>", t)
    t = re.sub(r"#\d+", "<NUM>", t)
    t = re.sub(r"\b\d{2,}\b", "<N>", t)
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t

clusters = defaultdict(list)  # key -> list[(file, original_text)]
for f in files:
    try:
        lines = [json.loads(l) for l in open(f) if l.strip()]
    except Exception: continue
    t = first_user_text(lines)
    if not t or len(t) < 40:  # ignore "hi", "/load", tiny prompts
        continue
    key = normalize(t)[:400]
    h = hashlib.sha1(key.encode()).hexdigest()[:10]
    clusters[h].append((Path(f).name, t))

# sort clusters by size
ranked = sorted(clusters.items(), key=lambda kv: -len(kv[1]))

index = ["# Extracted prompt templates from pi-mono",
         "",
         "Clusters of first-user-messages that recur across sessions. `n` = number of sessions using this template.",
         "",
         "| n | template | file |",
         "|---:|---|---|"]

n_written = 0
for h, items in ranked:
    if len(items) < 3:
        continue
    # pick longest example as canonical
    longest = max(items, key=lambda x: len(x[1]))
    preview = re.sub(r"\s+", " ", longest[1])[:120]
    out_path = OUT / f"{h}_n{len(items)}.md"
    body = [f"# Template (n={len(items)} sessions)", "",
            "## Canonical example", "", "```",
            longest[1].strip(), "```", "",
            "## Sessions using this template", ""]
    for fn, _ in items[:50]:
        body.append(f"- `{fn}`")
    if len(items) > 50:
        body.append(f"- ... and {len(items)-50} more")
    out_path.write_text("\n".join(body))
    index.append(f"| {len(items)} | {preview} | [{h}](artifacts/prompts/{out_path.name}) |")
    n_written += 1

(ROOT / "prompt_templates.md").write_text("\n".join(index))
print(f"wrote {n_written} template files → {OUT}")
print(f"wrote summary → {ROOT/'prompt_templates.md'}")

# also count singletons vs clustered
total = sum(len(v) for v in clusters.values())
clustered = sum(len(v) for k,v in clusters.items() if len(v) >= 3)
print(f"sessions with a non-trivial first prompt: {total}")
print(f"of those, {clustered} ({100*clustered/total:.0f}%) fall into recurring templates (n>=3)")
