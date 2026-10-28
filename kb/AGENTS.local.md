# Central Knowledge Base (`kb/`) — Agent Instructions

You are reading or updating `kb/` inside `civilization-2-0`.

## Rules for `kb/`

1. **Shared Canon:** All three agents (`claude`, `codex`, `agy`) read `kb/` as the canonical source of truth.
2. **Write Discipline:** Only modify files in `kb/` when the pilot explicitly instructs you to update the central knowledge base, file a new dictated transcript, or promote material from your agent studio (`../agents/<you>/`).
3. **`living-docs` in `kb/`:**
   - `THESIS.md` and files in `concepts/` are living documents: one accepted version in root, drafts with `-draft` beside them, superseded versions moved via `git mv` to `history/` (read-only).
   - `journal.md` is an append-only chronological log (`[Konuşmacı]`, `[Claude]`, `[Codex]`, `[Agy]`, `[Karar]`) and never retires.
   - `sources/transcript-*.md` are primary dictated records and never retire.
   - `bank/` (`cumle-bankasi.md`, `hikaye-bankasi.md`, `terimler.md`) holds shared building blocks indexed by ID (`A1`, `S1`, etc.). Preserve existing IDs when adding new entries.
