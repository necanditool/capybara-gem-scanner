# 💎 Capybara Gem Scanner — Community Edition

![Capybara Gem Scanner](capybara_banner.png)

**Unofficial community tool for Capybara Go.** It reads the **gems and skills off your screen**
(e.g. the game running in BlueStacks, German or English) and tells you — **for the build you pick** —
whether each gem or skill is actually worth it.

*Deutsch weiter unten ↓*

---

## What it does
- 🔎 **Reads gems & skills from the screen** via OCR — no typing, no game files touched.
- 🎯 **Rates everything for your build:** 8 meta builds, PvE & PvP. Pick a build at the top and every
  rating updates.
- ⚡ **Quick scan** — mark the game area once, it reads **all** gems and sorts them best → worst, with
  a "Build Doctor" (keep / swap).
- 🔍 **Slot scan** — compare a gem you're looking at vs your equipped ones → a clear **worth-it / not /
  embed** verdict. Value-aware: same effect but a higher % → it tells you to swap.
- 🦸 **Hero / Build Check** — shows which of your scanned gems **don't fit** the chosen build (and which
  build they *would* fit).
- 🧠 **Skill advisor** — per build, which skill to **learn** and which to **avoid**.
- 🎒 **Loadout & 📖 Guide** — full overview of your slots and the complete build specs.
- 🌐 **DE ⇄ EN**, 🌙 light/dark, and a 🔄 one-click **online database update** from GitHub.
- ❓ **Built-in Help** — a button that explains every function right inside the tool (no file to open).

## Download
Get the latest version from the GitHub repo:
**https://github.com/necanditool/capybara-gem-scanner**
(grab the ready-to-run **installer** from *Releases*, or download the source files).

## Install (Windows)
**Option A — Installer (easiest, no Python needed)**
1. Download **`CapybaraGemScanner-Setup-v…​.exe`**.
2. Run it and choose **Install** (Start-menu + desktop shortcut) **or Portable** (just unpack to a folder).
3. Start it. Done.

**Option B — From source**
1. Put all files in **one folder** (`Edelstein-Scanner starten.bat`, `capybara_gem_scanner.py`,
   `gems.json`, `builds.json`, `skills.json`, `capybara_banner.png`).
2. Double-click **`Edelstein-Scanner starten.bat`** — the first run installs the needed Python packages
   automatically. If Python was *just* installed, double-click the `.bat` **once more**.

> First launch opens the built-in **Help** that explains every function; reopen it any time via
> **❓ Help** (top right).

## How to use
1. Top-right: **DE ⇄ EN** language and 🌙 light/dark. Below the tabs, pick your **Build** — it drives
   every rating.
2. **⚡ Quick:** mark the game area with the gem effects once → it reads & rates all gems.
3. **🔍 Slot:** pick **PvE/PvP**, the **slot** and the number of **free slots**. Set two regions once —
   **1) Equipped** = the right column of effect boxes in-game; **2) Selection** = the left info panel
   (include the "Attribute" line). Select a gem in-game → **Scan & compare** → clear verdict.
4. **🦸 Hero:** scan your gems, then the **Build Check** flags whatever doesn't fit your build.
5. **🧠 Skills:** mark the offered skills → per build, learn / avoid.
6. **🎒 Loadout / 📖 Guide:** full overview + the selected build's specs.

## The gem database
The database (`gems.json`) is **curated and updated via the 🔄 online-update button** (one click pulls the
official version from GitHub), so values stay consistent. Unknown gems are still understood from keywords
on screen (marked ≈). If a gem is detected wrong or missing, turn on **🔍 show details**, copy the text and
report it — then it's added centrally and reaches everyone with the next update.

## ⚠️ Antivirus (false positive)
Some antivirus tools may flag this program. **This is a false positive — it is not malware.** Two harmless
behaviours trigger the heuristic warning: it **takes screenshots** (that's how it reads the gems), and the
launcher (`.bat`) **auto-installs Python packages** on first run. **No data is sent anywhere** — everything
runs locally; only the optional 🔄 online update downloads from a URL **you** type in. The source code is
open and readable. **Fix:** add the tool's folder as an exclusion in **Windows Defender** → *Virus & threat
protection → Manage settings → Exclusions → Add an exclusion → Folder* (or, after a block, *Protection
history → Allow on device*).

## ⚖️ Disclaimer
**Unofficial fan tool.** Not affiliated with, endorsed by, or connected to the makers of "Capybara Go"; all
game names, logos and trademarks belong to their respective owners. The tool only **reads your screen and
gives advice** — it does not modify the game, automate input, or access game memory/network. Using
third-party tools with a game may be subject to the game's Terms of Service, so **use it at your own risk**.
All values are **community estimates**, not official data. Provided **"as is", without warranty** (see
`LICENSE.txt`; bundled open-source components in `THIRD-PARTY-LICENSES.txt`; full text in `DISCLAIMER.txt`).

## 📝 Changelog
Full version history is in **[CHANGELOG.md](CHANGELOG.md)** (in the app folder, the same notes are in
`Patchnotes English.txt` / `Patchnotes Deutsch.txt`).

---

# 💎 Capybara Gem Scanner — Community Edition  [Deutsch]

**Inoffizielles Community-Tool für Capybara Go.** Es liest die **Edelsteine und Skills von deinem
Bildschirm** (z. B. das Spiel im BlueStacks, deutsch oder englisch) und sagt dir — **für den Build, den du
wählst** — ob ein Stein oder Skill sich wirklich lohnt.

## Was es macht
- 🔎 **Liest Steine & Skills vom Bildschirm** per Texterkennung — kein Tippen, keine Spieldateien angefasst.
- 🎯 **Bewertet alles für deinen Build:** 8 Meta-Builds, PvE & PvP. Oben Build wählen → alle Bewertungen
  passen sich an.
- ⚡ **Schnell-Scan** — Spielbereich einmal markieren, liest **alle** Steine und sortiert sie (bester →
  schwächster) inkl. „Build-Doktor" (behalten / tauschen).
- 🔍 **Slot-Scan** — einen angewählten Stein gegen deine ausgerüsteten vergleichen → klares **Lohnt-sich /
  Lohnt-nicht / Einbetten**-Urteil. Wert-bewusst: gleicher Effekt, aber höherer % → Tausch-Empfehlung.
- 🦸 **Held / Build-Check** — zeigt, welche deiner gescannten Steine **nicht zum Build passen** (und zu
  welchem Build sie gehören).
- 🧠 **Skill-Berater** — pro Build, welchen Skill **lernen** und welchen **meiden**.
- 🎒 **Loadout & 📖 Guide** — Gesamtübersicht deiner Slots und die kompletten Build-Specs.
- 🌐 **DE ⇄ EN**, 🌙 Hell/Dunkel und ein 🔄 Ein-Klick-**Online-Update der Datenbank** von GitHub.
- ❓ **Eingebaute Hilfe** — ein Knopf, der jede Funktion direkt im Tool erklärt (keine Datei nötig).

## Download
Neueste Version aus dem GitHub-Repo:
**https://github.com/necanditool/capybara-gem-scanner**
(fertigen **Installer** unter *Releases* laden, oder die Quelldateien).

## Installieren (Windows)
**Variante A — Installer (am einfachsten, kein Python nötig)**
1. **`CapybaraGemScanner-Setup-v…​.exe`** herunterladen.
2. Starten und **Installieren** (Startmenü- + Desktop-Verknüpfung) **oder Portable** (nur in einen Ordner
   entpacken) wählen.
3. Starten. Fertig.

**Variante B — Aus dem Quellcode**
1. Alle Dateien in **einen Ordner** legen (`Edelstein-Scanner starten.bat`, `capybara_gem_scanner.py`,
   `gems.json`, `builds.json`, `skills.json`, `capybara_banner.png`).
2. Doppelklick auf **`Edelstein-Scanner starten.bat`** — der erste Start installiert die nötigen
   Python-Pakete automatisch. Falls Python *gerade erst* kam: die `.bat` **noch einmal** doppelklicken.

> Beim ersten Start öffnet sich die eingebaute **Hilfe**, die jede Funktion erklärt; jederzeit wieder
> über **❓ Hilfe** (oben rechts).

## Benutzen
1. Oben rechts: **DE ⇄ EN** und 🌙 Hell/Dunkel. Unter den Tabs deinen **Build** wählen — er steuert alle
   Bewertungen.
2. **⚡ Schnell:** Spielbereich mit den Edelstein-Effekten einmal markieren → liest & bewertet alle Steine.
3. **🔍 Slot:** **PvE/PvP**, **Slot** und **freie Slots** wählen. Zwei Bereiche einmal festlegen —
   **1) Ausgerüstet** = rechte Spalte mit den Effekt-Kästen; **2) Auswahl** = linkes Info-Fenster (inkl.
   „Attribut"). Stein im Spiel anwählen → **Scannen & vergleichen** → klares Urteil.
4. **🦸 Held:** Steine scannen, dann markiert der **Build-Check**, was nicht zum Build passt.
5. **🧠 Skills:** angebotene Skills markieren → pro Build lernen / meiden.
6. **🎒 Loadout / 📖 Guide:** Gesamtübersicht + Specs des gewählten Builds.

## Die Stein-Datenbank
Die Datenbank (`gems.json`) wird **kuratiert und über den 🔄 Online-Update-Knopf aktualisiert** (ein Klick
lädt die offizielle Version von GitHub), damit die Werte einheitlich bleiben. Unbekannte Steine werden am
Wortsinn erkannt (mit ≈ markiert). Falsch erkannt oder fehlt etwas? **🔍 Details anzeigen** an, Text
kopieren und melden — dann kommt der Stein zentral rein und per nächstem Update zu allen.

## ⚠️ Antivirus (Fehlalarm)
Manche Virenscanner schlagen an. **Das ist ein Fehlalarm – es ist keine Schadsoftware.** Zwei harmlose
Verhaltensweisen lösen die Heuristik aus: es **macht Bildschirmfotos** (so liest es die Steine) und die
Start-Datei (`.bat`) **installiert beim ersten Start automatisch Python-Pakete**. **Es werden keine Daten
gesendet** — alles läuft lokal; nur das optionale 🔄 Online-Update lädt von einer URL, die **du** eingibst.
Der Quellcode ist offen und lesbar. **Lösung:** Tool-Ordner als Ausnahme in **Windows Defender** hinzufügen
→ *Viren- & Bedrohungsschutz → Einstellungen verwalten → Ausschlüsse → Ausschluss hinzufügen → Ordner*
(oder nach einer Blockierung im *Schutzverlauf* auf **Aktion zulassen**).

## ⚖️ Haftungsausschluss
**Inoffizielles Fan-Tool.** Steht in keiner Verbindung zu den Machern von „Capybara Go" und wird von ihnen
nicht unterstützt; alle Spielnamen, Logos und Marken gehören ihren jeweiligen Eigentümern. Das Tool **liest
nur deinen Bildschirm und gibt Empfehlungen** — es verändert das Spiel nicht, automatisiert keine Eingaben
und greift nicht auf Spielspeicher/Netzwerk zu. Die Nutzung von Drittanbieter-Tools kann den **AGB** des
Spiels unterliegen, daher **Nutzung auf eigene Gefahr**. Alle Werte sind **Community-Einschätzungen**, keine
offiziellen Daten. Bereitgestellt **„wie besehen", ohne Gewähr** (siehe `LICENSE.txt`; gebündelte
Open-Source-Komponenten in `THIRD-PARTY-LICENSES.txt`; Volltext in `DISCLAIMER.txt`).

## 📝 Änderungen
Die vollständige Versionshistorie steht in **[CHANGELOG.md](CHANGELOG.md)** (im Ordner; dieselben Notizen
auch in `Patchnotes Deutsch.txt` / `Patchnotes English.txt`).
