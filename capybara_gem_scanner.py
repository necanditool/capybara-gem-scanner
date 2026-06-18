#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
 Capybara Gem Scanner  ·  Capybara Go            (v41 – Community Edition)
================================================================================
 Erkennt ausgerüstete + angewählte Edelsteine vom Bildschirm und bewertet sie
 für den jeweiligen Build. / Reads equipped + selected gems from screen and
 rates them for the chosen build.

 Features (v41 – weniger CPU-Last):
  • Auto-Scan (Edelsteine & Skills) braucht jetzt deutlich weniger CPU: die OCR
    nutzte bisher ALLE Kerne pro Scan (Spitze ~100 %), jetzt auf wenige Kerne
    begrenzt -> Ausschlag fällt drastisch (Test: 30+ % -> unter 10 %), bei
    praktisch gleicher Geschwindigkeit. Screenshot-Greifer wird zudem
    wiederverwendet statt neu erzeugt (weniger Grundlast).

 Features (v40 – Stein-Erkennung-Fix):
  • „Schaden gegen geschützte Ziele" wird jetzt erkannt (echte Spielformulierung
    ergänzt – vorher nur „Ziele mit Schild", daher „unklar")

 Features (v39 – Fenster/Layout-Fix):
  • Slot-Tab ist jetzt scrollbar – „Angewählter Stein (Kandidat)" und „Ideal"
    werden nicht mehr abgeschnitten (alle Tabs scrollen jetzt)
  • Fensterhöhe passt sich an die Bildschirmhöhe an (Taskleiste bleibt frei);
    kleinere Mindestgröße -> passt auch auf kleinere Bildschirme

 Features (v38 – Auto-Scan CPU-Optimierung):
  • Auto-Scan (Slot & Skills) startet OCR jetzt NUR bei deutlicher UND ruhiger
    Änderung (Schwellenwert-Differenz statt exaktem Hash). Glitzern/Animationen
    lösen keinen Scan mehr aus -> drastisch weniger CPU-Last.

 Features (v37 – Übersetzung + Multi-Monitor):
  • Build-Namen werden im EN-Modus jetzt übersetzt (Bogen->Bow, Schwert->Sword,
    Blitz-Stab->Lightning staff … – interner Schlüssel bleibt unverändert)
  • Bereichs-Wähler spannt jetzt über ALLE Monitore (virtueller Desktop) –
    Markieren auf Monitor 1–4 möglich (z. B. BlueStacks auf 2. Bildschirm)

 Features (v36 – Auto-Scan auch für Edelsteine):
  • Slot-Tab: „🔁 Auto-Scan" – überwacht Bereich 1 (Ausgerüstet, rechts) und
    Bereich 2 (Auswahl, links) und vergleicht automatisch, sobald du im Spiel
    einen Edelstein anzeigst (kein Knopfdruck). Scannt nur bei Bild-Änderung.

 Features (v35 – Skill-Namen übersetzt):
  • Im EN-Modus werden Skill-Namen jetzt englisch angezeigt: mehr Skills sind
    kuratiert (mit DE+EN-Namen) und werden auch bei verklebter OCR erkannt
    (Blob-Suche zuerst, keine deutschen Doppel-Einträge mehr)
  • Für unbekannte Skills grobe DE->EN-Wortübersetzung des Namens

 Features (v34 – Skill: Lauf-Tracking, Synergie & Fixes):
  • Dolch-Skills (z. B. Wut-Dolch) zählen jetzt als Dolch-Skill -> stark in
    Dolch-Builds (Whisperer); Gift-Skills nur in Gift-/DoT-Builds (sonst meiden)
  • „🎒 Dein Lauf": gewählte Skills merken (Knopf „+ Lauf“) – auch andere als die
    vorgeschlagenen – mit Synergie-Erkennung (z. B. Kombo-Dolch + Wut-Dolch)
  • „🗑 Neuer Lauf" setzt den Lauf zurück (am Ende eines Laufs drücken)

 Features (v33 – Skill Auto-Scan):
  • Im Skill-Tab: „🔁 Auto-Scan" – nach dem Markieren überwacht das Tool den
    Bereich selbst und erkennt automatisch, sobald die Skill-Auswahl erscheint
    (kein Knopfdruck nötig). Scannt nur bei Bild-Änderung -> schont CPU.

 Features (v32 – NEU: Skill-Berater):
  • Neuer Tab „🧠 Skills": markiere die angebotenen Skills, das Tool sagt dir
    pro Build, welche du LERNEN und welche du MEIDEN solltest (Skill-Doktor)
  • Eigene Datenbank skills.json (45 Skills, Tier S+..D, Quelle allclash/meowdb/
    game-vault) + Wort-Verständnis für unbekannte Skills
  • Build-abhängig: z. B. „Mehrfach-Blitz" = LERNEN bei Nashir, MEIDEN bei Whisperer

 Features (v31 – Dark-Mode ohne Pink):
  • Dunkel-Modus an das Capybara-Bild angepasst: Nachthimmel-Navy mit
    HIMMELBLAU-Buttons, Gold (Krone), Türkis (Kristall) und Gras-Grün – kein Pink

 Features (v30 – Hell/Dunkel umschaltbar):
  • Neuer 🌙/☀️-Button im Kopf: schaltet zwischen hellem Capybara-Bild-Theme und
    dunklem Gem-Theme (Pink/Türkis) um; Auswahl wird gemerkt
  • Badge-/Button-Schrift wählt automatisch hell/dunkel für beste Lesbarkeit

 Features (v29 – Capybara-Bild-Theme):
  • Das Capybara-König-Bild ist jetzt das Kopf-Banner (capybara_banner.png)
  • KOMPLETTE Oberfläche auf die Bild-Farben umgestellt: helles Himmelblau,
    weiße Karten, dunkelbrauner Text, Gold/Kristall-Cyan/Gras-Grün-Akzente
  • Tier-Farben & alle Badges/Buttons an das helle Theme angepasst (lesbar)

 Features (v28 – Capybara-Banner + Erkennungs-Fixes):
  • Capybara-Banner oben: legt man „capybara_banner.png" in den Tool-Ordner,
    wird es als Kopf-Banner genutzt; sonst ein erzeugter Pink/Türkis-Farbverlauf
  • „Bei einem kritischen Treffer …% der max. HP des Ziels" (+ Konter-/Kombo-
    Varianten) werden jetzt sicher (100%) und ohne Verwechslung erkannt
  • final_dmg-Greedy-Fix: das zu kurze „endschaden" klaute fremde Texte
    („…zusätzlichen Schaden…") – entfernt; „Endschadensbonus" erkennt weiter sicher

 Features (v27 – Schärfe, Gem-Farben, Helden-Vergleich):
  • SCHÄRFE: App ist jetzt DPI-aware – keine unscharfe Windows-Hochskalierung
    mehr; Schrift an die echte Bildschirm-DPI gekoppelt (scharf & korrekt groß)
  • Neue Edelstein-Farben: Pink + Türkis (wie die In-Game-Gems) auf dunklem Grund
  • Held-Seite = Mehrfach-Scan + Vergleich: Region einmal (ganzer Screen reicht),
    dann 2 ausgerüstete + bis zu 4 Reserve-Helden scannen → Tool vergleicht Rang
    + Build-Eignung und empfiehlt Wechsel

 Features (v26 – Erkennungs-Fixes + Capybara-Design):
  • „Schon ausgerüstet"-Fehlalarm behoben: die Eigenschaft des ANGEWÄHLTEN
    Steins (Detailkarte, ab „Edelstein-Attribut") zählt nie als ausgerüstet –
    plus Warnung, wenn Bereich 1 versehentlich die Auswahl-Karte erfasst
  • „Waffe" wird nicht mehr als „Waffenkrit" fehlgelesen (Slot-Labels gefiltert);
    „Globaler Angriff" wird wieder zuverlässig erkannt
  • Neues warmes Capybara-/Heiße-Quelle-Design (Farben/Akzente)

 Features (v25 – Build-Doktor im Schnell-Scan):
  • Klare Empfehlung oben im ⚡ Schnell-Scan: „✅ Behalten / ❌ Tauschen" für
    den gewählten Build, jeder schwache Stein mit Grund, plus „💡 Ideal für
    diesen Build: …" (die bestbewerteten Steine als Ziel)

 Features (v24 – jeder Build versteht jetzt WIRKLICH, was gut/schlecht ist):
  • Feinkörnige Kategorien: Blitz / Feuer / Explosion / Normalangriff / Physisch
    sind von „globale ATK“ getrennt – ein Element-Stein zählt nur dort, wo der
    Build ihn nutzt (z. B. Blitzschaden ist NUR bei Nashir gut, sonst Tier D)
  • Alle 8 Builds neu eingestellt (prefs) – Dolch/​Krit hoch bei Whisperer,
    Wut/​Schwertchi bei Skysplitter, Blitz bei Nashir, Konter/​Survival bei
    Mushroom usw. (vorher hatte z. B. Whisperer nur EINE Anpassung)

 Features (v23 – Erkennungs-Fixes anhand echter Spieltexte):
  • „Normalangriff mit X% Chance auf 2× Schaden“ wird nicht mehr als
    „Normalschaden-Verstärkung“ gelesen (gieriges Stichwort entfernt)
  • „Beim Einsatz einer Fähigkeit … Schadensreduktion ignorieren“ wird jetzt
    erkannt, auch wenn der Effekttext im Scan abgeschnitten/verklebt ist
  • Allgemein robuster gegen geteilte/verklebte OCR-Zeilen durch echte DE-Phrasen

 Features (v22):
  • GROSSER Datenbank-Ausbau: +58 neue Effekte (jetzt 122 statt 64) aus der
    kompletten meowdb-Liste (986 Steine / 199 Effekt-Familien, Stand Juni 2026) –
    u. a. Schaden gegen Bosse, Geschwindigkeit, Schaden an Schild-Zielen,
    Skill-Wahl beim Stage-Start, elementare Boosts/Reduktionen (Feuer/Blitz/…),
    Kombo-/Konter-/Brand-Koeffizienten, Krit-Raten (Waffe/Dolch/Schwertchi/Blitz),
    erste-Runde-FDR, Reflexschaden, Pet-Anti-Krit u. v. m.
  • Genauerer Treffer: bei Score-Gleichstand gewinnt der spezifischere Stein
    (längere Phrase) – z. B. „Schwertchi-Kritrate“ wird nicht mehr als
    „Schwertchi-Koeffizient“ gelesen
  • Tier-Abgleich mit meowdb-Werten (SS=100,S=92,A=80,B=62,C=46,D=28,F=12)

 Features (v21):
  • Match-Schutz: gemeinsame Endungen („…schaden“ usw.) lösen keine Fehltreffer mehr aus –
    ein Stein matcht nur, wenn sein unterscheidendes Wort (z. B. Krit vs Blitz) im Text steht
  • Neuer Stein: Blitzschaden-Verstärkung
  • Slot-Tab erkennt ALLE ausgerüsteten Steine (kein Limit mehr); „freie Slots“ = leere Slots (Default 0)
  • Vergleich gegen den schwächsten ALLER erkannten ausgerüsteten Steine; strenge 80%-Schwelle gegen Fehltreffer
  • Schnell-Scan robuster: Blob-Suche findet DB-Steine auch bei verklebten OCR-Zeilen; Dedup nach Namen
  • Neuer Stein: Konter-Zusatzschaden (% der max. HP) erkannt
  • Neuer Stein: DoT-Dauer/-Schaden (Brand/Gift) erkannt
  • Schnell-Scan zeigt pro Stein eine Begründung (Build-Eignung + kuratierte Notiz)
  • DB-Werte lokal NICHT editierbar – nur das Online-Update ändert sie (saubere Werte)
  • Details-Ausgabe (erkannter Text) vollständig zweisprachig (DE/EN)
  • Online-Update-Knopf (oben): gems.json/builds.json von einer URL laden (.bak-Sicherung)
  • Aufgeräumtere Oberfläche (mehr Abstand, klarere Schrift)
  • Schnell-Scan: ein Knopf, eine Region, liest ALLE Steine und sortiert sie
  • Held-lesen-Modus: Rang + Roh-Boni + Build-Eignung aus dem Effekt-Text
  • Datenbank als externe Datei gems.json (Werte nur per Online-Update / values via update only)
  • Build-Guide als builds.json (mehrere Builds / multiple builds)
  • Deutsch / Englisch umschaltbar  ·  German / English toggle
  • versteht auch unbekannte Steine am Wortsinn (DE+EN keyword understanding)
  • Gesamt-Loadout-Übersicht über alle 4 Slots
  • robuste Erkennung + klare Fehlermeldungen

 Hinweis: Werte sind Community-Einschätzungen, keine offiziellen Spielzahlen.
 Note: values are community estimates, not official game numbers.

 Start: „Edelstein-Scanner starten.bat“ (Doppelklick). gems.json + builds.json
 müssen im selben Ordner liegen.
================================================================================
"""

import os
import sys
import json
import re
import shutil
import statistics
import threading
import traceback
import urllib.request
import urllib.error

import tkinter as tk
from tkinter import messagebox

_MISSING = []
for mod, pipname in [("mss", "mss"), ("PIL", "pillow"), ("numpy", "numpy"),
                     ("rapidfuzz", "rapidfuzz"), ("rapidocr_onnxruntime", "rapidocr-onnxruntime")]:
    try:
        __import__(mod)
    except ImportError:
        _MISSING.append(pipname)
if _MISSING:
    msg = ("Es fehlen Bausteine / Missing components. Starte über "
           "„Edelstein-Scanner starten.bat“ oder:\n\n    pip install " + " ".join(_MISSING))
    try:
        r = tk.Tk(); r.withdraw(); messagebox.showerror("Setup", msg); r.destroy()
    except Exception:
        pass
    print(msg); sys.exit(1)

import mss                       # noqa: E402
from PIL import Image, ImageOps  # noqa: E402
import numpy as np               # noqa: E402
from rapidfuzz import fuzz       # noqa: E402

# Daten-Ordner (gems.json/builds.json/skills.json/capybara_banner.png werden hier
# gelesen UND beim Online-Update überschrieben). Als PyInstaller-.exe liegt das
# Skript IM Bundle, die Daten aber NEBEN der .exe -> dann den .exe-Ordner nehmen.
if getattr(sys, "frozen", False):
    HERE = os.path.dirname(sys.executable)
else:
    HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".capybara_gem_scanner.json")


def load_config():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_config(cfg):
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def reload_gems():
    """Liest gems.json neu ein und aktualisiert die Modul-Globals (für Online-Update)."""
    global GEMS, SLOT_KEYS, CATS
    with open(os.path.join(HERE, "gems.json"), encoding="utf-8") as f:
        GEMS = json.load(f)
    SLOT_KEYS = [k for k in ["Weapon", "Armor", "Ring", "Accessory"] if k in GEMS] or SLOT_KEYS
    CATS = GEMS.get("_meta", {}).get("cats") or CATS


def reload_builds():
    """Liest builds.json neu ein und aktualisiert die Build-Globals."""
    global BUILDS, BUILD_LIST, BUILD_NAMES, BUILD_PREFS, BUILD_EN
    with open(os.path.join(HERE, "builds.json"), encoding="utf-8") as f:
        BUILDS = json.load(f)
    BUILD_LIST = BUILDS.get("builds", [])
    BUILD_NAMES = [b["name"] for b in BUILD_LIST] or ["—"]
    BUILD_PREFS = {b["name"]: b.get("prefs", {}) for b in BUILD_LIST}
    BUILD_EN = {b["name"]: b.get("name_en", b["name"]) for b in BUILD_LIST}


def fetch_url(url, timeout=15):
    """Lädt Text von einer URL (https/http/file). Stdlib, keine Zusatzpakete."""
    req = urllib.request.Request(url.strip(), headers={"User-Agent": "CapybaraGemScanner"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8-sig")


def backup_and_write_json(filename, data_obj):
    """Sichert die alte Datei als .bak und schreibt data_obj als JSON zurück."""
    path = os.path.join(HERE, filename)
    try:
        if os.path.exists(path):
            shutil.copyfile(path, path + ".bak")
    except Exception:
        pass
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data_obj, f, ensure_ascii=False, indent=2)


def reload_skills():
    """Liest skills.json neu ein (für Online-Update / Skill-Tab)."""
    global SKILLS_DB
    with open(os.path.join(HERE, "skills.json"), encoding="utf-8") as f:
        SKILLS_DB = json.load(f)


def load_data():
    """Lädt gems.json + builds.json + skills.json neben dem Skript.
    Fallback: leere DB (Klassifikator wirkt weiter)."""
    gems, builds, skills, warn = {}, {"builds": []}, {"skills": []}, None
    try:
        with open(os.path.join(HERE, "gems.json"), encoding="utf-8") as f:
            gems = json.load(f)
    except Exception as e:
        warn = "gems.json nicht gefunden/fehlerhaft – nutze nur Wort-Verständnis. (%s)" % e
        gems = {"Weapon": [], "Armor": [], "Ring": [], "Accessory": []}
    try:
        with open(os.path.join(HERE, "builds.json"), encoding="utf-8") as f:
            builds = json.load(f)
    except Exception:
        builds = {"builds": []}
    try:
        with open(os.path.join(HERE, "skills.json"), encoding="utf-8") as f:
            skills = json.load(f)
    except Exception:
        skills = {"skills": []}
    return gems, builds, skills, warn


GEMS, BUILDS, SKILLS_DB, DATA_WARN = load_data()
SLOT_KEYS = [k for k in ["Weapon", "Armor", "Ring", "Accessory"] if k in GEMS]
if not SLOT_KEYS:
    SLOT_KEYS = ["Weapon", "Armor", "Ring", "Accessory"]
    for k in SLOT_KEYS:
        GEMS.setdefault(k, [])
SLOT_DISP = {"Weapon": ("Waffe", "Weapon"), "Armor": ("Rüstung", "Armor"),
             "Ring": ("Ring", "Ring"), "Accessory": ("Halskette", "Accessory")}
# Held-Scan-Slots: 2 ausgerüstete + 4 Reserve. (key, rolle, de, en)
HERO_SLOTS = [
    ("eq1", "equipped", "Ausgerüstet 1", "Equipped 1"),
    ("eq2", "equipped", "Ausgerüstet 2", "Equipped 2"),
    ("res1", "reserve", "Reserve 1", "Reserve 1"),
    ("res2", "reserve", "Reserve 2", "Reserve 2"),
    ("res3", "reserve", "Reserve 3", "Reserve 3"),
    ("res4", "reserve", "Reserve 4", "Reserve 4"),
]
DEFAULT_FREE = {"Weapon": 0, "Armor": 0, "Ring": 0, "Accessory": 0}  # freie (leere) Slots
IDEAL_SHOW = 4  # wie viele "ideale" Steine pro Slot angezeigt werden
DETECT_THRESHOLD = 70
CATS = GEMS.get("_meta", {}).get("cats") or [
    "final", "rage", "dagger", "combo", "crit", "atk", "survival", "control",
    "pvp_ignore", "defensive", "coef_other", "conditional", "utility", "swordchi"]

BUILD_LIST = BUILDS.get("builds", [])
BUILD_NAMES = [b["name"] for b in BUILD_LIST] or ["—"]
BUILD_PREFS = {b["name"]: b.get("prefs", {}) for b in BUILD_LIST}
BUILD_EN = {b["name"]: b.get("name_en", b["name"]) for b in BUILD_LIST}


def tier_of(score):
    # Tier-Farben kommen aus dem aktiven Theme (hell = dunkle Töne, dunkel = helle Töne)
    if score >= 90: return TIERS[0]
    if score >= 75: return TIERS[1]
    if score >= 55: return TIERS[2]
    if score >= 35: return TIERS[3]
    return TIERS[4]


def _norm(s):
    s = s.lower().replace("ä", "a").replace("ö", "o").replace("ü", "u").replace("ß", "ss")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


# Generische Wörter, die KEIN Stein eindeutig machen (gemeinsame Endungen/Füllwörter).
# Ein schwacher Fuzzy-Treffer zählt nur, wenn ein NICHT-generisches Wort der Phrase im Text steht.
GENERIC_TOKENS = {
    "schaden", "schadens", "schadensbonus", "damage", "dmg", "bonus",
    "koeffizient", "coefficient", "reduktion", "reduzierung", "reduction",
    "verstarkung", "verstark", "verstarkt", "boost", "erhoht", "erhohte",
    "erhohter", "erhohten", "increased", "effekt", "effect", "chance",
}


def gem_score_detail(gem, text):
    """Wie gem_score, gibt zusätzlich die 'Spezifität' zurück = Länge der getroffenen
    Phrase. Bei Score-Gleichstand gewinnt damit der spezifischere (längere) Treffer,
    z. B. 'Schwertchi-Kritrate' vor dem generischen 'Schwertchi-Koeffizient'."""
    nt = _norm(text)
    if not nt:
        return 0, 0
    ntset = set(nt.split())
    ntjoin = nt.replace(" ", "")
    best, best_spec = 0, 0
    for phrase in gem.get("match", []):
        np_ = _norm(phrase)
        if not np_:
            continue
        s = max(fuzz.partial_ratio(np_, nt), fuzz.token_set_ratio(np_, nt))
        if s < 90:
            # Teil-/Schwachtreffer: nur zählen, wenn ein unterscheidendes Wort wirklich vorkommt
            ok = any(len(w) >= 4 and w not in GENERIC_TOKENS and (w in ntset or w in ntjoin)
                     for w in np_.split())
            if not ok:
                continue
        if s > best:
            best, best_spec = s, len(np_)
        elif s == best and len(np_) > best_spec:
            best_spec = len(np_)
    return best, best_spec


def gem_score(gem, text):
    return gem_score_detail(gem, text)[0]


def best_match(text, slot):
    best, bs, bspec = None, -1, -1
    for g in GEMS.get(slot, []):
        sc, spec = gem_score_detail(g, text)
        if (sc, spec) > (bs, bspec):
            best, bs, bspec = g, sc, spec
    return best, bs


def classify_unknown(orig):
    """Versteht einen Stein am Wortsinn (DE+EN), robust gegen OCR-Worttrennung.
    -> (pve, pvp, cat_de, cat_en, cat_key)."""
    t = _norm(orig)
    td = t.replace(" ", "")
    # has(): findet Wort gespaced ODER mit OCR-Trennung (Vergleich ohne Leerzeichen)
    has = lambda *ws: any((w in t) or (w.replace(" ", "") in td) for w in ws)
    if (has("finaler schaden", "endschadensbonus", "endschaden", "final damage", "final dmg", "end damage")
            and not has("redu", "reduction")):
        return 95, 95, "Finaler Schaden (Top)", "Final Damage (Top)", "final"
    if has("finale schadensreduktion", "final damage reduction", "final dmg reduction") or (has("final") and has("redu")):
        return 78, 92, "Finale Schadensreduktion (Survival)", "Final Damage Reduction (Survival)", "survival"
    if has("pro 1 erlernte", "per learned skill", "for each skill learned") or \
            (has("erlernt", "gelernt", "learned") and has("fahigkeit", "fertigkeit", "skill")):
        return 90, 0, "+1% Schaden pro erlernter Fähigkeit (PvE)", "+1% DMG per learned skill (PvE)", "final"
    if has("koeffizient", "coefficient"):
        if has("wuttechnik", "rage"): return 86, 80, "Wuttechnik-Koeffizient", "Rage Coefficient", "rage"
        if has("schwertchi", "schwert chi", "sword chi", "sword qi", "sword aura", "klingen chi", "blood shadow sword qi"):
            return 55, 52, "Schwertchi-Koeffizient", "Sword Chi Coefficient", "swordchi"
        if has("dolch", "dagger"): return 82, 72, "Dolch-Koeffizient", "Dagger Coefficient", "dagger"
        if has("kombo", "combo"): return 84, 72, "Kombo-Koeffizient", "Combo Coefficient", "combo"
        if has("lichtspeer", "light spear"): return 24, 22, "Lichtspeer-Koeffizient (nur Lichtspeer-Builds)", "Light Spear Coefficient (light-spear builds only)", "coef_other"
        return 80, 72, "Schadens-Koeffizient (uncapped)", "Damage Coefficient (uncapped)", "coef_other"
    if has("komboanzahl", "kombo anzahl", "kombozahl", "combo count") or ("combo" in t and "+1" in t):
        return 100, 70, "Kombo-Anzahl +1 (Top)", "Combo Count +1 (Top)", "combo"
    if has("wut dolch", "wut-dolch", "wutdolch", "rage dagger") or (has("dolch", "dagger") and has("wut", "rage")):
        return 94, 92, "Wut-Dolch (Top)", "Rage Dagger (Top)", "rage"
    if has("komborate", "kombo-rate", "combo rate") or (has("kombo", "combo") and "rate" in t):
        return 88, 60, "Kombo-Rate", "Combo Rate", "combo"
    if has("konterrate", "counter rate") or (has("konter", "counter") and "rate" in t):
        return 58, 52, "Konterrate", "Counter Rate", "utility"
    if has("krit", "crit") and has("rate", "chance"):
        return 85, 70, "Krit-Rate", "Crit Rate", "crit"
    if has("krit", "crit") and has("schaden", "damage"):
        return 72, 70, "Krit-Schaden", "Crit Damage", "crit"
    if has("dolch", "dagger") and has("trifft", "treffer", "hit"):
        return 85, 80, "ATK bei Dolchtreffer", "ATK on dagger hit", "dagger"
    if (has("blitz", "lightning") and has("brennend", "burning")) or has("lahmchance", "lahmung", "paralys"):
        return 30, 62, "Blitz-Lähmung (brennendes Ziel, PvP)", "Lightning paralysis (burning target, PvP)", "control"
    if has("blitzschaden", "blitzschadensverstarkung", "lightning damage") or \
            (has("blitz", "lightning") and has("schaden", "damage")):
        return 50, 52, "Blitzschaden-Verstärkung", "Lightning Damage Boost", "atk"
    if has("dot dauer", "dot schaden", "dot duration", "dot damage", "schaden uber zeit") or \
            (("dot" in t) and has("dauer", "schaden", "damage", "duration")):
        return 52, 48, "DoT-Schaden/-Dauer (Brand/Gift)", "DoT damage/duration (burn/poison)", "conditional"
    if has("schild", "shield") and has("beginn", "kampfbeginn", "battle start", "start of battle", "hohe von"):
        return 55, 72, "Schild zu Kampfbeginn", "Shield at battle start", "survival"
    if has("heilt pro runde", "heilung pro runde", "heals per round", "heal per round"):
        return 45, 48, "Heilt pro Runde", "Heals per round", "survival"
    if has("schildgewinnung", "shield gain") or (has("schild", "shield") and has("verring", "redu", "reduce")):
        return 15, 40, "Anti-Schild (Nische)", "Anti-shield (niche)", "defensive"
    if has("verstummen", "schweigen", "silence"):
        return 25, 85, "Silence (PvP)", "Silence (PvP)", "pvp_ignore"
    if has("ignorieren", "ignore") and has("kombo", "combo", "krit", "crit"):
        return 16, 82, "Ignorieren-Stein (PvP)", "Ignore gem (PvP)", "pvp_ignore"
    if has("kontrollimmunitat", "control immunity") and has("ignor"):
        return 18, 85, "Kontrollimmunität ignorieren (PvP)", "Ignore Control Immunity (PvP)", "pvp_ignore"
    if has("kontrollimmunitat", "control immunity"):
        return 22, 60, "Kontrollimmunität (PvP)", "Control Immunity (PvP)", "control"
    if has("immun", "immune") and has("kontrolle", "control"):
        return 30, 92, "Immun gegen Kontrolle (PvP)", "Immune to Control (PvP)", "control"
    if has("immun", "immune") and has("schaden", "damage"):
        return 62, 88, "Immun gegen Schaden", "Immune to Damage", "survival"
    if has("betaub", "stun"):
        return 56, 50, "Stun-Chance", "Stun chance", "survival"
    if (has("heilung", "heilungseffekt", "heal", "healing") and has("haustier", "pet")):
        return 35, 40, "Haustier-Heilung", "Pet Healing", "defensive"
    if has("heilung", "heilt", "heilungseffekt", "heal", "healing"):
        return 38, 42, "Heilung", "Healing", "defensive"
    if has("lebensraub", "lifesteal", "life steal"):
        return 52, 45, "Lifesteal", "Lifesteal", "survival"
    if has("konter", "counter") and has("schaden", "damage") and has("redu", "verring", "reduction"):
        return 30, 44, "Konterschaden-Reduzierung (defensiv)", "Counter DMG Reduction (defensive)", "defensive"
    if has("konterschaden", "konterschadensverstarkung", "konterschaden verstark", "counter damage", "counter dmg") or \
            (has("konter", "counter") and has("schaden", "damage") and has("verstark", "boost", "erhoht")):
        return 48, 55, "Konterschaden-Verstärkung", "Counter Damage Boost", "utility"
    if has("beim konter", "on counter") and has("schaden", "damage") and not has("redu", "verring", "reduction"):
        return 50, 55, "Konter-Zusatzschaden (% max HP)", "Counter bonus damage (% max HP)", "utility"
    if has("globale verteidigung", "global defense") or (has("verteidigung", "defense") and not has("schaden", "damage")):
        return 30, 50, "Globale Verteidigung (defensiv)", "Global Defense (defensive)", "defensive"
    if has("physisch", "physical") and has("redu", "verring", "reduction"):
        return 46, 55, "Physische Schadensreduktion", "Physical DMG Reduction", "defensive"
    if has("normalschaden", "normalangriff", "normal attack damage", "basic attack damage", "normal damage"):
        return 48, 46, "Normalschaden-Verstärkung", "Normal Attack DMG Boost", "atk"
    if has("physisch", "physical") and has("schaden", "damage"):
        return 50, 48, "Physischer Schaden", "Physical Damage", "atk"
    if has("chance", "35") and has("2x schaden", "double damage", "2 schaden"):
        return 55, 45, "Basisangriff 2× Schaden-Chance", "Basic attack double-damage chance", "atk"
    if has("angriffskraft des gegners", "enemy atk") or (has("gegner", "enemy") and has("redu")):
        return 58, 75, "Gegner-ATK senken (defensiv)", "Lower enemy ATK (defensive)", "survival"
    if has("global") and has("atk", "angriff"):
        return 70, 67, "Globale ATK", "Global ATK", "atk"
    if has("uber 70", "mehr als 70", "over 70", "above 70", "more than 70") or \
            (has("zielen", "ziele", "targets") and ("70" in t) and has("hp", "leben", "health")):
        return 32, 40, "Schaden an Zielen >70% HP", "DMG to targets >70% HP", "conditional"
    if has("lebenspunkte", "globale lp", "global hp", "global health"):
        return 28, 45, "Globale LP (defensiv)", "Global HP (defensive)", "defensive"
    if has("gegen bosse", "boss schaden", "schaden an bossen", "dmg vs boss", "boss damage", "vs boss"):
        return 80, 12, "Schaden gegen Bosse (PvE)", "DMG vs Boss (PvE)", "conditional"
    if (has("ziele mit schild", "abgeschirmte", "mit schild", "geschutzte ziele",
            "geschutzten zielen", "shielded targets", "guarded targets", "dmg to shielded")
            or (has("schild", "shield", "geschutzt", "guarded") and has("ziele", "ziel", "targets")
                and has("schaden", "damage"))):
        return 25, 72, "Schaden gegen geschützte Ziele (PvP)", "DMG to shielded targets (PvP)", "conditional"
    if has("geschwindigkeit", "tempo", "initiative") or (("speed" in t) and not has("schaden", "damage")):
        return 28, 80, "Geschwindigkeit (PvP wichtig)", "Speed (important in PvP)", "utility"
    if has("stiehlt", "stehlen", "steal"):
        return 84, 80, "ATK stehlen", "Steal ATK", "atk"
    if has("schaden", "damage") and has("redu", "verring", "reduction"):
        return 42, 52, "Schadensreduktion (defensiv)", "Damage Reduction (defensive)", "defensive"
    if has("angriff", "atk", "verstark"):
        return 65, 63, "Angriff/ATK-Boost", "Attack/ATK boost", "atk"
    return 50, 50, "Sonstiges (unklar)", "Other (unclear)", "atk"


def clean_name(orig):
    s = re.sub(r"\[?\s*(einzigartig|unique)\s*\]?", "", orig, flags=re.IGNORECASE)
    s = re.sub(r"\s+", " ", s).strip(" :,-·")
    return (s[:48].rstrip() + "…") if len(s) > 50 else s


def _auto_gem(orig):
    pve, pvp, cde, cen, ckey = classify_unknown(orig)
    name = clean_name(orig) or "?"
    unknown = (cde == "Sonstiges (unklar)")
    return dict(id="auto:" + name[:16], de=name, en=name, pve=pve, pvp=pvp, cat=ckey,
                note_de="≈ aus Text: " + cde, note_en="≈ from text: " + cen,
                auto=True, unknown=unknown)


# ---- Rauschfilter ----
NOISE = ["voreinstellung", "preset", "zubehorteil", "edelstein effekt", "gem effect",
         "edelstein attribut", "gem attribute", "edelstein", "menge", "amount", "im besitz",
         "owned", "veredeln", "refine", "einbetten", "embed", "freigeschaltet", "unlocked",
         "gottliche schmiedung", "divine forge", "schmiedung", "ausrustung", "equipment",
         "unvergleichlich", "incomparable", "unsterblich", "immortal", "mythisch", "mythic",
         "uberragend", "outstanding"]


# Kurze Label-Wörter, die NUR exakt (nicht per Teilstring) Rauschen sind – sonst würde
# z. B. „Waffe“ fälschlich „Waffenkrit“ treffen oder „Ring“ ein echtes Effektwort schlucken.
EXACT_NOISE = {"waffe", "rustung", "ring", "halskette", "weapon", "armor", "accessory",
               "necklace", "mythisch", "mythic", "lv", "ex", "stufe", "level", "menge", "amount",
               "normal", "selten", "rare", "episch", "epic", "legendar", "legendary"}


def _is_noise(text):
    nt = _norm(text)
    if not nt or len(nt) < 3:
        return True
    if nt in EXACT_NOISE:        # exaktes Label-Wort (z. B. „Waffe“, „Ring“) -> raus
        return True
    for ph in NOISE:
        if fuzz.partial_ratio(ph, nt) >= 86:
            return True
    if re.fullmatch(r"[^a-z]*", nt):
        return True
    return False


def filter_noise(items):
    return [it for it in items if not _is_noise(it[0])]


def cluster_into_lines(items):
    if not items:
        return []
    items = sorted(items, key=lambda t: t[2])
    hs = [t[3] for t in items if t[3] > 0]
    med = statistics.median(hs) if hs else 20
    blocks, cur = [], [items[0]]
    for prev, it in zip(items, items[1:]):
        if it[2] - prev[2] > 1.7 * med:
            blocks.append(cur); cur = [it]
        else:
            cur.append(it)
    blocks.append(cur)
    out = []
    for b in blocks:
        b2 = sorted(b, key=lambda t: (round(t[2] / max(1, med)), t[1]))
        out.append(" ".join(t[0] for t in b2))
    return out


def _attr_after_marker(raw):
    """Text nach dem 'Edelstein-Attribut'/'Gem Attribute'-Marker = Eigenschaft des
    ANGEWÄHLTEN Steins (Detailkarte). None, wenn kein Marker vorhanden."""
    parts = re.split(r"attribut|attribute", raw, maxsplit=1, flags=re.IGNORECASE)
    return parts[1].strip(" :\t\n·") if len(parts) > 1 else None


def detect_equipped(items, slot):
    """Erkennt ALLE ausgerüsteten Steine eines Slots (kein Limit): per Zeile (DB-Match
    ≥Schwelle, sonst classify_unknown) PLUS Blob-Suche für verklebte OCR-Zeilen.
    Dedupliziert nach Anzeigenamen.

    WICHTIG: Die Eigenschaft des ANGEWÄHLTEN Steins (Detailkarte, alles nach
    „Edelstein-Attribut“) zählt NIE als ausgerüstet – sonst meldet das Tool den
    gerade gewählten Stein fälschlich als „schon drin“, wenn Bereich 1 versehentlich
    die Auswahl-Karte statt der Effekt-Boxen erfasst.
    -> (liste[(gem, conf)], lines, card_seen)."""
    raw = " ".join(t[0] for t in items)
    card_txt = _attr_after_marker(raw)
    card_de, card_seen = None, bool(card_txt)
    if card_txt:
        cg, cs = best_match(card_txt, slot)
        if cg and cs >= 80:
            card_de = cg["de"]
    items = filter_noise(items)
    lines = cluster_into_lines(items)
    nblob = _norm(" ".join(t[0] for t in items)).replace(" ", "")
    found = {}
    for ln in lines:
        g, sc = best_match(ln, slot)
        if g and sc >= 80:   # streng (wie Schnell-Scan/Kandidat) – verhindert Fuzzy-Fehltreffer
            key = g["de"]
            if key not in found or sc > found[key][1]:
                found[key] = (g, sc)
        elif len(_norm(ln)) >= 6:
            ag = _auto_gem(ln)
            if not ag["unknown"]:
                found.setdefault(ag["de"], (ag, 72))
    for g in GEMS.get(slot, []):
        if g["de"] in found:
            continue
        for ph in g.get("match", []):
            p = _norm(ph).replace(" ", "")
            if len(p) >= 7 and p in nblob:
                found[g["de"]] = (g, 90)
                break
    if card_de:                      # Eigenschaft des angewählten Steins entfernen
        found.pop(card_de, None)
    return sorted(found.values(), key=lambda x: -x[1]), lines, card_seen


def detect_candidate(items, slot):
    blob = " ".join(t[0] for t in items)
    parts = re.split(r"attribut|attribute", blob, maxsplit=1, flags=re.IGNORECASE)
    attr = parts[1].strip(" :\t\n·") if len(parts) > 1 else blob
    best, bs, bspec = None, -1, -1
    for g in GEMS.get(slot, []):
        sc, spec = gem_score_detail(g, attr)
        if (sc, spec) > (bs, bspec):
            best, bs, bspec = g, sc, spec
    if best and bs >= 80:
        gem = dict(best); gem["auto"] = False; gem["unknown"] = False
        return gem, bs, blob
    return _auto_gem(attr), bs, blob


def top_matches(text, slot, lang, k=4):
    out = []
    for g in GEMS.get(slot, []):
        out.append((g[lang], gem_score(g, text)))
    return sorted(out, key=lambda x: -x[1])[:k]


def best_match_any(text):
    """Bester Treffer über ALLE Slots – für Schnell-Scan, da der Slot unbekannt ist."""
    best, bs, bspec = None, -1, -1
    for slot in SLOT_KEYS:
        for g in GEMS.get(slot, []):
            sc, spec = gem_score_detail(g, text)
            if (sc, spec) > (bs, bspec):
                best, bs, bspec = g, sc, spec
    return best, bs


def detect_quick(items):
    """Schnell-Scan: erkennt ALLE Edelstein-Zeilen einer Region, dedupliziert nach Namen.
    Nutzt dieselben Bausteine wie der Slot-Scan (Rauschfilter, Zeilen-Cluster, DB-Match
    ≥80 % sonst classify_unknown) PLUS eine Blob-Suche: jedes DB-Stichwort wird auch im
    gesamten Text gesucht, falls die Zeilen-Trennung zwei Kästen verklebt hat.
    -> (liste[(gem, conf)], lines, n_unklar)."""
    items = filter_noise(items)
    lines = cluster_into_lines(items)
    nblob = _norm(" ".join(t[0] for t in items)).replace(" ", "")
    found, unclear = {}, 0
    for ln in lines:
        if len(_norm(ln)) < 6:
            continue
        g, sc = best_match_any(ln)
        if g and sc >= 80:
            gem = dict(g); gem["auto"] = False; gem["unknown"] = False
            key = gem["de"]
            if key not in found or sc > found[key][1]:
                found[key] = (gem, sc)
        else:
            ag = _auto_gem(ln)
            if not ag["unknown"]:
                found.setdefault(ag["de"], (ag, 72))
            else:
                unclear += 1
    # Blob-Ergänzung: Steine fangen, deren Text durch das Zeilen-Clustering zerrissen wurde.
    # Exakte (entzwischenraumte) Teilstring-Suche -> präzise, keine Fuzzy-Fehltreffer.
    for slot in SLOT_KEYS:
        for g in GEMS.get(slot, []):
            if g["de"] in found:
                continue
            for ph in g.get("match", []):
                p = _norm(ph).replace(" ", "")
                if len(p) >= 7 and p in nblob:
                    gem = dict(g); gem["auto"] = False; gem["unknown"] = False
                    found[g["de"]] = (gem, 90)
                    break
    return list(found.values()), lines, unclear


# ============================================================================
#  SKILLS  (Skill-Berater: welche Fähigkeit lernen / meiden)
# ============================================================================
# Wort-Glossar DE->EN, um Namen unbekannter Skills im EN-Modus grob zu übersetzen
# (der rohe Skill-Name kommt vom deutschen Spiel; bekannte Skills haben echte EN-Namen).
SKILL_GLOSS = {
    "wutdolch": "rage dagger", "wutblitz": "rage bolt", "wutfahigkeit": "rage skill", "wut": "rage",
    "dolch": "dagger", "dolche": "daggers", "blitz": "lightning", "blitze": "bolts",
    "kombo": "combo", "krit": "crit", "kritische": "critical", "kritisch": "critical",
    "konter": "counter", "schild": "shield", "schaden": "damage", "angriff": "attack",
    "angriffe": "attacks", "angriffen": "attacks", "heilung": "heal", "heilt": "heals",
    "leben": "HP", "lp": "HP", "runde": "round", "runden": "rounds", "feinde": "enemies",
    "gegner": "enemy", "verteidigung": "DEF", "vtdg": "DEF", "ang": "ATK", "vergiften": "poison",
    "vergiftete": "poisoned", "waffe": "weapon", "beginn": "start", "kampfes": "battle",
    "kampf": "battle", "kampfschrei": "battle cry", "wirft": "throws", "erhohen": "increase",
    "immun": "immune", "ausweichen": "dodge", "lebensraub": "lifesteal",
    "beginn des": "start of", "des kampfes": "of battle",
}


def tr_skill_name(de):
    """Übersetzt einen (deutschen) Skill-Namen grob ins Englische per Wort-Glossar.
    Unbekannte Wörter/Zahlen bleiben stehen. Nur Best-Effort für unbekannte Skills."""
    out = []
    for w in re.split(r"(\s+)", de):
        lw = w.strip().lower()
        if lw in SKILL_GLOSS:
            out.append(SKILL_GLOSS[lw])
        else:
            out.append(w)
    res = re.sub(r"\s+", " ", "".join(out)).strip()
    return res or de


def classify_skill(orig):
    """Versteht einen Skill am Wortsinn (DE+EN), wenn er nicht in skills.json steht.
    -> skill-Dict (pve/pvp/cat) für die Build-Bewertung."""
    t = _norm(orig)
    td = t.replace(" ", "")
    has = lambda *ws: any((w in t) or (w.replace(" ", "") in td) for w in ws)
    name = clean_name(orig) or "?"
    name_en = tr_skill_name(name)

    def mk(pve, pvp, cat, cde, cen, unknown=False):
        return dict(id="auto:" + name[:16], de=name, en=name_en, pve=pve, pvp=pvp, cat=cat,
                    tier="?", note_de="≈ " + cde, note_en="≈ " + cen, auto=True, unknown=unknown)

    if has("vergift", "gift", "poison", "toxin"):
        return mk(40, 40, "fire", "Gift-Skill (skaliert nur in DoT/Gift-Builds)",
                  "Poison skill (scales only in DoT/poison builds)")
    if has("dolch", "dagger"):
        # Dolch-Skills (auch „Wutdolch") = mehr Dolche = mehr Angriffe -> Dolch-Builds
        return mk(74, 70, "dagger", "Dolch-Skill (mehr Dolche/Angriffe)",
                  "Dagger skill (more daggers/attacks)")
    if has("kombo", "combo"):
        return mk(72, 70, "combo", "Kombo-Skill", "Combo skill")
    if has("wut", "rage"):
        return mk(72, 72, "rage", "Wut-Skill", "Rage skill")
    if has("krit", "crit", "kritisch"):
        return mk(70, 68, "crit", "Krit-Skill", "Crit skill")
    if has("konter", "counter"):
        return mk(60, 64, "utility", "Konter-Skill", "Counter skill")
    if has("blitz", "lightning", "bolt", "donner"):
        return mk(55, 53, "lightning", "Blitz-Skill (nur Blitz-Builds)", "Lightning skill (lightning builds)")
    if has("schwertchi", "sword chi", "sword qi"):
        return mk(45, 44, "swordchi", "Schwertchi-Skill", "Sword-chi skill")
    if has("lichtspeer", "light spear"):
        return mk(22, 22, "coef_other", "Lichtspeer-Skill (Nische)", "Light-spear skill (niche)")
    if has("feuer", "brand", "verbrenn", "fire", "burn", "flamm"):
        return mk(48, 46, "fire", "Feuer/Brand-Skill", "Fire/burn skill")
    if has("schadensreduktion", "schaden reduz", "damage reduction") or (has("schaden", "damage") and has("redu")):
        return mk(68, 74, "defensive", "Schadensreduktion (Survival)", "Damage reduction (survival)")
    if has("schild", "shield"):
        return mk(64, 70, "survival", "Schild-Skill (Survival)", "Shield skill (survival)")
    if has("ausweich", "dodge") or (has("immun", "immune")):
        return mk(60, 66, "survival", "Ausweichen/Immunität", "Dodge/immunity")
    if has("betaub", "stun", "einfrier", "freeze", "frost", "verlangsam", "kontrolle", "control", "silence", "schweigen"):
        return mk(58, 72, "control", "Kontroll-Skill", "Control skill")
    if has("heilung", "heilt", "heal", "lebensraub", "lifesteal", "leben", "wiederbeleb", "revive"):
        return mk(56, 60, "survival", "Heilung/Survival", "Heal/survival")
    if has("basisangriff", "normalangriff", "basic attack", "normal attack"):
        return mk(64, 60, "atk", "Basisangriff-Skill", "Basic-attack skill")
    if has("angriff", "atk", "schaden", "damage", "starke", "verstark"):
        return mk(64, 60, "atk", "Angriff/Schaden-Skill", "Attack/damage skill")
    return mk(50, 48, "atk", "Sonstiger Skill (unklar)", "Other skill (unclear)", unknown=True)


def best_skill(text):
    """Bester Treffer in skills.json (Tie-Break: spezifischere Phrase gewinnt)."""
    best, bs, bspec = None, -1, -1
    for sk in SKILLS_DB.get("skills", []):
        sc, spec = gem_score_detail(sk, text)
        if (sc, spec) > (bs, bspec):
            best, bs, bspec = sk, sc, spec
    return best, bs


def detect_skills(items):
    """Erkennt die angebotenen Skills einer Region (gespiegelt an detect_quick):
    Zeilen-Match >=80 gegen skills.json, sonst Wort-Verständnis, plus Blob-Suche.
    -> liste[(skill, conf)]."""
    items = filter_noise(items)
    lines = cluster_into_lines(items)
    nblob = _norm(" ".join(t[0] for t in items)).replace(" ", "")
    found = {}
    covered = []   # entzwischenraumte Phrasen bereits erkannter kuratierter Skills (Dedup)
    # 1) Kuratierte Skills zuerst per Blob-Suche (fängt auch verklebte OCR) – echte EN-Namen.
    for sk in SKILLS_DB.get("skills", []):
        for ph in sk.get("match", []):
            p = _norm(ph).replace(" ", "")
            if len(p) >= 6 and p in nblob:
                if sk["en"] not in found:
                    found[sk["en"]] = (dict(sk, auto=False, unknown=False), 88)
                covered.append(p)
                break
    # 2) Pro Zeile: kuratierter Treffer >=80, sonst Wort-Verständnis (nur falls nicht schon
    #    von einem kuratierten Skill abgedeckt -> verhindert Doppel-Einträge / DE-Dubletten).
    for ln in lines:
        if len(_norm(ln)) < 5:
            continue
        lj = _norm(ln).replace(" ", "")
        sk, sc = best_skill(ln)
        if sk and sc >= 80:
            key = sk["en"]
            if key not in found or sc > found[key][1]:
                found[key] = (dict(sk, auto=False, unknown=False), sc)
            continue
        if any(p in lj for p in covered):
            continue
        ag = classify_skill(ln)
        if not ag.get("unknown"):
            found.setdefault(ag["de"], (ag, 70))
    return list(found.values())


# Effekt-Stichwörter (DE+EN) -> Edelstein-Kategorie, für die Build-Eignung eines Helden.
HERO_EFFECT_KW = [
    (["basisangriff", "normalangriff", "normalschaden"], ["basic attack", "normal attack"],
     "atk", "Basisangriff", "Basic attack"),
    (["kombo"], ["combo"], "combo", "Kombo", "Combo"),
    (["wut", "fertigkeit", "skill"], ["rage", "skill"], "rage", "Skill/Wut", "Skill/Rage"),
    (["schild"], ["shield"], "survival", "Schild", "Shield"),
    (["konter"], ["counter"], "utility", "Konter", "Counter"),
    (["krit"], ["crit"], "crit", "Krit", "Crit"),
]


def _hero_pct(blob, keys):
    """Sucht 'Label … +NN%' im Rohtext (behält %), gibt den ersten Treffer zurück."""
    for k in keys:
        m = re.search(re.escape(k) + r"[^0-9%+\-]{0,10}([+\-]?\d{1,3}(?:[.,]\d+)?\s*%)",
                      blob, flags=re.IGNORECASE)
        if m:
            return re.sub(r"\s+", "", m.group(1))
    return None


def analyze_hero(blob):
    """Liest eine Helden-Detailseite: Rang (+N), die drei Roh-Boni (LP/ANG/VTDG)
    und Effekt-Stichwörter. -> dict. Nur lesbarer Text wird ausgewertet (keine Icons)."""
    t = _norm(blob)
    rank_de = rank_en = None
    plus = 0
    m = re.search(r"(mythisch|mythic)\s*\+?\s*(\d+)", t)
    if m:
        plus = int(m.group(2)); rank_de = "Mythisch+%d" % plus; rank_en = "Mythic+%d" % plus
    elif "mythisch" in t or "mythic" in t:
        rank_de, rank_en = "Mythisch", "Mythic"
    elif "legend" in t:
        rank_de, rank_en = "Legendär", "Legendary"
    lp = _hero_pct(blob, ["Lebenspunkte", "Leben", "LP", "HP", "Health"])
    ang = _hero_pct(blob, ["Angriffskraft", "Angriff", "ANG", "ATK", "Attack"])
    vtdg = _hero_pct(blob, ["Verteidigung", "VTDG", "DEF", "Defense"])
    kw = []
    for de_ws, en_ws, cat, lde, len_ in HERO_EFFECT_KW:
        if any(w in t for w in de_ws) or any(w in t for w in en_ws):
            kw.append((cat, lde, len_))
    return dict(rank_de=rank_de, rank_en=rank_en, plus=plus,
                lp=lp, ang=ang, vtdg=vtdg, kw=kw)


# ================================================================== #
#  THEME                                                             #
# ================================================================== #
# Zwei umschaltbare Themes (Button im Kopf) – beide in den Capybara-Bild-Farben,
# KEIN Pink:
#  • light = heller Himmel-Look (Himmelblau/Weiß/Gold) – Akzente mittel-dunkel
#  • dark  = Nachthimmel-Look (dunkles Navy, Himmelblau-Buttons, Gold, Türkis, Gras-Grün)
# Badge-/Button-Schrift wird per _text_on() automatisch hell/dunkel gewählt.
THEMES = {
    "light": dict(BG="#c9e6f3", PANEL="#ffffff", PANEL2="#dfeef7", BORDER="#a7cee0",
                  TEXT="#39291e", DIM="#76675b", PURPLE="#1f8fc7", TEAL="#0f8f9c",
                  GOLD="#b8810c", RED="#d8442b", GREEN="#4f9e2f", AMBER="#cf7d12",
                  TIERS=[("S", "#b8810c"), ("A", "#0f8f9c"), ("B", "#2f6fc0"),
                         ("C", "#c5631a"), ("D", "#6f7d88")]),
    "dark": dict(BG="#141b24", PANEL="#1f2a35", PANEL2="#2a3744", BORDER="#3a4b5a",
                 TEXT="#eaf1f6", DIM="#93a7b5", PURPLE="#2f9bd6", TEAL="#2dd4bf",
                 GOLD="#f5c451", RED="#ef6a5a", GREEN="#5cc46a", AMBER="#f5b340",
                 TIERS=[("S", "#f5c451"), ("A", "#2dd4bf"), ("B", "#7c9bf2"),
                        ("C", "#f5b340"), ("D", "#9aa6b0")]),
}
_THEME = "light"
TIERS = THEMES["light"]["TIERS"]
BG = PANEL = PANEL2 = BORDER = TEXT = DIM = PURPLE = TEAL = GOLD = RED = GREEN = AMBER = "#000000"


def apply_theme(name):
    """Setzt die globalen Farb-Variablen auf das gewählte Theme (hell/dunkel)."""
    global _THEME, TIERS, BG, PANEL, PANEL2, BORDER, TEXT, DIM, PURPLE, TEAL, GOLD, RED, GREEN, AMBER
    _THEME = name if name in THEMES else "light"
    t = THEMES[_THEME]
    BG = t["BG"]; PANEL = t["PANEL"]; PANEL2 = t["PANEL2"]; BORDER = t["BORDER"]
    TEXT = t["TEXT"]; DIM = t["DIM"]; PURPLE = t["PURPLE"]; TEAL = t["TEAL"]; GOLD = t["GOLD"]
    RED = t["RED"]; GREEN = t["GREEN"]; AMBER = t["AMBER"]; TIERS = t["TIERS"]


apply_theme("light")


class RegionSelector:
    def __init__(self, root, title, on_done):
        self.on_done = on_done; self.start = None; self.rect = None
        self.top = tk.Toplevel(root)
        # Über ALLE Monitore spannen (virtueller Desktop) -> Markieren auf Monitor 1-4 möglich.
        vx = vy = 0
        vw, vh = self.top.winfo_screenwidth(), self.top.winfo_screenheight()
        try:
            import ctypes
            u = ctypes.windll.user32
            vx, vy = u.GetSystemMetrics(76), u.GetSystemMetrics(77)   # SM_X/YVIRTUALSCREEN
            vw, vh = u.GetSystemMetrics(78), u.GetSystemMetrics(79)   # SM_C X/Y VIRTUALSCREEN
            self.top.overrideredirect(True)
            self.top.geometry("%dx%d+%d+%d" % (vw, vh, vx, vy))
        except Exception:
            self.top.attributes("-fullscreen", True)
        try:
            self.top.attributes("-alpha", 0.30)
        except Exception:
            pass
        self.top.configure(bg="#000000"); self.top.attributes("-topmost", True)
        self.cv = tk.Canvas(self.top, cursor="cross", bg="#000000", highlightthickness=0)
        self.cv.pack(fill="both", expand=True)
        # Titel mittig auf dem PRIMÄR-Monitor platzieren (Canvas-Ursprung = virtueller Ursprung)
        self.cv.create_text((-vx) + self.top.winfo_screenwidth() // 2, max(40, (-vy) + 40),
                            text=title, fill="#ffffff", font=("Segoe UI", 15, "bold"))
        self.cv.bind("<ButtonPress-1>", self._press)
        self.cv.bind("<B1-Motion>", self._drag)
        self.cv.bind("<ButtonRelease-1>", self._release)
        self.top.bind("<Escape>", lambda e: self.top.destroy())

    def _press(self, e):
        self.start = (e.x_root, e.y_root)
        if self.rect:
            self.cv.delete(self.rect)
        self.rect = self.cv.create_rectangle(e.x, e.y, e.x, e.y, outline="#4ecdb0", width=3)

    def _drag(self, e):
        if self.rect and self.start:
            self.cv.coords(self.rect, self.start[0] - self.top.winfo_rootx(),
                           self.start[1] - self.top.winfo_rooty(),
                           e.x_root - self.top.winfo_rootx(), e.y_root - self.top.winfo_rooty())

    def _release(self, e):
        if not self.start:
            self.top.destroy(); return
        x1, y1 = self.start; x2, y2 = e.x_root, e.y_root
        region = {"left": int(min(x1, x2)), "top": int(min(y1, y2)),
                  "width": int(abs(x2 - x1)), "height": int(abs(y2 - y1))}
        self.top.destroy()
        if region["width"] > 10 and region["height"] > 10:
            self.on_done(region)


# ================================================================== #
#  OCR                                                               #
# ================================================================== #
_engine = None
_engine_err = None

# OCR-Threads begrenzen -> deutlich weniger CPU-Last (v41).
# onnxruntime nutzt sonst ALLE Kerne pro Erkennung; jeder (Auto-)Scan schießt
# damit kurz alle Kerne auf ~100 %. 2 Threads = niedriger Ausschlag, kaum
# langsamer (für den Auto-Scan völlig unkritisch). Wert nach Bedarf justierbar.
OCR_THREADS = 2


def get_engine():
    global _engine, _engine_err
    if _engine is None and _engine_err is None:
        try:
            # Diese rapidocr-Version reicht keinen Thread-Parameter durch und baut
            # ihre SessionOptions OHNE intra_op_num_threads (-> alle Kerne). Wir
            # ersetzen die SessionOptions-Klasse im rapidocr-Modul defensiv durch
            # eine, die die Thread-Zahl begrenzt. Schlägt das fehl (andere
            # Version), läuft OCR normal weiter – nur ohne Begrenzung.
            try:
                from rapidocr_onnxruntime import utils as _ro_utils
                _BaseSO = _ro_utils.SessionOptions

                def _limited_session_options(*a, **k):
                    so = _BaseSO(*a, **k)
                    try:
                        so.intra_op_num_threads = OCR_THREADS
                        so.inter_op_num_threads = OCR_THREADS
                    except Exception:
                        pass
                    return so

                _ro_utils.SessionOptions = _limited_session_options
            except Exception:
                pass

            from rapidocr_onnxruntime import RapidOCR
            _engine = RapidOCR()
        except Exception as e:
            _engine_err = e
    return _engine


_tls = threading.local()


def _thread_sct():
    """Pro Thread EINE wiederverwendete mss-Instanz, statt bei jedem Grab eine
    neue zu erzeugen (spart Grundlast). mss ist nicht thread-sicher -> deshalb
    thread-lokal, nicht global geteilt."""
    s = getattr(_tls, "sct", None)
    if s is None:
        s = mss.mss()
        _tls.sct = s
    return s


def ocr_detailed(region):
    shot = _thread_sct().grab(region)
    img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
    g = img.convert("L")
    g = ImageOps.autocontrast(g)
    w, h = g.size
    g = g.resize((max(1, w * 2), max(1, h * 2)))
    arr = np.array(g.convert("RGB"))
    eng = get_engine()
    if eng is None:
        raise RuntimeError("OCR-Engine: %s" % _engine_err)
    res, _ = eng(arr)
    items = []
    if res:
        for it in res:
            try:
                box, text = it[0], it[1]
                ys = [p[1] for p in box]; xs = [p[0] for p in box]
                items.append((str(text), sum(xs) / len(xs), sum(ys) / len(ys), max(ys) - min(ys)))
            except Exception:
                continue
    return items, " ".join(t[0] for t in items)


# ================================================================== #
#  APP                                                               #
# ================================================================== #
class App:
    def __init__(self, root):
        self.root = root
        self.cfg = load_config()
        self.lang = self.cfg.get("lang", "de")
        self.theme = self.cfg.get("theme", "light")
        apply_theme(self.theme)
        self.view = "quick"
        self.slot = "Accessory"
        self.mode = "pve"
        self.slot_count = dict(DEFAULT_FREE)   # freie (leere) Slots je Ausrüstung
        self.slot_count.update(self.cfg.get("free_slots", {}))
        self.build = self.cfg.get("build", BUILD_NAMES[0])
        if self.build not in BUILD_NAMES:
            self.build = BUILD_NAMES[0]
        self.region_eq = self.cfg.get("region_equipped")
        self.region_cand = self.cfg.get("region_candidate")
        self.region_quick = self.cfg.get("region_quick")
        self.region_hero = self.cfg.get("region_hero")
        self.region_skill = self.cfg.get("region_skill")
        self.equipped = {}     # slot -> [(gem, score)]
        self._eq_card_seen = False  # Bereich 1 hat die Auswahl-Karte erfasst (Warnhinweis)
        self.candidate = None
        self.cand_conf = 0
        self.manual_menu = None
        self._manual_slot = None
        self.show_debug = tk.BooleanVar(value=False)
        self.dbg_eq = ""; self.dbg_cand = ""
        self.prev_eq = ""; self.prev_cand = ""
        self.slot_btns = {}
        self.quick_results = []      # [(gem, conf)] aus Schnell-Scan
        self.quick_unclear = 0
        self.dbg_quick = ""; self.prev_quick = ""
        self.hero_scans = {}         # slot_key -> info  (Mehrfach: eq1/eq2/res1..res4)
        self.hero_btns = {}          # slot_key -> Button
        self.dbg_hero = ""; self.prev_hero = ""
        self.skill_results = []      # [(skill, conf)] aus Skill-Scan
        self.dbg_skill = ""; self.prev_skill = ""
        self.scan_auto = tk.BooleanVar(value=False)    # Slot-Auto-Scan (Edelsteine) an/aus
        self._scan_loop_running = False
        self._scan_busy = False
        # Frame-Puffer für die Änderungs-Erkennung (klein, Graustufen) – verhindert
        # OCR bei Animationen/Flackern; OCR nur bei deutlicher, ruhiger Änderung.
        self._cand_prev = self._cand_scanned = None
        self._eq_prev = self._eq_scanned = None
        self.run_skills = self.cfg.get("run_skills", [])  # in diesem Lauf gewählte Skills [{name,cat}]
        self.skill_auto = tk.BooleanVar(value=False)   # Skill-Auto-Scan an/aus
        self._skill_loop_running = False               # läuft die Überwachungsschleife?
        self._skill_busy = False                       # gerade ein (Auto-)Scan aktiv?
        self._skill_prev = self._skill_scanned = None

        root.title("Capybara Gem Scanner")
        root.configure(bg=BG)
        # Schrift an die echte Bildschirm-DPI koppeln -> scharf UND korrekt groß.
        # Fenster proportional mitskalieren, damit das Layout gleich groß bleibt.
        try:
            sc = max(1.0, root.winfo_fpixels("1i") / 96.0)
            root.tk.call("tk", "scaling", root.winfo_fpixels("1i") / 72.0)
        except Exception:
            sc = 1.0
        self._ui_scale = sc
        # Fensterhöhe an die Bildschirmhöhe anpassen (Taskleiste lassen), damit unten
        # nichts abgeschnitten wird. Alle Tabs sind scrollbar -> kleinere Fenster sind ok.
        win_w = int(600 * sc)
        try:
            scr_h = root.winfo_screenheight()
        except Exception:
            scr_h = int(1000 * sc)
        win_h = min(int(980 * sc), max(int(560 * sc), scr_h - int(70 * sc)))
        root.geometry("%dx%d" % (win_w, win_h))
        root.minsize(int(520 * sc), int(460 * sc))
        self._build()
        self._render()
        if DATA_WARN:
            self.root.after(400, lambda: messagebox.showwarning("gems.json", DATA_WARN))

    def _t(self, de, en):
        return de if self.lang == "de" else en

    def _q(self, s):
        # sprachgerechte Anführungszeichen für die Detail-Ausgabe
        return ("„%s“" % s) if self.lang == "de" else ('"%s"' % s)

    def _gname(self, g):
        return g.get(self.lang) or g.get("de") or g.get("en") or "?"

    def _bname(self, key):
        """Anzeigename des Builds je Sprache (interner Schlüssel bleibt der DE-Name)."""
        return BUILD_EN.get(key, key) if self.lang == "en" else key

    def _gnote(self, g):
        return g.get("note_" + self.lang) or g.get("note_de") or g.get("note_en") or ""

    def _sname(self, key):
        return SLOT_DISP[key][0 if self.lang == "de" else 1]

    def _score(self, g):
        base = g["pve"] if self.mode == "pve" else g["pvp"]
        mult = BUILD_PREFS.get(self.build, {}).get(g.get("cat", "atk"), 1.0)
        return int(round(min(100, base * mult)))

    # ---------- Capybara-Banner ----------
    @staticmethod
    def _hex(h):
        h = h.lstrip("#")
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

    @staticmethod
    def _text_on(hx):
        """Lesbare Schriftfarbe (hell/dunkel) für eine farbige Fläche – funktioniert
        in beiden Themes (helle Tier-Farben -> dunkle Schrift, dunkle -> weiße)."""
        r, g, b = App._hex(hx)
        return "#15121c" if (0.299 * r + 0.587 * g + 0.114 * b) > 150 else "#ffffff"

    def _gradient_banner(self, w, h):
        """Erzeugt einen Farbverlauf-Banner (Pink-Glow links, Türkis-Glow rechts,
        dunkle Mitte) als Fallback, falls kein eigenes Capybara-Bild vorhanden ist."""
        from PIL import Image, ImageDraw
        bg = self._hex(BG); pk = self._hex(PURPLE); tl = self._hex(TEAL); gd = self._hex(GOLD)
        img = Image.new("RGB", (w, h), bg); px = img.load()
        for x in range(w):
            t = x / max(1, w - 1)
            for y in range(h):
                vy = 1 - abs((y / max(1, h - 1)) - 0.5) * 2
                r = bg[0] + (pk[0] - bg[0]) * (1 - t) * 0.55 * vy + (tl[0] - bg[0]) * t * 0.55 * vy
                g = bg[1] + (pk[1] - bg[1]) * (1 - t) * 0.55 * vy + (tl[1] - bg[1]) * t * 0.55 * vy
                b = bg[2] + (pk[2] - bg[2]) * (1 - t) * 0.55 * vy + (tl[2] - bg[2]) * t * 0.55 * vy
                px[x, y] = (min(255, int(r)), min(255, int(g)), min(255, int(b)))
        d = ImageDraw.Draw(img)
        cy = int(h * 0.5)
        for i, cx in enumerate(range(int(w * 0.30), int(w * 0.72), int(w * 0.105) or 1)):
            s = int(h * (0.12 + 0.02 * (i % 2)))
            col = gd if i % 2 == 0 else tl
            d.polygon([(cx, cy - s), (cx + s, cy), (cx, cy + s), (cx - s, cy)], fill=col)
        return img

    def _banner_fade(self, img):
        """Unteren Rand weich in den hellen UI-Hintergrund auslaufen lassen."""
        bg = self._hex(BG); w, h = img.size; px = img.load()
        fade = max(1, int(h * 0.13))
        for y in range(h - fade, h):
            a = (y - (h - fade)) / fade
            for x in range(w):
                r, g, b = px[x, y]
                px[x, y] = (int(r + (bg[0] - r) * a), int(g + (bg[1] - g) * a), int(b + (bg[2] - b) * a))

    def _make_banner(self, parent):
        """Banner ganz oben: nutzt 'capybara_banner.(png|jpg)' aus dem Tool-Ordner,
        sonst einen erzeugten Farbverlauf. Bricht den Start nie ab."""
        try:
            from PIL import Image, ImageTk
        except Exception:
            return
        try:
            sc = getattr(self, "_ui_scale", 1.0)
            w, h = int(600 * sc), int(200 * sc)
            img = None
            for nm in ("capybara_banner.png", "capybara_banner.jpg",
                       "capybara_banner.jpeg", "capybara.png", "capybara.jpg"):
                p = os.path.join(HERE, nm)
                if os.path.exists(p):
                    img = Image.open(p).convert("RGB"); break
            if img is not None:
                r = w / img.width
                img = img.resize((w, max(1, int(img.height * r))), Image.LANCZOS)
                if img.height >= h:
                    top = int(img.height * 0.06)   # Krone + ganzes Gesicht + Schwert im Blick
                    if top + h > img.height:
                        top = img.height - h
                    img = img.crop((0, top, w, top + h))
                else:
                    base = Image.new("RGB", (w, h), self._hex(BG))
                    base.paste(img, (0, (h - img.height) // 2)); img = base
            else:
                img = self._gradient_banner(w, h)
            self._banner_fade(img)
            self._banner_img = ImageTk.PhotoImage(img)
            tk.Label(parent, image=self._banner_img, bd=0, bg=BG).pack(fill="x")
        except Exception:
            pass

    # ---------- UI ----------
    def _build(self):
        self._make_banner(self.root)   # Capybara-Banner (Bild oder Farbverlauf) ganz oben
        head = tk.Frame(self.root, bg=BG); head.pack(fill="x", padx=16, pady=(10, 6))
        tk.Label(head, text="💎 Capybara Gem Scanner 💎", bg=BG, fg=GOLD,
                 font=("Segoe UI", 16, "bold")).pack(side="left")
        self.btn_lang = tk.Button(head, command=self._toggle_lang, relief="flat", bd=0,
                                  bg=PANEL2, fg=TEXT, font=("Segoe UI", 9, "bold"), padx=8, pady=2)
        self.btn_lang.pack(side="right")
        self.btn_update = tk.Button(head, command=self._open_update, relief="flat", bd=0,
                                    bg=PANEL2, fg=TEXT, font=("Segoe UI", 9, "bold"), padx=8, pady=2)
        self.btn_update.pack(side="right", padx=(0, 6))
        self.btn_theme = tk.Button(head, command=self._toggle_theme, relief="flat", bd=0,
                                   bg=PANEL2, fg=TEXT, font=("Segoe UI", 9, "bold"), padx=8, pady=2)
        self.btn_theme.pack(side="right", padx=(0, 6))

        tabs = tk.Frame(self.root, bg=BG); tabs.pack(fill="x", padx=14, pady=(8, 0))
        self.tab_quick = tk.Button(tabs, command=lambda: self._set_view("quick"), relief="flat",
                                   bd=0, font=("Segoe UI", 9, "bold"))
        self.tab_scan = tk.Button(tabs, command=lambda: self._set_view("scanner"), relief="flat",
                                  bd=0, font=("Segoe UI", 9, "bold"))
        self.tab_hero = tk.Button(tabs, command=lambda: self._set_view("hero"), relief="flat",
                                  bd=0, font=("Segoe UI", 9, "bold"))
        self.tab_skill = tk.Button(tabs, command=lambda: self._set_view("skill"), relief="flat",
                                   bd=0, font=("Segoe UI", 9, "bold"))
        self.tab_load = tk.Button(tabs, command=lambda: self._set_view("loadout"), relief="flat",
                                  bd=0, font=("Segoe UI", 9, "bold"))
        self.tab_guide = tk.Button(tabs, command=lambda: self._set_view("guide"), relief="flat",
                                   bd=0, font=("Segoe UI", 9, "bold"))
        for b in (self.tab_quick, self.tab_scan, self.tab_hero, self.tab_skill,
                  self.tab_load, self.tab_guide):
            b.pack(side="left", fill="x", expand=True, padx=2, ipady=5)

        bsel = tk.Frame(self.root, bg=BG); bsel.pack(fill="x", padx=14, pady=(8, 0))
        self.lbl_build = tk.Label(bsel, bg=BG, fg=GOLD, font=("Segoe UI", 9, "bold"))
        self.lbl_build.pack(side="left", padx=(0, 6))
        self.build_var = tk.StringVar(value=self._bname(self.build))
        self.build_menu = tk.OptionMenu(bsel, self.build_var, self._bname(self.build))
        self.build_menu.configure(bg=PANEL2, fg=TEXT, activebackground=PURPLE, highlightthickness=0,
                                  bd=0, font=("Segoe UI", 9, "bold"), anchor="w")
        self.build_menu["menu"].configure(bg=PANEL2, fg=TEXT)
        self.build_menu.pack(side="left", fill="x", expand=True)
        self._rebuild_build_menu()   # Einträge mit sprachabhängigen Anzeigenamen füllen

        # ---- SCANNER ----
        self.scan_view = tk.Frame(self.root, bg=BG)
        # scrollbar machen, damit auf kleinen/hohen Fenstern nichts abgeschnitten wird
        _sco = tk.Frame(self.scan_view, bg=BG); _sco.pack(fill="both", expand=True)
        _scc = tk.Canvas(_sco, bg=BG, highlightthickness=0)
        _scsb = tk.Scrollbar(_sco, command=_scc.yview); _scc.configure(yscrollcommand=_scsb.set)
        _scsb.pack(side="right", fill="y"); _scc.pack(side="left", fill="both", expand=True)
        _scin = tk.Frame(_scc, bg=BG)
        _scwin = _scc.create_window((0, 0), window=_scin, anchor="nw")
        _scin.bind("<Configure>", lambda e: _scc.configure(scrollregion=_scc.bbox("all")))
        _scc.bind("<Configure>", lambda e: _scc.itemconfigure(_scwin, width=e.width))
        _scc.bind("<Enter>", lambda e: _scc.bind_all("<MouseWheel>",
                  lambda ev: _scc.yview_scroll(int(-1 * (ev.delta / 120)), "units")))
        _scc.bind("<Leave>", lambda e: _scc.unbind_all("<MouseWheel>"))
        w = tk.Frame(_scin, bg=BG); w.pack(fill="both", expand=True, padx=16, pady=12)

        mb = tk.Frame(w, bg=PANEL, highlightbackground=BORDER, highlightthickness=1); mb.pack(fill="x")
        self.btn_pve = tk.Button(mb, text="PvE", relief="flat", bd=0,
                                 command=lambda: self._set_mode("pve"), font=("Segoe UI", 10, "bold"))
        self.btn_pvp = tk.Button(mb, text="PvP", relief="flat", bd=0,
                                 command=lambda: self._set_mode("pvp"), font=("Segoe UI", 10, "bold"))
        self.btn_pve.pack(side="left", fill="x", expand=True, padx=2, pady=2)
        self.btn_pvp.pack(side="left", fill="x", expand=True, padx=2, pady=2)

        self.lbl_slot = tk.Label(w, bg=BG, fg=DIM, font=("Segoe UI", 9)); self.lbl_slot.pack(anchor="w", pady=(10, 2))
        sr = tk.Frame(w, bg=BG); sr.pack(fill="x")
        for key in SLOT_KEYS:
            b = tk.Button(sr, command=lambda k=key: self._set_slot(k), relief="flat", bd=0,
                          font=("Segoe UI", 9, "bold"), pady=6)
            b.pack(side="left", fill="x", expand=True, padx=2)
            self.slot_btns[key] = b

        cnt = tk.Frame(w, bg=BG); cnt.pack(fill="x", pady=(8, 0))
        self.lbl_slots = tk.Label(cnt, bg=BG, fg=DIM, font=("Segoe UI", 9)); self.lbl_slots.pack(side="left")
        tk.Button(cnt, text="−", command=lambda: self._cnt(-1), width=2, bg=PANEL2, fg=TEXT,
                  relief="flat", bd=0, font=("Segoe UI", 12, "bold")).pack(side="left", padx=(6, 2))
        self.lbl_cnt = tk.Label(cnt, text="3", bg=BG, fg=TEXT, width=2, font=("Segoe UI", 12, "bold"))
        self.lbl_cnt.pack(side="left")
        tk.Button(cnt, text="+", command=lambda: self._cnt(1), width=2, bg=PANEL2, fg=TEXT,
                  relief="flat", bd=0, font=("Segoe UI", 12, "bold")).pack(side="left", padx=(2, 0))

        st = tk.Frame(w, bg=BG); st.pack(fill="x", pady=(10, 0))
        self.btn_reg_eq = tk.Button(st, command=self._set_region_eq, bg=PANEL2, fg=TEXT, relief="flat",
                                    bd=0, font=("Segoe UI", 9), padx=8, pady=6, anchor="w")
        self.btn_reg_eq.pack(fill="x")
        self.lbl_prev_eq = tk.Label(st, text="", bg=BG, fg=DIM, font=("Consolas", 8), anchor="w",
                                    justify="left", wraplength=500); self.lbl_prev_eq.pack(fill="x", padx=4)
        self.btn_reg_cand = tk.Button(st, command=self._set_region_cand, bg=PANEL2, fg=TEXT, relief="flat",
                                      bd=0, font=("Segoe UI", 9), padx=8, pady=6, anchor="w")
        self.btn_reg_cand.pack(fill="x", pady=(4, 0))
        self.lbl_prev_cand = tk.Label(st, text="", bg=BG, fg=DIM, font=("Consolas", 8), anchor="w",
                                      justify="left", wraplength=500); self.lbl_prev_cand.pack(fill="x", padx=4)

        self.btn_scan = tk.Button(w, command=self._scan_all, bg=PURPLE, fg="#fff", relief="flat",
                                  bd=0, font=("Segoe UI", 13, "bold"), pady=11); self.btn_scan.pack(fill="x", pady=(10, 0))
        mini = tk.Frame(w, bg=BG); mini.pack(fill="x", pady=(6, 0))
        self.btn_eq_only = tk.Button(mini, command=self._scan_eq_only, bg=PANEL, fg=DIM, relief="flat",
                                     bd=0, font=("Segoe UI", 8), padx=6, pady=4)
        self.btn_cand_only = tk.Button(mini, command=self._scan_cand_only, bg=PANEL, fg=DIM, relief="flat",
                                       bd=0, font=("Segoe UI", 8), padx=6, pady=4)
        self.btn_eq_only.pack(side="left", expand=True, fill="x", padx=(0, 3))
        self.btn_cand_only.pack(side="left", expand=True, fill="x", padx=(3, 0))
        self.chk_scan_auto = tk.Checkbutton(w, variable=self.scan_auto, command=self._toggle_scan_auto,
                                            bg=BG, fg=GREEN, selectcolor=PANEL, activebackground=BG,
                                            activeforeground=GREEN, font=("Segoe UI", 9, "bold"),
                                            bd=0, highlightthickness=0)
        self.chk_scan_auto.pack(anchor="w", pady=(8, 0))
        self.lbl_scan_auto = tk.Label(w, text="", bg=BG, fg=DIM, font=("Segoe UI", 8),
                                      anchor="w", justify="left", wraplength=500)
        self.lbl_scan_auto.pack(fill="x", padx=4)
        self.chk_dbg = tk.Checkbutton(w, variable=self.show_debug, command=self._render, bg=BG, fg=DIM,
                                      selectcolor=PANEL, activebackground=BG, activeforeground=TEXT,
                                      font=("Segoe UI", 8), bd=0, highlightthickness=0)
        self.chk_dbg.pack(anchor="w", pady=(6, 0))

        self.verdict = tk.Frame(w, bg=PANEL2, highlightbackground=BORDER, highlightthickness=1)
        self.verdict.pack(fill="x", pady=(12, 0))
        self.vin = tk.Frame(self.verdict, bg=PANEL2); self.vin.pack(fill="x", padx=16, pady=14)

        self.manual_var = tk.StringVar(value="")
        self.manual_row = tk.Frame(w, bg=BG)
        self.lbl_manual = tk.Label(self.manual_row, bg=BG, fg=DIM, font=("Segoe UI", 8))
        self.lbl_manual.pack(side="left")

        self.result = tk.Frame(w, bg=BG); self.result.pack(fill="both", expand=True, pady=(10, 0))
        foot = tk.Frame(w, bg=BG); foot.pack(fill="x", pady=(6, 0))
        self.btn_reset = tk.Button(foot, command=self._reset, bg=PANEL, fg=DIM, relief="flat", bd=0,
                                   font=("Segoe UI", 8), padx=6, pady=4); self.btn_reset.pack(side="left")

        # ---- LOADOUT ----
        self.load_view = tk.Frame(self.root, bg=BG)
        _lc = tk.Canvas(self.load_view, bg=BG, highlightthickness=0)
        _lsb = tk.Scrollbar(self.load_view, command=_lc.yview)
        _lc.configure(yscrollcommand=_lsb.set)
        _lsb.pack(side="right", fill="y")
        _lc.pack(side="left", fill="both", expand=True)
        self.load_inner = tk.Frame(_lc, bg=BG)
        _win = _lc.create_window((0, 0), window=self.load_inner, anchor="nw")
        self.load_inner.bind("<Configure>", lambda e: _lc.configure(scrollregion=_lc.bbox("all")))
        _lc.bind("<Configure>", lambda e: _lc.itemconfigure(_win, width=e.width))

        def _wheel(e):
            _lc.yview_scroll(int(-1 * (e.delta / 120)), "units")
        _lc.bind("<Enter>", lambda e: _lc.bind_all("<MouseWheel>", _wheel))
        _lc.bind("<Leave>", lambda e: _lc.unbind_all("<MouseWheel>"))

        # ---- GUIDE ----
        self.guide_view = tk.Frame(self.root, bg=BG)
        gw = tk.Frame(self.guide_view, bg=BG); gw.pack(fill="both", expand=True, padx=14, pady=10)
        self.lbl_guide_hint = tk.Label(gw, bg=BG, fg=DIM, font=("Segoe UI", 8), anchor="w", justify="left")
        self.lbl_guide_hint.pack(fill="x")
        gframe = tk.Frame(gw, bg=BG); gframe.pack(fill="both", expand=True, pady=(6, 0))
        self.guide_txt = tk.Text(gframe, bg=PANEL, fg=TEXT, bd=0, highlightthickness=1,
                                 highlightbackground=BORDER, wrap="word", font=("Segoe UI", 10),
                                 padx=12, pady=12)
        sb = tk.Scrollbar(gframe, command=self.guide_txt.yview); self.guide_txt.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y"); self.guide_txt.pack(side="left", fill="both", expand=True)
        self.guide_txt.tag_configure("H2", foreground=TEAL, font=("Segoe UI", 11, "bold"), spacing1=10, spacing3=4)
        self.guide_txt.tag_configure("P", foreground=TEXT, font=("Segoe UI", 9), spacing3=6)
        self.guide_txt.tag_configure("B", foreground=TEXT, font=("Segoe UI", 9), spacing3=4, lmargin1=14, lmargin2=22)

        # ---- QUICK (Schnell-Scan) ----
        self.quick_view = tk.Frame(self.root, bg=BG)
        qt = tk.Frame(self.quick_view, bg=BG); qt.pack(fill="x", padx=14, pady=(10, 0))
        self.lbl_quick_intro = tk.Label(qt, bg=BG, fg=DIM, font=("Segoe UI", 8), anchor="w",
                                        justify="left", wraplength=500); self.lbl_quick_intro.pack(fill="x")
        qmb = tk.Frame(qt, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
        qmb.pack(fill="x", pady=(8, 0))
        self.btn_qpve = tk.Button(qmb, text="PvE", relief="flat", bd=0,
                                  command=lambda: self._set_mode("pve"), font=("Segoe UI", 10, "bold"))
        self.btn_qpvp = tk.Button(qmb, text="PvP", relief="flat", bd=0,
                                  command=lambda: self._set_mode("pvp"), font=("Segoe UI", 10, "bold"))
        self.btn_qpve.pack(side="left", fill="x", expand=True, padx=2, pady=2)
        self.btn_qpvp.pack(side="left", fill="x", expand=True, padx=2, pady=2)
        self.btn_reg_quick = tk.Button(qt, command=self._set_region_quick, bg=PANEL2, fg=TEXT,
                                       relief="flat", bd=0, font=("Segoe UI", 9), padx=8, pady=6, anchor="w")
        self.btn_reg_quick.pack(fill="x", pady=(10, 0))
        self.lbl_prev_quick = tk.Label(qt, text="", bg=BG, fg=DIM, font=("Consolas", 8), anchor="w",
                                       justify="left", wraplength=500); self.lbl_prev_quick.pack(fill="x", padx=4)
        self.btn_scan_quick = tk.Button(qt, command=self._scan_quick, bg=PURPLE, fg="#fff", relief="flat",
                                        bd=0, font=("Segoe UI", 13, "bold"), pady=11)
        self.btn_scan_quick.pack(fill="x", pady=(10, 0))
        self.chk_dbg_q = tk.Checkbutton(qt, variable=self.show_debug, command=self._render, bg=BG, fg=DIM,
                                        selectcolor=PANEL, activebackground=BG, activeforeground=TEXT,
                                        font=("Segoe UI", 8), bd=0, highlightthickness=0)
        self.chk_dbg_q.pack(anchor="w", pady=(6, 0))
        qres = tk.Frame(self.quick_view, bg=BG); qres.pack(fill="both", expand=True, padx=(14, 0))
        _qc = tk.Canvas(qres, bg=BG, highlightthickness=0)
        _qscb = tk.Scrollbar(qres, command=_qc.yview); _qc.configure(yscrollcommand=_qscb.set)
        _qscb.pack(side="right", fill="y"); _qc.pack(side="left", fill="both", expand=True)
        self.quick_inner = tk.Frame(_qc, bg=BG)
        _qwin = _qc.create_window((0, 0), window=self.quick_inner, anchor="nw")
        self.quick_inner.bind("<Configure>", lambda e: _qc.configure(scrollregion=_qc.bbox("all")))
        _qc.bind("<Configure>", lambda e: _qc.itemconfigure(_qwin, width=e.width))
        _qc.bind("<Enter>", lambda e: _qc.bind_all("<MouseWheel>",
                 lambda ev: _qc.yview_scroll(int(-1 * (ev.delta / 120)), "units")))
        _qc.bind("<Leave>", lambda e: _qc.unbind_all("<MouseWheel>"))

        # ---- SKILL (Skill-Berater) ----
        self.skill_view = tk.Frame(self.root, bg=BG)
        st = tk.Frame(self.skill_view, bg=BG); st.pack(fill="x", padx=14, pady=(10, 0))
        self.lbl_skill_intro = tk.Label(st, bg=BG, fg=DIM, font=("Segoe UI", 8), anchor="w",
                                        justify="left", wraplength=500); self.lbl_skill_intro.pack(fill="x")
        self.btn_reg_skill = tk.Button(st, command=self._set_region_skill, bg=PANEL2, fg=TEXT,
                                       relief="flat", bd=0, font=("Segoe UI", 9), padx=8, pady=6, anchor="w")
        self.btn_reg_skill.pack(fill="x", pady=(10, 0))
        self.lbl_prev_skill = tk.Label(st, text="", bg=BG, fg=DIM, font=("Consolas", 8), anchor="w",
                                       justify="left", wraplength=500); self.lbl_prev_skill.pack(fill="x", padx=4)
        self.btn_scan_skill = tk.Button(st, command=self._scan_skill, bg=PURPLE, fg="#fff", relief="flat",
                                        bd=0, font=("Segoe UI", 13, "bold"), pady=11)
        self.btn_scan_skill.pack(fill="x", pady=(10, 0))
        self.chk_skill_auto = tk.Checkbutton(st, variable=self.skill_auto, command=self._toggle_skill_auto,
                                             bg=BG, fg=GREEN, selectcolor=PANEL, activebackground=BG,
                                             activeforeground=GREEN, font=("Segoe UI", 9, "bold"),
                                             bd=0, highlightthickness=0)
        self.chk_skill_auto.pack(anchor="w", pady=(8, 0))
        self.lbl_skill_auto = tk.Label(st, text="", bg=BG, fg=DIM, font=("Segoe UI", 8),
                                       anchor="w", justify="left", wraplength=500)
        self.lbl_skill_auto.pack(fill="x", padx=4)
        self.chk_dbg_s = tk.Checkbutton(st, variable=self.show_debug, command=self._render, bg=BG, fg=DIM,
                                        selectcolor=PANEL, activebackground=BG, activeforeground=TEXT,
                                        font=("Segoe UI", 8), bd=0, highlightthickness=0)
        self.chk_dbg_s.pack(anchor="w", pady=(6, 0))
        sres = tk.Frame(self.skill_view, bg=BG); sres.pack(fill="both", expand=True, padx=(14, 0))
        _sc = tk.Canvas(sres, bg=BG, highlightthickness=0)
        _sscb = tk.Scrollbar(sres, command=_sc.yview); _sc.configure(yscrollcommand=_sscb.set)
        _sscb.pack(side="right", fill="y"); _sc.pack(side="left", fill="both", expand=True)
        self.skill_inner = tk.Frame(_sc, bg=BG)
        _swin = _sc.create_window((0, 0), window=self.skill_inner, anchor="nw")
        self.skill_inner.bind("<Configure>", lambda e: _sc.configure(scrollregion=_sc.bbox("all")))
        _sc.bind("<Configure>", lambda e: _sc.itemconfigure(_swin, width=e.width))
        _sc.bind("<Enter>", lambda e: _sc.bind_all("<MouseWheel>",
                 lambda ev: _sc.yview_scroll(int(-1 * (ev.delta / 120)), "units")))
        _sc.bind("<Leave>", lambda e: _sc.unbind_all("<MouseWheel>"))

        # ---- HERO (Held lesen) ----
        self.hero_view = tk.Frame(self.root, bg=BG)
        ht = tk.Frame(self.hero_view, bg=BG); ht.pack(fill="x", padx=14, pady=(10, 0))
        self.lbl_hero_intro = tk.Label(ht, bg=BG, fg=DIM, font=("Segoe UI", 8), anchor="w",
                                       justify="left", wraplength=500); self.lbl_hero_intro.pack(fill="x")
        self.btn_reg_hero = tk.Button(ht, command=self._set_region_hero, bg=PANEL2, fg=TEXT,
                                      relief="flat", bd=0, font=("Segoe UI", 9), padx=8, pady=6, anchor="w")
        self.btn_reg_hero.pack(fill="x", pady=(10, 0))
        self.lbl_prev_hero = tk.Label(ht, text="", bg=BG, fg=DIM, font=("Consolas", 8), anchor="w",
                                      justify="left", wraplength=500); self.lbl_prev_hero.pack(fill="x", padx=4)
        # Mehrfach-Scan: 2 ausgerüstete + 4 Reserve-Helden. Region einmal setzen,
        # dann je Held im Spiel anvisieren und den passenden Knopf drücken.
        grid = tk.Frame(ht, bg=BG); grid.pack(fill="x", pady=(10, 0))
        for c in range(2):
            grid.columnconfigure(c, weight=1, uniform="hero")
        for i, (key, role, _de, _en) in enumerate(HERO_SLOTS):
            b = tk.Button(grid, command=lambda k=key: self._scan_hero(k), relief="flat", bd=0,
                          fg="#fff" if role == "equipped" else TEXT,
                          bg=PURPLE if role == "equipped" else PANEL2,
                          font=("Segoe UI", 9, "bold"), pady=8)
            b.grid(row=i // 2, column=i % 2, sticky="ew", padx=3, pady=3)
            self.hero_btns[key] = b
        self.btn_hero_reset = tk.Button(ht, command=self._reset_hero, bg=PANEL, fg=DIM, relief="flat",
                                        bd=0, font=("Segoe UI", 8), pady=4)
        self.btn_hero_reset.pack(fill="x", pady=(4, 0))
        self.chk_dbg_h = tk.Checkbutton(ht, variable=self.show_debug, command=self._render, bg=BG, fg=DIM,
                                        selectcolor=PANEL, activebackground=BG, activeforeground=TEXT,
                                        font=("Segoe UI", 8), bd=0, highlightthickness=0)
        self.chk_dbg_h.pack(anchor="w", pady=(6, 0))
        hres = tk.Frame(self.hero_view, bg=BG); hres.pack(fill="both", expand=True, padx=(14, 0))
        _hc = tk.Canvas(hres, bg=BG, highlightthickness=0)
        _hscb = tk.Scrollbar(hres, command=_hc.yview); _hc.configure(yscrollcommand=_hscb.set)
        _hscb.pack(side="right", fill="y"); _hc.pack(side="left", fill="both", expand=True)
        self.hero_inner = tk.Frame(_hc, bg=BG)
        _hwin = _hc.create_window((0, 0), window=self.hero_inner, anchor="nw")
        self.hero_inner.bind("<Configure>", lambda e: _hc.configure(scrollregion=_hc.bbox("all")))
        _hc.bind("<Configure>", lambda e: _hc.itemconfigure(_hwin, width=e.width))
        _hc.bind("<Enter>", lambda e: _hc.bind_all("<MouseWheel>",
                 lambda ev: _hc.yview_scroll(int(-1 * (ev.delta / 120)), "units")))
        _hc.bind("<Leave>", lambda e: _hc.unbind_all("<MouseWheel>"))

    # ---------- helpers ----------
    def _set_build(self, key):
        self.build = key
        self.cfg["build"] = key; save_config(self.cfg)
        self.build_var.set(self._bname(key))
        self._fill_guide(); self._render()

    def _toggle_lang(self):
        self.lang = "en" if self.lang == "de" else "de"
        self.cfg["lang"] = self.lang; save_config(self.cfg)
        self._rebuild_build_menu()
        self._fill_guide(); self._render()

    def _toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.cfg["theme"] = self.theme; save_config(self.cfg)
        apply_theme(self.theme)
        self._rebuild()

    def _rebuild(self):
        """Oberfläche mit den neuen Theme-Farben komplett neu aufbauen (Zustand bleibt)."""
        try:
            self.root.unbind_all("<MouseWheel>")
        except Exception:
            pass
        self.root.configure(bg=BG)
        for w in self.root.winfo_children():
            w.destroy()
        self._build()
        self._render()

    def _set_view(self, v):
        self.view = v; self._render()

    def _set_mode(self, m):
        self.mode = m; self._render()

    def _set_slot(self, k):
        self.slot = k; self.candidate = None; self.cand_conf = 0; self._render()

    def _cnt(self, d):
        self.slot_count[self.slot] = max(0, min(6, self.slot_count[self.slot] + d))
        self.cfg["free_slots"] = self.slot_count; save_config(self.cfg); self._render()

    def _reset(self):
        self.equipped[self.slot] = []; self.candidate = None; self.cand_conf = 0
        self.dbg_eq = ""; self.dbg_cand = ""; self._render()

    # ---------- regions ----------
    def _set_region_eq(self):
        self.root.withdraw()
        self.root.after(250, lambda: RegionSelector(self.root, self._t(
            "RECHTS: Rechteck über die ausgerüsteten Steine ziehen · Esc = Abbruch",
            "RIGHT: drag a box over the EQUIPPED gems · Esc = cancel"), self._reg_eq_done))

    def _reg_eq_done(self, region):
        self.region_eq = region; self.cfg["region_equipped"] = region; save_config(self.cfg)
        self.root.deiconify(); self._render()
        threading.Thread(target=self._preview, args=("eq",), daemon=True).start()

    def _set_region_cand(self):
        self.root.withdraw()
        self.root.after(250, lambda: RegionSelector(self.root, self._t(
            "LINKS: Rechteck über das Info-Fenster (inkl. „Attribut“) · Esc = Abbruch",
            "LEFT: drag a box over the info panel (incl. 'Attribute') · Esc = cancel"), self._reg_cand_done))

    def _reg_cand_done(self, region):
        self.region_cand = region; self.cfg["region_candidate"] = region; save_config(self.cfg)
        self.root.deiconify(); self._render()
        threading.Thread(target=self._preview, args=("cand",), daemon=True).start()

    def _set_region_quick(self):
        self.root.withdraw()
        self.root.after(250, lambda: RegionSelector(self.root, self._t(
            "Rechteck über den Bereich mit den Edelstein-Effekten ziehen · Esc = Abbruch",
            "Drag a box over the area with the gem effects · Esc = cancel"), self._reg_quick_done))

    def _reg_quick_done(self, region):
        self.region_quick = region; self.cfg["region_quick"] = region; save_config(self.cfg)
        self.root.deiconify(); self._render()
        threading.Thread(target=self._preview, args=("quick",), daemon=True).start()

    def _set_region_hero(self):
        self.root.withdraw()
        self.root.after(250, lambda: RegionSelector(self.root, self._t(
            "Rechteck über die HELDEN-Detailseite (Rang + Effekt-Text) ziehen · Esc = Abbruch",
            "Drag a box over the HERO detail page (rank + effect text) · Esc = cancel"), self._reg_hero_done))

    def _reg_hero_done(self, region):
        self.region_hero = region; self.cfg["region_hero"] = region; save_config(self.cfg)
        self.root.deiconify(); self._render()
        threading.Thread(target=self._preview, args=("hero",), daemon=True).start()

    def _set_region_skill(self):
        self.root.withdraw()
        self.root.after(250, lambda: RegionSelector(self.root, self._t(
            "Rechteck über die angebotenen Skills (Namen + Beschreibung) ziehen · Esc = Abbruch",
            "Drag a box over the offered skills (names + descriptions) · Esc = cancel"), self._reg_skill_done))

    def _reg_skill_done(self, region):
        self.region_skill = region; self.cfg["region_skill"] = region; save_config(self.cfg)
        self.root.deiconify(); self._render()
        threading.Thread(target=self._preview, args=("skill",), daemon=True).start()

    def _preview(self, which):
        regions = {"eq": self.region_eq, "cand": self.region_cand,
                   "quick": self.region_quick, "hero": self.region_hero,
                   "skill": self.region_skill}
        try:
            _, blob = ocr_detailed(regions.get(which))
            snip = (blob[:90] + "…") if len(blob) > 90 else (blob or self._t("(nichts)", "(nothing)"))
            def upd():
                if which == "eq":
                    self.prev_eq = snip
                elif which == "cand":
                    self.prev_cand = snip
                elif which == "quick":
                    self.prev_quick = snip
                elif which == "skill":
                    self.prev_skill = snip
                else:
                    self.prev_hero = snip
                self._render()
            self.root.after(0, upd)
        except Exception:
            pass

    # ---------- scanning ----------
    def _busy(self, on, first=False):
        if on:
            self.btn_scan.configure(state="disabled", text=self._t("… lädt …", "… loading …") if first
                                    else self._t("… scanne …", "… scanning …"))
        else:
            self.btn_scan.configure(state="normal", text=self._t("📷  SCANNEN & VERGLEICHEN", "📷  SCAN & COMPARE"))
        self.root.update_idletasks()

    def _busy2(self, btn, on, first, idle_label):
        if on:
            btn.configure(state="disabled", text=self._t("… lädt …", "… loading …") if first
                          else self._t("… scanne …", "… scanning …"))
        else:
            btn.configure(state="normal", text=idle_label)
        self.root.update_idletasks()

    def _scan_all(self):
        if not self.region_eq and not self.region_cand:
            messagebox.showinfo(self._t("Bereiche", "Regions"), self._t(
                "Bitte zuerst die beiden Bereiche festlegen (Knöpfe 1 und 2).",
                "Please set the two regions first (buttons 1 and 2)."))
            return
        self._busy(True, _engine is None and _engine_err is None)
        threading.Thread(target=self._work_all, daemon=True).start()

    def _work_all(self):
        try:
            s = self.slot; out = {}
            if self.region_eq:
                items, blob = ocr_detailed(self.region_eq)
                eq, lines, card_seen = detect_equipped(items, s)
                out["eq"] = eq; out["dbg_eq"] = self._fmt_eq(blob, lines, s)
                out["card_seen"] = card_seen
            if self.region_cand:
                items, _ = ocr_detailed(self.region_cand)
                cand, conf, blob = detect_candidate(items, s)
                out["cand"] = (cand, conf); out["dbg_cand"] = self._fmt_cand(blob, s)
            self.root.after(0, lambda: self._apply(out))
        except Exception as e:
            err = "".join(traceback.format_exception_only(type(e), e)).strip()
            self.root.after(0, lambda: self._err(err))

    # ----- Änderungs-Erkennung (CPU-schonend, ignoriert Animationen) -----
    def _grab_small(self, region):
        """Kleiner Graustufen-Frame (48x48) des Bereichs als int16-Array, für Diff."""
        shot = _thread_sct().grab(region)
        img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX").convert("L").resize((48, 48))
        return np.asarray(img, dtype=np.int16)

    def _significant_change(self, region, prev_attr, scanned_attr):
        """True NUR bei deutlicher UND ruhiger Änderung ggü. dem zuletzt gescannten
        Frame. Kleine Animationen/Glitzern (geringe mittlere Differenz) lösen NICHTS
        aus; während eines Übergangs (hohe Tick-zu-Tick-Differenz) wird gewartet."""
        try:
            cur = self._grab_small(region)
        except Exception:
            return False
        prev = getattr(self, prev_attr, None)
        scanned = getattr(self, scanned_attr, None)
        setattr(self, prev_attr, cur)
        moving = prev is not None and float(np.mean(np.abs(cur - prev))) > 3.5
        changed = scanned is None or float(np.mean(np.abs(cur - scanned))) > 9.0
        if changed and not moving:
            setattr(self, scanned_attr, cur)
            return True
        return False

    # ----- Auto-Scan (Edelsteine): beide Bereiche selbst überwachen -----
    def _toggle_scan_auto(self):
        if self.scan_auto.get():
            if not self.region_eq and not self.region_cand:
                messagebox.showinfo(self._t("Bereiche", "Regions"), self._t(
                    "Erst die beiden Bereiche festlegen, dann Auto-Scan einschalten.",
                    "Set the two regions first, then enable auto-scan."))
                self.scan_auto.set(False)
                return
            self._cand_scanned = self._eq_scanned = None  # beim Einschalten einmal scannen
            if not self._scan_loop_running:
                self._scan_loop_running = True
                self._scan_auto_tick()
        self._render()

    def _scan_auto_tick(self):
        if not self.scan_auto.get():
            self._scan_loop_running = False
            return
        if self.view == "scanner" and (self.region_eq or self.region_cand) and not self._scan_busy:
            self._scan_busy = True
            threading.Thread(target=self._scan_auto_work, daemon=True).start()
        self.root.after(1300, self._scan_auto_tick)

    def _scan_auto_work(self):
        try:
            do_scan = False
            if self.region_cand:
                do_scan = self._significant_change(self.region_cand, "_cand_prev", "_cand_scanned") or do_scan
            if self.region_eq:
                do_scan = self._significant_change(self.region_eq, "_eq_prev", "_eq_scanned") or do_scan
            if not do_scan:
                return
            s = self.slot; out = {}
            if self.region_eq:
                items, blob = ocr_detailed(self.region_eq)
                eq, lines, card_seen = detect_equipped(items, s)
                out["eq"] = eq; out["dbg_eq"] = self._fmt_eq(blob, lines, s)
                out["card_seen"] = card_seen
                out["prev_eq"] = (blob[:90] + "…") if len(blob) > 90 else (blob or "")
            if self.region_cand:
                items, _ = ocr_detailed(self.region_cand)
                cand, conf, blob = detect_candidate(items, s)
                out["cand"] = (cand, conf); out["dbg_cand"] = self._fmt_cand(blob, s)
                out["prev_cand"] = (blob[:90] + "…") if len(blob) > 90 else (blob or "")
            self.root.after(0, lambda: self._apply_scan_auto(out))
        except Exception:
            pass
        finally:
            self._scan_busy = False

    def _apply_scan_auto(self, out):
        if "prev_eq" in out:
            self.prev_eq = out.pop("prev_eq")
        if "prev_cand" in out:
            self.prev_cand = out.pop("prev_cand")
        self._apply(out)

    def _scan_eq_only(self):
        if not self.region_eq:
            messagebox.showinfo("?", self._t("Bitte Knopf 1 festlegen.", "Set button 1 first.")); return
        self._busy(True, _engine is None and _engine_err is None)
        threading.Thread(target=self._work_eq, daemon=True).start()

    def _work_eq(self):
        try:
            s = self.slot; items, blob = ocr_detailed(self.region_eq)
            eq, lines, card_seen = detect_equipped(items, s)
            self.root.after(0, lambda: self._apply(
                {"eq": eq, "dbg_eq": self._fmt_eq(blob, lines, s), "card_seen": card_seen}))
        except Exception as e:
            err = "".join(traceback.format_exception_only(type(e), e)).strip()
            self.root.after(0, lambda: self._err(err))

    def _scan_cand_only(self):
        if not self.region_cand:
            messagebox.showinfo("?", self._t("Bitte Knopf 2 festlegen.", "Set button 2 first.")); return
        self._busy(True, _engine is None and _engine_err is None)
        threading.Thread(target=self._work_cand, daemon=True).start()

    def _work_cand(self):
        try:
            s = self.slot; items, _ = ocr_detailed(self.region_cand)
            cand, conf, blob = detect_candidate(items, s)
            self.root.after(0, lambda: self._apply({"cand": (cand, conf), "dbg_cand": self._fmt_cand(blob, s)}))
        except Exception as e:
            err = "".join(traceback.format_exception_only(type(e), e)).strip()
            self.root.after(0, lambda: self._err(err))

    # ----- Schnell-Scan -----
    def _scan_quick(self):
        if not self.region_quick:
            messagebox.showinfo(self._t("Bereich", "Region"), self._t(
                "Bitte zuerst den Spielbereich festlegen.", "Please set the game region first."))
            return
        self._busy2(self.btn_scan_quick, True, _engine is None and _engine_err is None, "")
        threading.Thread(target=self._work_quick, daemon=True).start()

    def _work_quick(self):
        try:
            items, blob = ocr_detailed(self.region_quick)
            results, lines, unclear = detect_quick(items)
            dbg = self._fmt_quick(blob, lines)
            self.root.after(0, lambda: self._apply_quick(results, unclear, dbg))
        except Exception as e:
            err = "".join(traceback.format_exception_only(type(e), e)).strip()
            self.root.after(0, lambda: (self._busy2(self.btn_scan_quick, False, False,
                            self._t("⚡  SCHNELL-SCAN", "⚡  QUICK SCAN")), self._err_box(err)))

    def _apply_quick(self, results, unclear, dbg):
        self._busy2(self.btn_scan_quick, False, False, self._t("⚡  SCHNELL-SCAN", "⚡  QUICK SCAN"))
        self.quick_results = results; self.quick_unclear = unclear; self.dbg_quick = dbg
        self._render()

    def _fmt_quick(self, blob, lines):
        out = [self._t("SCHNELL-SCAN – Text:", "QUICK SCAN – text:"), (blob or self._t("(leer)", "(empty)")), "",
               self._t("Zeilen → Stein:", "lines → gem:")]
        for ln in lines:
            g, sc = best_match_any(ln)
            mark = self._gname(g) if (g and sc >= 80) else "—"
            out.append("  • %s → %s (%d%%)" % (self._q(ln), mark, int(sc)))
        return "\n".join(out)

    # ----- Skill-Berater -----
    def _scan_skill(self):
        if not self.region_skill:
            messagebox.showinfo(self._t("Bereich", "Region"), self._t(
                "Bitte zuerst den Skill-Bereich festlegen.", "Please set the skill region first."))
            return
        self._busy2(self.btn_scan_skill, True, _engine is None and _engine_err is None, "")
        threading.Thread(target=self._work_skill, daemon=True).start()

    def _work_skill(self):
        try:
            items, blob = ocr_detailed(self.region_skill)
            results = detect_skills(items)
            dbg = self._t("SKILL-SCAN – Text:", "SKILL SCAN – text:") + "\n" + (blob or self._t("(leer)", "(empty)"))
            self.root.after(0, lambda: self._apply_skill(results, dbg))
        except Exception as e:
            err = "".join(traceback.format_exception_only(type(e), e)).strip()
            self.root.after(0, lambda: (self._busy2(self.btn_scan_skill, False, False,
                            self._t("🧠  SKILLS PRÜFEN", "🧠  CHECK SKILLS")), self._err_box(err)))

    def _apply_skill(self, results, dbg):
        self._busy2(self.btn_scan_skill, False, False, self._t("🧠  SKILLS PRÜFEN", "🧠  CHECK SKILLS"))
        self.skill_results = results; self.dbg_skill = dbg
        self._render()

    # ----- Auto-Scan: Bereich selbstständig überwachen -----
    def _toggle_skill_auto(self):
        if self.skill_auto.get():
            if not self.region_skill:
                messagebox.showinfo(self._t("Bereich", "Region"), self._t(
                    "Erst den Skill-Bereich festlegen, dann Auto-Scan einschalten.",
                    "Set the skill region first, then enable auto-scan."))
                self.skill_auto.set(False)
                return
            self._skill_scanned = None   # beim Einschalten einmal scannen
            if not self._skill_loop_running:
                self._skill_loop_running = True
                self._skill_auto_tick()
        self._render()

    def _skill_auto_tick(self):
        """Überwachungsschleife: prüft den Bereich regelmäßig (nur im Skill-Tab),
        scannt aber nur bei deutlicher, ruhiger Änderung (spart OCR/CPU)."""
        if not self.skill_auto.get():
            self._skill_loop_running = False
            return
        if self.view == "skill" and self.region_skill and not self._skill_busy:
            self._skill_busy = True
            threading.Thread(target=self._skill_auto_work, daemon=True).start()
        self.root.after(1300, self._skill_auto_tick)

    def _skill_auto_work(self):
        try:
            if not self._significant_change(self.region_skill, "_skill_prev", "_skill_scanned"):
                return                      # keine echte Änderung -> kein OCR
            items, blob = ocr_detailed(self.region_skill)
            results = detect_skills(items)
            snip = (blob[:90] + "…") if len(blob) > 90 else (blob or "")
            dbg = self._t("SKILL-SCAN (auto) – Text:", "SKILL SCAN (auto) – text:") + "\n" + (blob or "")
            self.root.after(0, lambda: self._apply_skill_auto(results, snip, dbg))
        except Exception:
            pass
        finally:
            self._skill_busy = False

    def _apply_skill_auto(self, results, snip, dbg):
        self.skill_results = results
        self.prev_skill = snip
        self.dbg_skill = dbg
        if self.view == "skill":
            self._render()

    # ----- Lauf-Tracking: gewählte Skills merken + Synergie -----
    def _skill_pick(self, sk):
        """Markiert einen Skill als in diesem Lauf gewählt (auch andere als die
        vorgeschlagenen) -> fließt in die Synergie-Bewertung ein."""
        name = self._gname(sk); cat = sk.get("cat", "atk")
        if not any(p.get("name") == name for p in self.run_skills):
            self.run_skills.append({"name": name, "cat": cat})
            self.cfg["run_skills"] = self.run_skills; save_config(self.cfg)
        self._render()

    def _skill_run_reset(self):
        """Lauf-Inhalt löschen (neuer Lauf beginnt)."""
        self.run_skills = []
        self.cfg["run_skills"] = []; save_config(self.cfg)
        self._render()

    def _skill_synergy(self, sk):
        """Bonus + Hinweis, wenn der Skill zum bisherigen Lauf passt (gleiche
        Archetyp-Kategorie schon gewählt, z. B. Kombo-Dolch + Wut-Dolch)."""
        cat = sk.get("cat", "atk")
        syn_cats = {"dagger", "combo", "rage", "crit", "lightning", "fire", "swordchi", "atk", "survival"}
        if cat in syn_cats:
            me = self._gname(sk)
            partners = [p["name"] for p in self.run_skills if p.get("cat") == cat and p["name"] != me]
            if partners:
                return 10, self._t("🔗 Synergie mit deinem Lauf: %s", "🔗 Synergy with your run: %s") \
                    % ", ".join(partners[:2])
        return 0, ""

    def _skill_score_run(self, sk):
        """Build-Bewertung + Lauf-Synergie-Bonus (max 100)."""
        return min(100, self._score(sk) + self._skill_synergy(sk)[0])

    # ----- Held lesen (Mehrfach-Scan + Vergleich) -----
    def _scan_hero(self, slot):
        if not self.region_hero:
            messagebox.showinfo(self._t("Bereich", "Region"), self._t(
                "Bitte zuerst den Bereich festlegen (ganzer Spiel-Screen reicht).",
                "Please set the region first (the whole game screen is fine)."))
            return
        self._busy2(self.hero_btns[slot], True, _engine is None and _engine_err is None, "")
        threading.Thread(target=self._work_hero, args=(slot,), daemon=True).start()

    def _work_hero(self, slot):
        try:
            items, blob = ocr_detailed(self.region_hero)
            info = analyze_hero(blob)
            dbg = self._t("HELD – Text:", "HERO – text:") + "\n" + (blob or self._t("(leer)", "(empty)"))
            self.root.after(0, lambda: self._apply_hero(slot, info, dbg))
        except Exception as e:
            err = "".join(traceback.format_exception_only(type(e), e)).strip()
            self.root.after(0, lambda: (self._render(), self._err_box(err)))

    def _apply_hero(self, slot, info, dbg):
        self.hero_scans[slot] = info
        self.dbg_hero = dbg
        self._render()

    def _reset_hero(self):
        self.hero_scans = {}; self._render()

    def _hero_fit(self, info):
        """(power, synergy) eines Helden: power = Rang-Aufstieg (+N, mehr Roh-Stats),
        synergy = Ø Build-Multiplikator der erkannten Effekt-Stichwörter."""
        prefs = BUILD_PREFS.get(self.build, {})
        kw = info.get("kw", []) if info else []
        synergy = (sum(prefs.get(c, 1.0) for c, _, _ in kw) / len(kw)) if kw else 1.0
        power = info.get("plus", 0) if info else 0
        return power, synergy

    def _hero_reco(self):
        """Vergleicht ausgerüstete vs. Reserve-Helden -> Wechsel-Empfehlung oder None."""
        eq = [(k, v) for k, v in self.hero_scans.items() if k.startswith("eq") and v]
        res = [(k, v) for k, v in self.hero_scans.items() if k.startswith("res") and v]
        if not eq or not res:
            return None
        keyf = lambda kv: (self._hero_fit(kv[1])[0], round(self._hero_fit(kv[1])[1], 3))
        weak = min(eq, key=keyf)
        best = max(res, key=keyf)
        wp, ws = self._hero_fit(weak[1]); bp, bs = self._hero_fit(best[1])
        better = (bp > wp) or (bp == wp and bs > ws + 0.03)
        return dict(better=better, weak_key=weak[0], best_key=best[0],
                    wp=wp, ws=ws, bp=bp, bs=bs)

    def _apply(self, out):
        self._busy(False); s = self.slot
        if "card_seen" in out:
            self._eq_card_seen = out["card_seen"]
        if "eq" in out:
            self.equipped[s] = out["eq"]
        if "dbg_eq" in out:
            self.dbg_eq = out["dbg_eq"]
        if "cand" in out:
            self.candidate, self.cand_conf = out["cand"]
            self.manual_var.set(self._gname(self.candidate) if self.candidate else "")
        if "dbg_cand" in out:
            self.dbg_cand = out["dbg_cand"]
        self._render()

    def _fmt_eq(self, blob, lines, slot):
        out = [self._t("AUSGERÜSTET – Text:", "EQUIPPED – text:"), (blob or self._t("(leer)", "(empty)")), "",
               self._t("Zeilen → Stein:", "lines → gem:")]
        for ln in lines:
            g, sc = best_match(ln, slot)
            mark = self._gname(g) if (g and sc >= DETECT_THRESHOLD) else "—"
            out.append("  • %s → %s (%d%%)" % (self._q(ln), mark, int(sc)))
        return "\n".join(out)

    def _fmt_cand(self, blob, slot):
        out = [self._t("AUSWAHL – Text:", "SELECTION – text:"), (blob or self._t("(leer)", "(empty)")), "",
               self._t("Beste Treffer:", "Top matches:")]
        for name, sc in top_matches(blob, slot, self.lang, 4):
            out.append(f"  • {name} ({int(sc)}%)")
        return "\n".join(out)

    def _err(self, err):
        self._busy(False)
        self._err_box(err)

    def _err_box(self, err):
        messagebox.showerror(self._t("Scan-Fehler", "Scan error"), self._t(
            "Beim Scannen ging etwas schief:\n\n", "Something went wrong while scanning:\n\n") + err +
            self._t("\n\nTipp: Bereiche neu festlegen oder Spielfenster sichtbar lassen.",
                    "\n\nTip: re-set the regions or keep the game window visible."))

    def _manual_apply(self, name):
        for g in GEMS.get(self.slot, []):
            if self._gname(g) == name:
                self.candidate = dict(g); self.candidate["auto"] = False; self.candidate["unknown"] = False
                self.cand_conf = 100; self._render(); break

    # ---------- Online-Update der Datenbank ----------
    def _rebuild_build_menu(self):
        """Dropdown mit sprachabhängigen Anzeigenamen füllen (interner Schlüssel bleibt DE)."""
        menu = self.build_menu["menu"]
        menu.delete(0, "end")
        for key in BUILD_NAMES:
            menu.add_command(label=self._bname(key), command=lambda k=key: self._set_build(k))
        if self.build not in BUILD_NAMES:
            self.build = BUILD_NAMES[0]
        self.build_var.set(self._bname(self.build))

    def _open_update(self):
        win = tk.Toplevel(self.root)
        win.title(self._t("Online-Update der Datenbank", "Online database update"))
        win.configure(bg=BG); win.attributes("-topmost", True); win.transient(self.root)
        try:
            win.grab_set()
        except Exception:
            pass
        tk.Label(win, text=self._t("Datenbank aus dem Internet aktualisieren",
                                   "Update the database from the internet"),
                 bg=BG, fg=TEXT, font=("Segoe UI", 13, "bold")).grid(
                 row=0, column=0, columnspan=2, sticky="w", padx=16, pady=(16, 2))
        tk.Label(win, text=self._t(
            "Trage die URL zu einer gehosteten gems.json ein (z. B. GitHub-Raw, Gist oder dein NAS). "
            "builds.json ist optional. Vor dem Überschreiben wird automatisch eine .bak-Sicherung angelegt.",
            "Enter the URL to a hosted gems.json (e.g. GitHub raw, Gist, or your NAS). "
            "builds.json is optional. A .bak backup is created before overwriting."),
            bg=BG, fg=DIM, font=("Segoe UI", 9), justify="left", wraplength=480).grid(
            row=1, column=0, columnspan=2, sticky="w", padx=16, pady=(0, 10))
        tk.Label(win, text="gems.json URL:", bg=BG, fg=DIM, font=("Segoe UI", 9)).grid(
            row=2, column=0, columnspan=2, sticky="w", padx=16)
        v_g = tk.StringVar(value=self.cfg.get("db_gems_url", ""))
        tk.Entry(win, textvariable=v_g, width=56, bg=PANEL, fg=TEXT, insertbackground=TEXT, bd=0,
                 highlightthickness=1, highlightbackground=BORDER, font=("Segoe UI", 9)).grid(
                 row=3, column=0, columnspan=2, sticky="we", padx=16, pady=(2, 8))
        tk.Label(win, text=self._t("builds.json URL (optional):", "builds.json URL (optional):"),
                 bg=BG, fg=DIM, font=("Segoe UI", 9)).grid(row=4, column=0, columnspan=2, sticky="w", padx=16)
        v_b = tk.StringVar(value=self.cfg.get("db_builds_url", ""))
        tk.Entry(win, textvariable=v_b, width=56, bg=PANEL, fg=TEXT, insertbackground=TEXT, bd=0,
                 highlightthickness=1, highlightbackground=BORDER, font=("Segoe UI", 9)).grid(
                 row=5, column=0, columnspan=2, sticky="we", padx=16, pady=(2, 8))
        status = tk.Label(win, text="", bg=BG, fg=DIM, font=("Segoe UI", 9), justify="left", wraplength=480)
        status.grid(row=6, column=0, columnspan=2, sticky="w", padx=16, pady=(2, 0))

        btns = tk.Frame(win, bg=BG); btns.grid(row=7, column=0, columnspan=2, sticky="we", padx=16, pady=(12, 16))
        btn_go = tk.Button(btns, text=self._t("Jetzt aktualisieren", "Update now"), bg=PURPLE, fg="#fff",
                           relief="flat", bd=0, font=("Segoe UI", 10, "bold"), padx=14, pady=7)
        btn_go.pack(side="left")
        tk.Button(btns, text=self._t("Schließen", "Close"), command=win.destroy, bg=PANEL2, fg=TEXT,
                  relief="flat", bd=0, font=("Segoe UI", 10), padx=14, pady=7).pack(side="left", padx=8)
        win.grid_columnconfigure(0, weight=1)

        def finish(res):
            btn_go.configure(state="normal", text=self._t("Jetzt aktualisieren", "Update now"))
            if "err" in res:
                status.configure(text=self._t("Fehlgeschlagen: ", "Failed: ") + res["err"], fg=RED); return
            msgs = []
            try:
                if "g" in res:
                    data = json.loads(res["g"])
                    if not any(k in data for k in ("Weapon", "Armor", "Ring", "Accessory")):
                        raise ValueError(self._t("keine gültige gems.json (Slots fehlen)",
                                                 "not a valid gems.json (slots missing)"))
                    backup_and_write_json("gems.json", data)
                    reload_gems()
                    n = sum(len(GEMS.get(k, [])) for k in SLOT_KEYS)
                    msgs.append(self._t("gems.json: %d Steine" % n, "gems.json: %d gems" % n))
                if "b" in res:
                    data = json.loads(res["b"])
                    if "builds" not in data:
                        raise ValueError(self._t("keine gültige builds.json", "not a valid builds.json"))
                    backup_and_write_json("builds.json", data)
                    reload_builds()
                    self._rebuild_build_menu()
                    msgs.append(self._t("builds.json: %d Builds" % len(BUILD_LIST),
                                        "builds.json: %d builds" % len(BUILD_LIST)))
            except Exception as e:
                status.configure(text=self._t("Datei ungültig: ", "Invalid file: ") + "%s" % e, fg=RED); return
            self.manual_menu = None
            self._render()
            status.configure(text="✓ " + " · ".join(msgs) + self._t("  (alte Version als .bak gesichert)",
                             "  (old version saved as .bak)"), fg=GREEN)

        def run():
            gurl = v_g.get().strip(); burl = v_b.get().strip()
            if not gurl and not burl:
                status.configure(text=self._t("Bitte mindestens eine URL eintragen.",
                                              "Please enter at least one URL."), fg=AMBER); return
            self.cfg["db_gems_url"] = gurl; self.cfg["db_builds_url"] = burl; save_config(self.cfg)
            btn_go.configure(state="disabled", text=self._t("… lädt …", "… loading …"))
            status.configure(text=self._t("Lade …", "Downloading …"), fg=DIM)

            def work():
                res = {}
                try:
                    if gurl:
                        res["g"] = fetch_url(gurl)
                    if burl:
                        res["b"] = fetch_url(burl)
                except Exception as e:
                    res["err"] = "%s" % e
                self.root.after(0, lambda: finish(res))
            threading.Thread(target=work, daemon=True).start()

        btn_go.configure(command=run)

    # ---------- verdict ----------
    def _verdict(self):
        s = self.slot; eq = self.equipped.get(s, []); free = self.slot_count[s]
        cand = self.candidate; eq_des = {g["de"] for g, _ in eq}
        if not eq and cand is None:
            return (self._t("Noch nichts gescannt", "Nothing scanned yet"), DIM,
                    self._t("Bereiche festlegen und „Scannen & vergleichen“ drücken.",
                            "Set the regions and press 'Scan & compare'."))
        if not eq:
            if getattr(self, "_eq_card_seen", False):
                return ("⚠️ " + self._t("Bereich 1 falsch", "Region 1 wrong"), AMBER,
                        self._t("Bereich 1 erfasst die Auswahl-Karte (mit „Edelstein-Attribut“), "
                                "nicht die ausgerüsteten Effekt-Boxen. Zieh Bereich 1 auf die "
                                "RECHTE Spalte mit den Effekt-Kästen.",
                                "Region 1 is capturing the selection card (with 'Gem Attribute'), "
                                "not the equipped effect boxes. Drag region 1 over the RIGHT column "
                                "with the effect boxes."))
            return (self._t("Ausgerüstete fehlen", "Equipped missing"), AMBER,
                    self._t("Scanne zuerst die ausgerüsteten Steine. Vorschau unter Knopf 1 prüfen.",
                            "Scan the equipped gems first. Check the preview under button 1."))
        if cand is None:
            return (self._t("Kandidat fehlt", "Candidate missing"), AMBER,
                    self._t("Wähle im Spiel links einen Stein an und scanne erneut.",
                            "Select a gem on the left in-game and scan again."))
        if cand.get("unknown"):
            return ("⚠️ " + self._t("STEIN UNKLAR", "GEM UNCLEAR"), AMBER,
                    self._t("Text nicht eindeutig. Rest: „%s“. Prüf „Details“ oder wähl manuell.",
                            "Text not clear. Rest: '%s'. Check 'Details' or pick manually.") % self._gname(cand))
        cs = self._score(cand)
        if cand.get("de") in eq_des:
            return ("ℹ️ " + self._t("Schon ausgerüstet", "Already equipped"), DIM,
                    self._t("„%s“ steckt bereits drin.", "'%s' is already slotted.") % self._gname(cand))
        if free > 0:
            return ("✅ " + self._t("EINFACH EINBETTEN", "JUST EMBED"), GREEN,
                    self._t("Du hast %d freie(n) Slot. Setz „%s“ (%d%%) ein – kein Tausch nötig.",
                            "You have %d free slot(s). Embed '%s' (%d%%) – no swap needed.")
                    % (free, self._gname(cand), cs))
        wk, _ = min(eq, key=lambda x: self._score(x[0])); ws = self._score(wk)
        if cs > ws:
            return ("✅ " + self._t("LOHNT SICH", "WORTH IT"), GREEN,
                    self._t("Tausche:\n  raus → %s (%d%%)\n  rein → %s (%d%%)\n= +%d Punkte",
                            "Swap:\n  out → %s (%d%%)\n  in → %s (%d%%)\n= +%d points")
                    % (self._gname(wk), ws, self._gname(cand), cs, cs - ws))
        return ("❌ " + self._t("LOHNT NICHT", "NOT WORTH IT"), RED,
                self._t("„%s“ (%d%%) ist nicht besser. Schwächster: %s (%d%%). Behalten.",
                        "'%s' (%d%%) is not better. Weakest: %s (%d%%). Keep it.")
                % (self._gname(cand), cs, self._gname(wk), ws))

    # ---------- render ----------
    def _render(self):
        self.btn_lang.configure(text="DE ⇄ EN")
        self.btn_update.configure(text=self._t("🔄 Update", "🔄 Update"))
        self.btn_theme.configure(text=self._t("🌙 Dunkel", "🌙 Dark") if self.theme == "light"
                                 else self._t("☀️ Hell", "☀️ Light"))
        self.lbl_build.configure(text=self._t("Build:", "Build:"))
        self.lbl_guide_hint.configure(text=self._t(
            "Build oben umschalten ändert auch die Bewertung im Scanner & Loadout.",
            "Switching the build above also changes the rating in Scanner & Loadout."))
        tabdefs = [(self.tab_quick, "quick", self._t("⚡ Schnell", "⚡ Quick")),
                   (self.tab_scan, "scanner", self._t("🔍 Slot", "🔍 Slot")),
                   (self.tab_hero, "hero", self._t("🦸 Held", "🦸 Hero")),
                   (self.tab_skill, "skill", self._t("🧠 Skills", "🧠 Skills")),
                   (self.tab_load, "loadout", self._t("🎒 Loadout", "🎒 Loadout")),
                   (self.tab_guide, "guide", self._t("📖 Guide", "📖 Guide"))]
        for btn, v, label in tabdefs:
            btn.configure(text=label, bg=PANEL2 if self.view == v else PANEL,
                          fg=TEXT if self.view == v else DIM)
        for vw in (self.quick_view, self.scan_view, self.hero_view, self.skill_view,
                   self.load_view, self.guide_view):
            vw.pack_forget()
        if self.view == "quick":
            self.quick_view.pack(fill="both", expand=True); self._render_quick()
        elif self.view == "scanner":
            self.scan_view.pack(fill="both", expand=True); self._render_scanner()
        elif self.view == "hero":
            self.hero_view.pack(fill="both", expand=True); self._render_hero()
        elif self.view == "skill":
            self.skill_view.pack(fill="both", expand=True); self._render_skill()
        elif self.view == "loadout":
            self.load_view.pack(fill="both", expand=True); self._render_loadout()
        else:
            self.guide_view.pack(fill="both", expand=True)
            self._fill_guide()

    def _render_scanner(self):
        self.btn_pve.configure(bg=PURPLE if self.mode == "pve" else PANEL, fg="#fff" if self.mode == "pve" else DIM)
        self.btn_pvp.configure(bg=PURPLE if self.mode == "pvp" else PANEL, fg="#fff" if self.mode == "pvp" else DIM)
        self.lbl_slot.configure(text=self._t("Ausrüstungs-Slot", "Equipment slot"))
        self.lbl_slots.configure(text=self._t("freie (leere) Slots — 0 = alle voll",
                                              "free (empty) slots — 0 = all full"))
        for key, b in self.slot_btns.items():
            on = (key == self.slot)
            b.configure(text=self._sname(key), bg=PURPLE if on else PANEL2, fg="#fff" if on else DIM)
        self.lbl_cnt.configure(text=str(self.slot_count[self.slot]))
        self.btn_reg_eq.configure(fg=GREEN if self.region_eq else TEXT, text=self._t(
            "🎯 1) Bereich „Ausgerüstet“ (rechts)", "🎯 1) Region 'Equipped' (right)") + ("   ✓" if self.region_eq else ""))
        self.btn_reg_cand.configure(fg=GREEN if self.region_cand else TEXT, text=self._t(
            "🎯 2) Bereich „Auswahl“ (links)", "🎯 2) Region 'Selection' (left)") + ("   ✓" if self.region_cand else ""))
        self.lbl_prev_eq.configure(text=(self._t("erfasst: ", "captured: ") + self.prev_eq) if self.prev_eq else "")
        self.lbl_prev_cand.configure(text=(self._t("erfasst: ", "captured: ") + self.prev_cand) if self.prev_cand else "")
        if self.btn_scan["state"] == "normal" or str(self.btn_scan["state"]) == "normal":
            self.btn_scan.configure(text=self._t("📷  SCANNEN & VERGLEICHEN", "📷  SCAN & COMPARE"))
        self.btn_eq_only.configure(text=self._t("↻ nur Ausgerüstete", "↻ equipped only"))
        self.btn_cand_only.configure(text=self._t("↻ nur Auswahl", "↻ selection only"))
        self.chk_scan_auto.configure(text=self._t(
            "🔁 Auto-Scan – vergleicht automatisch, sobald du einen Edelstein anzeigst",
            "🔁 Auto-scan – compares automatically when you view a gem"))
        self.lbl_scan_auto.configure(text=self._t(
            "● Auto-Scan läuft – wähle im Spiel einen Edelstein an; das Tool vergleicht von selbst.",
            "● Auto-scan running – select a gem in-game; the tool compares on its own.")
            if self.scan_auto.get() else "")
        self.chk_dbg.configure(text=self._t("🔍 Details anzeigen", "🔍 show details"))
        self.lbl_manual.configure(text=self._t("Auswahl falsch? manuell:", "Wrong selection? manual:"))
        self.btn_reset.configure(text=self._t("zurücksetzen", "reset"))

        for x in self.vin.winfo_children():
            x.destroy()
        title, col, body = self._verdict()
        self.verdict.configure(highlightbackground=col)
        tk.Label(self.vin, text=title, bg=PANEL2, fg=col, font=("Segoe UI", 15, "bold"),
                 anchor="w", justify="left", wraplength=520).pack(anchor="w")
        tk.Label(self.vin, text=body, bg=PANEL2, fg=TEXT, font=("Segoe UI", 10),
                 anchor="w", justify="left", wraplength=520).pack(anchor="w", pady=(6, 0))

        if self.candidate is not None:
            self.manual_row.pack(anchor="w", pady=(8, 0), before=self.result)
            if self.manual_menu is None or self._manual_slot != self.slot or getattr(self, "_manual_lang", None) != self.lang:
                if self.manual_menu is not None:
                    self.manual_menu.destroy()
                names = [self._gname(g) for g in GEMS.get(self.slot, [])] or ["—"]
                self.manual_menu = tk.OptionMenu(self.manual_row, self.manual_var, *names, command=self._manual_apply)
                self.manual_menu.configure(bg=PANEL, fg=TEXT, activebackground=PURPLE, highlightthickness=0,
                                           bd=0, font=("Segoe UI", 8))
                self.manual_menu["menu"].configure(bg=PANEL, fg=TEXT)
                self.manual_menu.pack(side="left", padx=6)
                self._manual_slot = self.slot; self._manual_lang = self.lang
        else:
            self.manual_row.pack_forget()

        for x in self.result.winfo_children():
            x.destroy()
        eq = self.equipped.get(self.slot, [])
        tk.Label(self.result, text=self._t("Aktuell ausgerüstet (erkannt)", "Currently equipped (detected)"),
                 bg=BG, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(anchor="w")
        if not eq:
            tk.Label(self.result, text=self._t("— noch nichts erkannt —", "— nothing detected yet —"),
                     bg=BG, fg=DIM, font=("Segoe UI", 9)).pack(anchor="w", pady=(2, 0))
        wkid = min(eq, key=lambda x: self._score(x[0]))[0]["id"] if eq else None
        for g, conf in sorted(eq, key=lambda x: -self._score(x[0])):
            sc = self._score(g); tl, tc = tier_of(sc)
            rf = tk.Frame(self.result, bg=BG); rf.pack(fill="x", pady=1)
            tk.Label(rf, text="●", bg=BG, fg=tc, font=("Segoe UI", 9)).pack(side="left", padx=(0, 4))
            disp = ("≈ " + self._gname(g)) if g.get("auto") else self._gname(g)
            tk.Label(rf, text=disp, bg=BG, fg=TEXT, font=("Segoe UI", 9), anchor="w",
                     wraplength=300, justify="left").pack(side="left", fill="x", expand=True)
            if len(eq) >= 2 and g["id"] == wkid:
                tk.Label(rf, text=self._t("schwächster", "weakest"), bg=BG, fg=AMBER,
                         font=("Segoe UI", 8)).pack(side="right", padx=4)
            tk.Label(rf, text=f"{sc}%", bg=tc, fg=self._text_on(tc), font=("Segoe UI", 9, "bold"), padx=5).pack(side="right")

        if self.candidate is not None:
            tk.Label(self.result, text=self._t("Angewählter Stein (Kandidat)", "Selected gem (candidate)"),
                     bg=BG, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(12, 2))
            g = self.candidate; sc = self._score(g); tl, tc = tier_of(sc)
            rf = tk.Frame(self.result, bg=BG); rf.pack(fill="x", pady=1)
            tk.Label(rf, text=f"[{tl}]", bg=BG, fg=tc, font=("Segoe UI", 9, "bold")).pack(side="left", padx=(0, 4))
            disp = ("≈ " + self._gname(g)) if g.get("auto") else self._gname(g)
            tk.Label(rf, text=disp, bg=BG, fg=TEXT, font=("Segoe UI", 9), anchor="w",
                     wraplength=280, justify="left").pack(side="left", fill="x", expand=True)
            tk.Label(rf, text=f"{sc}%", bg=tc, fg=self._text_on(tc), font=("Segoe UI", 9, "bold"), padx=5).pack(side="right")
            if g.get("unknown"):
                info = "⚠️ " + self._t("Text unklar – bitte prüfen/manuell wählen", "text unclear – check/pick manually")
            elif g.get("auto"):
                info = self._gnote(g) + self._t("  (nicht in DB – aus Text verstanden)", "  (not in DB – understood from text)")
            else:
                info = self._t("Erkennung: %s (%d%%) · ", "Recognition: %s (%d%%) · ") % (
                    self._t("sicher", "sure") if self.cand_conf >= 85 else self._t("wahrscheinlich", "likely"),
                    int(self.cand_conf)) + self._gnote(g)
            tk.Label(self.result, text=info, bg=BG, fg=DIM, font=("Segoe UI", 8),
                     wraplength=480, justify="left").pack(anchor="w")

        ref = sorted(GEMS.get(self.slot, []), key=lambda g: -self._score(g))[:IDEAL_SHOW]
        if ref:
            tk.Label(self.result, text=self._t("Ideal für %s – %s", "Ideal for %s – %s") % (
                self.mode.upper(), self._sname(self.slot)), bg=BG, fg=DIM,
                font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(12, 2))
            for g in ref:
                sc = self._score(g); _, tc = tier_of(sc)
                rf = tk.Frame(self.result, bg=BG); rf.pack(fill="x")
                tk.Label(rf, text="·", bg=BG, fg=DIM, font=("Segoe UI", 8)).pack(side="left", padx=(2, 4))
                tk.Label(rf, text=self._gname(g), bg=BG, fg=DIM, font=("Segoe UI", 8), anchor="w",
                         wraplength=320, justify="left").pack(side="left", fill="x", expand=True)
                tk.Label(rf, text=f"{sc}%", bg=BG, fg=tc, font=("Segoe UI", 8, "bold")).pack(side="right")

        if self.show_debug.get():
            dbg = (self.dbg_eq + "\n\n" + self.dbg_cand).strip() or self._t("(noch nichts gescannt)", "(nothing scanned)")
            box = tk.Frame(self.result, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            box.pack(fill="x", pady=(12, 0))
            tk.Label(box, text=self._t("🔍 Details (erkannter Text)", "🔍 Details (detected text)"), bg=PANEL,
                     fg=TEAL, font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=8, pady=(6, 0))
            tk.Label(box, text=dbg, bg=PANEL, fg=DIM, font=("Consolas", 8), anchor="w",
                     justify="left", wraplength=480).pack(anchor="w", padx=8, pady=(2, 6))

    def _char_box(self, title, d):
        box = tk.Frame(self.load_inner, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
        box.pack(fill="x", padx=14, pady=4)
        tk.Label(box, text=title, bg=PANEL, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(7, 2))
        if "pve_de" in d:
            pve = d.get("pve_" + self.lang) or d.get("pve_de") or ""
            pvp = d.get("pvp_" + self.lang) or d.get("pvp_de") or ""
            tk.Label(box, text="PvE: " + pve, bg=PANEL, fg=TEAL, font=("Segoe UI", 8), anchor="w",
                     wraplength=470, justify="left").pack(anchor="w", padx=10)
            tk.Label(box, text="PvP: " + pvp, bg=PANEL, fg="#2f6fc0", font=("Segoe UI", 8), anchor="w",
                     wraplength=470, justify="left").pack(anchor="w", padx=10, pady=(0, 7))
        else:
            v = d.get(self.lang) or d.get("de") or ""
            tk.Label(box, text=v, bg=PANEL, fg=TEXT, font=("Segoe UI", 8), anchor="w",
                     wraplength=470, justify="left").pack(anchor="w", padx=10, pady=(0, 7))

    def _render_loadout(self):
        for x in self.load_inner.winfo_children():
            x.destroy()
        PX = 14
        tk.Label(self.load_inner, text=self._t("Charakter-Analyse (%s)", "Character analysis (%s)") % self.mode.upper(),
                 bg=BG, fg=TEXT, font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=PX, pady=(10, 0))
        tk.Label(self.load_inner, text=self._t("Build: ", "Build: ") + self._bname(self.build),
                 bg=BG, fg=GOLD, font=("Segoe UI", 8, "bold"), wraplength=480,
                 justify="left").pack(anchor="w", padx=PX)

        # ---- 1) AUSRÜSTUNG (gescannt) ----
        tk.Label(self.load_inner, text=self._t("⚔️ 1) Ausrüstung — gescannt", "⚔️ 1) Equipment — scanned"),
                 bg=BG, fg=PURPLE, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=PX, pady=(12, 2))
        tk.Label(self.load_inner, text=self._t(
            "Scanne jeden Slot im Scanner-Tab; hier siehst du alles auf einen Blick.",
            "Scan each slot in the Scanner tab; here you see it all at a glance."),
            bg=BG, fg=DIM, font=("Segoe UI", 8), wraplength=480, justify="left").pack(anchor="w", padx=PX)

        total_have, total_slots = 0, 0
        for key in SLOT_KEYS:
            eq = self.equipped.get(key, [])
            total_slots += len(eq)
            box = tk.Frame(self.load_inner, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            box.pack(fill="x", padx=PX, pady=4)
            hd = tk.Frame(box, bg=PANEL); hd.pack(fill="x", padx=10, pady=(7, 2))
            tk.Label(hd, text=self._sname(key), bg=PANEL, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(side="left")
            avg = int(sum(self._score(g) for g, _ in eq) / len(eq)) if eq else 0
            if eq:
                _, gc = tier_of(avg)
                tk.Label(hd, text=self._t("Ø %d%%", "avg %d%%") % avg, bg=gc, fg=self._text_on(gc),
                         font=("Segoe UI", 8, "bold"), padx=5).pack(side="right")
            else:
                tk.Label(hd, text=self._t("nicht gescannt", "not scanned"), bg=PANEL, fg=DIM,
                         font=("Segoe UI", 8)).pack(side="right")
            if eq:
                for g, _ in sorted(eq, key=lambda x: -self._score(x[0])):
                    sc = self._score(g); _, tc = tier_of(sc)
                    if sc >= 75:
                        total_have += 1
                    rf = tk.Frame(box, bg=PANEL); rf.pack(fill="x", padx=10)
                    tk.Label(rf, text="●", bg=PANEL, fg=tc, font=("Segoe UI", 8)).pack(side="left", padx=(0, 4))
                    disp = ("≈ " + self._gname(g)) if g.get("auto") else self._gname(g)
                    tk.Label(rf, text=disp, bg=PANEL, fg=TEXT, font=("Segoe UI", 8), anchor="w",
                             wraplength=330, justify="left").pack(side="left", fill="x", expand=True)
                    tk.Label(rf, text=f"{sc}%", bg=PANEL, fg=tc, font=("Segoe UI", 8, "bold")).pack(side="right")
                have_ids = {g["id"] for g, _ in eq}
                ideal = sorted(GEMS.get(key, []), key=lambda g: -self._score(g))[:IDEAL_SHOW]
                missing = [g for g in ideal if g["id"] not in have_ids and self._score(g) >= 75]
                if missing:
                    tk.Label(box, text=self._t("Tipp: hol dir ", "Tip: aim for ") + ", ".join(self._gname(g) for g in missing[:2]),
                             bg=PANEL, fg=AMBER, font=("Segoe UI", 8), wraplength=460,
                             justify="left").pack(anchor="w", padx=10, pady=(2, 7))
                else:
                    tk.Label(box, text=self._t("solide ✓", "solid ✓"), bg=PANEL, fg=GREEN,
                             font=("Segoe UI", 8)).pack(anchor="w", padx=10, pady=(2, 7))
            else:
                tk.Label(box, text=self._t("Im Scanner-Tab „%s“ wählen und scannen.", "Select '%s' in Scanner tab and scan.")
                         % self._sname(key), bg=PANEL, fg=DIM, font=("Segoe UI", 8)).pack(anchor="w", padx=10, pady=(2, 7))

        tk.Label(self.load_inner, text=self._t(
            "Stark besetzte Slots (A/S): %d von %d", "Strong slots (A/S): %d of %d") % (total_have, total_slots),
            bg=BG, fg=TEXT, font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=PX, pady=(6, 0))

        # ---- 2) CHARAKTER (Empfehlungen) ----
        tk.Label(self.load_inner, text=self._t("👤 2) Charakter — Empfehlungen", "👤 2) Character — recommendations"),
                 bg=BG, fg=PURPLE, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=PX, pady=(14, 2))
        tk.Label(self.load_inner, text=self._t(
            "Helden, Brandmal & Sammlung sind Icons – nicht zuverlässig scannbar. Darum hier die "
            "Empfehlungen für deinen Build zum Abgleich mit deinem Spiel (siehe Screenshots „Held/Brandmal/Sammlung“).",
            "Heroes, brands & collection are icons – not reliably scannable. So here are the recommendations "
            "for your build to compare with your game (see your 'Hero/Brand/Collection' screens)."),
            bg=BG, fg=DIM, font=("Segoe UI", 8), wraplength=480, justify="left").pack(anchor="w", padx=PX, pady=(0, 4))

        build = next((b for b in BUILD_LIST if b["name"] == self.build), None)
        char = (build or {}).get("char", {})
        if char.get("note"):
            d = char["note"]
            tk.Label(self.load_inner, text=(d.get(self.lang) or d.get("de") or ""), bg=BG, fg=AMBER,
                     font=("Segoe UI", 8, "italic"), wraplength=480, justify="left").pack(anchor="w", padx=PX, pady=(0, 4))
        order = [("heroes", "🦸 Helden", "🦸 Heroes"), ("brands", "🔥 Brandmal", "🔥 Brands"),
                 ("pets", "🐾 Pets", "🐾 Pets"), ("mounts", "🐴 Reittier", "🐴 Mounts"),
                 ("collection", "🃏 Sammlung", "🃏 Collection"),
                 ("inheritance", "🌳 Vermächtnis", "🌳 Inheritance"),
                 ("adventurer", "🧭 Abenteurer", "🧭 Adventurer")]
        for key, tde, ten in order:
            if key in char:
                self._char_box(self._t(tde, ten), char[key])
        tk.Label(self.load_inner, text=self._t(
            "Community-Empfehlungen (NiaMeowDB) – keine offiziellen Werte.",
            "Community recommendations (NiaMeowDB) – not official numbers."),
            bg=BG, fg=DIM, font=("Segoe UI", 8), wraplength=480, justify="left").pack(anchor="w", padx=PX, pady=(8, 12))

    def _fill_guide(self):
        self.guide_txt.configure(state="normal")
        self.guide_txt.delete("1.0", "end")
        name = self.build
        build = next((b for b in BUILD_LIST if b["name"] == name), None)
        self.guide_txt.insert("end", name + "\n", "H2")
        self.guide_txt.insert("end", self._t(
            "Community-Einschätzung (NiaMeowDB Mai 2026, game-vault Wiki) – keine offiziellen Werte.\n",
            "Community estimate (NiaMeowDB May 2026, game-vault wiki) – not official numbers.\n"), "P")
        if build:
            for ln in build["lines"]:
                txt = ln.get(self.lang) or ln.get("de") or ln.get("en") or ""
                if ln["k"] == "B":
                    self.guide_txt.insert("end", "•  " + txt + "\n", "B")
                else:
                    self.guide_txt.insert("end", txt + "\n", ln["k"])
        self.guide_txt.configure(state="disabled")

    # ---------- render: Schnell-Scan ----------
    def _quick_reason(self, g, sc):
        """Kurze Begründung pro Stein: Build-Eignung + kuratierte Notiz."""
        note = self._gnote(g)
        if g.get("auto"):
            return note
        cat = g.get("cat", "atk")
        mult = BUILD_PREFS.get(self.build, {}).get(cat, 1.0)
        if mult <= 0.9 or sc < 55:
            tag = self._t("schwach für diesen Build", "weak for this build")
        elif sc >= 90:
            tag = self._t("Top-Pick für diesen Build", "top pick for this build")
        elif sc >= 75:
            tag = self._t("stark", "strong")
        else:
            tag = self._t("solide", "solid")
        return ("%s — %s" % (tag, note)) if note else tag

    def _build_top_gems(self, k=5):
        """Die k bestbewerteten Steine (über alle Slots) für den aktuellen Build/Modus,
        dedupliziert nach Anzeigename – für „ideal für diesen Build"."""
        seen, out = set(), []
        pool = [g for slot in SLOT_KEYS for g in GEMS.get(slot, [])]
        for g in sorted(pool, key=lambda x: -self._score(x)):
            nm = self._gname(g)
            if nm in seen:
                continue
            seen.add(nm)
            out.append((nm, self._score(g)))
            if len(out) >= k:
                break
        return out

    def _render_quick(self):
        self.lbl_quick_intro.configure(text=self._t(
            "Ein Knopf: Markiere einmal den Spielbereich mit den Edelstein-Effekten (z. B. Inventar). "
            "Der Scan liest ALLE Steine, bewertet sie für deinen Build und sortiert sie (bester → schwächster).",
            "One button: mark the game area with the gem effects once (e.g. inventory). "
            "The scan reads ALL gems, rates them for your build and sorts them (best → weakest)."))
        self.btn_qpve.configure(bg=PURPLE if self.mode == "pve" else PANEL, fg="#fff" if self.mode == "pve" else DIM)
        self.btn_qpvp.configure(bg=PURPLE if self.mode == "pvp" else PANEL, fg="#fff" if self.mode == "pvp" else DIM)
        self.btn_reg_quick.configure(fg=GREEN if self.region_quick else TEXT, text=self._t(
            "🎯 Spielbereich festlegen", "🎯 Set game region") + ("   ✓" if self.region_quick else ""))
        self.lbl_prev_quick.configure(
            text=(self._t("erfasst: ", "captured: ") + self.prev_quick) if self.prev_quick else "")
        if str(self.btn_scan_quick["state"]) == "normal":
            self.btn_scan_quick.configure(text=self._t("⚡  SCHNELL-SCAN", "⚡  QUICK SCAN"))
        self.chk_dbg_q.configure(text=self._t("🔍 Details anzeigen", "🔍 show details"))

        for x in self.quick_inner.winfo_children():
            x.destroy()
        tk.Label(self.quick_inner, text=self._t("Gefundene Steine – %s · %s", "Found gems – %s · %s")
                 % (self.mode.upper(), self._bname(self.build)), bg=BG, fg=GOLD, font=("Segoe UI", 9, "bold"),
                 anchor="w", justify="left", wraplength=500).pack(anchor="w", pady=(8, 4))
        res = self.quick_results
        if not res:
            tk.Label(self.quick_inner, text=self._t(
                "— noch nichts gescannt — Bereich festlegen und „Schnell-Scan“ drücken.",
                "— nothing scanned yet — set the region and press 'Quick Scan'."),
                bg=BG, fg=DIM, font=("Segoe UI", 9), wraplength=500, justify="left").pack(anchor="w")

        # ---- 🩺 Build-Doktor: klare Empfehlung was behalten / tauschen ----
        if res:
            real = [(g, self._score(g)) for g, conf in res if not g.get("auto")]
            keepers = [x for x in real if x[1] >= 75]
            swaps = [x for x in real if x[1] < 55]
            doc = tk.Frame(self.quick_inner, bg=PANEL2, highlightbackground=GOLD, highlightthickness=1)
            doc.pack(fill="x", pady=(2, 8))
            tk.Label(doc, text=self._t("🩺 Build-Doktor — %s · %s", "🩺 Build doctor — %s · %s")
                     % (self._bname(self.build), self.mode.upper()), bg=PANEL2, fg=GOLD,
                     font=("Segoe UI", 9, "bold"), anchor="w", wraplength=480,
                     justify="left").pack(anchor="w", padx=10, pady=(7, 2))
            tk.Label(doc, text=self._t("✅ Behalten: %d starke Steine   ·   ❌ Tauschen: %d",
                                       "✅ Keep: %d strong gems   ·   ❌ Swap: %d")
                     % (len(keepers), len(swaps)), bg=PANEL2, fg=TEXT,
                     font=("Segoe UI", 9), anchor="w").pack(anchor="w", padx=10)
            for g, sc in sorted(swaps, key=lambda x: x[1]):
                tk.Label(doc, text="❌ %s (%d%%) — %s" % (
                    self._gname(g), sc,
                    self._t("schwach für %s", "weak for %s") % self._bname(self.build).split("(")[0].strip()),
                    bg=PANEL2, fg=AMBER, font=("Segoe UI", 8), anchor="w",
                    wraplength=470, justify="left").pack(anchor="w", padx=(16, 8))
            top = self._build_top_gems(5)
            if top:
                tk.Label(doc, text=self._t("💡 Ideal für diesen Build: ", "💡 Best for this build: ")
                         + ", ".join("%s (%d%%)" % (n, s) for n, s in top),
                         bg=PANEL2, fg=GREEN, font=("Segoe UI", 8), anchor="w",
                         wraplength=470, justify="left").pack(anchor="w", padx=10, pady=(3, 7))

        for g, conf in sorted(res, key=lambda x: -self._score(x[0])):
            sc = self._score(g); tl, tc = tier_of(sc)
            if g.get("auto"):
                sym, syc = "≈", AMBER
            elif sc >= 75:
                sym, syc = "✅", GREEN
            elif sc >= 55:
                sym, syc = "•", DIM
            else:
                sym, syc = "⚠️", AMBER
            rf = tk.Frame(self.quick_inner, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            rf.pack(fill="x", pady=2)
            top = tk.Frame(rf, bg=PANEL); top.pack(fill="x")
            tk.Label(top, text=sym, bg=PANEL, fg=syc, font=("Segoe UI", 10)).pack(side="left", padx=(8, 2), pady=(6, 0))
            tk.Label(top, text="[%s]" % tl, bg=PANEL, fg=tc, font=("Segoe UI", 10, "bold")).pack(side="left", padx=(0, 4), pady=(6, 0))
            tk.Label(top, text=self._gname(g), bg=PANEL, fg=TEXT, font=("Segoe UI", 9), anchor="w",
                     wraplength=300, justify="left").pack(side="left", fill="x", expand=True, pady=(6, 0))
            tk.Label(top, text="%d%%" % sc, bg=tc, fg=self._text_on(tc), font=("Segoe UI", 9, "bold"),
                     padx=5).pack(side="right", padx=8, pady=(6, 0))
            reason = self._quick_reason(g, sc)
            if reason:
                tk.Label(rf, text=reason, bg=PANEL, fg=DIM, font=("Segoe UI", 8), anchor="w",
                         justify="left", wraplength=480).pack(anchor="w", padx=(34, 8), pady=(1, 6))
        if self.quick_unclear:
            tk.Label(self.quick_inner, text=self._t(
                "%d Zeile(n) nicht eindeutig (UI-Text/unbekannt) – ggf. enger markieren.",
                "%d line(s) not clear (UI text/unknown) – mark more tightly if needed.")
                % self.quick_unclear, bg=BG, fg=AMBER, font=("Segoe UI", 8), wraplength=500,
                justify="left").pack(anchor="w", pady=(8, 0))
        tk.Label(self.quick_inner, text=self._t(
            "✅ stark · • solide · ⚠️ schwach für Build · ≈ aus Text verstanden (nicht in DB)",
            "✅ strong · • solid · ⚠️ weak for build · ≈ understood from text (not in DB)"),
            bg=BG, fg=DIM, font=("Segoe UI", 8), wraplength=500, justify="left").pack(anchor="w", pady=(8, 4))
        if self.show_debug.get() and self.dbg_quick:
            box = tk.Frame(self.quick_inner, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            box.pack(fill="x", pady=(4, 8))
            tk.Label(box, text=self.dbg_quick, bg=PANEL, fg=DIM, font=("Consolas", 8), anchor="w",
                     justify="left", wraplength=500).pack(anchor="w", padx=8, pady=6)

    # ---------- render: Skill-Berater ----------
    def _skill_reason(self, sk, sc):
        note = self._gnote(sk)
        cat = sk.get("cat", "atk")
        mult = BUILD_PREFS.get(self.build, {}).get(cat, 1.0)
        tier = sk.get("tier", "?")
        if sc >= 75:
            tag = self._t("LERNEN – stark für diesen Build", "LEARN – strong for this build")
        elif sc >= 55:
            tag = self._t("solide", "solid")
        elif sc >= 40:
            tag = self._t("schwach für diesen Build", "weak for this build")
        else:
            tag = self._t("MEIDEN", "AVOID")
        base = "%s (Tier %s)" % (tag, tier) if tier and tier != "?" else tag
        if mult <= 0.85:
            base += self._t(" · falscher Build", " · wrong build")
        return ("%s — %s" % (base, note)) if note else base

    def _render_skill(self):
        self.lbl_skill_intro.configure(text=self._t(
            "Markiere EINMAL den Bereich mit den angebotenen Skills (Namen + Beschreibung). "
            "Beim Level-Up / in der Auswahl drück „Skills prüfen“ – das Tool sagt dir, welchen "
            "du LERNEN und welchen du MEIDEN solltest, passend zu deinem Build.",
            "Mark the area with the offered skills (names + descriptions) ONCE. On level-up / in "
            "the choice screen press 'Check skills' – the tool tells you which to LEARN and which "
            "to AVOID for your build."))
        self.btn_reg_skill.configure(fg=GREEN if self.region_skill else TEXT, text=self._t(
            "🎯 Skill-Bereich festlegen", "🎯 Set skill region") + ("   ✓" if self.region_skill else ""))
        self.lbl_prev_skill.configure(
            text=(self._t("erfasst: ", "captured: ") + self.prev_skill) if self.prev_skill else "")
        if str(self.btn_scan_skill["state"]) == "normal":
            self.btn_scan_skill.configure(text=self._t("🧠  SKILLS PRÜFEN", "🧠  CHECK SKILLS"))
        self.chk_skill_auto.configure(text=self._t(
            "🔁 Auto-Scan – erkennt automatisch, sobald Skills erscheinen",
            "🔁 Auto-scan – detects automatically when skills appear"))
        self.lbl_skill_auto.configure(text=self._t(
            "● Auto-Scan läuft – kein Knopfdruck nötig; sobald sich der Bereich ändert, wird geprüft.",
            "● Auto-scan running – no click needed; it checks whenever the area changes.")
            if self.skill_auto.get() else "")
        self.chk_dbg_s.configure(text=self._t("🔍 Details anzeigen", "🔍 show details"))

        for x in self.skill_inner.winfo_children():
            x.destroy()
        tk.Label(self.skill_inner, text=self._t("Angebotene Skills – %s · %s", "Offered skills – %s · %s")
                 % (self.mode.upper(), self._bname(self.build)), bg=BG, fg=GOLD, font=("Segoe UI", 9, "bold"),
                 anchor="w", justify="left", wraplength=500).pack(anchor="w", pady=(8, 4))
        res = self.skill_results
        if not res:
            tk.Label(self.skill_inner, text=self._t(
                "— noch nichts gescannt — Bereich festlegen und „Skills prüfen“ drücken.",
                "— nothing scanned yet — set the region and press 'Check skills'."),
                bg=BG, fg=DIM, font=("Segoe UI", 9), wraplength=500, justify="left").pack(anchor="w")
            self._skill_note()
            return

        score = self._skill_score_run
        ranked = sorted(res, key=lambda x: -score(x[0]))
        learn = [(sk, score(sk)) for sk, _ in ranked if score(sk) >= 60]
        avoid = [(sk, score(sk)) for sk, _ in ranked if score(sk) < 40]

        # ---- 🎒 Dein Lauf (gewählte Skills) + Reset ----
        runf = tk.Frame(self.skill_inner, bg=PANEL2, highlightbackground=BORDER, highlightthickness=1)
        runf.pack(fill="x", pady=(2, 6))
        names = (", ".join(p["name"] for p in self.run_skills) if self.run_skills
                 else self._t("(noch leer – unten „+ Lauf“ drücken)", "(empty – press '+ run' below)"))
        tk.Label(runf, text=self._t("🎒 Dein Lauf (%d): ", "🎒 Your run (%d): ") % len(self.run_skills) + names,
                 bg=PANEL2, fg=TEAL, font=("Segoe UI", 8, "bold"), anchor="w", wraplength=370,
                 justify="left").pack(side="left", padx=10, pady=5)
        tk.Button(runf, text=self._t("🗑 Neuer Lauf", "🗑 New run"), command=self._skill_run_reset,
                  relief="flat", bd=0, bg=PANEL, fg=DIM, font=("Segoe UI", 8, "bold"),
                  padx=8, pady=3).pack(side="right", padx=8, pady=4)

        # ---- 🧠 Skill-Doktor ----
        doc = tk.Frame(self.skill_inner, bg=PANEL2, highlightbackground=GOLD, highlightthickness=1)
        doc.pack(fill="x", pady=(2, 8))
        tk.Label(doc, text=self._t("🧠 Skill-Doktor — %s · %s", "🧠 Skill doctor — %s · %s")
                 % (self._bname(self.build).split("(")[0].strip(), self.mode.upper()), bg=PANEL2, fg=GOLD,
                 font=("Segoe UI", 9, "bold"), anchor="w", wraplength=480,
                 justify="left").pack(anchor="w", padx=10, pady=(7, 2))
        if learn:
            bsk, bsc = learn[0]
            syn = self._skill_synergy(bsk)[1]
            tk.Label(doc, text="👉 " + self._t("LERNEN: %s (%d%%)", "LEARN: %s (%d%%)")
                     % (self._gname(bsk), bsc) + (("  " + syn) if syn else ""),
                     bg=PANEL2, fg=GREEN, font=("Segoe UI", 10, "bold"),
                     anchor="w", wraplength=470, justify="left").pack(anchor="w", padx=10)
            if len(learn) > 1:
                tk.Label(doc, text=self._t("auch gut: ", "also good: ")
                         + ", ".join("%s (%d%%)" % (self._gname(s), sc) for s, sc in learn[1:4]),
                         bg=PANEL2, fg=TEXT, font=("Segoe UI", 8), anchor="w",
                         wraplength=470, justify="left").pack(anchor="w", padx=10, pady=(1, 0))
        else:
            tk.Label(doc, text=self._t("Kein klarer Top-Skill erkannt – nimm den höchsten unten.",
                                       "No clear top skill detected – take the highest below."),
                     bg=PANEL2, fg=TEXT, font=("Segoe UI", 9), anchor="w").pack(anchor="w", padx=10)
        if avoid:
            tk.Label(doc, text="❌ " + self._t("MEIDEN: ", "AVOID: ")
                     + ", ".join("%s (%d%%)" % (self._gname(s), sc) for s, sc in avoid),
                     bg=PANEL2, fg=AMBER, font=("Segoe UI", 8), anchor="w",
                     wraplength=470, justify="left").pack(anchor="w", padx=10, pady=(3, 7))
        else:
            tk.Label(doc, text="", bg=PANEL2, font=("Segoe UI", 2)).pack()

        picked_names = {p["name"] for p in self.run_skills}
        for sk, conf in ranked:
            sc = score(sk); tl, tc = tier_of(sc)
            if sk.get("auto"):
                sym, syc = "≈", AMBER
            elif sc >= 75:
                sym, syc = "✅", GREEN
            elif sc >= 55:
                sym, syc = "•", DIM
            elif sc >= 40:
                sym, syc = "⚠️", AMBER
            else:
                sym, syc = "❌", RED
            rf = tk.Frame(self.skill_inner, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            rf.pack(fill="x", pady=2)
            top = tk.Frame(rf, bg=PANEL); top.pack(fill="x")
            tk.Label(top, text=sym, bg=PANEL, fg=syc, font=("Segoe UI", 10)).pack(side="left", padx=(8, 2), pady=(6, 0))
            tk.Label(top, text="[%s]" % tl, bg=PANEL, fg=tc, font=("Segoe UI", 10, "bold")).pack(side="left", padx=(0, 4), pady=(6, 0))
            tk.Label(top, text=self._gname(sk), bg=PANEL, fg=TEXT, font=("Segoe UI", 9), anchor="w",
                     wraplength=240, justify="left").pack(side="left", fill="x", expand=True, pady=(6, 0))
            picked = self._gname(sk) in picked_names
            tk.Button(top, text=self._t("✓ im Lauf", "✓ in run") if picked else self._t("+ Lauf", "+ run"),
                      command=(None if picked else (lambda s=sk: self._skill_pick(s))),
                      relief="flat", bd=0, state=("disabled" if picked else "normal"),
                      bg=(GREEN if picked else PANEL2), fg=(self._text_on(GREEN) if picked else TEXT),
                      font=("Segoe UI", 8, "bold"), padx=6, pady=1).pack(side="right", padx=(4, 6), pady=(6, 0))
            tk.Label(top, text="%d%%" % sc, bg=tc, fg=self._text_on(tc), font=("Segoe UI", 9, "bold"),
                     padx=5).pack(side="right", padx=(2, 2), pady=(6, 0))
            reason = self._skill_reason(sk, sc)
            if reason:
                tk.Label(rf, text=reason, bg=PANEL, fg=DIM, font=("Segoe UI", 8), anchor="w",
                         justify="left", wraplength=480).pack(anchor="w", padx=(34, 8), pady=(1, 2))
            syn = self._skill_synergy(sk)[1]
            if syn:
                tk.Label(rf, text=syn, bg=PANEL, fg=TEAL, font=("Segoe UI", 8, "bold"), anchor="w",
                         justify="left", wraplength=480).pack(anchor="w", padx=(34, 8), pady=(0, 6))
        self._skill_note()

    def _skill_note(self):
        tk.Label(self.skill_inner, text=self._t(
            "✅ lernen · • solide · ⚠️ schwach · ❌ meiden · ≈ aus Text verstanden (nicht in DB)",
            "✅ learn · • solid · ⚠️ weak · ❌ avoid · ≈ understood from text (not in DB)"),
            bg=BG, fg=DIM, font=("Segoe UI", 8), wraplength=500, justify="left").pack(anchor="w", pady=(8, 2))
        tk.Label(self.skill_inner, text=self._t(
            "Tipp: spät im Spiel zählt Schaden mehr als Survival (Bosse haben viel HP + Rundenlimit). "
            "Community-Einschätzung, keine offiziellen Werte.",
            "Tip: late game, damage matters more than survival (bosses have huge HP + turn limits). "
            "Community estimate, not official numbers."),
            bg=BG, fg=DIM, font=("Segoe UI", 8), wraplength=500, justify="left").pack(anchor="w", pady=(0, 10))
        if self.show_debug.get() and self.dbg_skill:
            box = tk.Frame(self.skill_inner, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            box.pack(fill="x", pady=(0, 8))
            tk.Label(box, text=self.dbg_skill, bg=PANEL, fg=DIM, font=("Consolas", 8), anchor="w",
                     justify="left", wraplength=500).pack(anchor="w", padx=8, pady=6)

    # ---------- render: Held lesen (Mehrfach-Scan + Vergleich) ----------
    def _hero_label(self, key):
        for k, role, de, en in HERO_SLOTS:
            if k == key:
                return self._t(de, en), role
        return key, "reserve"

    def _render_hero(self):
        self.lbl_hero_intro.configure(text=self._t(
            "Region EINMAL festlegen (der ganze Spiel-Screen reicht). Dann nacheinander Helden "
            "scannen: zuerst die AUSGERÜSTETEN (1–2), dann die RESERVE. Visiere jeden Helden "
            "im Spiel an und drück den passenden Knopf. Das Tool vergleicht Rang + Build-Eignung.",
            "Set the region ONCE (the whole game screen is fine). Then scan heroes one by one: "
            "first the EQUIPPED (1–2), then the RESERVE. Aim at each hero in-game and press the "
            "matching button. The tool compares rank + build suitability."))
        self.btn_reg_hero.configure(fg=GREEN if self.region_hero else TEXT, text=self._t(
            "🎯 Bereich festlegen (ganzer Screen ok)", "🎯 Set region (whole screen ok)")
            + ("   ✓" if self.region_hero else ""))
        self.lbl_prev_hero.configure(
            text=(self._t("erfasst: ", "captured: ") + self.prev_hero) if self.prev_hero else "")
        for key, role, de, en in HERO_SLOTS:
            b = self.hero_btns.get(key)
            if not b:
                continue
            info = self.hero_scans.get(key)
            base = self._t(de, en)
            if str(b["state"]) != "disabled":
                b.configure(text=(base + "  ✓") if info else base,
                            bg=(GREEN if info else (PURPLE if role == "equipped" else PANEL2)),
                            fg=(self._text_on(GREEN) if info else ("#fff" if role == "equipped" else TEXT)))
        self.btn_hero_reset.configure(text=self._t("↺ Helden zurücksetzen", "↺ reset heroes"))
        self.chk_dbg_h.configure(text=self._t("🔍 Details anzeigen", "🔍 show details"))

        for x in self.hero_inner.winfo_children():
            x.destroy()
        if not self.hero_scans:
            tk.Label(self.hero_inner, text=self._t(
                "— noch nichts gescannt — Bereich festlegen, Held im Spiel anvisieren und einen "
                "der Knöpfe oben drücken (Ausgerüstet 1/2, dann Reserve).",
                "— nothing scanned yet — set the region, aim at a hero in-game and press one of "
                "the buttons above (Equipped 1/2, then Reserve)."),
                bg=BG, fg=DIM, font=("Segoe UI", 9), wraplength=500, justify="left").pack(anchor="w", pady=(8, 0))
            self._hero_note()
            return

        # --- Vergleich / Empfehlung ---
        reco = self._hero_reco()
        if reco is not None:
            doc = tk.Frame(self.hero_inner, bg=PANEL2, highlightbackground=GOLD, highlightthickness=1)
            doc.pack(fill="x", pady=(8, 6))
            tk.Label(doc, text=self._t("⚔️ Helden-Vergleich · %s", "⚔️ Hero comparison · %s") % self._bname(self.build),
                     bg=PANEL2, fg=GOLD, font=("Segoe UI", 9, "bold"), wraplength=470,
                     justify="left").pack(anchor="w", padx=10, pady=(7, 2))
            wl, _ = self._hero_label(reco["weak_key"]); bl, _ = self._hero_label(reco["best_key"])
            if reco["better"]:
                txt = self._t(
                    "❌ Tausch-Tipp: „%s\" (Rang +%d, Eignung ×%.2f) ist stärker als dein "
                    "ausgerüsteter „%s\" (Rang +%d, ×%.2f) → erwäge Wechsel.",
                    "❌ Swap tip: '%s' (rank +%d, fit ×%.2f) is stronger than your equipped "
                    "'%s' (rank +%d, ×%.2f) → consider swapping.") % (
                    bl, reco["bp"], reco["bs"], wl, reco["wp"], reco["ws"])
                col = AMBER
            else:
                txt = self._t(
                    "✅ Deine ausgerüsteten Helden sind stark genug – keine Reserve ist klar besser.",
                    "✅ Your equipped heroes are strong enough – no reserve is clearly better.")
                col = GREEN
            tk.Label(doc, text=txt, bg=PANEL2, fg=col, font=("Segoe UI", 8), wraplength=470,
                     justify="left").pack(anchor="w", padx=10, pady=(0, 8))

        # --- Pro Held eine kompakte Karte (gruppiert: ausgerüstet, dann Reserve) ---
        prefs = BUILD_PREFS.get(self.build, {})
        for key, role, de, en in HERO_SLOTS:
            info = self.hero_scans.get(key)
            if not info:
                continue
            power, syn = self._hero_fit(info)
            rank = (info["rank_de"] if self.lang == "de" else info["rank_en"]) or \
                self._t("Rang ?", "rank ?")
            card = tk.Frame(self.hero_inner, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            card.pack(fill="x", pady=3)
            top = tk.Frame(card, bg=PANEL); top.pack(fill="x")
            badge = self._t("ausgerüstet", "equipped") if role == "equipped" else self._t("Reserve", "reserve")
            tk.Label(top, text="%s — %s" % (self._t(de, en), rank), bg=PANEL, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(side="left", padx=10, pady=(7, 0))
            tk.Label(top, text=badge, bg=PANEL,
                     fg=(PURPLE if role == "equipped" else TEAL),
                     font=("Segoe UI", 8, "bold")).pack(side="right", padx=10, pady=(7, 0))
            if syn >= 1.05:
                smsg, scol = self._t("passt gut zum Build", "fits the build"), GREEN
            elif syn <= 0.95:
                smsg, scol = self._t("eher schwach für Build", "rather weak for build"), AMBER
            else:
                smsg, scol = self._t("neutral", "neutral"), DIM
            tk.Label(card, text=self._t("Build-Eignung: %s (Ø ×%.2f)", "Build fit: %s (avg ×%.2f)")
                     % (smsg, syn), bg=PANEL, fg=scol, font=("Segoe UI", 8), anchor="w",
                     wraplength=470, justify="left").pack(anchor="w", padx=12, pady=(1, 0))
            kws = info.get("kw", [])
            if kws:
                chips = ", ".join("%s%s" % (self._t(lde, len_),
                                  " ✓" if prefs.get(cat, 1.0) >= 1.05 else
                                  (" ✗" if prefs.get(cat, 1.0) <= 0.9 else ""))
                                  for cat, lde, len_ in kws)
                tk.Label(card, text=self._t("Effekte: ", "Effects: ") + chips, bg=PANEL, fg=DIM,
                         font=("Segoe UI", 8), anchor="w", wraplength=470,
                         justify="left").pack(anchor="w", padx=12, pady=(0, 7))
            else:
                tk.Label(card, text=self._t("Keine Effekt-Stichwörter erkannt (Effekt-Text mitscannen).",
                                            "No effect keywords found (include the effect text)."),
                         bg=PANEL, fg=DIM, font=("Segoe UI", 8), anchor="w", wraplength=470,
                         justify="left").pack(anchor="w", padx=12, pady=(0, 7))
        self._hero_note()

    def _hero_note(self):
        tk.Label(self.hero_inner, text=self._t(
            "Hinweis: ALLE Helden geben dieselben drei Boni – nur die Höhe steigt mit dem Rang "
            "(ein +2-Held ≈ 120 % mehr Roh-Stats als +0). Die Heldenwahl entscheidet sich über die "
            "Effekt-Synergie mit deinem Build, nicht nur über den Rang.",
            "Note: ALL heroes give the same three bonuses – only the magnitude grows with rank "
            "(a +2 hero ≈ 120% more raw stats than +0). So hero choice comes down to effect synergy "
            "with your build, not just rank."),
            bg=BG, fg=AMBER, font=("Segoe UI", 8), wraplength=500, justify="left").pack(anchor="w", padx=4, pady=(10, 4))
        tk.Label(self.hero_inner, text=self._t(
            "Community-Einschätzung – keine offiziellen Werte.",
            "Community estimate – not official numbers."),
            bg=BG, fg=DIM, font=("Segoe UI", 8), wraplength=500, justify="left").pack(anchor="w", padx=4, pady=(0, 12))
        if self.show_debug.get() and self.dbg_hero:
            box = tk.Frame(self.hero_inner, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            box.pack(fill="x", pady=(0, 8))
            tk.Label(box, text=self.dbg_hero, bg=PANEL, fg=DIM, font=("Consolas", 8), anchor="w",
                     justify="left", wraplength=500).pack(anchor="w", padx=8, pady=6)


def _enable_hidpi():
    """Windows: Prozess DPI-aware machen, damit die Oberfläche SCHARF rendert statt
    von Windows unscharf hochskaliert zu werden (Hauptursache für „alles unscharf")."""
    if sys.platform != "win32":
        return
    try:
        import ctypes
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)   # System-DPI-aware (Win 8.1+)
        except Exception:
            ctypes.windll.user32.SetProcessDPIAware()        # Fallback (Win Vista+)
    except Exception:
        pass


def _run_selftest():
    """Headless-Eigentest (Aufruf: CapybaraGemScanner.exe --selftest): prueft,
    dass die OCR-Engine + Modelle (auch im gebuendelten .exe-Zustand) laden und
    Text erkannt wird. Ergebnis per Exit-Code: 0=ok, 2=Engine fehlt, 3=kein Text,
    4=Fehler. Oeffnet KEIN Fenster."""
    try:
        import numpy as _np
        from PIL import Image as _Img, ImageDraw as _Dr
        try:
            from PIL import ImageFont as _IF
            _font = _IF.truetype("arial.ttf", 34)
        except Exception:
            _font = None
        _im = _Img.new("RGB", (520, 90), "white")
        _Dr.Draw(_im).text((12, 22), "Kritischer Schaden +50%", fill="black", font=_font)
        eng = get_engine()
        if eng is None:
            print("SELFTEST FAIL: OCR-Engine nicht geladen:", _engine_err)
            sys.exit(2)
        res, _ = eng(_np.array(_im))
        txt = [r[1] for r in res] if res else []
        print("SELFTEST OCR:", txt)
        sys.exit(0 if txt else 3)
    except SystemExit:
        raise
    except Exception as e:
        print("SELFTEST ERROR:", repr(e))
        sys.exit(4)


def main():
    if "--selftest" in sys.argv:
        _run_selftest()
        return
    _enable_hidpi()
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
