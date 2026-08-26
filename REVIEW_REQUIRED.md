# Vor Veröffentlichung zu prüfen / freizugeben

Stand: 26.08.2026

Diese Punkte konnten technisch nicht belastbar entschieden werden und dürfen nicht stillschweigend als freigegeben gelten:

1. **Impressum:** Die vom Nutzer vorerst unverändert gewünschte Angabe „Krefeld-Traar, Deutschland“ ist möglicherweise keine vollständige ladungsfähige Anschrift im Sinne der Anbieterkennzeichnung. Vollständige Anschrift und aktuelle rechtliche Fundstellen fachkundig prüfen.
2. **Datenschutz:** Verantwortlichenangaben einschließlich vollständiger Anschrift, Rechtsgrundlagen, Auftragsverarbeitung, internationale Datentransfers und konkrete Speicher-/Löschfristen für Cloudflare, YouTube und Giscus fachkundig prüfen.
3. **Externe Dienste:** Bewusste Aktivierung von YouTube und Giscus ist technisch umgesetzt. Trotzdem ist zu entscheiden, ob diese Dienste in der vorgesehenen schulnahen Zielgruppe überhaupt freigegeben werden und ob der Einwilligungs-/Aktivierungsmechanismus rechtlich genügt.
4. **Schulstatus:** Keiner der fünf bestehenden Beiträge ist als offizielle Schulanleitung gekennzeichnet. Eine spätere Umstellung auf „offiziell“ darf nur nach dokumentierter Abstimmung mit der zuständigen Schule erfolgen.
5. **Redaktion:** Produktstände, Screenshots, Download-Vorlage, externe Links und Nutzungsrechte vor Veröffentlichung inhaltlich prüfen. Die vorhandenen Aussagen wurden differenziert, aber nicht durch eine fachjuristische oder schulische Freigabe ersetzt.
6. **Cloudflare:** Im Dashboard muss die dokumentierte Buildfolge `./scripts/build.sh` mit Ausgabeordner `public` tatsächlich hinterlegt bzw. gegen die aktuelle Git-Integration abgeglichen werden.
7. **Stale Live-Route:** Der saubere lokale Build erzeugt `/posts/my-first-post/` nicht mehr. Nach einer späteren Veröffentlichung prüfen, dass Cloudflare die alte Datei wirklich entfernt bzw. die Route 404 liefert; falls nicht, Deployment-Artefakte/Cache bereinigen oder gezielt umleiten.

Der Parent-Agent übernimmt unabhängige Prüfung und eine etwaige Veröffentlichung. Dieser Arbeitsauftrag endet mit einem lokalen Commit und führt weder Push noch Deployment aus.
