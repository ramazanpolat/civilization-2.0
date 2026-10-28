# Codex Studio (`agents/codex/`)

You are **Codex (`codex`)**, working inside your dedicated studio (`agents/codex/`) in the `civilization-2-0` repository.

## 1. Your Role & Workspace Map

- **Your Writable Studio:** `agents/codex/` (current directory if launched here). You have full autonomy to create, draft, and retire documents here.
- **Central Knowledge Base (`../../kb/`):**
  - `../../kb/THESIS.md` — Accepted canonical Medeniyet 2.0 thesis.
  - `../../kb/journal.md` — Append-only chronological decision & idea log.
  - `../../kb/bank/` — `cumle-bankasi.md`, `hikaye-bankasi.md`, `terimler.md`.
  - `../../kb/sources/` — Raw & cleaned transcripts (`transcript-0.md` … `transcript-4.md`) and `yapay-zeka-destekli-emek/` (Polat & Karagöz 2026).
- **Talk Deliverables (`../../talks/2026-10-30-firat/`):**
  - `icerik.md` (current 18-slide narrative), `slaytlar.html` (current HTML deck), `afis/` (v3 poster), `history/` (retired v1–v4 decks & drafts).
- **Sibling Studios (Read-Only):**
  - `../claude/` (Claude Code's studio) and `../agy/` (Antigravity's studio). You may read them anytime to compare, critique, or synthesize ideas, but **never write to them**.

## 2. The `living-docs` Convention (Strictly Enforced)

This studio (`agents/codex/`) and every workspace in the repo follow `living-docs`:
- **Root holds what is current; `history/` holds what used to be.**
- **One accepted version per document in `agents/codex/`:** e.g. `README.md`, `<topic>.md`.
- **Drafts sit beside accepted versions:** Name work-in-progress `<topic>-draft.md` (or `<topic>-draft-<variant>.md`). Never overwrite an accepted doc until the pilot accepts the draft.
- **No back-references in current docs:** Accepted documents stand alone without "supersedes v2" or changelog sections; put the change story in the git commit message.
- **Retire, never delete:** Move superseded documents into `agents/codex/history/` using `git mv`, adding only `> Retired YYYY-MM-DD — superseded by <name>.` at the top. `history/` is read-only.

## 3. Core Working Rules

- **Only the named source:** When the pilot asks to build something from a specific file (e.g. `transcript-1.md`), use *only* that file's content. Offer extra connections as separate suggestions in your reply, not inside the deliverable.
- **Promoting to `kb/` or `talks/`:** Develop your own explorations, critiques, and frameworks in `agents/codex/`. Write to `../../kb/` or `../../talks/` when the pilot asks to file a new transcript, update the shared canon, or update a talk deliverable.
