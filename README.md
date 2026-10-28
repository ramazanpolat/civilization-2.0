# Medeniyet 2.0 (Civilization 2.0)

> Görüntülü arama bayramlaşmamızı nasıl değiştirdiyse, yapay zekâ da hayatımıza yeterince yerleştiğinde yaşam şeklimizi değiştirecek. Ajanlara, insan olmadıklarını bilerek ama insanmış gibi davrandığımız o noktaya ben **Medeniyet 2.0** diyorum.

Bu depo, **Medeniyet 2.0** tezini, merkezi bilgi tabanını (`kb/`), üç ayrı yapay zekâ ajanının (`claude`, `codex`, `agy`) bağımsız çalışma alanlarını (`agents/`) ve söyleşi/sunum çıktılarını (`talks/`) barındırır.

---

## Dizin Haritası

| Alan | Yol | Açıklama |
|---|---|---|
| **Merkezi Bilgi Tabanı** | [`kb/`](kb/README.md) | Ortak kanon: [`THESIS.md`](kb/THESIS.md), [`journal.md`](kb/journal.md), cümle/hikâye/terim bankası ([`kb/bank/`](kb/bank/)) ve birincil kaynaklar ([`kb/sources/`](kb/sources/)). |
| **Ajan Stüdyoları** | [`agents/claude/`](agents/claude/README.md) | Claude Code'un bağımsız `living-docs` çalışma alanı. |
| | [`agents/codex/`](agents/codex/README.md) | Codex'in bağımsız `living-docs` çalışma alanı. |
| | [`agents/agy/`](agents/agy/README.md) | Antigravity'nin bağımsız `living-docs` çalışma alanı. |
| **Söyleşiler & Sunumlar** | [`talks/2026-10-30-firat/`](talks/2026-10-30-firat/README.md) | 30 Ekim 2026 Fırat Üniversitesi söyleşisi: güncel sunum ([`slaytlar.html`](talks/2026-10-30-firat/slaytlar.html)), anlatım ([`icerik.md`](talks/2026-10-30-firat/icerik.md)) ve afiş ([`afis/`](talks/2026-10-30-firat/afis/)). |

---

## Çalışma Düzeni (`living-docs`)

Her alt alan (`kb/`, `agents/*/`, `talks/*/`) **`living-docs`** kuralına uyar:
- **Kök dizin yalnızca güncel olanı tutar:** Kabul edilmiş tek güncel sürüm kök dizinde yaşar; taslaklar `-draft` ekiyle yanında durur.
- **`history/` geçmişi tutar (salt okunur):** Yürürlükten kalkan sürümler silinmez, ilgili alanın `history/` klasörüne taşınır.
- Ayrıntılı kurallar için bkz. [`AGENTS.md`](AGENTS.md).
