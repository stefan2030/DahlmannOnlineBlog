---
title: "Korrekturhilfe für Lehrerinnen und Lehrer: Automatisiert ausgefüllter Erwartungshorizont mit Excel und Word"
date: 2026-04-29
draft: false
description: "Wie Lehrerinnen und Lehrer mit Excel und Word einen Erwartungshorizont als Serienbrief automatisiert ausfüllen und so Korrekturen effizienter gestalten können."
tags:
  - Schule
  - Korrektur
  - Excel
  - Word
  - Serienbrief
categories:
  - Arbeitsorganisation
---

Korrekturen gehören für Lehrerinnen und Lehrer zu den zeitaufwendigsten Aufgaben im Schulalltag. Besonders bei Klassenarbeiten, Klausuren oder Tests mit vielen Schülerinnen und Schülern wiederholen sich viele Arbeitsschritte immer wieder.

Ein typisches Beispiel ist der **Erwartungshorizont**: Punkte müssen eingetragen, Rückmeldungen ergänzt und individuelle Ergebnisse sauber dokumentiert werden. Das ist wichtig, kostet aber viel Zeit.

In meinem Video zeige ich, wie man mit **Excel und Word** eine praktische Korrekturhilfe bauen kann: Ein Erwartungshorizont wird mit Hilfe eines **Serienbriefs** automatisch für jede Schülerin und jeden Schüler ausgefüllt.

## Video: Automatisierter Erwartungshorizont mit Excel und Word

{{< youtube oSLVrrOt1uY >}}

Falls das Video nicht angezeigt wird, findest du es direkt auf YouTube:

[https://www.youtube.com/watch?v=oSLVrrOt1uY](https://www.youtube.com/watch?v=oSLVrrOt1uY)

## Das Problem: Korrekturen sind oft repetitive Arbeit

Bei vielen Korrekturen wiederholen sich dieselben Arbeitsschritte:

- Namen der Schülerinnen und Schüler eintragen
- erreichte Punkte übertragen
- Gesamtpunktzahl berechnen
- Note eintragen
- Rückmeldungen ergänzen
- Erwartungshorizont individuell ausfüllen
- Dokumente ausdrucken oder als PDF speichern

Gerade wenn man viele Lernende in einer Klasse oder einem Kurs hat, summiert sich dieser Aufwand schnell.

Natürlich muss die inhaltliche Bewertung weiterhin durch die Lehrkraft erfolgen. Aber viele organisatorische und formale Schritte lassen sich automatisieren.

Genau hier helfen Excel und Word.

## Die Grundidee

Die Idee ist einfach:

> Excel enthält die Daten. Word erzeugt daraus automatisch individuelle Erwartungshorizonte.

Excel wird dabei als Datenquelle genutzt. Dort werden alle relevanten Informationen gesammelt, zum Beispiel:

- Name
- Vorname
- Klasse oder Kurs
- erreichte Punkte pro Aufgabe
- Gesamtpunktzahl
- Note
- individuelle Hinweise
- Rückmeldungen oder Kommentare

Word nutzt diese Daten anschließend über die Serienbrief-Funktion und erstellt daraus für jede Person ein eigenes Dokument.

Das Ergebnis: Der Erwartungshorizont wird automatisch mit den passenden Daten befüllt.

## Warum Excel?

Excel eignet sich sehr gut als Grundlage, weil Tabellen für Korrekturen ohnehin praktisch sind.

Man kann dort:

- Punktzahlen übersichtlich eintragen
- Summen automatisch berechnen lassen
- Noten berechnen oder zuordnen
- Kommentare sammeln
- Daten sortieren und filtern
- eine saubere Grundlage für den Serienbrief erstellen

Ein einfaches Beispiel für eine Excel-Tabelle könnte so aussehen:

| Vorname | Nachname | Klasse | Aufgabe 1 | Aufgabe 2 | Aufgabe 3 | Gesamt | Note | Kommentar |
|---|---|---|---:|---:|---:|---:|---|---|
| Max | Müller | 8a | 8 | 6 | 10 | 24 | 2 | Gute Argumentation. |
| Lisa | Becker | 8a | 5 | 7 | 8 | 20 | 3 | Achte auf genauere Begründungen. |
| Ali | Yilmaz | 8a | 9 | 9 | 11 | 29 | 1 | Sehr überzeugende Lösung. |

Wichtig ist dabei: Jede Zeile steht für eine Schülerin oder einen Schüler. Jede Spalte enthält eine Information, die später in Word verwendet werden kann.

## Warum Word als Serienbrief?

Word hat mit dem Serienbrief eine eingebaute Funktion, mit der man aus einer Vorlage viele individuelle Dokumente erzeugen kann.

Diese Funktion wird häufig für Briefe, Etiketten oder Bescheinigungen genutzt. Sie eignet sich aber genauso gut für schulische Dokumente wie:

- Erwartungshorizonte
- Bewertungsbögen
- Feedbackbögen
- individuelle Rückmeldungen
- Förderhinweise
- Zertifikate
- Elterninformationen

Der große Vorteil: Man erstellt die Vorlage nur einmal. Danach füllt Word automatisch die passenden Felder aus Excel ein.

## Der Arbeitsablauf

Der grundlegende Ablauf sieht so aus:

1. Erwartungshorizont in Word vorbereiten
2. Excel-Tabelle mit Schülerdaten und Punkten erstellen
3. Word-Dokument mit der Excel-Tabelle verbinden
4. Seriendruckfelder einfügen
5. Vorschau kontrollieren
6. Serienbrief erzeugen
7. Dokumente drucken oder als PDF speichern

Schauen wir uns die Schritte genauer an.

## Schritt 1: Excel-Tabelle vorbereiten

Zuerst wird eine Excel-Datei erstellt. Diese Datei enthält alle Daten, die später im Erwartungshorizont erscheinen sollen.

Typische Spalten sind:

- `Vorname`
- `Nachname`
- `Klasse`
- `Aufgabe_1`
- `Aufgabe_2`
- `Aufgabe_3`
- `Gesamtpunkte`
- `Note`
- `Kommentar`

Wichtig ist, dass die erste Zeile der Tabelle klare Spaltenüberschriften enthält. Diese Überschriften werden später in Word als Seriendruckfelder angezeigt.

Ein Beispiel:

```text
Vorname | Nachname | Klasse | Aufgabe_1 | Aufgabe_2 | Gesamtpunkte | Note | Kommentar
```

Bei den Spaltennamen sollte man möglichst auf Sonderzeichen verzichten. Statt `Aufgabe 1` kann man zum Beispiel `Aufgabe_1` schreiben. Das macht die Arbeit in Word oft einfacher.

## Schritt 2: Punkte und Noten berechnen

In Excel können die Gesamtpunkte automatisch berechnet werden.

Beispiel:

```excel
=SUMME(D2:F2)
```

Damit werden die Punkte aus mehreren Aufgaben addiert.

Auch Noten können in Excel automatisch berechnet oder über eine Tabelle zugeordnet werden. Je nach Bewertungssystem kann man mit Formeln, Verweisen oder festen Notengrenzen arbeiten.

Ein einfaches Beispiel könnte so aussehen:

```excel
=WENN(G2>=27;"1";WENN(G2>=23;"2";WENN(G2>=18;"3";WENN(G2>=13;"4";WENN(G2>=7;"5";"6")))))
```

Das ist nur ein Beispiel. Die tatsächlichen Notengrenzen müssen natürlich zur jeweiligen Arbeit passen.

## Schritt 3: Word-Vorlage erstellen

In Word wird nun der Erwartungshorizont gestaltet.

Das kann zum Beispiel ein Dokument sein mit:

- Überschrift
- Name der Schülerin oder des Schülers
- Klasse oder Kurs
- Tabelle mit Aufgaben
- maximaler Punktzahl
- erreichter Punktzahl
- Gesamtpunktzahl
- Note
- individuellem Kommentar

Ein einfacher Aufbau könnte so aussehen:

```text
Erwartungshorizont zur Klassenarbeit

Name: «Vorname» «Nachname»
Klasse: «Klasse»

Aufgabe 1: «Aufgabe_1» Punkte
Aufgabe 2: «Aufgabe_2» Punkte
Aufgabe 3: «Aufgabe_3» Punkte

Gesamtpunktzahl: «Gesamtpunkte»
Note: «Note»

Kommentar:
«Kommentar»
```

Die Begriffe in den französischen Anführungszeichen sind später die Seriendruckfelder aus Excel.

## Schritt 4: Excel-Datei mit Word verbinden

In Word wird nun die Excel-Datei als Datenquelle eingebunden.

Der Weg ist ungefähr:

1. In Word auf **Sendungen** gehen
2. **Seriendruck starten** auswählen
3. Dokumenttyp wählen, zum Beispiel **Briefe**
4. **Empfänger auswählen**
5. **Vorhandene Liste verwenden**
6. Excel-Datei auswählen
7. passende Tabelle oder Arbeitsmappe auswählen

Danach kennt Word die Spalten aus der Excel-Tabelle.

## Schritt 5: Seriendruckfelder einfügen

Jetzt können die einzelnen Felder an den gewünschten Stellen im Word-Dokument eingefügt werden.

Dazu nutzt man in Word:

```text
Sendungen → Seriendruckfeld einfügen
```

Dort erscheinen dann die Spalten aus Excel, zum Beispiel:

- `Vorname`
- `Nachname`
- `Klasse`
- `Aufgabe_1`
- `Gesamtpunkte`
- `Note`
- `Kommentar`

Diese Felder werden an den passenden Stellen im Erwartungshorizont eingefügt.

## Schritt 6: Vorschau kontrollieren

Bevor man den Serienbrief erzeugt, sollte man unbedingt die Vorschau prüfen.

In Word gibt es dafür die Funktion:

```text
Vorschau Ergebnisse
```

Damit sieht man, wie der Erwartungshorizont für einzelne Schülerinnen und Schüler aussehen wird.

Dabei sollte man kontrollieren:

- Stimmen die Namen?
- Werden die richtigen Punkte angezeigt?
- Ist die Gesamtpunktzahl korrekt?
- Passt die Note?
- Werden Kommentare richtig übernommen?
- Gibt es Formatierungsprobleme?

Gerade beim ersten Durchlauf lohnt es sich, hier gründlich zu prüfen.

## Schritt 7: Serienbrief erzeugen

Wenn alles passt, kann der Serienbrief abgeschlossen werden.

Word kann daraus entweder:

- einzelne Dokumente erstellen
- alle Erwartungshorizonte in ein neues Word-Dokument schreiben
- die Dokumente direkt drucken

Oft ist es sinnvoll, zuerst ein neues Word-Dokument mit allen Datensätzen zu erzeugen. Dann kann man noch einmal kontrollieren und anschließend drucken oder als PDF speichern.

## Vorteile dieser Methode

Diese Arbeitsweise bringt mehrere Vorteile.

### 1. Weniger Tipparbeit

Namen, Punkte und Kommentare müssen nicht mehrfach eingetragen werden. Die Daten werden einmal in Excel gepflegt und dann automatisch übernommen.

### 2. Weniger Fehler

Wer Daten manuell von einer Liste in viele einzelne Dokumente überträgt, macht schnell Fehler. Ein automatisierter Serienbrief reduziert dieses Risiko.

### 3. Einheitliches Layout

Alle Erwartungshorizonte sehen gleich aus. Das wirkt professionell und sorgt für Klarheit.

### 4. Schnellere Korrekturorganisation

Die eigentliche Bewertung bleibt natürlich pädagogische Arbeit. Aber der organisatorische Teil wird deutlich schneller.

### 5. Wiederverwendbare Vorlage

Hat man einmal eine gute Word-Vorlage erstellt, kann man sie für zukünftige Arbeiten anpassen und wiederverwenden.

## Mögliche Einsatzbereiche

Die Methode eignet sich nicht nur für Erwartungshorizonte.

Man kann sie auch nutzen für:

- Klassenarbeiten
- Klausuren
- Tests
- mündliche Prüfungen
- Projektbewertungen
- Präsentationsbewertungen
- Kompetenzraster
- Feedbackbögen
- Lernentwicklungsberichte
- Förderempfehlungen

Überall dort, wo viele ähnliche Dokumente mit individuellen Daten erstellt werden müssen, kann ein Serienbrief helfen.

## Datenschutz beachten

Bei dieser Methode werden personenbezogene Daten verarbeitet. Deshalb sollte man sorgfältig damit umgehen.

Wichtig ist:

- Dateien sicher speichern
- keine sensiblen Daten unnötig weitergeben
- lokale oder schulisch freigegebene Speicherorte nutzen
- Vorgaben der Schule bzw. des Schulträgers beachten
- Dateien nach Gebrauch sinnvoll archivieren oder löschen

Gerade wenn Namen, Noten und Kommentare enthalten sind, sollte die Datei nicht ungeschützt auf privaten Cloud-Diensten liegen.

## Praktische Tipps

Ein paar Hinweise aus der Praxis:

### Klare Spaltennamen verwenden

Nutze einfache Spaltenüberschriften ohne Sonderzeichen.

Gut:

```text
Aufgabe_1
Gesamtpunkte
Kommentar
```

Weniger gut:

```text
Aufgabe 1 (Punkte)
Gesamt-Punkte!
Kommentar/Feedback
```

### Excel-Tabelle sauber halten

Jede Schülerin und jeder Schüler sollte genau eine Zeile haben. Leere Zeilen oder zusammengeführte Zellen können beim Serienbrief Probleme verursachen.

### Vorlage testen

Bevor du die Methode bei einer echten Klassenarbeit einsetzt, teste sie mit ein paar Beispieldaten.

### Erst als Word-Dokument ausgeben

Statt sofort zu drucken, erstelle zunächst ein neues Word-Dokument mit allen Ergebnissen. So kannst du Fehler noch korrigieren.

### Vorlage wiederverwenden

Speichere dir eine allgemeine Vorlage. Für die nächste Arbeit musst du dann nur Aufgaben, Punkte und Bewertungskriterien anpassen.

## Fazit

Ein automatisiert ausgefüllter Erwartungshorizont mit Excel und Word ist eine einfache, aber sehr wirkungsvolle Korrekturhilfe für Lehrerinnen und Lehrer.

Die Methode spart Zeit, reduziert Fehler und sorgt für ein einheitliches Layout. Besonders bei größeren Klassen oder Kursen lohnt sich die einmalige Einrichtung schnell.

Die inhaltliche Bewertung bleibt natürlich Aufgabe der Lehrkraft. Aber die formale Erstellung der individuellen Erwartungshorizonte kann deutlich effizienter ablaufen.

Wer regelmäßig Klassenarbeiten, Klausuren oder Tests korrigiert, sollte diese Möglichkeit unbedingt ausprobieren.

## Zugang zur Vorlage

Ihr könnt euch meine Vorlage hier herunterladen: [Vorlage und Anleitung im PDF Format](/downloads/Korrektur-Excel-mit-Serienbrief-als_Arbeitserleichterung.zip)