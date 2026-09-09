"""Offline consistency check. No model calls or external dependencies."""
from pathlib import Path
import hashlib,json,math,statistics,re
root=Path(__file__).resolve().parents[1]
d=json.loads((root/'evals/results.json').read_text())
for model,cases in d['cases'].items():
 assert len(cases)==20 and len({c['case_id'] for c in cases})==20
 for row in d['workflows']:
  matched=[c for c in cases if c['workflow'] in (row['workflow'],row['label'])]
  assert len(matched)==4,(model,row['workflow'])
  delta=statistics.mean(100*(c['skill_score']-c['baseline_score']) for c in matched)
  assert math.isclose(delta,row[model+'_mean_improvement_pp'],abs_tol=1e-9),(model,delta,row)
for relative,digest in d['evaluated_files'].items():
 assert hashlib.sha256((root/'plugin'/relative).read_bytes()).hexdigest()==digest,relative
for skill in (root/'plugin/skills').glob('*/SKILL.md'):
 for rel in re.findall(r'\.\./\.\./references/[\w-]+\.md',skill.read_text()):
  assert (skill.parent/rel).exists(),rel
readme=(root/'README.md').read_text()
for row in d['workflows']:
 expected='| '+row['label']+' | '+' | '.join(f"{row[m+'_mean_improvement_pp']:+.1f}" for m in ['sonnet','opus','sol'])+' |'
 assert expected in readme,expected
assert not any(p.is_symlink() for p in root.rglob('*') if '.git' not in p.parts)
print('PASS: 60 case pairs, summary arithmetic, README rows, unchanged evaluated skill/reference identities and reference paths')
