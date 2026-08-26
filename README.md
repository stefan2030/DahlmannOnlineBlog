# DahlmannOnline Blog

Öffentlicher Hugo-Blog unter <https://blog.dahlmannonline.com> mit dem Theme PaperMod und lokaler Pagefind-Suche.

## Inhaltliche Einordnung

Die veröffentlichten Beiträge sind persönliche Beiträge oder erprobte Arbeitshilfen. Sie sind keine offiziellen Anleitungen des Michael-Ende-Gymnasiums. Verbindliche Statusangaben stehen im Front Matter und werden im Artikel sichtbar ausgegeben.

## Voraussetzungen

- Hugo Extended (getestet mit 0.165.0)
- Node.js 22 oder neuer
- `npm ci`

Das PaperMod-Theme ist ein Git-Submodul:

```bash
git submodule update --init --recursive
```

## Build

```bash
npm ci
npm run build
```

`npm run build` leert `public/`, baut Hugo minimiert und erzeugt anschließend den Pagefind-Index. Nur `public/` ist das Deployment-Verzeichnis; generierte Dateien werden nicht versioniert.

## Prüfung

```bash
npm test
```

Die Tests prüfen Front Matter und Status-Badges, Suche mit Treffer-/Nichttrefferfällen, interne Links, Desktop/Mobilansicht, horizontales Overflow, Accessibility sowie die datensparsame YouTube-/Giscus-Aktivierung.

## Cloudflare Pages

- Produktionsbranch: `main`
- Build-Befehl: `npm run build`
- Ausgabeverzeichnis: `public`
- Root-Verzeichnis: Repository-Wurzel
- Empfohlene Umgebungsvariable: `HUGO_VERSION=0.165.0`

Vor einer Veröffentlichung müssen der lokale Build und die Tests erfolgreich sein. Nach dem Push ist der Cloudflare-Check abzuwarten und die Live-Suche erneut praktisch zu testen.

## Neuer Beitrag

`archetypes/default.md` enthält das verbindliche Grundschema: Zielgruppe, Status, letzte Prüfung, Voraussetzungen, Schritte, Erfolgskontrolle, Fehlerbehebung und Datenschutz. Bestehende Beiträge dürfen nur nach ausdrücklicher Abstimmung als offizielle Schulanleitung gekennzeichnet werden.

## Offene rechtliche Freigaben

Siehe `REVIEW_REQUIRED.md`. Die vollständige ladungsfähige Anschrift bleibt auf Wunsch des Betreibers vorerst unverändert und ist weiterhin offen.

## Rollback

1. Letzten funktionierenden Commit in Git ermitteln.
2. Revert-Commit erstellen oder den vorherigen Stand auf `main` zurückführen.
3. Cloudflare-Build abwarten.
4. Startseite, Suche, Impressum, Datenschutz und einen Beitrag live testen.
