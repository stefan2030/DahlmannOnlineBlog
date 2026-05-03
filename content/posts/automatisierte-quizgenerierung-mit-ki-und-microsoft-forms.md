---
title: "Automatisierte Quiz-Generierung mit KI und Microsoft Forms"
date: 2025-01-30
draft: false
tags: ["Microsoft Forms", "Künstliche Intelligenz", "Unterricht", "Quiz", "ChatGPT"]
---

{{< youtube qbzK9sLekJ4 >}}

[Hier geht's zu Teil 1 auf YouTube](https://youtu.be/qbzK9sLekJ4)

{{< youtube b4VGXZfHs-M >}}

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

- ✅ Kein manuelles Erstellen von Fragen
- ✅ Automatische Korrektur durch Microsoft Forms
- ✅ Zufällige Fragenreihenfolge gegen Abschreiben
- ✅ Ergebnisse direkt auswertbar

Viel Erfolg beim Nachbauen!