"""Recon: parse pi-mono JSONL files directly; print schema + aggregate stats."""
from collections import Counter
from pathlib import Path
import json, glob

CACHE = Path.home() / ".cache/huggingface/hub/datasets--badlogicgames--pi-mono/snapshots"
files = sorted(glob.glob(str(CACHE / "*/*.jsonl")))
print(f"found {len(files)} session files")

type_c, role_c, model_c, tool_c = Counter(), Counter(), Counter(), Counter()
cwds = Counter()
stop_reasons = Counter()
lengths, user_turns, assistant_turns = [], [], []
first_user = []  # (file, text)
all_tool_names = Counter()
cost_total = 0.0
token_total = 0
thinking_levels = Counter()
providers = Counter()

for f in files:
    try:
        lines = [json.loads(l) for l in open(f) if l.strip()]
    except Exception as e:
        print("skip", f, e); continue
    lengths.append(len(lines))
    u = a = 0
    user_text_captured = False
    for e in lines:
        t = e.get("type"); type_c[t] += 1
        if t == "session":
            cwds[e.get("cwd","?")] += 1
            if e.get("provider"): providers[e["provider"]] += 1
            if e.get("modelId"): model_c[e["modelId"]] += 1
            if e.get("thinkingLevel"): thinking_levels[e["thinkingLevel"]] += 1
        elif t == "model_change":
            model_c[e.get("modelId") or e.get("model") or "?"] += 1
        elif t == "thinking_level_change":
            thinking_levels[e.get("to") or e.get("level") or "?"] += 1
        elif t == "message":
            m = e.get("message") or {}
            r = m.get("role"); role_c[r] += 1
            if r == "user":
                u += 1
                if not user_text_captured:
                    c = m.get("content")
                    txt = ""
                    if isinstance(c, list):
                        txt = " ".join(x.get("text","") for x in c if isinstance(x,dict) and x.get("type")=="text")
                    elif isinstance(c, str):
                        txt = c
                    first_user.append((Path(f).name, txt[:200].replace("\n"," ")))
                    user_text_captured = True
            elif r == "assistant":
                a += 1
                if m.get("usage"):
                    token_total += m["usage"].get("totalTokens") or 0
                    cst = m["usage"].get("cost") or {}
                    if isinstance(cst, dict):
                        cost_total += cst.get("total") or 0
                if m.get("stopReason"): stop_reasons[m["stopReason"]] += 1
                # scan content for tool_use
                c = m.get("content") or []
                if isinstance(c, list):
                    for x in c:
                        if isinstance(x, dict) and x.get("type") == "tool_use":
                            all_tool_names[x.get("name","?")] += 1
            elif r == "toolResult":
                tool_c[m.get("toolName") or m.get("name") or "?"] += 1
            elif r == "bashExecution":
                tool_c["bash"] += 1
    user_turns.append(u); assistant_turns.append(a)

print(f"\nsessions: {len(files)}")
print(f"events/session: min={min(lengths)} max={max(lengths)} mean={sum(lengths)/len(lengths):.0f}")
print(f"user turns/session mean: {sum(user_turns)/len(user_turns):.1f}  max={max(user_turns)}")
print(f"assistant turns/session mean: {sum(assistant_turns)/len(assistant_turns):.1f}  max={max(assistant_turns)}")
print(f"total tokens (all sessions, approx): {token_total:,}")
print(f"total cost (USD, approx): ${cost_total:.2f}")

def show(name, c, n=15):
    print(f"\n{name}:")
    for k,v in c.most_common(n): print(f"  {v:>6}  {k}")

show("event types", type_c)
show("roles", role_c)
show("models", model_c)
show("providers", providers)
show("thinking levels", thinking_levels)
show("stop reasons", stop_reasons)
show("tool_use names (assistant)", all_tool_names, 25)
show("toolResult names", tool_c, 15)
show("cwds", cwds, 20)

print("\nfirst user messages (10 random-ish):")
import random; random.seed(0); random.shuffle(first_user)
for fn, txt in first_user[:15]:
    print(f"  [{fn[:30]}] {txt}")
