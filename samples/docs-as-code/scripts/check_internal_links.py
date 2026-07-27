from pathlib import Path
import re
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
pattern = re.compile(r"\[[^]]+\]\((?!https?://|mailto:|#)([^)#]+)(?:#[^)]+)?\)")
missing = []
for page in root.rglob("*.md"):
    for target in pattern.findall(page.read_text(encoding="utf-8")):
        candidate = (page.parent / target).resolve()
        if not candidate.exists():
            missing.append(f"{page}: {target}")
if missing:
    print("Broken internal links:")
    print("\n".join(missing))
    raise SystemExit(1)
print("Internal links OK")
