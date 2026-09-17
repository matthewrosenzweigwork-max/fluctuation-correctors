#!/usr/bin/env python3
from pathlib import Path
import argparse
import datetime
import shutil

p = argparse.ArgumentParser()
p.add_argument("number", type=int)
args = p.parse_args()
root = Path(__file__).resolve().parents[1]
template = root / "TEMPLATES/ROUND_REPORT.md"
out = root / "REPORTS/ROUND_REPORTS" / f"ROUND_{args.number:03d}.md"
if out.exists():
    raise SystemExit(f"Refusing to overwrite {out}")
out.parent.mkdir(parents=True, exist_ok=True)
text = template.read_text(encoding="utf-8")
text = text.replace("Round XXX", f"Round {args.number:03d}", 1)
text = text.replace("- Date:", f"- Date: {datetime.date.today().isoformat()}", 1)
out.write_text(text, encoding="utf-8")
print(out)
