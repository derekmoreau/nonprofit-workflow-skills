# Grant Report artifact contract

Use this contract when office-file tools are available. It defines a bounded
first DOCX class and a fail-closed alternative; it does not promise arbitrary
Word-template round trips.

## Canonical working record

Before rendering, maintain one structured working record for:

- funder fields in their required order;
- reporting period and current-versus-cumulative scope;
- requested, awarded, budgeted, and actual amounts as distinct facts;
- values, units, populations, denominators, source locations, and calculations;
- conflicts, gaps, assumptions, disclosure audience, and staff approvals.

Use normalized canonical unit codes where the pilot defines them: `percent`,
`percentage_points`, `USD`, `people`, and `count`. Percent symbols and the words
"percent" or "percentage" are equivalent recipient renderings of `percent`;
they are not equivalent to `percentage_points`. Use uppercase ISO 4217 currency
codes. Preserve an unrecognized domain unit exactly rather than guessing a
conversion.

Give every canonical fact a normalized semantic role so equal-unit values cannot
silently trade meanings (for example, `budget` versus `actual`, or `enrolled`
versus `completed`). A case may declare a narrow set of allowed roles for one
stable required-fact key when its period and source topology make those roles
equivalent (for example, `participants` and `current_participants` when there
is one current reporting period and no cumulative comparator). Do not apply
that equivalence globally or across current/cumulative, budget/actual,
requested/awarded, source-specific actual, or percentage/percentage-point
distinctions. Deterministic checks enforce the case-level structured role and
the rendered value/unit; semantic review evaluates whether flexible recipient
prose communicates the role correctly.

Fact audience describes disclosure of the value itself. Mark a fact `recipient`
whenever its value appears in recipient-facing content, even if the staff artifact
also repeats it. Mark it `staff_only` only when the value itself is absent from the
recipient artifact. Source IDs, source locations, and provenance may remain
staff-only even when the supported value is recipient-facing.

Repair this working record when a defect is found, then regenerate and recheck
all related artifacts. Do not patch one rendered sibling while leaving the
canonical record inconsistent.

## Supported basic DOCX class

A template may be filled as DOCX in this pilot only when inspection confirms
that every named `[FIELD:F##]` placeholder occupies one complete cell in a
simple body table. Ordinary styled paragraphs, headers or footers, and page
breaks may be preserved, but placeholders in those surfaces or embedded beside
other cell text are outside this first renderer class and must fail closed.
Reopen the actual written DOCX and
verify its text, field order, tables, audience boundaries, and archive security.
Render it to PDF and page images and inspect every page. A formal evaluation
must fail preflight when that renderer dependency is unavailable.

The pilot does not support macros, ActiveX, embedded objects, external
relationships, content controls, protected regions, text boxes, tracked
changes, comments, or custom XML. If one is present, do not flatten, rewrite,
or claim to preserve the template. Create a copy-ready portal HTML package in
the same field order and identify the unsupported feature in staff-only notes.

## Required artifacts

Create exactly one recipient artifact:

- `recipient.docx` for a supported basic DOCX template; or
- self-contained `portal.html` when no template is supplied, the task is portal
  constrained, or the template is unsupported.

Also create `staff-only.html`, clearly marked **STAFF ONLY**, containing the
field-completion map, evidence notes, reconciliations, gaps, assumptions, and
approvals. Recipient output must not contain source IDs, reviewer notes,
sensitive row keys, credentials, or other staff-only material.

Staff narrative wording is not fixed. Validation compares the reopened staff
artifact with the canonical field, fact, calculation, conflict, gap,
assumption, approval, audience, and source records, rather than requiring
particular explanatory phrases.

HTML must escape source text and contain no scripts, event-handler attributes,
forms, frames, remote active content, `javascript:` or `data:` URLs, or refresh
redirects. Output paths must remain below the assigned workspace and must not
use symlinks, traversal segments, or unsafe filenames. DOCX must remain
macro-free and contain no external relationships, comments, tracked changes,
custom XML, or credential-like strings.

## Validation and failure behavior

Reopen each actual file and compare it independently with the expected field,
fact, calculation, gap, source, and audience inventory. DOCX and HTML do not
need layout parity, but each must preserve the required semantics for its
audience. A valid failing output is evaluation evidence: never auto-repair it
during a formal run, and stop later inference on a deterministic critical
failure.

Every field expected to need input must have all three aligned representations:
a canonical `needs_input` status, a visible nonempty `[NEEDS INPUT: ...]` marker
in that field's recipient text, and one nonempty staff gap record for the same
field. The wording inside the marker and staff prompt is not fixed.

The bracketed marker is canonical-protocol syntax, not the only acceptable
user-facing language in an ordinary artifact. Outside that protocol, an
equally clear actionable label such as `Action required` or `To complete` can
communicate the same workflow state. Do not require a fact to be duplicated
across fields unless each field asks for it, and do not create an unrequested
calculation merely because its operands are available.

A field may use `reported_unverified` only when it preserves every value and
source in an explicit unresolved conflict and the canonical conflict record has
the same source set with `needs_staff_review`. This is a non-gap status for a
fully disclosed but unresolved choice: it must not carry a needs-input marker or
gap record. It never substitutes for a required missing value, explanation, or
other component, which must remain `needs_input` with the aligned marker and gap.
