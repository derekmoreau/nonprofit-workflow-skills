"""Check original result arithmetic, rubric inventory, and local links offline."""
from pathlib import Path
import csv
import json
import math
import re
import statistics

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ('grant-proposal', 'grant-report', 'logic-model', 'program-results', 'review-before-sending')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def compare_value(actual, expected, name):
    require(math.isclose(actual, expected, abs_tol=1e-12), name)


def verify_history(root):
    path = root / 'evals/results.json'
    old = json.loads(path.read_text())
    require(set(old['cases']) == {'sonnet', 'opus', 'sol'}, 'historical models')
    for model, cases in old['cases'].items():
        require(len(cases) == len({c['case_id'] for c in cases}) == 20, 'historical cases')
        for row in old['workflows']:
            matched = [c for c in cases if c['workflow'] in (row['workflow'], row['label'])]
            require(len(matched) == 4, 'historical workflow cases')
            delta = statistics.mean(100 * (c['skill_score'] - c['baseline_score']) for c in matched)
            compare_value(delta, row[model + '_mean_improvement_pp'], 'historical mean')
    guide = (root / 'evals/README.md').read_text()
    for row in old['workflows']:
        expected = '| ' + row['label'] + ' | ' + ' | '.join(f"{row[m + '_mean_improvement_pp']:+.1f}" for m in ('sonnet', 'opus', 'sol')) + ' |'
        require(expected in guide, 'historical table: ' + row['label'])
    means = [statistics.mean(row[m + '_mean_improvement_pp'] for row in old['workflows']) for m in ('sonnet', 'opus', 'sol')]
    overall = '| **Overall mean** | ' + ' | '.join(f'**{x:+.1f}**' for x in means) + ' |'
    require(overall in guide, 'historical overall means')
    rubric_dir = root / 'evals/rubrics'
    require({p.stem for p in rubric_dir.glob('*.csv')} == set(WORKFLOWS) | {'shared'}, 'rubric inventory')
    count = 0
    for path in rubric_dir.glob('*.csv'):
        with path.open() as handle:
            count += len(list(csv.DictReader(handle)))
    require(count == 104, '104 public rubric criteria')


def verify_files(root):
    require({p.parent.name for p in (root / 'plugin/skills').glob('*/SKILL.md')} == set(WORKFLOWS), 'five workflows')
    for path in root.rglob('*'):
        if '.git' in path.parts or '__pycache__' in path.parts:
            continue
        if path.is_symlink():
            relative = path.relative_to(root)
            allowed = {Path('.agents/skills') / name: root / 'plugin/skills' / name for name in WORKFLOWS}
            require(relative in allowed, 'unexpected symlink')
            require(path.resolve() == allowed[relative].resolve(), 'incorrect skill symlink target')
            continue
        if path.suffix == '.md':
            source = path.read_text()
            for target in re.findall(r'\]\(([^)]+)\)', source):
                if re.match(r'^[a-z]+:', target) or target.startswith('#'):
                    continue
                local = (path.parent / target.split('#')[0]).resolve()
                require(local.is_relative_to(root.resolve()) and local.exists(), 'local link: ' + str(path) + ' -> ' + target)
            if path.name == 'SKILL.md':
                for target in re.findall(r'\.\./\.\./references/[\w-]+\.md', source):
                    require((path.parent / target).exists(), 'skill reference: ' + target)


def verify(root=ROOT):
    verify_history(root)
    verify_files(root)
    print('PASS: 60 original case pairs, summary arithmetic, rubric inventory, five workflows, and local links')
    print('Limits: October comparison records are not included or checked. Historical hashes identify the original evaluated files, not V2.')


if __name__ == '__main__':
    verify()
