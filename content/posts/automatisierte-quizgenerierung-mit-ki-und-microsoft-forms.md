---
title: "Quiz-Generierung mit KI und Microsoft Forms"
date: 2025-01-30
draft: false
description: "Eine erprobte Arbeitshilfe, um Quizfragen mit KI vorzubereiten, fachlich zu prüfen und per Schnellimport in Microsoft Forms zu übernehmen."
content_type: "arbeitshilfe"
audience: "Lehrerinnen und Lehrer"
last_reviewed: 2026-08-26
school_status: "persoenlich"
software_versions: "Microsoft Forms und generative KI-Angebote; geprüft August 2026"
duration: "ca. 30–60 Minuten für ein erstes geprüftes Quiz"
tags: ["Microsoft Forms", "Künstliche Intelligenz", "Unterricht", "Quiz", "ChatGPT"]
categories:
  - Unterricht und KI
---

## Kurzüberblick

- **Für wen:** Lehrkräfte, die aus eigenen Notizen einen kontrollierten Quizentwurf erstellen möchten.
- **Ziel:** KI-generierte Fragen fachlich und didaktisch prüfen, in Word strukturieren und in Microsoft Forms importieren.
- **Voraussetzungen und Rechte:** Zugriff auf ein freigegebenes KI-Angebot und Microsoft Forms; keine personenbezogenen Schülerdaten oder nicht freigegebenen Materialien hochladen.
- **Dauer:** Etwa 30–60 Minuten einschließlich fachlicher Prüfung und Testdurchlauf.
- **Geprüfter Stand:** 26.08.2026. KI-Modelle, Tarife und Forms-Menüs ändern sich; die Videos zeigen einen früheren Oberflächenstand.

{{< youtube id="qbzK9sLekJ4" title="Teil 1: Quizfragen mit KI vorbereiten" >}}

[Hier geht's zu Teil 1 auf YouTube](https://youtu.be/qbzK9sLekJ4)

{{< youtube id="b4VGXZfHs-M" title="Teil 2: Quiz in Microsoft Forms importieren" >}}

[Hier geht's zu Teil 2 auf YouTube](https://youtu.be/b4VGXZfHs-M)

---

## Hausaufgaben automatisiert überprüfen – mit KI und Microsoft Forms

In diesem zweiteiligen Video-Workshop zeige ich, wie sich mithilfe von KI auf Basis eigener Unterrichtsnotizen und Screenshots ein Multiple-Choice-Quiz erstellen und direkt in Microsoft Forms importieren lässt – inklusive automatischer Korrektur, ganz ohne manuelle Nacharbeit.

---

## Teil 1: Quiz-Fragen mit KI generieren

### Das Ziel

Das Ziel ist eine automatisch korrigierte Hausaufgaben-Überprüfung. Der Workflow sieht so aus:

1. Unterrichtsnotizen und Screenshots als Grundlage aufbereiten
2. Einen detaillierten Prompt an eine KI schicken
3. Aus dem KI-Output ein Word-Dokument erstellen
4. Dieses Dokument in Microsoft Forms als Quiz importieren

### Die KI-Wahl

In diesem Beispiel nutze ich **ChatGPT 4o** (das Plus-Modell), da es deutlich leistungsfähiger ist als die kostenlose Variante – vor allem beim Verarbeiten von Screenshots. Grundsätzlich funktioniert der Ansatz aber auch mit anderen Modellen wie **DeepSeek**, **Claude** oder **Gemini**.

### Den Prompt aufbauen

Ein guter Prompt ist entscheidend. Ich gebe der KI folgende Informationen mit:

- **Kontext:** Wer bin ich, an welcher Schule unterrichte ich, was ist das Ziel?
- **Unterrichtsthema:** In diesem Fall „Endogene Kräfte" (Geographie, Klasse 7/8)
- **Unterrichtsinhalte:** Meine eigenen Notizen zu den behandelten Themen:
  - Schild- und Schichtvulkane
  - Plattentektonik und Plattengrenzen
  - Erdbeben und Seebeben
  - Hotspots (Beispiel Island)
  - Gefahren und Schutzmaßnahmen
- **Screenshots:** Fotos aus dem Unterrichtsmaterial direkt in den Chat einfügen (bei der kostenpflichtigen Variante problemlos möglich)

> **Tipp:** In ChatGPT einfach mit **Shift + Enter** Zeilenumbrüche innerhalb des Prompts machen, um den Text übersichtlich zu strukturieren, ohne ihn versehentlich abzuschicken.

### Ergebnis prüfen und anpassen

Die KI generiert zunächst einige Fragen. Diese lassen sich direkt im Chat weiter verfeinern:

- **Fragen ergänzen:** „Erstelle insgesamt 20 Fragen."
- **Einzelne Fragen überarbeiten:** „Frage 15 gefällt mir nicht, bitte umformulieren."
- **Fragen ersetzen:** „Tausche Frage 15 gegen eine neue aus."

Einige Antwortmöglichkeiten mögen auf den ersten Blick offensichtlich falsch klingen – das ist aber durchaus gewollt, um auch Schülerinnen und Schüler zu entlarven, die den Stoff nicht gelernt haben.

### Export als Word-Dokument

Sobald die 20 Fragen final sind, kopiere ich alles in ein **Word-Dokument** und speichere es lokal ab (z. B. als `endogene-kraefte-quiz.docx`).

---

## Teil 2: Import in Microsoft Forms und Feinschliff

### Import über Microsoft Forms

1. [forms.microsoft.com](https://forms.microsoft.com) öffnen
2. Oben auf **„Schnellimport"** klicken
3. Das Word-Dokument hochladen und als **Quiz** importieren

Microsoft Forms erkennt dabei automatisch Titel, Fragen und Antwortmöglichkeiten. Nach einem kurzen Ladevorgang (bei Serverproblemen hilft ein einfaches Neuladen der Seite) erscheint das Quiz zur Bearbeitung.

### Richtige Antworten markieren

Nach dem Import sind die richtigen Antworten noch nicht hinterlegt – das ist der einzige manuelle Schritt. Für jede Frage:

1. In die Frage klicken
2. Die korrekte Antwort als **„Richtige Antwort"** markieren
3. Punktzahl vergeben (hier: 1 Punkt pro Frage, also 20 Punkte gesamt)

> **Achtung:** Nicht vergessen, jede Frage durchzugehen – eine übersehene Frage bedeutet hinterher doppelte Arbeit.

### Sinnvolle Einstellungen

Unter den **Einstellungen** des Quiz lassen sich hilfreiche Optionen aktivieren:

| Einstellung | Empfehlung |
|---|---|
| Übungsmodus | Deaktivieren |
| Ergebnisse automatisch anzeigen | Deaktivieren (manuell nachher freigeben) |
| Fragen in zufälliger Reihenfolge | **Aktivieren** (verhindert Abschreiben) |
| Fragenummer für Befragte deaktivieren | **Aktivieren** (erschwert Abgucken beim Nachbarn) |
| Antworten sperren/Name oben fixieren | Optional |
| Start- und Enddatum | Optional, wenn nicht über Teams verteilt |

### Namen der Schülerinnen und Schüler erfassen

Wenn das Quiz über **Microsoft Teams** ausgeteilt wird, sind die Antworten den Schülerinnen und Schülern automatisch zugeordnet. Wird der Link frei verschickt, empfiehlt sich eine zusätzliche Textfrage am Ende:

> „Wie lautet dein Name? Bitte zuerst Vorname, dann Nachname."

Diese Frage bekommt keine Punkte, wird aber als **Pflichtfeld** markiert.

### Auswertung und Notenverwaltung

Nach der Durchführung stehen alle Ergebnisse direkt in Microsoft Forms zur Verfügung. Die Prozentwerte lassen sich unkompliziert in gängige Notenverwaltungsprogramme (z. B. **Dino** oder andere Schulverwaltungslösungen) als 0–100-Punkte-Skala übertragen. Die Ergebnisse können außerdem als Grundlage für die anschließende **Klassenbesprechung** genutzt werden.

---

## Fazit

Der gesamte Workflow von den Unterrichtsnotizen bis zum fertigen, automatisch korrigierten Online-Quiz lässt sich in wenigen Minuten umsetzen:

- ✅ Fragenentwurf schneller vorbereitbar
- ✅ Fachliche und didaktische Kontrolle bleibt bei der Lehrkraft
- ✅ Zufällige Fragenreihenfolge als eine mögliche Einstellung
- ✅ Ergebnisse direkt auswertbar

Vor der Verwendung mit einer Lerngruppe das Quiz selbst vollständig durchspielen, Lösungen und Punkte prüfen und die schulischen Vorgaben zu KI, Konten, Einwilligungen und Leistungsdaten beachten.

## Erfolgskontrolle

Ein Testkonto kann das Quiz öffnen und abschließen; alle richtigen Antworten, Punktwerte, Pflichtfelder, Freigabezeitpunkte und Ergebnisanzeigen entsprechen der beabsichtigten Unterrichtssituation. KI-Ausgaben wurden gegen die eigenen Unterrichtsgrundlagen geprüft.

## Häufige Fehler und Lösungen

- **Forms erkennt das Word-Dokument nicht korrekt:** Schlicht formatieren, Fragen eindeutig nummerieren und Import anschließend vollständig prüfen.
- **KI erfindet oder vereinfacht Inhalte:** Jede Frage und jede Lösung fachlich gegen belastbare Unterrichtsquellen prüfen.
- **Nicht freigegebene Daten/Materialien hochgeladen:** Nur freigegebene Dienste und Inhalte verwenden; keine Schülerdaten und keine unklar lizenzierten Buchseiten/Screenshots an externe KI-Dienste übermitteln.

## Quellen und Stand

Geprüft am 26.08.2026:

- [Microsoft Support: Word- oder PDF-Formular bzw. Quiz in Microsoft Forms importieren](https://support.microsoft.com/de-de/office/konvertieren-eines-word-oder-pdf-formulars-oder-tests-in-microsoft-forms-66b7e9bc-eb0d-4c65-b7e6-f9f92dcd71cb)
- [Microsoft Support: Ein Quiz mit Microsoft Forms erstellen](https://support.microsoft.com/de-de/office/erstellen-eines-quiz-mit-microsoft-forms-a082a018-24a1-48c1-b176-4b3616cdc83d)

Produktnamen und gezeigte Funktionen beschreiben den geprüften Stand; Tarife und Oberflächen können sich ändern.