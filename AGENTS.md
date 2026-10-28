# civilization-2-0 — Multi-Agent Workspace & Living Docs Contract

This repository holds the **Civilization 2.0 (Medeniyet 2.0)** thesis, central knowledge base, independent agent studios, and event talks.

Three coding/thinking agents work in this repository concurrently:
- **Claude Code** (`claude`) → owns `agents/claude/`
- **Codex** (`codex`) → owns `agents/codex/`
- **Antigravity** (`agy`) → owns `agents/agy/`

---

## 1. Repository Layout & Write-Ownership

```text
civilization-2-0/
├── AGENTS.md                  # This contract (CLAUDE.md -> AGENTS.md)
├── README.md                  # Root entry point & project map
├── kb/                        # Central Knowledge Base (shared canon & raw sources)
│   ├── README.md              # KB index
│   ├── THESIS.md              # Accepted canonical thesis (living doc)
│   ├── journal.md             # Append-only chronological log of pilot notes & decisions
│   ├── concepts/              # Canonical concept notes (living docs)
│   ├── bank/                  # Shared building blocks: cumle-bankasi.md, hikaye-bankasi.md, terimler.md
│   ├── sources/               # Raw & cleaned pilot transcripts (transcript-0..N.md) and papers
│   └── history/               # Retired canonical KB documents (read-only)
├── agents/                    # Sovereign Agent Studios (one per agent)
│   ├── claude/                # Owned by Claude Code (+ history/)
│   ├── codex/                 # Owned by Codex (+ history/)
│   └── agy/                   # Owned by Antigravity (+ history/)
└── talks/                     # Event-specific deliverables & slide decks
    └── 2026-10-30-firat/      # Fırat University talk (+ history/)
```

### Write-Ownership Rules (Preventing Collisions)

1. **Your Studio (`agents/<you>/`):**
   - You have **full read/write autonomy** inside your own studio (`agents/claude/`, `agents/codex/`, or `agents/agy/`).
   - **Never write to another agent's studio.** You may freely **read** the other two agents' studios (`agents/*/*.md`) when the pilot asks you to compare, critique, or synthesize across agents.
2. **Central Knowledge Base (`kb/`) & Talks (`talks/`):**
   - All agents **read** from `kb/` as the shared ground truth.
   - Only write or promote to `kb/` or `talks/` when the pilot explicitly asks you to (e.g., filing a new dictated transcript, adding to `kb/bank/`, promoting an exploration from `agents/<you>/` into `kb/`, or updating a talk).

---

## 2. The `living-docs` Convention (Applies Everywhere)

Every workspace in this repo (`kb/`, `agents/claude/`, `agents/codex/`, `agents/agy/`, `talks/<event>/`) follows the **`living-docs`** discipline: **the root of that workspace holds what is current; its `history/` holds what used to be.**

- **One accepted version in the workspace root.** If a document is versioned or iteratively rewritten, only the current accepted version lives in the workspace root (e.g., `THESIS.md`, `icerik.md`, `slaytlar.html`). Everything superseded moves to that workspace's `history/`.
- **A draft sits beside the accepted version, never on top of it.** Work in progress carries a `-draft` marker (e.g., `icerik-draft.md`, `protocol-essay-draft.md`) and does not displace the accepted version until the pilot accepts it. Multiple drafts may coexist in the root for diffing.
- **A current version never references an older one** — no "supersedes v4", no "what changed since", no version changelog paragraph inside the document. `history/` keeps the old version and git keeps the diff; the story of the change belongs in the commit message. Test: a reader who has never seen an earlier version notices nothing missing.
- **`history/` is read-only.** A retired document is a browsable record of what was true when written, not something to maintain. Never edit or update cross-references inside `history/`. The only edit a retired document may receive when moved is a single line near the top: `> Retired YYYY-MM-DD — superseded by <name>.`
- **Retire, never delete.** Use `git mv <path> <workspace>/history/<name>` so git tracks the rename. Repoint live indexes (`README.md`) so nothing current points into `history/` by accident.
- **Append-only records never retire:** `kb/journal.md` and raw source transcripts in `kb/sources/` are historical records, not living design docs; they are appended to and never retired.

---

## 3. Working Rules

- **Only use the source the pilot names:** When the pilot asks to build an artifact or draft from a specific file (e.g., `kb/sources/transcript-1.md`), use *only* that file's content. Keep extra ideas or cross-references as separate suggestions in your chat reply, not blended into the deliverable.
- **Ground claims in sources:** Every claim about external research, quotes, or statistics needs a source. Mark unverified claims as `Doğrula` / `unverified`.
- **No machine paths or secrets in commits:** Follow `~/DEV/AGENTS.md` — never commit secrets, tokens, or local home paths (`/Users/...`) into files or commit messages. Use repo-relative paths.
