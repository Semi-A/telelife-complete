# Handover guide — read before writing any code

You are continuing an existing project. Follow the plan; do not restart it.

## Read first, in this order
1. `TeleLife_Master_Plan.md` — product definition, stack, phase map
2. `docs/PHASE_1.md` and `docs/PHASE_2.md` — what already exists
3. `docs/CONVENTIONS.md` — non-negotiable rules

## Hard rules from the project owner
- Never remove an existing requirement without asking.
- Never redesign the architecture without asking.
- Never add a major feature without asking.
- Never overengineer. Simpler beats clever.
- If you have a better idea, present it in exactly this format and WAIT for approval:
  current solution / suggested solution / advantages / disadvantages /
  performance impact / scalability impact / security impact / approval required.

## Priority order for trade-offs
Optimization > Scalability > Security > Economy balance > Performance >
Maintainability > UX > Clean architecture.

## Where things go