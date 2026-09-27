# Korrekturen der Literaturverzeichnisse (2026-09-27)

Grundlage: `quellen-bewertung.csv` (Spalte `begruendung`). Bearbeitet: `lit-A-acc-bim.bib` bis `lit-G-luecken.bib`; `lit-H-ff4-ff5.bib` nicht angefasst. Keine Einträge hinzugefügt oder gelöscht, keine Keys geändert. Jede korrigierte Quelle trägt im `note` den Zusatz „korrigiert 2026-09-27: …“.

Prüfweg: Crossref-API (`api.crossref.org`, über Exa-Fetch, da direkt gesperrt), DataCite-API, Verlags- und Repositoriumsseiten, DIN Media, amtliche Fundstellen (gesetze-im-internet.de, gesetze-bayern.de, bundestag.de).

## Stabilitätsprüfung

- `bibmerge.py` auf lit-A…G: 465 Einträge, **462 eindeutig**, 3 Duplikate (wie vorher: du2026text2bim, iso16739-2024→iso2024ifc, ids2024→bsi2024ids).
- Reihenfolge von id/key/alias in `quellen-master.csv` identisch zur Sicherung vor der Korrektur (462/462).
- Brace-Balance aller sieben .bib-Dateien: Endtiefe 0, keine negativen Tiefen; keine doppelten Feldnamen innerhalb eines Eintrags.
- Hinweis: Im Ordner liegt inzwischen `lit-H-ff4-ff5.bib` (parallel in Arbeit). Weil `bibmerge.py` alle `lit-*.bib` einliest, wurde der Lauf auf einer Kopie mit lit-A…G ausgeführt und das Ergebnis als `quellen-master.csv` übernommen. Ein Lauf im Ordner nimmt lit-H mit auf und ändert die Zahl.

## Änderungen

| id | key | Feld | alt | neu | Prüfweg |
|---|---|---|---|---|---|
| Q031 | fauth2026digital | author | Fauth, Judith and Guler, Dogus and Lavikka, Rita and Noardo, Francesca and N{\o}rkj{\ae}r Gade, Peter and Mastrolembo Ventura, Silvia | (entfernt) | Routledge-Produktseite und taylorfrancis.com ("Edited By", eBook 08.07.2026, ISBN Print 9781041091752); Crossref führt die Personen als author |
| Q031 | fauth2026digital | editor | (leer) | Fauth, Judith and Guler, Dogus and Lavikka, Rita and Noardo, Francesca and N{\o}rkj{\ae}r Gade, Peter and Mastrolembo Ventura, Silvia | Routledge-Produktseite und taylorfrancis.com ("Edited By", eBook 08.07.2026, ISBN Print 9781041091752); Crossref führt die Personen als author |
| Q031 | fauth2026digital | isbn | (leer) | 978-1-04-109175-2 | Routledge-Produktseite und taylorfrancis.com ("Edited By", eBook 08.07.2026, ISBN Print 9781041091752); Crossref führt die Personen als author |
| Q031 | fauth2026digital | note | – | korrigiert 2026-09-27: author->editor (Herausgeberwerk), ISBN ergänzt | s. o. |
| Q062 | idis2021szenarien | author | Czarny, Damian A. and Diemer, Johannes and Schacht, Mario and others | Czarny, Damian A. and Diemer, Johannes and Schacht, Mario and B{\"u}low, Gilles and Noll, Michael and Lochner, Dietmar and Gayko, Jens and Pervin, Jui Nahid and Rauh, Peter and Diedrich, Christian | Whitepaper-PDF dke.de, Seite "Authors/Contacts" |
| Q062 | idis2021szenarien | note | – | korrigiert 2026-09-27: abgekürzte Autorenliste ("others") vollständig ausgeschrieben | s. o. |
| Q064 | kaufmann2018manual | author | Kaufmann, Hermann and Kr{\"o}tsch, Stefan and Winter, Stefan | (entfernt) | Crossref 10.11129/9783955533953 (type edited-book) |
| Q064 | kaufmann2018manual | editor | (leer) | Kaufmann, Hermann and Kr{\"o}tsch, Stefan and Winter, Stefan | Crossref 10.11129/9783955533953 (type edited-book) |
| Q064 | kaufmann2018manual | note | – | korrigiert 2026-09-27: author->editor (edited-book) | s. o. |
| Q077 | stehn2002integrated | author | Stehn, Lars and Bergstr{\"o}m, Manja | Stehn, Lars and Bergstr{\"o}m, Max | Crossref 10.1016/S0925-5273(00)00153-5 |
| Q077 | stehn2002integrated | note | – | korrigiert 2026-09-27: Vorname Koautor Manja->Max | s. o. |
| Q109 | schoenwitz2012nature | author | Schoenwitz, Marcus and Naim, Mohamed and Potter, Andrew | Schoenwitz, Manuel and Naim, Mohamed and Potter, Andrew | Crossref 10.1080/01446193.2012.664277 |
| Q109 | schoenwitz2012nature | note | – | korrigiert 2026-09-27: Vorname Erstautor Marcus->Manuel | s. o. |
| Q110 | schoenwitz2017product | author | Schoenwitz, Marcus and Potter, Andrew and Gosling, Jonathan and Naim, Mohamed | Schoenwitz, Manuel and Potter, Andrew and Gosling, Jonathan and Naim, Mohamed | Crossref 10.1016/j.ijpe.2016.10.015 |
| Q110 | schoenwitz2017product | note | – | korrigiert 2026-09-27: Vorname Erstautor Marcus->Manuel | s. o. |
| Q111 | frutos2003object | author | Frutos, Jos{\'e} D. and Borenstein, Denis | Frutos, Juan Diego and Borenstein, Denis | Crossref 10.1061/(ASCE)0733-9364(2003)129:3(302) |
| Q111 | frutos2003object | note | – | korrigiert 2026-09-27: Vorname Erstautor José D.->Juan Diego | s. o. |
| Q134 | merrell2010computer | doi | 10.1145/1882262.1866203 | 10.1145/1882261.1866203 | Crossref 10.1145/1882261.1866203 (ACM Trans. Graph. 29(6), journal-article), 10.1145/1866158.1866203 -> 10.1145/1882262.1866203 (proceedings-article) |
| Q134 | merrell2010computer | note | – | korrigiert 2026-09-27: DOI der TOG-Fassung (29(6)) statt Proceedings-DOI; die in der Bewertung genannte 10.1145/1866158.1866203 ist bei Crossref nur Alias der Proceedings-DOI 10.1145/1882262.1866203 | s. o. |
| Q136 | yu2011make | doi | 10.1145/1964921.1964981 | 10.1145/2010324.1964981 | Crossref 10.1145/2010324.1964981 (ACM Trans. Graph. 30(4)); 10.1145/1964921.1964981 = ACM SIGGRAPH 2011 papers |
| Q136 | yu2011make | note | – | korrigiert 2026-09-27: DOI der TOG-Fassung (30(4)) statt Proceedings-DOI 10.1145/1964921.1964981 (zusätzlich gefunden, analog Q134) | s. o. |
| Q138 | laignel2021floor | author | Laignel, Gauthier and Pozin, Nicolas and Geffrier, Xavier and Delevaux, Loukas and Brun, Florian and Dolla, Bastien | Laignel, Graziella and Pozin, Nicolas and Geffrier, Xavier and Delevaux, Loukas and Brun, Florian and Dolla, Bastien | Crossref 10.1016/j.autcon.2020.103491 |
| Q138 | laignel2021floor | note | – | korrigiert 2026-09-27: Vorname Erstautorin Gauthier->Graziella | s. o. |
| Q150 | eu2024aiact | note | – | Dublette von aiact2024; korrigiert 2026-09-27: Dublette markiert | identischer Rechtsakt/ELI wie aiact2024 (Bewertung Q150/Q173) |
| Q027 | du2026text2bim | note | – | Dublette von du2026text2bim (lit-A-acc-bim.bib); korrigiert 2026-09-27: Dublette markiert (zweites Vorkommen desselben Keys) | bibmerge.py: gleiche DOI 10.1061/JCCEE5.CPENG-6386 |
| Q039 | iso16739-2024 | note | – | Dublette von iso2024ifc; korrigiert 2026-09-27: Dublette markiert | bibmerge.py: Titelgleichheit mit iso2024ifc |
| Q040 | ids2024 | note | – | Dublette von bsi2024ids; korrigiert 2026-09-27: Dublette markiert | bibmerge.py: Titelgleichheit mit bsi2024ids |
| Q161 | bauvorlv | title | Verordnung über Bauvorlagen und bauaufsichtliche Anzeigen (Bauvorlagenverordnung -- BauVorlV) | Verordnung über Bauvorlagen und bauaufsichtliche Anzeigen (Bauvorlagenverordnung -- BauVorlV) vom 10. November 2007 (GVBl. S. 792), zuletzt geändert durch {\S}~13 Abs.~2 des Gesetzes vom 23. Dezember 2024 (GVBl. S. 619) | gesetze-bayern.de, Vollzitat nach RedR |
| Q161 | bauvorlv | url | https://www.gesetze-bayern.de/Content/Document/BayBauVorlV | https://www.gesetze-bayern.de/Content/Document/BayBauVorlV2008 | gesetze-bayern.de, Vollzitat nach RedR |
| Q161 | bauvorlv | note | – | korrigiert 2026-09-27: Titel um Vollzitat ergänzt, URL korrigiert (Jahr 2026 = Abrufstand) | s. o. |
| Q162 | dbauv2026 | title | Verordnung über digitale Verfahren im Bauordnungsrecht (DBauV), zuletzt geändert am 15. Mai 2026 | Verordnung über die digitale Einreichung bauaufsichtlicher Anträge und Anzeigen (Digitale Bauantragsverordnung -- DBauV) vom 2. Februar 2021 (GVBl. S. 26), zuletzt geändert durch Verordnung vom 15. Mai 2026 (GVBl. S. 300) | gesetze-bayern.de, Vollzitat nach RedR |
| Q162 | dbauv2026 | note | – | korrigiert 2026-09-27: amtlicher Titel statt "Verordnung über digitale Verfahren im Bauordnungsrecht" | s. o. |
| Q163 | bayDigitalisierungEntwurf2026 | url | https://www.bayika.de | https://www.bayika.de/bayika-wAssets/docs/aktuelles/2026/2026-07-21_StMB_Entwurf_Gesetz_zur_Digitalisierung_bauaufsichtlicher_Verfahren.pdf | Entwurfs-PDF auf bayika.de (Stand 21.07.2026) und bayika-Meldung 24.07.2026 |
| Q163 | bayDigitalisierungEntwurf2026 | note | – | korrigiert 2026-09-27: URL auf das Entwurfsdokument statt Startseite | s. o. |
| Q167 | egbgb249 | url | https://www.gesetze-im-internet.de/bgbeg/art_249.html | https://www.gesetze-im-internet.de/bgbeg/art_249__1.html | gesetze-im-internet.de (Art 249 § 1 und § 2 EGBGB) |
| Q167 | egbgb249 | note | – | korrigiert 2026-09-27: URL korrigiert (art_249.html existiert nicht; § 2 unter .../art_249__2.html) | s. o. |
| Q168 | gmodg2026 | title | Gebäudemodernisierungsgesetz (GModG), BGBl. 2026 I Nr. 226 | Gebäudemodernisierungsgesetz (GModG) vom 8. August 2020 (BGBl. I S. 1728), zuletzt geändert durch Art.~4 des Gesetzes vom 23. Juli 2026 (BGBl. 2026 I Nr. 226) | gesetze-im-internet.de/geg/BJNR172810020.html (Vollzitat) |
| Q168 | gmodg2026 | note | – | korrigiert 2026-09-27: Titel = amtliches Vollzitat statt nur Änderungsgesetz | s. o. |
| Q171 | wd2020normen | title | Urheberrechtlicher Schutz von DIN-Normen (WD 10-045-20) | Die Entwicklung des Urheberrechts an privaten Normwerken. Zum Diskurs um {\S}~5 Abs.~3 UrhG (Sachstand WD 10 - 045/20) | PDF bundestag.de (WD 10 - 045/20) |
| Q171 | wd2020normen | url | (leer) | https://www.bundestag.de/resource/blob/817174/WD-10-045-20-pdf-3-.pdf | PDF bundestag.de (WD 10 - 045/20) |
| Q171 | wd2020normen | note | – | korrigiert 2026-09-27: Titel laut Dokument, URL ergänzt | s. o. |
| Q174 | prodhaftg2026 | title | Gesetz zur Modernisierung des Produkthaftungsrechts, BT-Drs. 21/4297 | Entwurf eines Gesetzes zur Modernisierung des Produkthaftungsrechts (Gesetzentwurf der Bundesregierung), BT-Drs. 21/4297 vom 25.02.2026 | BT-Drs. 21/4297 (dserver.bundestag.de), BMJV-Verfahrensseite |
| Q174 | prodhaftg2026 | url | (leer) | https://dserver.bundestag.de/btd/21/042/2104297.pdf | BT-Drs. 21/4297 (dserver.bundestag.de), BMJV-Verfahrensseite |
| Q174 | prodhaftg2026 | note | – | [U] Verkündung im BGBl. bis 27.09.2026 nicht nachgewiesen; nach Verkündung BGBl.-Fundstelle bzw. RL (EU) 2024/2853 zitieren; korrigiert 2026-09-27: als Gesetzentwurf gekennzeichnet, URL ergänzt | s. o. |
| Q178 | din4108-2 | title | DIN 4108-2:2026-05 Wärmeschutz und Energie-Einsparung in Gebäuden -- Teil 2: Mindestanforderungen an den Wärmeschutz | DIN 4108-2:2026-05 Wärmeschutz und Energie-Einsparung in Gebäuden -- Teil 2: Wärmeschutz -- Anforderungen, Berechnungsverfahren und Hinweise für Planung und Ausführung | DIN Media (Ausgabe 2026-05, Änderungsvermerk ggü. 2013-02); gesetze-im-internet.de § 11 GModG |
| Q178 | din4108-2 | note | – | korrigiert 2026-09-27: Titel der Ausgabe 2026-05; ersetzte Ausgabe DIN 4108-2:2013-02 (auf diese verweist § 11 Abs. 1 GModG datiert, für den GModG-Nachweis maßgeblich) | s. o. |
| Q179 | din4108-4 | note | – | korrigiert 2026-09-27: Normausgabe ersetzt: DIN 4108-4:2017-03 durch DIN 4108-4:2020-11 ersetzt; 2017-03 bleibt zitiert, weil § 20 Abs. 6 GModG datiert darauf verweist | DIN Media (4108-4:2020-11 ersetzt 2017-03); § 20 Abs. 6 GModG |
| Q180 | iso6946 | note | – | korrigiert 2026-09-27: Normausgabe ersetzt: DIN EN ISO 6946:2008-04 durch 2018-03 (+ Berichtigung 1:2023-04) ersetzt; 2008-04 bleibt zitiert, weil § 20 Abs. 6 Nr. 2 GModG datiert darauf verweist | DIN Media (6946:2018-03, Ber. 1:2023-04); § 20 Abs. 6 GModG |
| Q181 | din18599 | note | – | korrigiert 2026-09-27: Normausgabe ersetzt: DIN V 18599:2018-09 seit 10/2025 durch DIN/TS 18599:2025-10 zurückgezogen; 2018-09 bleibt zitiert, weil § 20 Abs. 1 GModG darauf verweist | din.de (Auslegungen DIN V 18599 / DIN/TS 18599); § 20 Abs. 1 GModG |
| Q184 | din4102-4 | note | entfernt: „unsicher: Ausgabe nicht erneut geprüft“ | Ausgabe 2016-05 bei DIN Media bestätigt; [U] ob BayTB 11/2025 noch 2016-05 oder bereits 2025-06 einführt, nicht geprüft; korrigiert 2026-09-27: Ausgabe 2016-05 bestätigt; laut DIN Media inzwischen durch DIN 4102-4:2025-06 ersetzt | DIN Media (4102-4:2016-05, Ersatzvermerk 2025-06) |
| Q185 | din5034-1 | title | DIN 5034-1:2021-08 Tageslicht in Innenräumen -- Teil 1: Allgemeine Anforderungen | DIN 5034-1:2021-08 Tageslicht in Innenräumen -- Teil 1: Begriffe und Mindestanforderungen | DIN Media (DIN 5034-1:2021-08) |
| Q185 | din5034-1 | note | – | korrigiert 2026-09-27: Titel ("Allgemeine Anforderungen" -> "Begriffe und Mindestanforderungen") | s. o. |
| Q187 | din18290-2 | title | DIN 18290-2:2023 BIM-basierte Leistungsverzeichnisse (Container IFC + GAEB) | DIN 18290-2:2023-11 Verlinkter BIM-Datenaustausch von Bauwerksinformationsmodellen mit weiteren Fachmodellen -- Teil 2: Verlinkter BIM-Datenaustausch von Bauwerksinformationsmodellen und Leistungsverzeichnissen (BIM-LV-Container) | DIN Media (Inhaltsverzeichnis BIM-Normen online), baunormenlexikon.de |
| Q187 | din18290-2 | note | entfernt: „unsicher: Titel sinngemäß“ | verifiziert: DIN Media, Ausgabe 2023-11; korrigiert 2026-09-27: exakter Normtitel, Ausgabe 2023-11 | s. o. |
| Q195 | bimbauantrag2020 | author | {BIM Deutschland} | Theiler, Michael | PDF bimdeutschland.de (Titelblatt, PDF-Metadaten "Michael Theiler", "Verantwortung ... beim Autor") |
| Q195 | bimbauantrag2020 | title | Modellierungsrichtlinie BIM-basierter Bauantrag | Modellierungsrichtlinie für den BIM-basierten Bauantrag | PDF bimdeutschland.de (Titelblatt, PDF-Metadaten "Michael Theiler", "Verantwortung ... beim Autor") |
| Q195 | bimbauantrag2020 | note | – | korrigiert 2026-09-27: Verfasser laut PDF statt Hoster "BIM Deutschland"; Titel laut Titelblatt (Stand 18.08.2020, Zukunft Bau SWD-10.08.18.7-17.67) | s. o. |
| Q196 | mbo2bim2023 | author | (leer) | K{\"o}nig, Markus and Stepien, Marcel and Aziz, Angelina and Vonthron, Andr{\'e} and Schulz-Witte, Nicolai and Walter, Thorsten and Kohlhaas, Andreas and Polay, Sarah | Abschlussbericht-PDF irbnet.de (Titelblatt) |
| Q196 | mbo2bim2023 | title | MBO2BIM -- Abschlussbericht | Digitalisierung der Musterbauordnung (MBO) -- Aufbereitung der MBO für BIM-basierte Prüfwerkzeuge. Abschlussbericht | Abschlussbericht-PDF irbnet.de (Titelblatt) |
| Q196 | mbo2bim2023 | institution | Deutsches Institut für Bautechnik / Ruhr-Universität Bochum | Ruhr-Universität Bochum (Auftraggeber: Deutsches Institut für Bautechnik, Gz. P 52-5-19.94-2078.21) | Abschlussbericht-PDF irbnet.de (Titelblatt) |
| Q196 | mbo2bim2023 | note | – | Dublette von mbo2bim2023 (lit-A-acc-bim.bib, Q034; identischer Key in zwei Dateien); korrigiert 2026-09-27: Titel laut Bericht (31.05.2023), Bearbeiter ergänzt, DIBt als Auftraggeber | s. o. |
| Q197 | nrw2026bimbauantrag | author | (leer) | K{\"o}nig, Markus and Exner, Hannah and Vonthron, Andr{\'e} | Berichts-PDF mhkbd.nrw (Titelblatt "bearbeitet von") |
| Q197 | nrw2026bimbauantrag | institution | Ministerium für Heimat, Kommunales, Bau und Digitalisierung NRW | Ruhr-Universität Bochum, Lehrstuhl für Informatik im Bauwesen (Hrsg./Hoster: Ministerium für Heimat, Kommunales, Bau und Digitalisierung NRW) | Berichts-PDF mhkbd.nrw (Titelblatt "bearbeitet von") |
| Q197 | nrw2026bimbauantrag | note | – | korrigiert 2026-09-27: Verfasser ergänzt (RUB mit VSK Software, Stadt Bochum); Ministerium nur Hrsg./Hoster | s. o. |
| Q200 | bdf2026quote | url | (leer) | https://www.fertigbau.de/presse/2307/fertigbau-kommt-schneller-aus-der-baukrise.html | fertigbau.de Pressemitteilung 09.03.2026 |
| Q200 | bdf2026quote | note | – | korrigiert 2026-09-27: URL ergänzt (Pressemitteilung "Fertigbau kommt schneller aus der Baukrise", 09.03.2026) | s. o. |
| Q201 | ingmonitor2025 | author | {VDI Verein Deutscher Ingenieure} and {Institut der deutschen Wirtschaft} | Pl{\"u}nnecke, Axel and Haag, Maike | iwkoeln.de Studienseite, vdi.de Publikationsseite (Ausgabedatum 2026-01), idw-Meldung 28.01.2026 |
| Q201 | ingmonitor2025 | title | VDI-/IW-Ingenieurmonitor, 3. Quartal 2025 | VDI/IW-Ingenieurmonitor 2025/III: Der regionale Arbeitsmarkt in den Ingenieurberufen. Sonderteil: ausländische Beschäftigte | iwkoeln.de Studienseite, vdi.de Publikationsseite (Ausgabedatum 2026-01), idw-Meldung 28.01.2026 |
| Q201 | ingmonitor2025 | year | 2025 | 2026 | iwkoeln.de Studienseite, vdi.de Publikationsseite (Ausgabedatum 2026-01), idw-Meldung 28.01.2026 |
| Q201 | ingmonitor2025 | url | (leer) | https://www.iwkoeln.de/studien/axel-pluennecke-maike-haag-der-regionale-arbeitsmarkt-in-den-ingenieurberufen-sonderteil-auslaendische-beschaeftigte-2025-iii.html | iwkoeln.de Studienseite, vdi.de Publikationsseite (Ausgabedatum 2026-01), idw-Meldung 28.01.2026 |
| Q201 | ingmonitor2025 | note | – | korrigiert 2026-09-27: Verfasser, Titel, Erscheinungsjahr 2026 (Berichtsquartal Q3/2025, veröffentlicht 01/2026), URL; Gutachten des IW für den VDI | s. o. |
| Q202 | destatis61261 | title | GENESIS-Online 61261: Baupreisindizes, u. a. Preisindex für Einfamilienfertighäuser ohne Keller | GENESIS-Online, Statistik 61261: Preisindizes für die Bauwirtschaft, Tabellen 61261-0015/-0016 (Preisindex für Einfamilienfertighäuser ohne Keller) | GENESIS-Online Statistik 61261 (Tabellenliste) |
| Q202 | destatis61261 | url | https://www-genesis.destatis.de | https://genesis.destatis.de/datenbank/online/statistic/61261/details | GENESIS-Online Statistik 61261 (Tabellenliste) |
| Q202 | destatis61261 | note | – | korrigiert 2026-09-27: amtlicher Statistikname, Tabellen und URL | s. o. |
| Q210 | sass2006wood | note | – | korrigiert 2026-09-27: Jahr 2006 bestätigt (Publikationsliste 2005 abweichend) | Crossref 10.1260/147807706777008920 (IJAC 4(1), 01/2006, Autor "Larry Sass") |
| Q212 | kwiecinski2016wood | doi | (leer) | 10.52842/conf.ecaade.2016.2.349 | Crossref 10.52842/conf.ecaade.2016.2.349 |
| Q212 | kwiecinski2016wood | pages | 349 | 349--358 | Crossref 10.52842/conf.ecaade.2016.2.349 |
| Q212 | kwiecinski2016wood | note | entfernt: „Endseite und DOI nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt, Seiten vervollständigt | s. o. |
| Q216 | puusepp2017enabling | doi | (leer) | 10.52842/conf.caadria.2017.251 | Crossref 10.52842/conf.caadria.2017.251 |
| Q216 | puusepp2017enabling | note | entfernt: „DOI nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q224 | popovic2021configuration | doi | (leer) | 10.1016/j.autcon.2021.103661 | Crossref 10.1016/j.autcon.2021.103661 |
| Q224 | popovic2021configuration | pages | (leer) | 103661 | Crossref 10.1016/j.autcon.2021.103661 |
| Q224 | popovic2021configuration | note | entfernt: „Artikelnummer/DOI nicht geprüft“ | korrigiert 2026-09-27: DOI und Artikelnummer ergänzt | s. o. |
| Q226 | lennartsson2022exploring | doi | (leer) | 10.3233/ATDE220629 | Crossref 10.3233/atde220629 |
| Q226 | lennartsson2022exploring | note | entfernt: „DOI nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q228 | hussamadin2020conceptual | doi | (leer) | 10.22260/ISARC2020/0152 | Crossref 10.22260/isarc2020/0152 |
| Q228 | hussamadin2020conceptual | note | entfernt: „DOI nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q231 | barlow2005building | doi | (leer) | 10.1068/a3579 | Crossref 10.1068/a3579 (Environment and Planning A 37(1), 9-20) |
| Q231 | barlow2005building | note | entfernt: „DOI nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q238 | adel2020computational | doi | (leer) | 10.3929/ethz-b-000439443 | DataCite 10.3929/ethz-b-000439443 (Dissertation ETH 2020) |
| Q238 | adel2020computational | note | entfernt: „DOI (10.3929/ethz-b-...) nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt (ETH führt den Autor als "Adel Ahmadian, Arash") | s. o. |
| Q239 | graser2020dfab | pages | (leer) | 130--139 | Crossref 10.2307/j.ctv13xpsvw.21 (S. 130-139) |
| Q239 | graser2020dfab | note | entfernt: „Seiten nicht geprüft“ | korrigiert 2026-09-27: Seiten ergänzt (Autorenliste vollständig, 11 Personen) | s. o. |
| Q240 | alwisy2019bim | doi | (leer) | 10.1080/15623599.2017.1411458 | Crossref 10.1080/15623599.2017.1411458 (published-print 2019-05, online 2018-01-20) |
| Q240 | alwisy2019bim | note | entfernt: „DOI nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt; Jahr 2019 = Heftjahr 19(3) bestätigt (online 20.01.2018) | s. o. |
| Q241 | liu2018bim | doi | (leer) | 10.1016/j.autcon.2018.02.001 | Crossref 10.1016/j.autcon.2018.02.001 |
| Q241 | liu2018bim | note | entfernt: „DOI nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q242 | wang2019automatic | doi | (leer) | 10.29173/mocs71 | Crossref 10.29173/mocs71 (S. 9-16) |
| Q242 | wang2019automatic | pages | (leer) | 9--16 | Crossref 10.29173/mocs71 (S. 9-16) |
| Q242 | wang2019automatic | note | entfernt: „Seiten nicht geprüft“ | korrigiert 2026-09-27: DOI und Seiten ergänzt | s. o. |
| Q245 | isaac2016methodology | doi | (leer) | 10.1016/j.autcon.2015.12.017 | Crossref 10.1016/j.autcon.2015.12.017 |
| Q245 | isaac2016methodology | note | entfernt: „DOI nicht geprüft“ | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q252 | montali2017knowledge | doi | (leer) | 10.1080/17452007.2017.1364216 | Crossref 10.1080/17452007.2017.1364216 (published-print 2018-03-04, online 2017-08-23) |
| Q252 | montali2017knowledge | volume | (leer) | 14 | Crossref 10.1080/17452007.2017.1364216 (published-print 2018-03-04, online 2017-08-23) |
| Q252 | montali2017knowledge | number | (leer) | 1--2 | Crossref 10.1080/17452007.2017.1364216 (published-print 2018-03-04, online 2017-08-23) |
| Q252 | montali2017knowledge | pages | (leer) | 78--94 | Crossref 10.1080/17452007.2017.1364216 (published-print 2018-03-04, online 2017-08-23) |
| Q252 | montali2017knowledge | year | 2017 | 2018 | Crossref 10.1080/17452007.2017.1364216 (published-print 2018-03-04, online 2017-08-23) |
| Q252 | montali2017knowledge | note | entfernt: „Band/Seiten/DOI der Druckfassung nicht geprüft“ | korrigiert 2026-09-27: DOI, Band, Heft, Seiten ergänzt; Jahr 2017->2018 (Heft 14(1-2), Druck 03/2018; online 23.08.2017) | s. o. |
| Q253 | granello2022structural | author | Granello, Gabriele and Reynolds, Thomas and Prest, C. | Granello, Gabriele and Reynolds, Thomas and Prest, Clayton | Crossref 10.1016/j.engstruct.2021.113639 |
| Q253 | granello2022structural | note | entfernt: „Vorname von C. Prest nicht ermittelt“ | korrigiert 2026-09-27: Vorname dritter Autor ergänzt (Clayton) | s. o. |
| Q256 | rabeneck2021history | title | A History of Failed Dreams: Modern Methods of Construction | A History of Failed Dreams: Modern Methods of Construction and Katerra | buildingsandcities.org (Kommentar vom 17.08.2021) |
| Q256 | rabeneck2021history | note | – | korrigiert 2026-09-27: Titel vervollständigt | s. o. |
| Q261 | niemeijer2009checkmate | note | – | [U] Seiten widersprüchlich: Crossref (CRC-Kapitel) 497--504, laut Bewertung TU/e-PDF 479--486; korrigiert 2026-09-27: Seitenangabe geprüft, nicht eingetragen | Crossref 10.1201/9781482266665-68 (S. 497-504) |
| Q262 | niemeijer2011constraint | doi | (leer) | 10.6100/IR715226 | DataCite 10.6100/ir715226 (TU Eindhoven 2011, ISBN) |
| Q262 | niemeijer2011constraint | isbn | (leer) | 978-90-6814-638-7 | DataCite 10.6100/ir715226 (TU Eindhoven 2011, ISBN) |
| Q262 | niemeijer2011constraint | note | entfernt: „DOI/ISBN nicht geprueft [U]“ | korrigiert 2026-09-27: DOI und ISBN ergänzt | s. o. |
| Q263 | retik1994automated | doi | (leer) | 10.1016/0360-1323(94)90002-7 | Crossref 10.1016/0360-1323(94)90002-7 (B&E 29(4), 421-436) |
| Q263 | retik1994automated | note | entfernt: „DOI nicht geprueft [U]“ | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q265 | erhan2026dcodeweaver | booktitle | Proceedings of the AHFE 2026 International Conference (Innovations in Sustainable Industry) | Sustainable Built Environment (AHFE 2026 International Conference) | Crossref 10.54941/ahfe1007893 (AHFE International, "Sustainable Built Environment", Bd. 225) |
| Q265 | erhan2026dcodeweaver | volume | (leer) | 225 | Crossref 10.54941/ahfe1007893 (AHFE International, "Sustainable Built Environment", Bd. 225) |
| Q265 | erhan2026dcodeweaver | doi | (leer) | 10.54941/ahfe1007893 | Crossref 10.54941/ahfe1007893 (AHFE International, "Sustainable Built Environment", Bd. 225) |
| Q265 | erhan2026dcodeweaver | note | entfernt: „DOI/Seiten offen“ | ; Seiten offen; korrigiert 2026-09-27: Tagungsband laut Crossref, Band 225 und DOI ergänzt (Seiten weiter offen) | s. o. |
| Q266 | pang2026natural | doi | (leer) | 10.2139/ssrn.6947980 | Crossref 10.2139/ssrn.6947980 (posted-content) |
| Q266 | pang2026natural | note | – | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q268 | abushwereb2019knowledge | doi | (leer) | 10.29173/mocs82 | Crossref 10.29173/mocs82 (S. 100-107) |
| Q268 | abushwereb2019knowledge | pages | (leer) | 100--107 | Crossref 10.29173/mocs82 (S. 100-107) |
| Q268 | abushwereb2019knowledge | note | entfernt: „Seitenangabe offen [U]“ | korrigiert 2026-09-27: DOI und Seiten ergänzt | s. o. |
| Q271 | mork2020parametric | Eintragstyp | @mastersthesis | @phdthesis | NTNU Open / NORA hdl 11250/2673875 (Titelei: Doctoral theses at NTNU 2020:238, PhD, ISBN) |
| Q271 | mork2020parametric | school | [U] Hochschule nicht geprueft (vermutl. NTNU) | Norwegian University of Science and Technology (NTNU), Trondheim | NTNU Open / NORA hdl 11250/2673875 (Titelei: Doctoral theses at NTNU 2020:238, PhD, ISBN) |
| Q271 | mork2020parametric | type | (leer) | Doctoral theses at NTNU, 2020:238 | NTNU Open / NORA hdl 11250/2673875 (Titelei: Doctoral theses at NTNU 2020:238, PhD, ISBN) |
| Q271 | mork2020parametric | isbn | (leer) | 978-82-326-4825-2 | NTNU Open / NORA hdl 11250/2673875 (Titelei: Doctoral theses at NTNU 2020:238, PhD, ISBN) |
| Q271 | mork2020parametric | url | (leer) | https://hdl.handle.net/11250/2673875 | NTNU Open / NORA hdl 11250/2673875 (Titelei: Doctoral theses at NTNU 2020:238, PhD, ISBN) |
| Q271 | mork2020parametric | note | entfernt: „[U] nur Exa-Publikationsindex“ | korrigiert 2026-09-27: Dissertation statt Masterarbeit (@mastersthesis->@phdthesis), Hochschule, Reihe, ISBN, URL | s. o. |
| Q277 | hellin2025natural | volume | (leer) | 6 | Crossref 10.35490/EC3.2025.265 (volume 6; given/family doppelt erfasst) |
| Q277 | hellin2025natural | note | – | korrigiert 2026-09-27: Band 6 (Reihe Computing in Construction) ergänzt; Autorennamen in Crossref fehlerhaft, Bib-Form beibehalten | s. o. |
| Q281 | kou2010knowledge | volume | (leer) | 42 | Crossref 10.1016/j.cad.2010.02.002 |
| Q281 | kou2010knowledge | number | (leer) | 6 | Crossref 10.1016/j.cad.2010.02.002 |
| Q281 | kou2010knowledge | pages | (leer) | 545--557 | Crossref 10.1016/j.cad.2010.02.002 |
| Q281 | kou2010knowledge | note | entfernt: „Band/Seiten offen [U]“ | korrigiert 2026-09-27: Band, Heft, Seiten ergänzt | s. o. |
| Q283 | mirhosseini2026ambiguity | volume | (leer) | 16 | Crossref 10.3390/buildings16173432 (online 27.08.2026) |
| Q283 | mirhosseini2026ambiguity | number | (leer) | 17 | Crossref 10.3390/buildings16173432 (online 27.08.2026) |
| Q283 | mirhosseini2026ambiguity | pages | (leer) | 3432 | Crossref 10.3390/buildings16173432 (online 27.08.2026) |
| Q283 | mirhosseini2026ambiguity | doi | (leer) | 10.3390/buildings16173432 | Crossref 10.3390/buildings16173432 (online 27.08.2026) |
| Q283 | mirhosseini2026ambiguity | note | entfernt: „[U] Exa-Index“, „Band/Artikelnr./DOI offen“ | Exa-Index; korrigiert 2026-09-27: Band, Heft, Artikelnummer, DOI ergänzt (U->V) | s. o. |
| Q286 | choi2022modification | author | Choi, Wonjun and others | Choi, Wonjun and Kim, Cheekyeong and Heo, Seokjae and Na, Seunguk | Crossref 10.1109/access.2022.3184106 |
| Q286 | choi2022modification | volume | (leer) | 10 | Crossref 10.1109/access.2022.3184106 |
| Q286 | choi2022modification | pages | (leer) | 65784--65800 | Crossref 10.1109/access.2022.3184106 |
| Q286 | choi2022modification | doi | (leer) | 10.1109/ACCESS.2022.3184106 | Crossref 10.1109/access.2022.3184106 |
| Q286 | choi2022modification | note | entfernt: „[U] IEEE“, „vollstaendige Autorenliste, Band, Seiten, DOI offen“ | IEEE; korrigiert 2026-09-27: Autorenliste ("others") vollständig, Band, Seiten, DOI ergänzt (U->V) | s. o. |
| Q290 | aichholzer1995novel | pages | (leer) | 752--761 | Crossref 10.1007/978-3-642-80350-5_65 (J.UCS-Nachdruck, S. 752-761) |
| Q290 | aichholzer1995novel | note | entfernt: „Seiten nicht geprueft“ | korrigiert 2026-09-27: Seiten ergänzt; Springer-Nachdruck 1996 mit DOI 10.1007/978-3-642-80350-5_65 (Originalheft ohne DOI) | s. o. |
| Q301 | jeong2009benchmark | author | Jeong, Yongwook and Eastman, Charles M. and Sacks, Rafael and Kaner, Israel | Jeong, Yeon-Suk and Eastman, Charles M. and Sacks, Rafael and Kaner, Israel | Crossref 10.1016/j.autcon.2008.11.001 (Y.-S. Jeong, AutCon 18(4), 469-484); ausgeschrieben wie in Crossref 10.1016/j.autcon.2009.07.002 (Yeon-suk Jeong, Georgia Tech/Eastman) |
| Q301 | jeong2009benchmark | note | – | korrigiert 2026-09-27: Vorname Erstautor Yongwook->Yeon-Suk | s. o. |
| Q314 | ohly2016attention | note | entfernt: „Heftnummer 7 [unsicher]“ | korrigiert 2026-09-27: Heftnummer 7 bestätigt | Crossref 10.1080/10937404.2016.1196155 |
| Q317 | aries2015daylight | note | entfernt: „Seitenangabe in Quellen uneinheitlich (6--27 bzw. 16--27) [unsicher]“ | korrigiert 2026-09-27: Seiten 6--27 bestätigt (online 2013) | Crossref 10.1177/1477153513509258 |
| Q327 | bonin2023goodnight | volume | (leer) | 9 | Crossref 10.1007/s40806-023-00377-w |
| Q327 | bonin2023goodnight | number | (leer) | 4 | Crossref 10.1007/s40806-023-00377-w |
| Q327 | bonin2023goodnight | pages | (leer) | 463--476 | Crossref 10.1007/s40806-023-00377-w |
| Q327 | bonin2023goodnight | note | entfernt: „Band/Seiten nicht erhoben [unsicher]“ | korrigiert 2026-09-27: Band, Heft, Seiten ergänzt | s. o. |
| Q342 | wilms2018color | note | entfernt: „Heftnummer [unsicher]“ | korrigiert 2026-09-27: Heftnummer 5 bestätigt (online 2017) | Crossref 10.1007/s00426-017-0880-8 |
| Q343 | hillier1984social | doi | (leer) | 10.1017/CBO9780511597237 | Crossref 10.1017/CBO9780511597237 (monograph, print 1984) |
| Q343 | hillier1984social | note | – | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q344 | hanson1998decoding | doi | (leer) | 10.1017/CBO9780511518294 | Crossref 10.1017/CBO9780511518294 |
| Q344 | hanson1998decoding | note | – | [U] Jahr: Crossref published-print 28.01.1999, Bib 1998 unverändert; korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q347 | ostwald2011mathematics | note | entfernt: „Heftnummer [unsicher]“ | korrigiert 2026-09-27: Heftnummer 2 bestätigt | Crossref 10.1007/s00004-011-0075-3 |
| Q364 | coburn2020interiors | author | Coburn, Alex and Vartanian, Oshin and Kenett, Yoed N. and Nadal, Marcos and Hartung, Franziska and Hayn-Leichsenring, Gregor and Navarrete, Gorka and Gonz{\'a}lez-Mora, Jos{\'e} L. and Chatterjee, Anjan | Coburn, Alexander and Vartanian, Oshin and Kenett, Yoed N. and Nadal, Marcos and Hartung, Franziska and Hayn-Leichsenring, Gregor and Navarrete, Gorka and Gonz{\'a}lez-Mora, Jos{\'e} L. and Chatterjee, Anjan | Crossref 10.1016/j.cortex.2020.01.009 |
| Q364 | coburn2020interiors | note | – | korrigiert 2026-09-27: Vorname Erstautor Alex->Alexander | s. o. |
| Q371 | lin2012fengshui | author | Lin, Chu-Chia and Chen, Chien-Liang and Twu, Yu-Chen | Lin, Chu-Chia and Chen, Chien-Liang and Twu, Ya-Chien | IRER-Artikelseite gssinst.org und RePEc ire/issued v15n03 (Autorenangaben) |
| Q371 | lin2012fengshui | note | entfernt: „ausgeschriebene Vornamen [unsicher]“ | korrigiert 2026-09-27: Vorname Twu Yu-Chen->Ya-Chien, Vornamen bestätigt | s. o. |
| Q372 | tam1999fengshui | note | entfernt: „Vornamen Tso [unsicher]“ | korrigiert 2026-09-27: Vorname Tso (Tony Y. N.) bestätigt | Crossref 10.1061/(ASCE)0733-9488(1999)125:4(152) |
| Q373 | prpj2022fengshui | Eintragstyp | @misc | @article | Crossref 10.1080/14445921.2022.2110370 (published-print 2021-09-02, online 2022-08-11) |
| Q373 | prpj2022fengshui | author | (leer) | Lam, Kwok-Chiu | Crossref 10.1080/14445921.2022.2110370 (published-print 2021-09-02, online 2022-08-11) |
| Q373 | prpj2022fengshui | journal | (leer) | Pacific Rim Property Research Journal | Crossref 10.1080/14445921.2022.2110370 (published-print 2021-09-02, online 2022-08-11) |
| Q373 | prpj2022fengshui | volume | (leer) | 27 | Crossref 10.1080/14445921.2022.2110370 (published-print 2021-09-02, online 2022-08-11) |
| Q373 | prpj2022fengshui | number | (leer) | 3 | Crossref 10.1080/14445921.2022.2110370 (published-print 2021-09-02, online 2022-08-11) |
| Q373 | prpj2022fengshui | pages | (leer) | 217--229 | Crossref 10.1080/14445921.2022.2110370 (published-print 2021-09-02, online 2022-08-11) |
| Q373 | prpj2022fengshui | year | 2022 | 2021 | Crossref 10.1080/14445921.2022.2110370 (published-print 2021-09-02, online 2022-08-11) |
| Q373 | prpj2022fengshui | howpublished | Pacific Rim Property Research Journal 27(3) | (entfernt) | Crossref 10.1080/14445921.2022.2110370 (published-print 2021-09-02, online 2022-08-11) |
| Q373 | prpj2022fengshui | note | entfernt: „Autor nicht ermittelt [unsicher] -- vor Zitation nachtragen“ | korrigiert 2026-09-27: @misc->@article; Autor, Zeitschrift, Band, Heft, Seiten ergänzt; Jahr 2022->2021 (Heft 27(3) datiert 2021, online-first 11.08.2022); Key unverändert | s. o. |
| Q374 | peng2012concern | author | Peng, Yu-Shu and Hsiung, Hsin-Hui and Chen, Kuang-Hsun | Peng, Yu-Shu and Hsiung, Hsin-Hua and Chen, Ke-Hung | Crossref 10.1002/mar.20539 |
| Q374 | peng2012concern | note | entfernt: „ausgeschriebene Vornamen und Heftnummer [unsicher]“ | korrigiert 2026-09-27: Vornamen Koautoren (Hsin-Hui->Hsin-Hua, Kuang-Hsun->Ke-Hung); Heft 7 bestätigt | s. o. |
| Q376 | patra2009vaastu | note | entfernt: „Vorname und Heftnummer [unsicher]“ | korrigiert 2026-09-27: Heft 4 und Vorname bestätigt (online 2008) | Crossref 10.1002/sd.388 |
| Q379 | enright1995dowsing | doi | (leer) | 10.1007/BF01134560 | SpringerLink link.springer.com/article/10.1007/BF01134560; Crossref (beide DOIs: Naturwiss. 82(8), 360-369) |
| Q379 | enright1995dowsing | note | entfernt: „DOI widerspruechlich (10.1007/BF01134560 vs. 10.1007/s001140050198) [unsicher], daher weggelassen“ | korrigiert 2026-09-27: DOI festgelegt (10.1007/BF01134560, SpringerLink-Artikelseite; zweiter Crossref-Datensatz 10.1007/s001140050198) | s. o. |
| Q381 | air2016formaldehyd | volume | (leer) | 59 | Crossref 10.1007/s00103-016-2389-5 |
| Q381 | air2016formaldehyd | number | (leer) | 8 | Crossref 10.1007/s00103-016-2389-5 |
| Q381 | air2016formaldehyd | pages | (leer) | 1040--1044 | Crossref 10.1007/s00103-016-2389-5 |
| Q381 | air2016formaldehyd | note | entfernt: „Band/Seiten nicht erhoben [unsicher]“ | korrigiert 2026-09-27: Band, Heft, Seiten ergänzt | s. o. |
| Q385 | fischer1991critiquing | doi | 10.1145/123757.123758 | 10.1145/123078.128727 | Crossref 10.1145/123078.128727 (ACM TOIS 9(2), 123-151) |
| Q385 | fischer1991critiquing | note | entfernt: „Heftnummer 2 vs. 3 in Quellen uneinheitlich [unsicher]“ | korrigiert 2026-09-27: DOI falsch (10.1145/123757.123758, nicht in Crossref), richtig 10.1145/123078.128727; Heft 2 bestätigt | s. o. |
| Q386 | silverman1992critiquing | doi | (leer) | 10.1145/129852.129861 | Crossref 10.1145/129852.129861 (CACM 35(4), 106-127) |
| Q386 | silverman1992critiquing | note | entfernt: „DOI nicht ermittelt [unsicher]“ | korrigiert 2026-09-27: DOI ergänzt | s. o. |
| Q360 | iwbi2020wellv2 | note | – | [U] Jahr und Mind-Feature-Nummern nicht an der Primärquelle (v2.wellcertified.com) geprüft | nur Sekundärquellen (Bewertung) |
| Q398 | rabold0000vibroakustik | note | – | [U] Kurzbericht selbst undatiert; er zitiert den ift-Forschungsbericht 2017, erschien also frühestens 2017 -- Jahr nicht eingetragen | iVTH-PDF (ohne Datum), baufachinformation.de (Forschungsbericht TP4 06/2017) |
| Q413 | fraunhoferipa0000designchain | year | (leer) | 2023 | IPA-Referenzprojektseite (Projektlaufzeit) |
| Q413 | fraunhoferipa0000designchain | note | entfernt: „[U] Existenz“, „Jahr nicht angegeben (Key-Platzhalter 0000)“ | Existenz; korrigiert 2026-09-27: Jahr 2023 ergänzt (= Projektende laut Laufzeitangabe 03/2022--04/2023, Seite selbst undatiert; Key unverändert) | s. o. |
| Q420 | bsz0000fertighaustour | year | (leer) | 2025 | Artikelseite bayerische-staatszeitung.de (Datum 25.07.2025) |
| Q420 | bsz0000fertighaustour | note | entfernt: „[U] Artikel verifiziert, Erscheinungsdatum nicht ermittelt (Key-Platzhalter 0000)“ | Artikel verifiziert, erschienen 25.07.2025; korrigiert 2026-09-27: Jahr 2025 ergänzt (Artikel vom 25.07.2025; Key unverändert) | s. o. |
| Q422 | flade2008architektur | note | entfernt: „ISBN nur über Wikipedia [U], Katalogabgleich ausstehend.“ | ; ISBN über Das Schweizer Buch 2008 und DDB bestätigt.; korrigiert 2026-09-27: ISBN bestätigt | Das Schweizer Buch 17/2008 (Nationalbibliothek, NB 001542125) und DDB (ISBN 9783456846125, 334 S.) |
| Q424 | flade2020kompendium | title | Kompendium der Architekturpsychologie | Kompendium der Architekturpsychologie. Zur Gestaltung gebauter Umwelten | Crossref 10.1007/978-3-658-31338-8 |
| Q424 | flade2020kompendium | note | – | korrigiert 2026-09-27: Untertitel ergänzt (Reihe essentials laut Crossref) | s. o. |
| Q425 | flade2020individualisiert | title | Wohnen in der individualisierten Gesellschaft | Wohnen in der individualisierten Gesellschaft. Psychologisch kommentiert | Crossref 10.1007/978-3-658-29836-4 |
| Q425 | flade2020individualisiert | note | – | korrigiert 2026-09-27: Untertitel ergänzt | s. o. |
| Q427 | hellbrueck1999umweltpsychologie | author | Hellbr{\"u}ck, J{\"u}rgen and Fischer, M. | Hellbr{\"u}ck, J{\"u}rgen and Fischer, Manfred | DNB-Inhaltsverzeichnis d-nb.info/956515355 (Titelblatt), Hogrefe eLibrary |
| Q427 | hellbrueck1999umweltpsychologie | note | entfernt: „Nur Initiale M. für Fischer belegt.“ | korrigiert 2026-09-27: Vorname Fischer ergänzt (M.->Manfred) | s. o. |
| Q429 | dieckmann1998psychologie | author | Dieckmann, F. and Flade, Antje and Schuemer, R. and Str{\"o}hlein, G. and Walden, Rotraut | Dieckmann, Friedrich and Flade, Antje and Schuemer, Rudolf and Str{\"o}hlein, Gerhard and Walden, Rotraut | IWU-Publikationsseite FF4-1998, DDB-Eintrag |
| Q429 | dieckmann1998psychologie | note | entfernt: „[U] nur über die Publikationsliste R. Walden (Universität Koblenz) belegt; nur Initialen von Dieckmann, Schuemer, Ströhlein belegt; Katalogabgleich ausstehend.“ | verifiziert via IWU-Publikationsseite und DDB (327 S.).; korrigiert 2026-09-27: Vornamen ergänzt; Rolle: Beitragszitate nennen die Fünf als Hrsg., die IWU-Publikationsliste ohne Hrsg.-Vermerk (als author belassen) | s. o. |
| Q431 | harlander2001villa | note | entfernt: „Hrsg. gemeinsam mit Bodenschatz, Fehl, Jessen, Kuhn, Zimmermann laut Autorenseite.“ | Titelblatt: hrsg. von Tilman Harlander in Verbindung mit Harald Bodenschatz, Gerhard Fehl, Johann Jessen, Gerd Kuhn, Clemens Zimmermann.; korrigiert 2026-09-27: Mitherausgeber präzisiert: Titelblatt "herausgegeben von Tilman Harlander in Verbindung mit ..." | Titelblatt-Scan (dandelon), Wüstenrot Stiftung ("Herausgegeben von Tilman Harlander u.a."), Uni Stuttgart IWE |
| Q436 | eisele2024standards | author | Eisele, B. and Albus, J. | Eisele, Bj{\"o}rn and Albus, Jutta | DataCite 10.58007/jwz9-ze04 |
| Q436 | eisele2024standards | note | – | korrigiert 2026-09-27: Vornamen ausgeschrieben | s. o. |
| Q437 | ammann2022wohneigentum | author | Ammann, Iris and M{\"u}ther, A. M. | Ammann, Iris and M{\"u}ther, Anna Maria | DataCite 10.58007/cqa5-jm26 |
| Q437 | ammann2022wohneigentum | note | – | korrigiert 2026-09-27: Vorname Müther ausgeschrieben | s. o. |
| Q440 | duerr2021familien | type | BBSR-Online-Publikation | BBSR-Online-Publikation 25/2021 | BBSR-Veröffentlichungsseite bbsr-online-25-2021 (URN urn:nbn:de:101:1-2022031611023120381732); HKA-PDF-Impressum 05/2021 |
| Q440 | duerr2021familien | url | (leer) | https://www.bbsr.bund.de/BBSR/DE/veroeffentlichungen/bbsr-online/2021/bbsr-online-25-2021.html | BBSR-Veröffentlichungsseite bbsr-online-25-2021 (URN urn:nbn:de:101:1-2022031611023120381732); HKA-PDF-Impressum 05/2021 |
| Q440 | duerr2021familien | note | entfernt: „[U] Angabe „BBSR-Online-Publikation 5/2021“ laut DJI-Pressemitteilung 21.07.2021; die BBSR-Seite 05/2021 gehört jedoch zu einem anderen Titel (Leichtbeton-3D-Druck). Heftnummer offen.“ | BBSR-Katalog: Ausgabe 25/2021; PDF-Impressum und DJI-Pressemitteilung nennen 5/2021.; korrigiert 2026-09-27: Heftnummer 25/2021 nach BBSR-Katalog (PDF-Impressum: 5/2021), URL ergänzt | s. o. |
| Q444 | heinze1997neuewohnung | author | Heinze, Rolf G. and others | Heinze, Rolf G. and Eichener, Volker and Naegele, Gerhard and Bucksteeg, Mathias and Schauerte, Martin | Schader-PDF (Titelblatt) und lobid/hbz |
| Q444 | heinze1997neuewohnung | note | entfernt: „Weitere Autoren im Eintrag mit „...“ abgekürzt.“ | korrigiert 2026-09-27: abgekürzte Autorenliste ("others") vollständig ausgeschrieben | s. o. |
| Q402 | schuster2022bimwood | author | Schuster, Sandra and Arnold, J. and Behm, J. | Schuster, Sandra and Arnold, Johanna and Behm, Julia | mediaTUM 1688369 (Beitrag) und mediaTUM 1712381 (BIMwood-Bericht, gleiche Personen mit Vornamen) |
| Q402 | schuster2022bimwood | note | – | [U] Seitenangabe im Tagungsband (Forum Bauinformatik 2022, München) nicht ermittelt; korrigiert 2026-09-27: Vornamen ausgeschrieben | s. o. |
| Q461 | iso2018usability | note | entfernt: „DIN-Ausgabedatum nach Standardzitation, nicht bei DIN Media geprüft.“ | DIN-Ausgabe 2018-11 bei DIN Media bestätigt.; korrigiert 2026-09-27: DIN-Ausgabe DIN EN ISO 9241-11:2018-11 bestätigt | DIN Media (DIN EN ISO 9241-11:2018-11) |
| Q462 | iso2020interaction | note | entfernt: „DIN-Ausgabedatum nach Standardzitation, nicht bei DIN Media geprüft.“ | DIN-Ausgabe 2020-10 über DIN Media bestätigt.; korrigiert 2026-09-27: DIN-Ausgabe DIN EN ISO 9241-110:2020-10 bestätigt | DIN Media (Entwurf 2019-09 ersetzt durch DIN EN ISO 9241-110:2020-10), regelrechtaktuell.de |

## Weitere Hinweise zu Entscheidungen

- **Q413**: Jahr 2023 = Projektende laut Laufzeitangabe (Seite undatiert); als Konvention eingetragen, im note vermerkt.
- **Q429**: Beitragszitate führen die fünf Personen als Hrsg., die IWU-Verlagsseite ohne Hrsg.-Vermerk; Rolle als author belassen.
- **Q373**: Jahr auf 2021 gesetzt (Heft 27(3), published-print 2021-09-02); online-first 11.08.2022. Key prpj2022fengshui unverändert.
- **Q252**: Jahr auf 2018 gesetzt (Heft 14(1-2), Druck 03/2018); Key montali2017knowledge unverändert.
- **Q201**: Jahr auf 2026 gesetzt (Erscheinen 01/2026, Berichtsquartal Q3/2025); Key ingmonitor2025 unverändert.
- **Q161**: Jahr 2026 als Abrufstand belassen (konsistent mit den übrigen Rechtsquellen), Fassung im Titel.

## Geprüft, keine Änderung nötig

Q021 (Crossref: 14 Autoren, „Gonçal Costa“ korrekt), Q036, Q037, Q100, Q140, Q218, Q305, Q307, Q321, Q355, Q433 (editor bereits im BibTeX; der Master zeigt Herausgeber nicht, weil bibmerge.py nur author/organization/institution liest), Q142, Q148 (Autorenliste im BibTeX vollständig, nur 150-Zeichen-Kürzung im Master; Crossref geprüft), Q133 (ACL Anthology bestätigt „Lu, Wei“), Q173 (führender Eintrag der Dublette Q150).

## nicht klärbar

| id | key | Problem |
|---|---|---|
| Q174 | prodhaftg2026 | Verkündung des ProdHaftG-neu (BT-Drs. 21/4297) bis 27.09.2026 nicht nachgewiesen; Eintrag als Gesetzentwurf gekennzeichnet, nach Verkündung BGBl.-Fundstelle bzw. RL (EU) 2024/2853 zitieren. |
| Q184 | din4102-4 | Ausgabe 2016-05 laut DIN Media durch DIN 4102-4:2025-06 ersetzt. Die Bewertung meint 2016-05 (bauaufsichtlicher Nachweis); ob BayTB 11/2025 (beruht auf MVV TB 2025/1 vom 20.05.2025) noch 2016-05 einführt, wurde nicht am BayTB-Text geprüft. Titel unverändert. |
| Q261 | niemeijer2009checkmate | Seiten widersprüchlich: Crossref (CRC-Kapitel) 497–504, laut Bewertung TU/e-PDF 479–486; kein pages-Feld eingetragen. |
| Q265 | erhan2026dcodeweaver | Seitenangabe weiterhin offen (Crossref ohne page). |
| Q344 | hanson1998decoding | Jahr: Crossref published-print 28.01.1999, Bib 1998; nicht an Verlagsseite geklärt, Jahr unverändert. |
| Q360 | iwbi2020wellv2 | Jahr und Mind-Feature-Nummern nur über Sekundärquellen; Primärquelle (v2.wellcertified.com) nicht geprüft. |
| Q398 | rabold0000vibroakustik | Kurzbericht undatiert; zitiert den ift-Forschungsbericht 2017, erschien also frühestens 2017. Kein year eingetragen (Key 0000 bleibt). |
| Q402 | schuster2022bimwood | Seiten im Tagungsband Forum Bauinformatik 2022 nicht ermittelt (mediaTUM ohne Seitenangabe). |
| Q404 | standtke2024etim | Jahr 2024 nur aus dem Text erschlossen, wh40.ch-Seite undatiert; unverändert (bereits [U]). |
| Q417 | kuhl2023robotik | Kein Repositorium ermittelt, nur Exa-Bibliothekseintrag; unverändert (bereits [U]). Typ @thesis mit type={Bachelorarbeit} ist biblatex-konform und wurde belassen. |
| Q034/Q196 | mbo2bim2023 | Derselbe Key steht in lit-A-acc-bim.bib (@misc, Projektseite) und lit-C-recht-normen.bib (@techreport, Abschlussbericht). Keys dürfen nicht geändert werden; der C-Eintrag ist als Dublette markiert. bibmerge.py meldet weiterhin „Key-Kollisionen [mbo2bim2023]“; beim Einbinden nur eine Datei-Fassung verwenden. |


## Runde 2: Q463–Q811

Grundlage: `quellen-bewertung.csv` (Spalte `begruendung`, Q463–Q811). Bearbeitet: `lit-H-ff4-ff5.bib`, `lit-I-schneeball-a.bib`, `lit-I-schneeball-b.bib`; lit-A…G und lit-J-*.bib nicht angefasst. Keine Einträge hinzugefügt oder gelöscht, keine Keys geändert (Keys mit altem Jahr bleiben stehen). Jede korrigierte Quelle trägt im `note` den Zusatz „korrigiert 2026-09-27: …“. Konventionen wie Runde 1: Artikelnummern im Feld `pages`, `year` = Jahr des Heftes (published-print), erledigte Vorbehalte im note entfernt.

Prüfweg: Crossref-API (`api.crossref.org/works?filter=doi:…&select=…`, über Exa-Fetch, da direkt gesperrt), Verlags- und Repositoriumsseiten (itcon.org, AIS eLibrary, PMLR), EUR-Lex, iso.org, DIN Media.

In `lit-I-schneeball-a.bib` war nach Prüfung keine Korrektur nötig (die dort genannten Online-/Heftjahr-Hinweise Q549, Q559, Q562, Q571, Q584, Q596 sind bereits mit dem Heftjahr eingetragen).

### Stabilitätsprüfung

- Sicherung vor der Korrektur: `quellen-master.csv` und die drei .bib-Dateien im Scratchpad.
- `bibmerge.py` auf einer Kopie des Ordners (lit-A…I; eine lit-J-*.bib lag nicht vor): 814 Einträge, **811 eindeutig**, 3 Duplikate wie vorher (du2026text2bim, iso16739-2024→iso2024ifc, ids2024→bsi2024ids); Key-Kollision mbo2bim2023 unverändert (s. Runde 1).
- Reihenfolge von id/key/alias identisch zur Sicherung (811/811). `quellen-master.csv` im Originalordner nicht überschrieben (byte-identisch zur Sicherung).
- Brace-Balance der drei .bib-Dateien: Endtiefe 0, keine negativen Tiefen; keine doppelten Feldnamen innerhalb eines Eintrags.

### Änderungen (23 Quellen, 30 Feldkorrekturen zuzüglich note)

| id | key | Feld | alt | neu | Prüfweg |
|---|---|---|---|---|---|
| Q464 | naser2026engineers | pages | (leer) | 04526016 | Crossref 10.1061/JLADAH.LADR-1499 (18(3), article-number 04526016) |
| Q464 | naser2026engineers | note | entfernt: „Seitenzahl/Artikelnummer in Crossref nicht angegeben.“ | korrigiert 2026-09-27: Artikelnummer 04526016 ergänzt (Crossref article-number) | s. o. |
| Q465 | ng2023liability | pages | (leer) | 04522043 | Crossref 10.1061/(ASCE)LA.1943-4170.0000578 (15(1), article-number 04522043) |
| Q465 | ng2023liability | note | – | korrigiert 2026-09-27: Artikelnummer 04522043 ergänzt (Crossref article-number) | s. o. |
| Q470 | zou2023lessons | pages | (leer) | 04023019 | Crossref 10.1061/JMENEA.MEENG-5051 (39(4), article-number 04023019) |
| Q470 | zou2023lessons | note | – | korrigiert 2026-09-27: Artikelnummer 04023019 ergänzt (Crossref article-number) | s. o. |
| Q471 | zou2022investigating | pages | (leer) | 05022013 | Crossref 10.1061/(ASCE)CO.1943-7862.0002384 (148(12), article-number 05022013) |
| Q471 | zou2022investigating | note | – | korrigiert 2026-09-27: Artikelnummer 05022013 ergänzt (Crossref article-number) | s. o. |
| Q495 | darocha2016managing | pages | (leer) | 05016005 | Crossref 10.1061/(ASCE)CO.1943-7862.0001119 (142(8), article-number 05016005) |
| Q495 | darocha2016managing | note | – | korrigiert 2026-09-27: Artikelnummer 05016005 ergänzt (Crossref article-number) | s. o. |
| Q503 | ittmann2018standard | pages | (leer) | 06518001 | Crossref 10.1061/(ASCE)LA.1943-4170.0000265 (10(3), article-number 06518001) |
| Q503 | ittmann2018standard | note | – | korrigiert 2026-09-27: Artikelnummer 06518001 ergänzt (Crossref article-number) | s. o. |
| Q506 | alwash2017impact | pages | (leer) | 04517005 | Crossref 10.1061/(ASCE)LA.1943-4170.0000219 (9(3), article-number 04517005) |
| Q506 | alwash2017impact | note | – | korrigiert 2026-09-27: Artikelnummer 04517005 ergänzt (Crossref article-number) | s. o. |
| Q521 | abdulnabi2022proactive | pages | (leer) | 04022052 | Crossref 10.1061/(ASCE)CO.1943-7862.0002311 (148(7), article-number 04022052) |
| Q521 | abdulnabi2022proactive | note | – | korrigiert 2026-09-27: Artikelnummer 04022052 ergänzt (Crossref article-number) | s. o. |
| Q468 | jaskula2024common | year | 2024 | 2025 | Crossref 10.1108/CI-04-2023-0088 (published-print 2025-11-17, online 2024-01-29) |
| Q468 | jaskula2024common | note | – | korrigiert 2026-09-27: Jahr 2024 (online) -> 2025 (Heft 25(5), published-print 17.11.2025); Key unverändert | s. o. |
| Q498 | tremblay2010focus | pages | (leer) | 27 | AIS eLibrary aisel.aisnet.org/cais/vol26/iss1/27; Crossref 10.17705/1CAIS.02627 (ohne page) |
| Q498 | tremblay2010focus | note | – | korrigiert 2026-09-27: Artikelnummer 27 aus note ins Feld pages übernommen (AIS eLibrary cais/vol26/iss1/27, DOI-Suffix 02627) | s. o. |
| Q502 | dellacqua2026navigating | volume | (leer) | 37 | Crossref 10.1287/orsc.2025.21838 (37(2), 403-423, published-print 2026-03) |
| Q502 | dellacqua2026navigating | number | (leer) | 2 | Crossref 10.1287/orsc.2025.21838 (37(2), 403-423, published-print 2026-03) |
| Q502 | dellacqua2026navigating | pages | (leer) | 403--423 | Crossref 10.1287/orsc.2025.21838 (37(2), 403-423, published-print 2026-03) |
| Q502 | dellacqua2026navigating | note | entfernt: „Band/Heft in Crossref noch nicht angegeben.“ | korrigiert 2026-09-27: Band 37, Heft 2, S. 403--423 ergänzt (Crossref, published-print 03/2026) | s. o. |
| Q520 | wuni2019critical | year | 2019 | 2022 | Crossref 10.1080/15623599.2019.1613212 (published-print 2022-01-25, online 2019-05-13) |
| Q520 | wuni2019critical | note | – | korrigiert 2026-09-27: Jahr 2019 (online) -> 2022 (Heft 22(2), published-print 25.01.2022); Key unverändert | s. o. |
| Q480 | eu2014eidas | howpublished | ABl. L 257 vom 28.08.2014, S. 73; Änderung ABl. L, 2024/1183, 30.04.2024 | ABl. L 257 vom 28.08.2014, S. 73--114; Änderung ABl. L, 2024/1183, 30.04.2024 | EUR-Lex CELEX 32014R0910 (ABl. L 257 vom 28.8.2014, S. 73-114) |
| Q480 | eu2014eidas | url | http://data.europa.eu/eli/reg/2024/1183/oj | http://data.europa.eu/eli/reg/2014/910/oj | EUR-Lex CELEX 32014R0910 (ABl. L 257 vom 28.8.2014, S. 73-114) |
| Q480 | eu2014eidas | note | entfernt: „Seitenzahl vor Zitation gegenprüfen.“ | korrigiert 2026-09-27: URL auf ELI der Grundverordnung 910/2014 statt Änderungs-VO 2024/1183; Seiten 73--114 an EUR-Lex bestätigt | s. o. |
| Q643 | gao2023pal | doi | 10.48550/arxiv.2211.10435 | (entfernt) | PMLR proceedings.mlr.press/v202/gao23f (BibTeX der Seite ohne DOI); 10.48550 = arXiv-DOI |
| Q643 | gao2023pal | note | – | korrigiert 2026-09-27: DOI 10.48550/arxiv.2211.10435 (arXiv-Preprint) entfernt; zitiert wird die PMLR-Fassung (Bd. 202, ohne DOI), Preprint über eprint | s. o. |
| Q666 | bakhshi2021dfma | year | 2021 | 2022 | Crossref 10.1016/j.autcon.2021.104015 (Bd. 133, published-print 2022-01) |
| Q666 | bakhshi2021dfma | note | – | korrigiert 2026-09-27: Jahr 2021 (online) -> 2022 (AutCon 133, published-print 01/2022); Key unverändert | s. o. |
| Q685 | haug2018costs | year | 2018 | 2019 | Crossref 10.1016/j.compind.2018.11.005 (Bd. 105, published-print 2019-02) |
| Q685 | haug2018costs | note | – | korrigiert 2026-09-27: Jahr 2018 (online) -> 2019 (CompInd 105, published-print 02/2019); Key unverändert | s. o. |
| Q687 | hentschke2019conjoint | year | 2019 | 2020 | Crossref 10.1590/s1678-86212020000100372 (20(1), 2020-03) |
| Q687 | hentschke2019conjoint | note | – | korrigiert 2026-09-27: Jahr 2019 -> 2020 (Ambiente Construído 20(1), Crossref 03/2020); Key unverändert | s. o. |
| Q742 | asare2026dimensionality | pages | (leer) | 04025112 | Crossref 10.1061/jccee5.cpeng-6479 (40(1), article-number 04025112) |
| Q742 | asare2026dimensionality | note | – | korrigiert 2026-09-27: Artikelnummer 04025112 ergänzt (Crossref article-number) | s. o. |
| Q753 | chateauvieuxhellwig2025schallschutz | editor | (leer) | Fouad, Nabil A. | Crossref 10.1002/9783433612095 (edited-book, editor Nabil Fouad); Verlagsangabe laut Bewertung |
| Q753 | chateauvieuxhellwig2025schallschutz | note | entfernt: „[U] … Unsicher: Herausgeber im Crossref-Record nicht angegeben ([U]->[V])“ | korrigiert 2026-09-27: Herausgeber Fouad, Nabil A. ergänzt (Crossref edited-book 10.1002/9783433612095; Verlagsangabe) | s. o. |
| Q762 | dosen2017lived | title | Lived spaceandgeometric space: comparing people’s perceptions of spatial enclosure and exposure with metric room properties and isovist measures | Lived space and geometric space: comparing people’s perceptions of spatial enclosure and exposure with metric room properties and isovist measures | Crossref 10.1080/00038628.2016.1235545 (Titel mit Kursivauszeichnung, Leerzeichen fehlen dort) |
| Q762 | dosen2017lived | note | – | korrigiert 2026-09-27: fehlende Leerzeichen im Titel ergänzt ("Lived space and geometric space"; Crossref-Titel mit Kursivauszeichnung ohne Leerzeichen) | s. o. |
| Q777 | iso23387 | title | ISO 23387:2020 Building information modelling ({BIM}) -- Data templates for construction objects used in the life cycle of built assets -- Concepts and principles | ISO 23387:2025 Building information modelling ({BIM}) -- Data templates for objects used in the life cycle of assets | iso.org/standard/85391.html (ISO 23387:2025, 2. Ausgabe); DIN Media (DIN EN ISO 23387:2026-01 ersetzt 2020-12); CEN: EN ISO 23387:2025 ersetzt EN ISO 23387:2020 |
| Q777 | iso23387 | year | 2020 | 2025 | iso.org/standard/85391.html (ISO 23387:2025, 2. Ausgabe); DIN Media (DIN EN ISO 23387:2026-01 ersetzt 2020-12); CEN: EN ISO 23387:2025 ersetzt EN ISO 23387:2020 |
| Q777 | iso23387 | doi | 10.3403/30376819 | (entfernt) | iso.org/standard/85391.html (ISO 23387:2025, 2. Ausgabe); DIN Media (DIN EN ISO 23387:2026-01 ersetzt 2020-12); CEN: EN ISO 23387:2025 ersetzt EN ISO 23387:2020 |
| Q777 | iso23387 | url | (leer) | https://www.iso.org/standard/85391.html | iso.org/standard/85391.html (ISO 23387:2025, 2. Ausgabe); DIN Media (DIN EN ISO 23387:2026-01 ersetzt 2020-12); CEN: EN ISO 23387:2025 ersetzt EN ISO 23387:2020 |
| Q777 | iso23387 | note | entfernt: „[U] OpenAlex-Record zur BSI-Ausgabe … Unsicher: DIN-Ausgabe (DIN EN ISO 23387) nicht separat geprüft. ([U]->[V], Prüfweg neu)“ | korrigiert 2026-09-27: Normausgabe aktualisiert: ISO 23387:2020 durch ISO 23387:2025 (2. Ausgabe, 2025-09) ersetzt, Titel angepasst; DOI 10.3403/30376819 (BSI-Ausgabe BS EN ISO 23387:2020) entfernt, URL iso.org ergänzt; deutsche Ausgabe DIN EN ISO 23387:2026-01 ersetzt DIN EN ISO 23387:2020-12 (DIN Media) | s. o. |
| Q786 | mellenthinfilardo2026requirements | volume | (leer) | 31 | Verlagsseite itcon.org/2026/10 (Zitierangabe ITcon 31, 225-245); Crossref ohne volume |
| Q786 | mellenthinfilardo2026requirements | pages | 225 | 225--245 | Verlagsseite itcon.org/2026/10 (Zitierangabe ITcon 31, 225-245); Crossref ohne volume |
| Q786 | mellenthinfilardo2026requirements | note | entfernt: „[U] … Unsicher: Band/Heft im Record noch nicht vergeben (Online-First). ([U]->[V])“ | korrigiert 2026-09-27: Band 31 und Seiten 225--245 ergänzt (Verlagsseite itcon.org/2026/10, Zitierangabe) | s. o. |
| Q804 | ulusoy2024preferences | number | (leer) | 4 | Crossref 10.3390/architecture4040045 (4(4), 854-876) |
| Q804 | ulusoy2024preferences | note | – | korrigiert 2026-09-27: Heft 4 ergänzt (Crossref: Architecture 4(4), 854-876) | s. o. |

### Weitere Hinweise zu Entscheidungen

- **Q468, Q520, Q666, Q685, Q687**: Jahr auf das Heftjahr gesetzt (Konvention wie Q252/Q373); Keys (jaskula2024common, wuni2019critical, bakhshi2021dfma, haug2018costs, hentschke2019conjoint) unverändert.
- **Q498**: CAIS vergibt Artikelnummern statt Seiten; Nummer 27 wie die übrigen Artikelnummern in `pages` gesetzt.
- **Q643**: Das arXiv-Preprint bleibt über `eprint`/`archiveprefix` auffindbar; die PMLR-Fassung hat keine DOI.
- **Q777**: Keine rechtliche oder inhaltliche Bindung an die Ausgabe 2020 erkennbar (anders als bei den GModG-Normen in Runde 1), daher auf die geltende Ausgabe ISO 23387:2025 umgestellt; Organisation ISO belassen, die deutsche Ausgabe DIN EN ISO 23387:2026-01 steht im note.
- **Q753**: Crossref führt den Herausgeber nur als „Nabil Fouad“; die Initiale „A.“ folgt der Verlagsangabe aus der Bewertung.
- **Q480**: Die Änderungs-VO 2024/1183 bleibt in Titel und howpublished genannt; die URL zeigt jetzt auf die Grundverordnung.

### Geprüft, keine Änderung nötig

Q472 cheung2026institutionalizing, Q669 campogay2026quality, Q729 wyke2025productivity (Crossref am 27.09.2026 weiterhin ohne Band/Heft, Online-First; Q669/Q729 bleiben [U]), Q710 piroozfar2013mass (editor bereits im BibTeX; der Master zeigt Herausgeber nicht, weil bibmerge.py nur author/organization/institution liest), Q474, Q636, Q656, Q663 (Abstract aus arXiv-Vorfassung gelesen, DOI im Eintrag ist die Journalfassung), Q500 (QJE-Fassung bereits zitiert), Q490 (Crossref 35(1–4), 2018 wie eingetragen), Q549, Q559, Q562, Q571, Q584, Q596, Q639, Q659, Q670, Q677, Q683, Q689, Q701, Q708, Q719, Q721, Q728, Q731, Q744, Q792 (Heftjahr bereits eingetragen), Q759 (Ausgabe 2024-11 aktuell), Q473, Q475 (Autorennamen im BibTeX korrekt, Crossref fehlerhaft).

### nicht klärbar

| id | key | Problem |
|---|---|---|
| Q478 | wilhelmi2020haftung | Kapitel-DOI bei Crossref nicht registriert (Suche Präfix 10.3790, Typ book-chapter, Autor Wilhelmi ohne Treffer); Band-DOI 10.3790/978-3-428-55963-3 unverändert, note um „[U] …“ ergänzt. |
