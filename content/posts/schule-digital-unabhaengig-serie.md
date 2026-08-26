---
title: "Schule digital unabhängig #00: Warum offene Alternativen eine Prüfung wert sind"
date: 2026-05-05
draft: false
description: "Ein persönliches Konzept für die differenzierte Prüfung offener und selbstbestimmt betreibbarer Schul-IT."
content_type: "meinungsbeitrag"
audience: "Schule und Schul-IT"
last_reviewed: 2026-08-26
school_status: "persoenlich"
software_versions: "Konzeptbeitrag zu Nextcloud, Mailcow und offenen Alternativen; geprüft August 2026"
duration: "ca. 10 Minuten Lesezeit"
tags: ["Schule digital unabhängig", "Open Source", "Schule", "Datenschutz", "Nextcloud", "Mailcow"]
categories:
  - Schul-IT und Open Source
---

## Kurzüberblick

- **Für wen:** Schulleitungen, Schulträger und technisch Verantwortliche, die Alternativen zu großen Plattformanbietern diskutieren.
- **Ziel:** Prüfkriterien und mögliche Bausteine für mehr Anbieterunabhängigkeit skizzieren.
- **Voraussetzungen und Rechte:** Für eine Umsetzung wären ein Mandat des Schulträgers, Datenschutz-/IT-Sicherheitsprüfung, belastbare Zuständigkeiten, Finanzierung und Betriebskonzepte nötig.
- **Dauer:** Etwa 10 Minuten Lesezeit; keine unmittelbar umsetzbare Schulanleitung.
- **Geprüfter Stand:** 26.08.2026. Dies ist ein persönlicher Konzeptbeitrag und keine rechtliche Bewertung oder offizielle Schulstrategie.

## Die Idee hinter „Schule digital unabhängig“

Ich starte eine neue Blog- und Videoreihe, die mir schon lange am Herzen liegt: **„Schule digital unabhängig"**. In dieser Reihe möchte ich zeigen, wie Schulen – aber auch andere Bildungseinrichtungen – ihre digitale Infrastruktur so aufbauen können, dass sie nicht länger von großen amerikanischen Tech-Konzernen abhängig sind. Der Fokus liegt dabei auf zwei zentralen Themenbereichen:

1. **E-Mail** – die digitale Kommunikationsgrundlage jeder Institution
2. **Kollaboration** – gemeinsames Arbeiten mit Tools wie Nextcloud

---

## Motivation: Warum überhaupt unabhängig werden?

Google Workspace for Education und Microsoft 365 sind verbreitete, ausgereifte Plattformen. Gleichzeitig können bei US-Anbietern Fragen zu Abhängigkeit, Vertragsgestaltung, internationalen Datenübermittlungen und Zugriffsrisiken entstehen. Der US CLOUD Act ist dabei ein relevanter Prüfbaustein, führt aber nicht automatisch dazu, dass jede Nutzung oder jede Speicherung auf europäischen Servern unzulässig ist. Eine datenschutzrechtliche Bewertung muss den konkreten Dienst, die Datenarten, Rollen, Verträge, Schutzmaßnahmen und die jeweils geltende Rechtslage berücksichtigen.

> Wenn wir ein neues System einführen, sollten wir Abhängigkeiten und einen realistischen Ausstieg von Anfang an mitprüfen.

Mein zentrales Argument ist deshalb nicht, einen Anbieter pauschal auszuschließen, sondern Alternativen und Wechselmöglichkeiten systematisch zu bewerten. Quelloffene Software kann dabei ein Baustein sein, sofern Betrieb, Sicherheit, Support, Barrierefreiheit, Datenschutz und Kosten dauerhaft geklärt sind.

---

## Was ist quelloffene Software und warum ist sie der Schlüssel?

Open-Source-Software hat mehrere entscheidende Vorteile gegenüber proprietären Lösungen:

- **Transparenz**: Einsehbarer Quellcode ermöglicht unabhängige Prüfung, ersetzt aber keine Audits, sichere Konfiguration oder ein funktionierendes Updateverfahren.
- **Anbieterunabhängigkeit**: Offene Standards und exportierbare Daten können einen Anbieterwechsel erleichtern; in der Praxis bleiben Migration, Know-how und Dienstleisterverfügbarkeit zu planen.
- **Community und Langlebigkeit**: Aktive Projekte können von vielen Beteiligten getragen werden. Aktivität, Finanzierung und Wartungszusagen müssen dennoch für jedes Projekt einzeln geprüft werden.
- **Kostenstruktur**: Lizenzkosten können geringer sein, dafür entstehen reale Kosten für Hosting, Administration, Support, Schulung, Monitoring, Backups und Notfallvorsorge.

---

## Die Inhalte der Reihe im Überblick

### 📧 Kapitel 1: E-Mail mit Mailcow

Das erste große Thema der Reihe ist **E-Mail**. Als konkrete Lösung werde ich **Mailcow** vorstellen – eine vollständige, Docker-basierte E-Mail-Server-Suite, die sich für den schulischen Einsatz eignet.

In einem eigenen Beitrag und Video werde ich folgende Aspekte beleuchten:

- **Überlegungen**: Was braucht eine Schule wirklich von einem E-Mail-System?
- **Bedenken und Problematik**: Wo liegen die Herausforderungen beim Selbsthosting? Stichwort: Wartung, Spam-Abwehr, Ausfallsicherheit.
- **Chancen**: Mehr Gestaltungsspielraum und Datenkontrolle; Datenschutzkonformität entsteht jedoch erst durch passende Rechtsgrundlage, Verträge, Konfiguration, technische und organisatorische Maßnahmen sowie einen sicheren Betrieb.
- **Risiken**: Was passiert, wenn der Server ausfällt? Wie sieht es mit Backups aus?
- **Kosten**: Ein realistischer Vergleich – was kostet Mailcow im Betrieb wirklich, und wie steht das im Verhältnis zu kommerziellen Alternativen?

---

### ☁️ Kapitel 2: Kollaboration mit Nextcloud

Der zweite große Schwerpunkt ist **Nextcloud** – die wohl bekannteste Open-Source-Lösung für kollaboratives Arbeiten in der Cloud. Hier plane ich nicht nur ein einzelnes Video, sondern eine **ganze Unter-Reihe**, da das Thema so vielschichtig ist:

- **Nextcloud Dateien**: Die Grundlage – sicheres Speichern, Teilen und gemeinsames Bearbeiten von Dokumenten, direkt im Browser oder per Desktop-Client.
- **Nextcloud Talk**: Die integrierte Kommunikationslösung für Chat, Audio- und Videokonferenzen – eine echte Alternative zu Teams oder Meet.
- **Nextcloud Teams / Groupware**: Kalender, Kontakte und Aufgaben für das gesamte Kollegium – koordiniertes Arbeiten ohne externe Abhängigkeiten.

Jeder dieser Bereiche verdient eine eigene, tiefergehende Betrachtung, und genau das werden wir uns in den kommenden Beiträgen vornehmen.

---

### 🔐 Optional: Passwortmanagement mit Vaultwarden

Als ergänzendes Thema überlege ich außerdem, einen Beitrag zu **Vaultwarden** zu erstellen. Vaultwarden ist ein selbst gehosteter, Open-Source-kompatibler Server für den bekannten Passwortmanager **Bitwarden**. Gerade in Schulen, wo viele Menschen mit vielen verschiedenen Diensten arbeiten, ist ein zentraler, sicherer Passwortmanager Gold wert – und ein selbst gehosteter erst recht.

---

## Wie geht es weiter?

Die Reihe „Schule digital unabhängig" wird sowohl hier im Blog als auch als Videoreihe erscheinen. Mein Ziel ist es, nicht nur Konzepte vorzustellen, sondern **praktische Anleitungen** zu liefern, die wirklich umsetzbar sind.

Zugegeben, aktuell ist das ganze Thema noch ein Gedankenexperiment, allerdings weiß man ja nie wie es weitergeht.


Wenn dich das Thema interessiert, freue ich mich über deinen Kommentar: Welche Herausforderungen siehst du beim Einsatz von Open-Source-Lösungen in deiner Schule? Was würde dich am meisten interessieren?

Bis zum nächsten Beitrag – dort soll Mailcow als möglicher Baustein mit Chancen, Risiken und Betriebsaufwand genauer betrachtet werden.

## Was du jetzt tun kannst

- Bestehende Abhängigkeiten, Datenarten, Verträge und Exportmöglichkeiten inventarisieren.
- Nicht mit einem Produkt starten, sondern Anforderungen, Schutzbedarf, Zuständigkeiten, Betrieb und Ausstiegsszenario festhalten.
- Datenschutzbeauftragte, IT-Sicherheit, Schulträger, Personalvertretung und betroffene Nutzergruppen früh einbeziehen.
- Erst in einer abgegrenzten Testumgebung mit nicht personenbezogenen Testdaten evaluieren.

## Erfolgskontrolle

Dieser Konzeptbeitrag ist erfolgreich genutzt, wenn eine ergebnisoffene Prüfliste entsteht – nicht, wenn bereits vor der Analyse ein bestimmtes Produkt feststeht. Ein späterer Pilot braucht benannte Verantwortliche, Monitoring, Backup-/Restore-Test, Notfallverfahren und dokumentierte Freigaben.

## Quellen und Stand

Geprüft am 26.08.2026. Die Quellen liefern Prüfinformationen, aber keine pauschale Freigabe oder Ablehnung eines konkreten schulischen Systems.

- [EUR-Lex: Datenschutz-Grundverordnung (DSGVO)](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de)
- [U.S. Department of Justice: CLOUD Act Resources](https://www.justice.gov/dag/cloudact)
- [BSI: IT-Grundschutz](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html)
- [Nextcloud: Security](https://nextcloud.com/security/)
- [Mailcow-Dokumentation](https://docs.mailcow.email/)
