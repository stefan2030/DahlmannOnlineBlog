---
title: "Schule digital unabhängig #00: Warum wir Google und Microsoft den Rücken kehren sollten"
date: 2026-05-05
draft: false
tags: ["Open Source", "Schule", "Datenschutz", "Nextcloud", "Mailcow"]
---

## Die Idee hinter „Schule digital unabhängig"

Ich starte eine neue Blog- und Videoreihe, die mir schon lange am Herzen liegt: **„Schule digital unabhängig"**. In dieser Reihe möchte ich zeigen, wie Schulen – aber auch andere Bildungseinrichtungen – ihre digitale Infrastruktur so aufbauen können, dass sie nicht länger von großen amerikanischen Tech-Konzernen abhängig sind. Der Fokus liegt dabei auf zwei zentralen Themenbereichen:

1. **E-Mail** – die digitale Kommunikationsgrundlage jeder Institution
2. **Kollaboration** – gemeinsames Arbeiten mit Tools wie Nextcloud

---

## Motivation: Warum überhaupt unabhängig werden?

Die meisten Schulen greifen heute auf eine von zwei Lösungen zurück: **Google Workspace for Education** oder **Microsoft 365**. Beide Plattformen sind ausgereifte Produkte, keine Frage – aber sie kommen mit einem erheblichen Haken.

Google und Microsoft sind amerikanische Unternehmen, die dem US-amerikanischen Recht unterliegen. Das bedeutet konkret: Unsere Schülerdaten, Lehrerkommunikation und interne Dokumente liegen auf Servern, über die wir nur begrenzte Kontrolle haben. Mit dem **CLOUD Act** hat die US-Regierung weitreichende Möglichkeiten, auf diese Daten zuzugreifen – unabhängig davon, ob die Server physisch in Europa stehen oder nicht. Das ist aus datenschutzrechtlicher Sicht, insbesondere im Hinblick auf die **DSGVO**, höchst problematisch.

> Wenn wir ein neues System einführen, sollten wir nicht einfach die nächste Sackgasse wählen.

Genau das ist mein zentrales Argument: Wer heute von Google zu Microsoft wechselt (oder umgekehrt), löst das eigentliche Problem nicht. Man tauscht lediglich einen Anbieter gegen einen anderen aus und bleibt genauso abhängig wie zuvor. Die Lösung liegt in **quelloffener Software** – also Open-Source-Lösungen, die von verschiedenen Anbietern gehostet oder sogar selbst betrieben werden können.

---

## Was ist quelloffene Software und warum ist sie der Schlüssel?

Open-Source-Software hat mehrere entscheidende Vorteile gegenüber proprietären Lösungen:

- **Transparenz**: Der Quellcode ist öffentlich einsehbar. Jede und jeder kann nachprüfen, was die Software tatsächlich mit den Daten macht.
- **Anbieterunabhängigkeit**: Man ist nicht an einen einzigen Hersteller gebunden. Wer heute selbst hostet, kann morgen zu einem anderen Dienstleister wechseln – der Quellcode bleibt derselbe.
- **Community und Langlebigkeit**: Beliebte Open-Source-Projekte werden von großen Communities gepflegt und entwickeln sich kontinuierlich weiter.
- **Kostenstruktur**: Die Software selbst ist meist kostenlos. Es fallen lediglich Hosting- und Betriebskosten an, über die man selbst die volle Kontrolle hat.

---

## Die Inhalte der Reihe im Überblick

### 📧 Kapitel 1: E-Mail mit Mailcow

Das erste große Thema der Reihe ist **E-Mail**. Als konkrete Lösung werde ich **Mailcow** vorstellen – eine vollständige, Docker-basierte E-Mail-Server-Suite, die sich für den schulischen Einsatz eignet.

In einem eigenen Beitrag und Video werde ich folgende Aspekte beleuchten:

- **Überlegungen**: Was braucht eine Schule wirklich von einem E-Mail-System?
- **Bedenken und Problematik**: Wo liegen die Herausforderungen beim Selbsthosting? Stichwort: Wartung, Spam-Abwehr, Ausfallsicherheit.
- **Chancen**: Volle Datenkontrolle, DSGVO-Konformität, individuelle Anpassbarkeit.
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

Bis zum nächsten Beitrag – und dann tauchen wir tief in die Welt von **Mailcow** ein. 🚀
