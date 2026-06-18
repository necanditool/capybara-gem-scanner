# 💎 Capybara Gem Scanner — Community Edition (v41)

**Deutsch unten / German below.**

## New in v41 — lower CPU usage
- **Auto-scan (gems & skills) now uses far less CPU.** Text recognition (OCR) previously
  used **all** CPU cores per scan, briefly spiking the CPU to ~100%. It is now capped to a
  few cores, so the spike drops drastically (in one test from 30+% down to under 10%) — at
  practically the same recognition speed. The screen grabber is also reused instead of being
  recreated on every check (lower idle load).

## New in v40 — gem recognition fix
- **"DMG vs guarded/shielded targets" is now recognized.** The real in-game wording ("Schaden
  gegen geschützte Ziele") was added — previously only "Ziele mit Schild" was known, so it showed
  "gem unclear".

## New in v39 — window / layout fix
- The **Slot tab is now scrollable** — "Selected gem (candidate)" and "Best for slot" are no
  longer cut off (all tabs scroll now).
- The **window height adapts to your screen height** (leaves room for the taskbar), with a smaller
  minimum size so it fits smaller screens too.

## New in v38 — auto-scan CPU optimization
- Auto-scan (Slot & Skills) now triggers OCR **only on a significant AND settled change**
  (threshold-based image diff instead of an exact hash). Sparkles/animations no longer trigger a
  scan → **drastically lower CPU usage**. It also waits until the image is stable (not mid-fade)
  before scanning.

## New in v37 — translation + multi-monitor
- **Build names are now translated in English mode** (Bogen→Bow, Schwert→Sword, Blitz-Stab→
  Lightning staff, …). The internal key stays the same, so ratings are unaffected.
- **The region selector now spans ALL monitors** (the whole virtual desktop), so you can mark
  regions on monitor 1–4 (e.g. BlueStacks on a second screen). Capture already works across
  monitors. *(Note: fully markerless auto-detection of the game's inner areas isn't reliable —
  you mark each area once, then it works.)*

## New in v36 — gem auto-scan
- **Slot tab now has "🔁 Auto-scan"** too: it watches region 1 (Equipped, right) and region 2
  (Selection, left) and **compares automatically as soon as you view a gem in-game** — no click
  needed. It only re-scans when the image changes (light on the CPU).

## New in v35 — skill names translated in English mode
- In English mode, **skill names now show in English**: more skills are curated (with DE+EN names)
  and are recognized even with glued OCR (blob search runs first — no more German duplicates).
- For unknown skills, the name gets a rough DE→EN word translation.

## New in v34 — skill run-tracking, synergy & fixes
- **Dagger skills (e.g. Rage Dagger / "Wutdolch") now count as dagger skills** → strong in
  dagger builds (Whisperer). **Poison skills only matter in poison/DoT builds** (avoid otherwise).
- **"🎒 Your run":** remember the skills you picked (the **"+ run"** button) — also ones other than
  the suggestion — with **synergy detection** (e.g. Combo Dagger + Rage Dagger).
- **"🗑 New run"** resets the run (press it when a run ends).

## New in v33 — skill auto-scan
- In the Skills tab: **"🔁 Auto-scan"** — after you mark the region once, the tool watches it
  itself and **detects automatically as soon as the skill choice appears** (no click needed).
  It only runs OCR when the image actually changes, so it stays light on the CPU.

## New in v32 — Skill advisor (big update)
- **New "🧠 Skills" tab:** mark the offered skills (on level-up / skill choice) and the tool
  tells you, **per build**, which to **LEARN** and which to **AVOID** (the "Skill doctor").
- Own database `skills.json` (45 skills, tier S+…D — sources: allclash, meowdb, game-vault) plus
  keyword understanding for unknown skills.
- Build-dependent: e.g. **"Multiple Bolt" = LEARN on Nashir, AVOID on Whisperer**.

## New in v31 — dark mode without pink
- The **dark mode now matches the Capybara image**: a night-sky navy with **sky-blue buttons**,
  gold (crown), turquoise (crystal) and grass-green accents — **no more pink**.

## New in v30 — light / dark toggle
- New **🌙 / ☀️ button** in the header switches between the **light** Capybara-image theme and a
  **dark** gem theme (pink/turquoise). Your choice is remembered.
- Badge/button text now auto-picks light or dark for best contrast in either theme.

## New in v29 — Capybara image theme
- The **Capybara king artwork is now the header banner** (`capybara_banner.png`).
- The **entire UI was recolored to the image's palette**: light sky-blue background, white cards,
  dark-brown text, with gold / crystal-cyan / grass-green accents.
- Tier colors and all badges/buttons were adapted to the light theme for readability.
- To use your own art, replace `capybara_banner.png` in the tool folder.

## New in v28 — Capybara banner + detection fixes
- **Capybara banner:** drop a `capybara_banner.png` into the tool folder and it becomes the
  header banner (your own Capybara artwork). Without a file, a generated pink/turquoise gradient
  banner is shown. (A full see-through window background isn't possible in Tkinter, so the look
  is delivered as a hero banner up top.)
- **Crit / counter / combo "% of max HP" gems** are now detected reliably (100%) from the real
  German wording ("Bei einem kritischen Treffer … der maximalen HP des Ziels"), with no more
  cross-confusion between them.
- **final_dmg greedy fix:** the too-short keyword "endschaden" was matching foreign texts
  ("…zusätzlichen Schaden…") at 90% and stealing them — removed. "Endschadensbonus" / "Finaler
  Schaden" still detected reliably.

## New in v27 — sharpness, gem colors, hero comparison
- **Crisp UI:** the app is now DPI-aware, so Windows no longer bitmap-upscales it into a blur.
  Fonts are tied to the real screen DPI (sharp and correctly sized).
- **Gem colors:** pink + turquoise (like the in-game gems) on a dark base.
- **Hero page = multi-scan + comparison:** set the region once (the whole game screen is fine),
  then scan 2 equipped + up to 4 reserve heroes. The tool compares rank + build suitability and
  recommends swaps.

## New in v26 — detection fixes + Capybara look
- **No more false "already equipped":** the **selected gem's own attribute** (the detail card,
  everything after "Gem Attribute") never counts as equipped — so the candidate is no longer
  reported as "already slotted". If region 1 accidentally captures the selection card, the tool
  now **warns you** to drag region 1 onto the effect boxes.
- **"Waffe" no longer misread as "Weapon Crit":** short slot labels (Waffe/Ring/…) are filtered,
  and **"Global ATK" is detected reliably again** (a stray noise filter was eating "Globaler").
- **New warm Capybara hot-spring theme** (colors & accents).

## New in v25 — Build doctor in the Quick Scan
- The ⚡ Quick Scan now opens with a clear **🩺 Build doctor** verdict: **✅ keep / ❌ swap**
  for your selected build, every weak gem listed with the reason, plus **💡 Best for this
  build:** the highest-rated gems to aim for. One scan → you immediately see what to change.

## New in v24 — every build now truly understands good vs bad
- **Element/type gems are build-aware now.** Lightning, Fire, Explosion, Normal-attack and
  Physical damage are separate categories from plain "global ATK". So **Lightning DMG is only
  good on Nashir** (the lightning build) and shows **tier D for Whisperer/Skysplitter/etc.** —
  no more "lightning is worth it" on a dagger build.
- **All 8 builds re-tuned (prefs):** dagger/crit high on Whisperer, rage/sword-chi on
  Skysplitter, lightning on Nashir, counter/survival on Mushroom, and so on. (Previously e.g.
  Whisperer had only a single adjustment, so most off-build gems were over-rated.)

## New in v23 (detection fixes from real game text)
- **"Normal attack: X% chance for 2× DMG" is no longer misread as "Normal ATK DMG Boost".**
  The boost gem's greedy bare keyword ("normalangriff") was removed, so the double-damage
  gem is now identified correctly.
- **"When casting a skill … ignore DMG reduction" is now detected** even when the effect text
  is cut off or glued together in the scan (added the real German lead-in phrase).
- More robust against split/glued OCR lines in general (real German phrases added).

## New in v22
- **Huge database expansion:** +58 new gem effects (now **122**, up from 64), pulled from
  the **complete meowdb gem list** (986 gems → 199 effect families, June 2026). New entries
  include **DMG vs Boss**, **Speed**, **DMG to shielded targets**, **instant skill pick on
  stage entry**, elemental boosts/reductions (Fire/Lightning/Explosion/…), **Combo/Counter/
  Burn coefficients**, crit-rate variants (Weapon/Dagger/Sword-Qi/Lightning/DoT),
  **first-turn FDR**, damage reflect, **pet anti-crit (PvP)**, and many more — for all 4 slots.
- **Sharper matching — no more "wrong cousin":** when two gems tie on score, the **more
  specific** one wins (longer phrase). E.g. "Sword-Qi Crit Rate" is no longer read as
  "Sword-Qi Coefficient", "First-turn FDR" not as plain "FDR".
- **Tier-aligned values:** scores were cross-checked against meowdb's PvE/PvP tiers
  (SS=100, S=92, A=80, B=62, C=46, D=28, F=12); a few stale values (Global DEF/HP) were fixed.

## New in v21
- **No more "wrong gem" mix-ups:** gems that share a common ending (e.g. "…damage") no longer
  fuzzy-match the wrong gem. A gem is only accepted if its distinctive word (e.g. crit vs
  lightning vs counter) actually appears in the text. Fixes cases like
  "Lightning Damage Boost" being read as "Crit Damage".
- **New gem:** Lightning Damage Boost.

## New in v20
- **Slot tab detects ALL equipped gems** now — it is no longer limited by a number, so every
  equipped gem in the column is read and the candidate is compared against the **weakest of all**
  of them. The "free slots" field now means **empty slots** (default 0); raise it only if the
  item has an empty slot (then it suggests "just embed"). A stricter match threshold removes
  false hits where an unknown gem fuzzy-matched the wrong one.

## New in v19
- **Quick Scan catches more gems:** when the OCR glues two effect boxes into one line, a
  database gem could slip through. A new whole-text search now finds every database gem
  present even if the line split is off, and duplicate entries are merged by name.
  (A gem that is genuinely not in the database yet still needs to be added — report its text.)

## New in v18
- **New gem recognized:** "Counter bonus damage (% of target max HP, capped)".

## New in v17
- **New gem recognized:** "DoT Duration +1 / DoT Damage +X%" (burn/poison damage over time).

## New in v16
- **Quick Scan now explains each gem:** under every result it shows a short reason —
  whether it fits your build (top pick / strong / solid / weak) plus the curated note
  (e.g. "weak for this build — good for basic-attack builds"). So you see *why* a gem
  ranks where it does.

## New in v15
- **Database values are locked locally:** the in-app "Teach gem" button was removed.
  Values can only change through the 🔄 **Online update** button, so they stay curated and
  consistent and can't be altered (by mistake or on purpose) on your PC. Unknown gems still
  get the read-only ≈ guess on screen, and you can report them for the next update.

## New in v14
- **Details panel fully bilingual:** in English mode all of the tool's own text in the
  "Details (detected text)" panel is English now (labels, quotes, "(empty)"). The long
  German lines you may still see there are the **raw text read from the game** (your game
  is set to German) — that is data, not the tool's language, and must stay as-is for matching.

## New in v13
- **Online update button (top, 🔄):** point it at a hosted `gems.json` (and optionally
  `builds.json`) — e.g. a GitHub raw URL, a Gist, or your own NAS — and pull the newest
  database without reinstalling. The old file is backed up as `.bak`, the new one is
  validated and loaded live. URLs are remembered.
- **Cleaner interface:** more spacing and clearer, slightly larger text.

## New in v12
- **Light Spear coefficient correctly de-valued:** it's a dead stat for every build that
  doesn't actually cast light spears (all current builds), so it's no longer wrongly
  recommended over real damage gems.

Reads your equipped + selected gems from the screen (e.g. BlueStacks) and tells you
whether a gem is worth it **for the build you choose**. 8 build guides, German/English,
a curated gem database (updated via the online button), and a loadout analyzer.

> Values are **community estimates** (NiaMeowDB May 2026, game-vault wiki, meowdb gem
> list, MrGuider, Theria), not official game numbers.

## New in v11
- **More gems in the database:** Counter Damage Boost, Lightning-paralysis (burning target),
  battle-start shield, heal-per-round, combo coefficient on armor, plus fixes so
  "Counter damage" is no longer misread as "Final Damage" and ">70% HP" is understood.

## New in v10
- **Quick Scan tab (⚡):** one button, one region — reads **all** gems in the area,
  rates each for your build and shows a sorted list (best → weakest) with ✅/⚠️.
  No slot picking, no two-region drawing.
- **Hero tab (🦸):** mark a hero detail page — reads the rank (Legendary / Mythic+N),
  the three raw bonuses (HP/ATK/DEF) and checks the effect-text keywords (basic attack /
  combo / skill / shield / counter / crit) against your chosen build. Reminder: all heroes
  give the **same three bonuses**; only the rank scales them, so hero choice is about
  effect synergy, not just rank.

## New in v9
- **All 8 official weapon builds aligned** to the NiaMeowDB guides, each with a direct source link (Whisperer/Elres, Skysplitter/Ailoren, Helos/BoJ, Angel Bow/St. Mung, Nashir/Reaper, Durian/Seles, Star Staff, Mushroom Hammer).
- New gem **Sword Chi Coefficient** + per-build scoring (e.g. high for Skysplitter, rage-coefficient correctly de-valued for Nashir).

## New in v8
- **Loadout = full character analysis** (scrollable): equipment is scanned per slot; Heroes, Brands, Collection, Pets, Mounts, Inheritance & Adventurer show build-specific PvE/PvP recommendations to compare with your game (icons can't be reliably scanned).

## New in v7
- **Build switcher** (top of window): Whisperer/Elres, Skysplitter/Ailoren, Angel Bow,
  Mushroom-Hammer counter, Durian/Seles, Nashirs/Helos, Warrior's Sword, general rules.
  Switching the build re-rates every gem (e.g. rage coefficients rank higher for
  Skysplitter, dagger gems for Whisperer).
- Understands gems even when OCR splits words (e.g. "Koeffizie nt").
- Many more gems + correct German terms (Endschadensbonus, Globale Verteidigung,
  Lichtspeer-Koeffizient, Normalschaden-Verstärkung, pet healing, "über/mehr als 70% HP").

## Start (one click)
1. Keep all files in **one folder**: `Edelstein-Scanner starten.bat`,
   `capybara_gem_scanner.py`, `gems.json`, `builds.json`.
2. Double-click **`Edelstein-Scanner starten.bat`**. First run installs everything
   automatically. If Python was just installed, double-click the .bat **once more**.

## Use it
1. Top-right **DE ⇄ EN** toggles language. Below the tabs, pick your **Build**.
2. **Scanner tab:** pick **PvE/PvP**, the **slot** and the number of **free slots**.
3. Set the two regions once: **1) Equipped** = the right column of gem effects in-game;
   **2) Selection** = the left info panel (include the 'Attribute' line). The
   **"captured: …"** preview shows what was read.
4. Select a gem in-game, press **Scan & compare** → clear verdict (✅/❌/embed),
   rated for your chosen build.
5. **Loadout tab:** analyzes all 4 scanned slots with tips for the chosen build.
   **Build Guide tab:** full spec of the selected build.

## The gem database
The database (`gems.json`) is **curated and updated through the 🔄 Online update button**,
so the values stay consistent and can't be falsified locally. Unknown gems are still
understood from keywords on screen (marked ≈).

If a gem is detected wrong or missing, turn on **🔍 show details**, copy the text, and
report it so it can be added centrally and shipped to everyone via the next update.

## ⚠️ Antivirus (false positive)
Some antivirus tools may flag this program. **This is a false positive — it is not malware.**
Two harmless behaviours trigger the heuristic warning:
- it **takes screenshots** (that's how it reads the gems off the screen), and
- the launcher (`.bat`) **auto-installs Python packages** on the first run.

**No data is sent anywhere.** Everything runs locally; only the optional 🔄 online update
downloads from a URL **you** type in yourself. The source code (`capybara_gem_scanner.py`) is
open and readable — you can inspect every line.

**Fix:** add the tool's folder as an exclusion / whitelist. In **Windows Defender**:
*Virus & threat protection → Manage settings → Exclusions → Add an exclusion → Folder*, then
pick this folder. (Or, after a block, open *Protection history* and choose **Allow on device**.)

## ⚖️ Disclaimer
**Unofficial fan tool.** Not affiliated with, endorsed by, or connected to the makers of
"Capybara Go"; all game names, logos and trademarks belong to their respective owners. The tool
only **reads your screen and gives advice** — it does not modify the game, automate input, or
access game memory/network. Using third-party tools with a game may be subject to the game's
Terms of Service, so **use it at your own risk**. All values are **community estimates**, not
official data. The software is provided **"as is", without warranty** (see `LICENSE.txt`).
Bundled open-source components: see `THIRD-PARTY-LICENSES.txt`. Full text: `DISCLAIMER.txt`.

---

# 💎 Capybara Gem Scanner — Community Edition (v41)  [Deutsch]

## Neu in v41 — weniger CPU-Last
- **Der Auto-Scan (Edelsteine & Skills) braucht jetzt deutlich weniger CPU.** Die
  Texterkennung (OCR) nutzte bisher **alle** Prozessorkerne pro Scan und ließ die CPU kurz
  auf ~100% springen. Jetzt ist sie auf wenige Kerne begrenzt – der Ausschlag fällt drastisch
  (in einem Test von 30+% auf unter 10%), bei praktisch gleicher Erkennungsgeschwindigkeit.
  Zusätzlich wird der Screenshot-Greifer wiederverwendet statt bei jeder Prüfung neu erzeugt
  (weniger Grundlast).

## Neu in v40 — Stein-Erkennung-Fix
- **„Schaden gegen geschützte Ziele" wird jetzt erkannt.** Die echte Spielformulierung wurde
  ergänzt – vorher kannte das Tool nur „Ziele mit Schild", daher kam „Stein unklar".

## Neu in v39 — Fenster-/Layout-Fix
- Der **Slot-Tab ist jetzt scrollbar** – „Angewählter Stein (Kandidat)" und „Ideal" werden
  nicht mehr abgeschnitten (alle Tabs scrollen jetzt).
- Die **Fensterhöhe passt sich an deine Bildschirmhöhe an** (Taskleiste bleibt frei), mit
  kleinerer Mindestgröße, damit es auch auf kleineren Bildschirmen passt.

## Neu in v38 — Auto-Scan CPU-Optimierung
- Der Auto-Scan (Slot & Skills) startet OCR jetzt **nur bei deutlicher UND ruhiger Änderung**
  (Schwellenwert-Differenz statt exaktem Hash). Glitzern/Animationen lösen **keinen** Scan mehr
  aus → **drastisch weniger CPU-Last**. Außerdem wird gewartet, bis das Bild ruhig ist (nicht
  mitten in einer Einblendung), bevor gescannt wird.

## Neu in v37 — Übersetzung + Multi-Monitor
- **Build-Namen werden im EN-Modus jetzt übersetzt** (Bogen→Bow, Schwert→Sword, Blitz-Stab→
  Lightning staff, …). Der interne Schlüssel bleibt gleich, die Bewertung ändert sich also nicht.
- **Der Bereichs-Wähler spannt jetzt über ALLE Monitore** (virtueller Desktop) – Markieren auf
  Monitor 1–4 möglich (z. B. BlueStacks auf dem 2. Bildschirm). Das Abgreifen funktioniert
  ohnehin monitorübergreifend. *(Hinweis: ein vollautomatisches Erkennen der Spiel-Innenbereiche
  ohne Markieren ist nicht zuverlässig – jeden Bereich einmal markieren, dann läuft es.)*

## Neu in v36 — Edelstein-Auto-Scan
- **Auch der Slot-Tab hat jetzt „🔁 Auto-Scan":** überwacht Bereich 1 (Ausgerüstet, rechts) und
  Bereich 2 (Auswahl, links) und **vergleicht automatisch, sobald du im Spiel einen Edelstein
  anzeigst** — kein Knopfdruck nötig. Scannt nur bei Bild-Änderung (schont die CPU).

## Neu in v35 — Skill-Namen im EN-Modus übersetzt
- Im Englisch-Modus werden **Skill-Namen jetzt englisch angezeigt**: mehr Skills sind kuratiert
  (mit DE+EN-Namen) und werden auch bei verklebter OCR erkannt (Blob-Suche zuerst — keine
  deutschen Doppel-Einträge mehr).
- Für unbekannte Skills wird der Name grob DE→EN Wort-für-Wort übersetzt.

## Neu in v34 — Skill: Lauf-Tracking, Synergie & Fixes
- **Dolch-Skills (z. B. Wut-Dolch) zählen jetzt als Dolch-Skill** → stark in Dolch-Builds
  (Whisperer). **Gift-Skills zählen nur in Gift-/DoT-Builds** (sonst meiden).
- **„🎒 Dein Lauf":** merkt sich die gewählten Skills (Knopf **„+ Lauf"**) — auch andere als die
  vorgeschlagenen — mit **Synergie-Erkennung** (z. B. Kombo-Dolch + Wut-Dolch).
- **„🗑 Neuer Lauf"** setzt den Lauf zurück (am Ende eines Laufs drücken).

## Neu in v33 — Skill-Auto-Scan
- Im Skills-Tab: **„🔁 Auto-Scan"** — nach dem einmaligen Markieren überwacht das Tool den
  Bereich selbst und **erkennt automatisch, sobald die Skill-Auswahl erscheint** (kein
  Knopfdruck nötig). Es scannt nur, wenn sich das Bild wirklich ändert — schont die CPU.

## Neu in v32 — Skill-Berater (großes Update)
- **Neuer Tab „🧠 Skills":** markiere die angebotenen Skills (beim Level-Up / in der Auswahl),
  und das Tool sagt dir **pro Build**, welche du **LERNEN** und welche du **MEIDEN** solltest
  (der „Skill-Doktor").
- Eigene Datenbank `skills.json` (45 Skills, Tier S+…D — Quellen: allclash, meowdb, game-vault)
  plus Wort-Verständnis für unbekannte Skills.
- Build-abhängig: z. B. **„Mehrfach-Blitz" = LERNEN bei Nashir, MEIDEN bei Whisperer**.

## Neu in v31 — Dunkel-Modus ohne Pink
- Der **Dunkel-Modus passt jetzt zum Capybara-Bild**: Nachthimmel-Navy mit **Himmelblau-Buttons**,
  Gold (Krone), Türkis (Kristall) und Gras-Grün – **kein Pink mehr**.

## Neu in v30 — Hell/Dunkel-Schalter
- Neuer **🌙 / ☀️-Button** im Kopf schaltet zwischen dem **hellen** Capybara-Bild-Theme und
  einem **dunklen** Gem-Theme (Pink/Türkis) um. Die Auswahl wird gemerkt.
- Schrift auf Badges/Buttons wählt jetzt automatisch hell oder dunkel für beste Lesbarkeit.

## Neu in v29 — Capybara-Bild-Theme
- Das **Capybara-König-Bild ist jetzt das Kopf-Banner** (`capybara_banner.png`).
- Die **komplette Oberfläche wurde auf die Bild-Farben umgestellt**: helles Himmelblau als
  Hintergrund, weiße Karten, dunkelbrauner Text, Gold-/Kristall-Cyan-/Gras-Grün-Akzente.
- Tier-Farben und alle Badges/Buttons wurden an das helle Theme angepasst (gut lesbar).
- Eigenes Bild nutzen? Einfach `capybara_banner.png` im Tool-Ordner ersetzen.

## Neu in v28 — Capybara-Banner + Erkennungs-Fixes
- **Capybara-Banner:** Leg eine `capybara_banner.png` in den Tool-Ordner – sie wird als
  Kopf-Banner verwendet (dein eigenes Capybara-Bild). Ohne Datei zeigt das Tool einen erzeugten
  Pink/Türkis-Farbverlauf. (Ein echter durchscheinender Fenster-Hintergrund ist in Tkinter nicht
  möglich, daher kommt der Look als Banner oben.)
- **Krit-/Konter-/Kombo-„% der max. HP"-Steine** werden jetzt sicher (100%) am echten deutschen
  Text erkannt („Bei einem kritischen Treffer … der maximalen HP des Ziels") – ohne Verwechslung
  untereinander.
- **final_dmg-Greedy-Fix:** Das zu kurze Stichwort „endschaden" matchte fremde Texte
  („…zusätzlichen Schaden…") mit 90% und klaute sie – entfernt. „Endschadensbonus" / „Finaler
  Schaden" werden weiter sicher erkannt.

## Neu in v27 — Schärfe, Gem-Farben, Helden-Vergleich
- **Scharfe Oberfläche:** Die App ist jetzt DPI-aware – Windows skaliert sie nicht mehr
  unscharf hoch. Die Schrift ist an die echte Bildschirm-DPI gekoppelt (scharf & korrekt groß).
- **Gem-Farben:** Pink + Türkis (wie die Edelsteine im Spiel) auf dunklem Grund.
- **Held-Seite = Mehrfach-Scan + Vergleich:** Region einmal festlegen (ganzer Spiel-Screen reicht),
  dann 2 ausgerüstete + bis zu 4 Reserve-Helden scannen. Das Tool vergleicht Rang + Build-Eignung
  und empfiehlt Wechsel.

## Neu in v26 — Erkennungs-Fixes + Capybara-Look
- **Kein falsches „Schon ausgerüstet" mehr:** Die **Eigenschaft des angewählten Steins**
  (Detailkarte, alles ab „Edelstein-Attribut") zählt nie als ausgerüstet – der Kandidat wird
  also nicht mehr fälschlich als „steckt bereits drin" gemeldet. Erfasst Bereich 1 versehentlich
  die Auswahl-Karte, **warnt** das Tool jetzt, Bereich 1 auf die Effekt-Boxen zu ziehen.
- **„Waffe" wird nicht mehr als „Waffenkrit" gelesen:** kurze Slot-Labels (Waffe/Ring/…) werden
  gefiltert, und **„Globaler Angriff" wird wieder zuverlässig erkannt** (ein Rausch-Filter hat
  „Globaler" verschluckt).
- **Neues warmes Capybara-/Heiße-Quelle-Design** (Farben & Akzente).

## Neu in v25 — Build-Doktor im Schnell-Scan
- Der ⚡ Schnell-Scan zeigt jetzt oben ein klares **🩺 Build-Doktor**-Urteil: **✅ Behalten /
  ❌ Tauschen** für deinen gewählten Build, jeder schwache Stein mit Grund, plus **💡 Ideal
  für diesen Build:** die bestbewerteten Steine als Ziel. Ein Scan → du siehst sofort, was zu
  ändern ist.

## Neu in v24 — jeder Build versteht jetzt wirklich gut vs. schlecht
- **Element-/Typ-Steine sind jetzt build-abhängig.** Blitz, Feuer, Explosion, Normalangriff
  und Physisch sind eigene Kategorien (getrennt von „globale ATK"). Damit ist **Blitzschaden
  nur bei Nashir gut** und zeigt **Tier D bei Whisperer/Skysplitter/…** – kein „Blitzschaden
  lohnt sich" mehr auf einem Dolch-Build.
- **Alle 8 Builds neu eingestellt (prefs):** Dolch/Krit hoch bei Whisperer, Wut/Schwertchi bei
  Skysplitter, Blitz bei Nashir, Konter/Survival bei Mushroom usw. (Vorher hatte z. B.
  Whisperer nur EINE Anpassung – dadurch wurden Fremd-Build-Steine zu hoch bewertet.)

## Neu in v23 (Erkennungs-Fixes anhand echter Spieltexte)
- **„Normalangriff mit X% Chance auf 2× Schaden" wird nicht mehr als
  „Normalschaden-Verstärkung" gelesen.** Das zu gierige Stichwort („normalangriff")
  wurde entfernt – der Doppelschaden-Stein wird jetzt korrekt erkannt.
- **„Beim Einsatz einer Fähigkeit … Schadensreduktion ignorieren" wird jetzt erkannt** –
  auch wenn der Effekttext beim Scan abgeschnitten oder verklebt ist (echte DE-Phrase ergänzt).
- Allgemein robuster gegen geteilte/verklebte OCR-Zeilen (echte deutsche Phrasen ergänzt).

## Neu in v22
- **Großer Datenbank-Ausbau:** +58 neue Stein-Effekte (jetzt **122** statt 64), gezogen aus
  der **kompletten meowdb-Edelsteinliste** (986 Steine → 199 Effekt-Familien, Stand Juni 2026).
  Neu u. a. **Schaden gegen Bosse**, **Geschwindigkeit**, **Schaden an Zielen mit Schild**,
  **sofortige Skill-Wahl beim Stage-Start**, elementare Boosts/Reduktionen (Feuer/Blitz/
  Explosion/…), **Kombo-/Konter-/Brand-Koeffizienten**, Krit-Raten (Waffe/Dolch/Schwertchi/
  Blitz/DoT), **Erste-Runde-FDR**, Reflexschaden, **Pet-Anti-Krit (PvP)** und vieles mehr –
  für alle 4 Slots.
- **Genauere Erkennung – kein „falscher Cousin“ mehr:** Bei Score-Gleichstand gewinnt der
  **spezifischere** Stein (längere Phrase). Z. B. wird „Schwertchi-Kritrate“ nicht mehr als
  „Schwertchi-Koeffizient“ gelesen, „Erste-Runde-FDR“ nicht als normales „FDR“.
- **Tier-Abgleich:** Werte wurden gegen die meowdb-PvE/PvP-Tiers geprüft
  (SS=100, S=92, A=80, B=62, C=46, D=28, F=12); ein paar veraltete Werte (Globale VTDG/LP) korrigiert.

## Neu in v21
- **Keine „falscher Stein"-Verwechslungen mehr:** Steine mit gemeinsamer Endung (z. B.
  „…schaden") matchen nicht mehr fälschlich auf den falschen Stein. Ein Stein wird nur
  akzeptiert, wenn sein unterscheidendes Wort (z. B. Krit vs Blitz vs Konter) wirklich im
  Text steht. Behebt Fälle wie „Blitzschaden-Verstärkung", das als „Krit-Schaden" gelesen wurde.
- **Neuer Stein:** Blitzschaden-Verstärkung.

## Neu in v20
- **Slot-Tab erkennt jetzt ALLE ausgerüsteten Steine** — nicht mehr durch eine Zahl begrenzt;
  es werden alle Steine der Spalte gelesen und der Kandidat gegen den **schwächsten aller**
  verglichen. Das Feld „freie Slots" bedeutet jetzt **leere Slots** (Standard 0); nur erhöhen,
  wenn das Teil einen leeren Slot hat (dann sagt es „einfach einbetten"). Eine strengere
  Trefferschwelle entfernt Fehltreffer, bei denen ein unbekannter Stein den falschen anzog.

## Neu in v19
- **Schnell-Scan erkennt mehr Steine:** Wenn die Texterkennung zwei Effekt-Kästen zu einer
  Zeile verklebt, konnte ein DB-Stein durchrutschen. Eine neue Volltext-Suche findet jetzt
  jeden in der DB vorhandenen Stein auch bei schiefer Zeilen-Trennung; Duplikate werden nach
  Namen zusammengeführt. (Ein Stein, der noch gar nicht in der DB ist, muss weiterhin
  aufgenommen werden — bitte den Text melden.)

## Neu in v18
- **Neuer Stein erkannt:** „Konter-Zusatzschaden (% der max. HP des Ziels, gedeckelt)".

## Neu in v17
- **Neuer Stein erkannt:** „DoT-Dauer +1 / DoT-Schaden +X%" (Schaden über Zeit, Brand/Gift).

## Neu in v16
- **Schnell-Scan begründet jetzt jeden Stein:** unter jedem Treffer steht eine kurze
  Begründung – ob er zu deinem Build passt (Top-Pick / stark / solide / schwach) plus die
  kuratierte Notiz (z. B. „schwach für diesen Build — Gut für Basisangriff-Builds"). So
  siehst du, *warum* ein Stein wo steht.

## Neu in v15
- **DB-Werte sind lokal gesperrt:** Der „Stein lernen"-Knopf wurde entfernt. Werte ändern
  sich nur noch über den 🔄 **Online-Update**-Knopf – so bleiben sie kuratiert und einheitlich
  und können auf dem PC nicht (versehentlich oder absichtlich) verfälscht werden. Unbekannte
  Steine zeigen weiter die rein lesende ≈-Schätzung; du kannst sie fürs nächste Update melden.

## Neu in v14
- **Details-Feld vollständig zweisprachig:** Im Englisch-Modus sind jetzt alle *eigenen*
  Tool-Texte im Feld „Details (detected text)" englisch (Labels, Anführungszeichen, „(empty)").
  Die langen deutschen Zeilen dort sind der **rohe Spieltext** (dein Spiel ist auf Deutsch) –
  das ist Daten, keine Tool-Sprache, und muss für den Abgleich so bleiben.

## Neu in v13
- **Online-Update-Knopf (oben, 🔄):** Zeig ihn auf eine gehostete `gems.json` (optional auch
  `builds.json`) – z. B. GitHub-Raw-URL, ein Gist oder dein eigenes NAS – und hol die neueste
  Datenbank, ohne neu zu installieren. Die alte Datei wird als `.bak` gesichert, die neue geprüft
  und live geladen. URLs werden gemerkt.
- **Aufgeräumtere Oberfläche:** mehr Abstand und klarere, etwas größere Schrift.

## Neu in v12
- **Lichtspeer-Koeffizient korrekt abgewertet:** Außerhalb echter Lichtspeer-Builds (also bei
  allen aktuellen Builds) ist er ein toter Stat und wird nicht mehr fälschlich über echte
  Schadens-Steine empfohlen.

Liest ausgerüstete + angewählte Edelsteine vom Bildschirm und sagt dir, ob sich ein
Stein **für den gewählten Build** lohnt. 8 Build-Guides, Deutsch/Englisch, kuratierte
Stein-Datenbank (per Online-Update aktualisiert), Loadout-Analyse.

> Werte sind **Community-Einschätzungen** (NiaMeowDB Mai 2026, game-vault Wiki, meowdb
> Gem-Liste, MrGuider, Theria), keine offiziellen Spielzahlen.

## Neu in v11
- **Mehr Steine in der Datenbank:** Konterschaden-Verstärkung, Blitz-Lähmung (brennendes Ziel),
  Kampfstart-Schild, Heilung-pro-Runde, Kombo-Koeffizient auf Rüstung – plus Fixes, damit
  „Konterschaden" nicht mehr als „Finaler Schaden" gelesen wird und „>70% HP" verstanden wird.

## Neu in v10
- **Tab „⚡ Schnell-Scan":** ein Knopf, eine Region — liest **alle** Steine im Bereich,
  bewertet jeden für deinen Build und zeigt eine sortierte Liste (bester → schwächster)
  mit ✅/⚠️. Kein Slot-Wählen, kein Zwei-Regionen-Zeichnen.
- **Tab „🦸 Held":** Bereich einer Helden-Detailseite markieren — liest den Rang
  (Legendär / Mythisch+N), die drei Roh-Boni (LP/ANG/VTDG) und prüft die Effekt-Stichwörter
  (Basisangriff / Kombo / Skill / Schild / Konter / Krit) gegen deinen Build. Hinweis: alle
  Helden geben **dieselben drei Boni**, nur der Rang skaliert sie — die Heldenwahl entscheidet
  sich also über die Effekt-Synergie, nicht nur über den Rang.

## Neu in v9
- **Alle 8 offiziellen Waffen-Builds** an die NiaMeowDB-Guides angeglichen, je mit direktem Quellen-Link (Whisperer/Elres, Skysplitter/Ailoren, Helos/BoJ, Angel Bow/St. Mung, Nashir/Reaper, Durian/Seles, Star Staff, Mushroom-Hammer).
- Neuer Stein **Schwertchi-Koeffizient** + build-spezifische Bewertung (z. B. hoch bei Skysplitter, Wut-Koeffizient bei Nashir korrekt abgewertet).

## Neu in v8
- **Loadout = volle Charakter-Analyse** (scrollbar): Ausrüstung wird pro Slot gescannt; Helden, Brandmal, Sammlung, Pets, Reittier, Vermächtnis & Abenteurer zeigen build-spezifische PvE/PvP-Empfehlungen zum Abgleich mit deinem Spiel (Icons sind nicht zuverlässig scannbar).

## Neu in v7
- **Build-Umschalter** (oben): Whisperer/Elres, Skysplitter/Ailoren, Angel Bow,
  Mushroom-Hammer-Konter, Durian/Seles, Nashirs/Helos, Warrior's Sword, allgemeine Regeln.
  Der Build ändert die Bewertung jedes Steins (z. B. Wut-Koeffizienten höher bei
  Skysplitter, Dolch-Steine bei Whisperer).
- Versteht Steine auch bei OCR-Worttrennung (z. B. „Koeffizie nt").
- Viele neue Steine + korrekte deutsche Begriffe (Endschadensbonus, Globale Verteidigung,
  Lichtspeer-Koeffizient, Normalschaden-Verstärkung, Haustier-Heilung, „über/mehr als 70 % HP").

## Start (ein Klick)
1. Alle Dateien in **einen Ordner**: `Edelstein-Scanner starten.bat`,
   `capybara_gem_scanner.py`, `gems.json`, `builds.json`.
2. Doppelklick auf **`Edelstein-Scanner starten.bat`**. Erster Start installiert alles.
   Falls Python neu kam: `.bat` **noch einmal** doppelklicken.

## Benutzen
1. Oben rechts **DE ⇄ EN**. Unter den Tabs deinen **Build** wählen.
2. **Scanner-Tab:** **PvE/PvP**, **Slot** und **freie Slots** wählen.
3. Zwei Bereiche einmal festlegen: **1) Ausgerüstet** = rechte Spalte mit den Effekt-
   Kästen; **2) Auswahl** = linkes Info-Fenster (inkl. „Attribut"). Vorschau „erfasst: …"
   zeigt den gelesenen Text.
4. Stein im Spiel anwählen, **Scannen & vergleichen** → klares Urteil, passend zum Build.
5. **Loadout-Tab:** analysiert alle 4 gescannten Slots mit Tipps für den gewählten Build.
   **Build-Guide-Tab:** komplette Specs des gewählten Builds.

## Die Stein-Datenbank
Die Datenbank (`gems.json`) wird **kuratiert und über den 🔄 Online-Update-Knopf aktualisiert**,
damit die Werte einheitlich bleiben und lokal nicht verfälscht werden können. Unbekannte Steine
werden weiter am Wortsinn erkannt (mit ≈ markiert).
Falsch erkannt oder fehlt etwas? **🔍 Details anzeigen** an, Text kopieren und melden – dann
kommt der Stein zentral rein und per nächstem Update zu allen.

## ⚠️ Antivirus (Fehlalarm)
Manche Virenscanner schlagen bei diesem Programm an. **Das ist ein Fehlalarm – es ist keine
Schadsoftware.** Zwei harmlose Verhaltensweisen lösen die Heuristik-Warnung aus:
- es **macht Bildschirmfotos** (so liest es die Edelsteine vom Bildschirm), und
- die Start-Datei (`.bat`) **installiert beim ersten Start automatisch Python-Pakete**.

**Es werden keine Daten gesendet.** Alles läuft lokal; nur das optionale 🔄 Online-Update lädt
von einer URL, die **du** selbst eingibst. Der Quellcode (`capybara_gem_scanner.py`) ist offen
und lesbar – du kannst jede Zeile prüfen.

**Lösung:** den Tool-Ordner als Ausnahme/Whitelist hinzufügen. In **Windows Defender**:
*Viren- & Bedrohungsschutz → Einstellungen verwalten → Ausschlüsse → Ausschluss hinzufügen →
Ordner*, dann diesen Ordner wählen. (Oder nach einer Blockierung im *Schutzverlauf* auf
**Aktion zulassen** klicken.)

## ⚖️ Haftungsausschluss
**Inoffizielles Fan-Tool.** Steht in keiner Verbindung zu den Machern von „Capybara Go" und wird
von ihnen nicht unterstützt; alle Spielnamen, Logos und Marken gehören ihren jeweiligen
Eigentümern. Das Tool **liest nur deinen Bildschirm und gibt Empfehlungen** — es verändert das
Spiel nicht, automatisiert keine Eingaben und greift nicht auf Spielspeicher/Netzwerk zu. Die
Nutzung von Drittanbieter-Tools kann den **AGB** des Spiels unterliegen, daher **Nutzung auf
eigene Gefahr**. Alle Werte sind **Community-Einschätzungen**, keine offiziellen Daten. Die
Software wird **„wie besehen", ohne Gewähr** bereitgestellt (siehe `LICENSE.txt`). Gebündelte
Open-Source-Komponenten: siehe `THIRD-PARTY-LICENSES.txt`. Volltext: `DISCLAIMER.txt`.
