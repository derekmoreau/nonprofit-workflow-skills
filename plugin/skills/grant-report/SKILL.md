---
name: grant-report
description: Fill a funder's progress or final-report template from reporting-period program and financial information, citing numbers and marking gaps for staff review.
---
# Draft a Grant Report

Fill a funder's progress or final-report template using the current reporting-period packet. A template is preferred but not required: when it is absent, use a short generic structure and flag that the funder's format still needs confirmation. First use works from attached files; no setup interview is required.

Read `../../references/source-and-consent.md` and
`../../references/grant-report-artifact-contract.md` before drafting.

## Workflow

1. Read the template or instructions and make a field map with one row for every supplied field: question, order, constraint or limit, response type, requested period, required evidence, source, and status. Keep every dimension explicit even when the packet does not provide it: use `not provided`, `not applicable`, or a specific missing-input marker as appropriate rather than omitting the column or inventing a value. Do not replace field-level rows with a section range or separate partial lists. Preserve required headings and tables. Explicit destination restrictions govern each field; generic gap or placeholder guidance does not authorize extra workflow text in a contact-only, certification, numeric, or similarly constrained field.
2. Read program and financial files. Reconcile reporting period, awarded/requested amount, actual spending, people served, outputs, outcomes, and remaining balance. Keep calculations visible and label estimates. Before returning the output, compare every recipient and staff number with its source or visible derivation, including prose differences and missing counts, and confirm compatible units, populations, and periods. Generalize unnecessary person-linked row or case IDs; retain an exact key only in staff-only notes when it is needed to correct the source, label it sensitive, and ask staff to confirm its use.
   Use `actual` (or `current_actual` when current-versus-cumulative scope requires it) for an ordinary sourced actual. Reserve `actual_finance_export` for a distinct export or ledger comparator when the packet requires that source-specific role; a filename such as `financial.csv` alone does not make an actual an export comparator.
   Field status reflects whether the requested field is complete, not merely whether the included text is sourced. A multi-part financial summary remains partial when it has only an actual, requested, awarded, or budget amount but lacks a required comparison baseline, variance, or remaining-balance context. Include the sourced amount, keep the field `needs_input`, and ask for the missing component.
   Use `reported_unverified` only for a field that preserves every conflicting sourced value and source while an explicit matching conflict remains `needs_staff_review`. This status records an unresolved choice among fully disclosed values; it never replaces `needs_input` for a required missing value, explanation, or other component.
   When the requested field has multiple conflicting sourced values that are safe to disclose, show every value with a neutral source label in recipient-facing text, keep their fact audiences `recipient`, record the matching unresolved conflict, and use `reported_unverified`. Do not hide those values only in staff notes or turn the conflict itself into `needs_input`; reserve `needs_input` for information that is actually absent or an action the field still requires.
   When a requested calculation depends on conflicting values, compute and label each source-contingent result separately when its operands are supported (for example, one reported actual is `$100 over budget` while the other is `$100 under budget`). Keep the choice unresolved; do not select one result, average them, or omit both merely because staff must reconcile the inputs.
   Calculate what the funder asks for or what is needed to interpret a requested result. For every displayed rate or change, preserve its operands, denominator, unit, period, exclusions, and rounding in the working record, and show the recipient-relevant operands with the result. A single period heading may govern facts that unambiguously share one scope; label comparisons and mixed current/cumulative results locally. Do not invent a subtraction, rate, or variance merely because two operands are present. Do not repeat the same fact in multiple fields unless each field requests it; one correct realization in an appropriate field is enough.
3. Draft each field in plain language. Put registered source IDs in the staff-only appendix and track missing evidence with gap markers outside source fields. Show numerator/denominator for rates in the clean response where useful to the recipient. Separate actuals, targets, explanations, and next-period plans. Preserve qualifiers such as `staff reported`, `proposed`, `approved as of [date]`, and `current-period` wherever dropping them would strengthen or change the claim. A caution in the working record does not repair stronger recipient prose.
   Set each canonical fact's audience from the value itself: use `recipient` whenever that value appears in recipient-facing content, even when staff also sees it. Use `staff_only` only when the value itself does not appear recipient-side. Source IDs and provenance may remain staff-only for a recipient-facing value. Keep internal approval history, record-level QA or deduplication mechanics, and provisional figures whose validity or disclosure remains unresolved because of record-level QA staff-only unless the funder requests the value and the packet supports a safe, accurate recipient disclosure.
   Preserve an explicit staff-only provenance entry for every supplied source. A template, portal-instruction, consent, or release-control source that supports no recipient fact still needs a staff evidence note; do not attach it to an unrelated fact merely to make it appear. Conversely, cite every source that independently supports the exact fact rather than discarding corroboration.
4. When the award or reporting packet supplies objectives, milestones, targets, a work plan, or a budget, compare the corresponding reporting-period activities, outputs, outcomes, milestones, and spending with those commitments. Apply any supplied funder, award, or organizational variance threshold. Without one, do not invent a percentage cutoff: treat a difference as material when it could change the recipient's understanding of performance or stewardship, affects an objective or restriction, requires approval or corrective action, or threatens delivery. Disclose every variance the destination requests. For a material delay, shortfall, overperformance, financial variance, or changed condition, state the supported difference and explanation without minimizing uncertainty or assigning unsupported blame; if the reason is missing, leave one specific gap. Do not demand explanations for every small difference merely because two values differ. When learning or next steps are requested or supplied, connect each lesson or adaptation to a sourced result, challenge, or feedback item, and distinguish a completed change from a future plan. Do not invent a commitment, explanation, lesson, or adaptation to complete the narrative.
5. For a missing source that the field actually requires or that materially affects accuracy or interpretation, use a neutral recipient placeholder containing only the missing value or choice, such as `[NEEDS INPUT: reporting-period end date]`, and add the specific completion action in the staff-only appendix. Keep staff procedure—including instructions to confirm, verify, attach, upload, approve, or complete a portal step—out of recipient fields unless the destination explicitly requires that procedure as part of the substantive answer. Use `[NEEDS INPUT: ...]` when the output contract requires that exact protocol token; otherwise an equally clear neutral missing-value label is acceptable. Do not create gaps for details the destination does not request when the supported answer is already complete. A staff prompt may ask staff to add, complete, confirm, document, insert, provide, record, remove, resolve, review, or verify, and may state a necessary approval or consent prerequisite when aligned with the missing item. Use supplied negative facts directly. Do not borrow a number from an older period without labeling it and confirming relevance.
6. Check participant stories and quotations against consent and source text. Prefer a de-identified aggregate when consent or destination is unclear.

## Output

Return two clearly separated parts:

1. **Recipient-facing report:** clean response copy in the funder's template order. Do not insert source IDs or reviewer notes into clean funder prose. A visible missing-input action remains blocking until staff replaces it and rechecks the affected limit.
2. **Staff-only evidence, reconciliation, and gap appendix:** field-completion table, source notes for every number and named fact, program/finance reconciliations, missing data, assumptions, and staff approvals still needed. Source IDs and reviewer notes belong here and do not count toward funder limits.

Do not describe a report containing unresolved flags as sendable. If no office-file tools are available, preserve the template's section order in markdown and say which conversion step remains. Do not imply that a file has been filed, sent, or approved.

When office-file tools are available, first inspect the template class. Fill a
DOCX only when it is within the bounded basic class defined in the artifact
contract. Fail closed to a copy-ready portal HTML package for an absent,
portal-constrained, or unsupported template; never flatten or silently rewrite
unsupported Word features. Build both recipient and staff views from one
canonical field/fact/calculation/gap record, reopen the actual files, check
audience separation and security, and render the DOCX for visual verification
where the environment supports it. Render tabular content as actual document or
HTML tables rather than visible Markdown pipe syntax, and include that table
structure in the post-render inspection.

The staff-only appendix includes:

- a field-completion table;
- source notes beside every number and named fact;
- a reconciliation note for any program/finance mismatch;
- missing-data and assumptions sections;
- a short list of staff approvals still needed.

## Final check

- Compare every required template field with the supplied sources and instructions. The final field-completion table must have one row per field and explicit entries for question, constraint or limit, response type, requested period, required evidence, source, and status. Reopen the table and verify those dimensions field by field; use `not provided`, `not applicable`, or a specific gap instead of omitting a dimension.
- Use `needs_input` only when a blocking action is genuinely missing, and make the recipient marker and staff gap ask for the same thing.
- Apply supplied character or word limits directly; do not ask staff to reconfirm a limit already in the packet.
- Verify each requested quantitative fact or calculation appears once in an appropriate recipient field with its role, period, and unit preserved. Recalculate displayed totals from their stated components and the funder's definitions, then compare the result with every prose total, table total, balance, and variance; do not carry a subtotal forward as an all-in total when another contribution must be added.
- Scan every recipient field for staff procedure. Replace instructions to enter, confirm, provide records, upload, attach, approve, certify, or submit with only the missing recipient value or neutral placeholder, unless the funder explicitly asks for that procedure as the substantive response. Put the corresponding action, owner, evidence request, and approval dependency in the staff appendix.
- First remove source-designated staff-only or confidential content from recipient copy; never reclassify a protected source fact because a draft exposes it. Verify audience metadata from intended placement: an authorized public value or neutral recipient placeholder is `recipient`; its staff procedure, provenance, internal approval history, or protected source value remains `staff_only`.
- Check descriptions of proposed activity and reported change for causal upgrades. Preserve `staff reported`, `proposed`, and observational qualifiers; do not turn a design feature or before/after observation into a guaranteed or attributed effect.
- Keep internal approver names, roles, review/release status, and related procedure staff-only unless the destination explicitly requests that status as substantive content.

## What not to do

- Do not fabricate an actual, variance explanation, result, quote, or consent record.
- Do not turn a staff-reported explanation, before/after observation, or comparison of different populations into a causal claim.
- Do not infer authority expiry from the age of a dated record or select between conflicting approved scopes without supplied authority.
- Do not turn a denominator change into an outcome change.
- Do not omit a blank template field just because it is inconvenient; mark the gap.
- Do not put staff workflow into a recipient placeholder. Use `[NEEDS INPUT: attachment status]` recipient-side and keep `Confirm and upload the attachment` in the staff appendix.
- Do not hide a prior-period comparison or a financial reconciliation issue.
- Do not treat the presence or absence of a rubric/check as evidence about the report; determine what is applicable from the funder request, sources, and template.

## Example

In the fictional packet, fill `20 completions / 24 enrolled = 83.3%` from S3. Reconcile S7's `$12,000` budget with `$12,100` actual spending, a `$100` overage. Mark the funder award amount `[NEEDS INPUT]` because the packet does not identify it.
