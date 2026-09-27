# Werteparser: Grammatik für deutsche Zahl-, Maß- und Richtungsangaben

Version 0.1.0, Stand 27.09.2026. Quelle: Kapitel 10.3. Referenzimplementierung (Teilmenge): `beispiele/b6_intent_pipeline.py` (`normalisiere`, `zahlwort`, `tokenisiere`, `parse_masse`). Status der Regeln: **[B6]** in B6 umgesetzt und getestet, **[neu]** in der App umzusetzen, **[U]** Konvention, die mit Nutzern zu prüfen ist.

## 1 Zweck und Geltung

Das Intent-Modell (Laya, Jev) beantwortet nur typisierte Fragen und liefert keine Werte wie „1,20 m“ oder „35 Grad“ (Recherche 03). Diese Werte liest ausschließlich der deterministische Werteparser. Er arbeitet auf dem Transkript der Spracherkennung (Ziffern oder Zahlwörter, je nach Modell) und liefert für jede Äußerung eine Liste von Messwerten. Welcher Messwert welchem Slot zugeordnet wird, entscheidet die Slotzuordnung (Abschnitt 5) anhand der Slottypen in `intents.yaml`.

Der Parser ist eine Funktion ohne Zustand und ohne Zufall. Gleiche Eingabe ergibt gleiche Ausgabe (Test `test_pipeline_deterministisch`).

## 2 Verarbeitungsschritte

1. **Normalisierung** [B6]: Kleinschreibung, Unicode NFC, ä→ae, ö→oe, ü→ue, ß→ss; Ziffer und Einheit trennen („120cm“ → „120 cm“, „12m²“ → „12 m²“); Satzzeichen entfernen, Dezimaltrenner zwischen Ziffern erhalten.
2. **Tokenisierung** [B6]: Jedes Wort wird Zahl, Einheit oder Wort. Zahlwörter werden morphologisch zerlegt (Abschnitt 3.2).
3. **Maßerkennung** [B6, erweitert]: Die Wortgrammatik (Abschnitt 3.1) erkennt Maßausdrücke in der Reihenfolge der Muster A, B, C, D, F. Die erste passende Alternative gewinnt (geordnete Auswahl wie in einer PEG).
4. **Disambiguierung** [neu]: Regeln D1–D14 (Abschnitt 4).
5. **Slotzuordnung und Plausibilisierung** [neu]: Abschnitt 5.

## 3 Grammatik (EBNF nach ISO/IEC 14977)

Terminale stehen in Anführungszeichen und sind normalisierte Wörter. `ZIFFERN` ist eine nichtleere Folge der Ziffern 0–9. In der **Wortebene** (3.1) trennt das Komma Wörter, in der **Morphemebene** (3.2) trennt es Morpheme innerhalb eines Wortes ohne Leerzeichen. Kommentare stehen in `(* … *)`.

### 3.1 Wortebene

```ebnf
aeusserung        = { element } ;
element           = massausdruck | formatausdruck | modusausdruck | richtungsausdruck
                  | ordinalausdruck | anzahlausdruck | wort ;

(* Maßausdrücke; die Reihenfolge der Alternativen ist die Priorität *)
massausdruck      = muster_a | muster_b | muster_c | muster_f | muster_d ;
muster_a          = zahl , meterwort , unter_hundert_zahl ;          (* "zwei meter sechzig" = 2,60 m; "ein meter fuenf" = 1,05 m [B6] *)
muster_b          = zahl , einheit ;                                   (* "1,20 m", "35 grad", "zwoelf quadratmeter" [B6] *)
muster_c          = einer_wort , unter_hundert_zahl                    (* "eins zwanzig" = 1,20 m, nur ohne folgende Einheit [B6] *)
                  | einer_wort , "null" , einer_wort                   (* "eins null fuenf" = 1,05 m [neu] *)
                  | umgangsmass_kompositum ;                           (* "einsachtzig" = 1,80 m [neu] *)
muster_f          = zahl , "mal" , zahl , [ einheit ] ;                (* "vier mal sechs meter": beide Werte in Meter [neu] *)
muster_d          = zahl ;                                             (* ohne Einheit; Einheit aus dem Slot (D4) [B6: dim "ohne"] *)

formatausdruck    = zahl , "mal" , zahl , [ laengeneinheit ] ;        (* Fliesenformat "sechzig mal sechzig" in cm (D7) [neu] *)
modusausdruck     = relativmarker | absolutmarker ;
relativmarker     = "um" | komparativ | "mehr" | "weniger" ;
absolutmarker     = "auf" | positiv_adjektiv | "haben" ;
komparativ        = "breiter" | "schmaler" | "tiefer" | "hoeher" | "niedriger" | "laenger" | "kuerzer"
                  | "groesser" | "kleiner" | "flacher" | "steiler" | "weiter" | "naeher" ;
positiv_adjektiv  = "breit" | "tief" | "hoch" | "lang" | "gross" | "steil" | "flach" ;
richtungsausdruck = [ "nach" | "richtung" | "an" , "die" ] , himmelsrichtung , [ "seite" | "fassade" ]
                  | relativrichtung ;
himmelsrichtung   = "norden" | "nord" | "noerdlich" | "nordosten" | "nordost" | "osten" | "ost" | "oestlich"
                  | "suedosten" | "suedost" | "sueden" | "sued" | "suedlich" | "suedwesten" | "suedwest"
                  | "westen" | "west" | "westlich" | "nordwesten" | "nordwest" | himmelsrichtung_kompositum ;
himmelsrichtung_kompositum = ( "nordseite" | "ostseite" | "suedseite" | "westseite"
                  | "nordfassade" | "ostfassade" | "suedfassade" | "westfassade" | "sueddach" | "norddach" ) ;
relativrichtung   = "links" | "rechts" | "vorne" | "hinten" | "oben" | "unten" | "mittig" | "mitte" ;
ordinalausdruck   = ordinalwort | ZIFFERN , "." ;
ordinalwort       = "erste" | "ersten" | "zweite" | "zweiten" | "dritte" | "dritten" | "vierte" | "vierten" ;
anzahlausdruck    = zahl , zaehlnomen ;                                (* "drei fenster", "vier steckdosen" [neu] *)
zaehlnomen        = wort ;                                             (* Nomen aus dem Slot "anzahl" des Intents *)

(* Zahlen *)
zahl              = ziffernzahl | kommazahl | bruchzahl | zahlwort | artikelzahl ;
ziffernzahl       = ZIFFERN , [ dezimalteil ] | tausendergruppe ;
dezimalteil       = ( "," | "." ) , ZIFFERN ;                         (* "." nur mit 1 oder 2 Nachkommastellen, sonst D1 *)
tausendergruppe   = ZIFFERN , "." , ZIFFERN ;                         (* genau drei Ziffern nach dem Punkt: Tausender (D1) [neu] *)
kommazahl         = zahlwort , "komma" , ziffernwort , { ziffernwort } ; (* "drei komma fuenf", "null komma eins drei" [B6] *)
bruchzahl         = "halb" | "halbe" | "halben" | "anderthalb" | "eineinhalb" | "zweieinhalb" | "dreieinhalb"
                  | "viertel" | "dreiviertel" ;                        (* viertel, dreiviertel [neu] *)
artikelzahl       = artikel , ( einheit | bruchzahl ) ;               (* "einen meter", "einen halben meter"; sonst kein Zahlwert (D6) [B6] *)
artikel           = "ein" | "eine" | "einen" | "einem" | "einer" | dialektartikel ;
dialektartikel    = "an" | "oan" | "a" ;                               (* bairisch, nur vor Einheit (D8) [neu, U] *)
unter_hundert_zahl = zahl ;                                            (* semantisch: ganze Zahl < 100 *)
einer_wort        = "eins" | "zwei" | "zwo" | "drei" | "vier" | "fuenf" | "sechs" | "sieben" | "acht" | "neun"
                  | "ein" ;
ziffernwort       = "null" | einer_wort ;

(* Einheiten mit Faktor auf SI-Basis (Tabelle 3.3) *)
einheit           = laengeneinheit | flaecheneinheit | winkeleinheit | prozenteinheit | leistungseinheit
                  | energieeinheit | volumeneinheit | temperatureinheit | uwerteinheit ;
meterwort         = "m" | "meter" | "metern" ;
laengeneinheit    = meterwort | "cm" | "zentimeter" | "zentimetern" | "mm" | "millimeter" | "millimetern" ;
flaecheneinheit   = "m2" | "m²" | "qm" | "quadratmeter" | "quadratmetern" ;
winkeleinheit     = "grad" | "°" ;
prozenteinheit    = "prozent" | "%" ;                                  (* [neu] *)
leistungseinheit  = "kw" | "kilowatt" | "kwp" | "kilowatt" , "peak" | "kilowattpeak" ; (* [neu] *)
energieeinheit    = "kwh" | "kilowattstunde" | "kilowattstunden" ;      (* [neu] *)
volumeneinheit    = "l" | "liter" | "litern" | "m3" | "m³" | "kubikmeter" | "kubikmetern" ; (* [neu] *)
temperatureinheit = "k" | "kelvin" ;                                   (* Farbtemperatur [neu] *)
uwerteinheit      = "watt" , "pro" , "quadratmeter" , "kelvin" ;       (* [neu] *)

wort              = ? jedes andere normalisierte Wort ? ;
zahlwort          = ? ein Wort, das die Morphemgrammatik 3.2 vollständig erkennt ? ;
umgangsmass_kompositum = ? ein Wort, das die Morphemgrammatik 3.2 als kompositum_mass erkennt ? ;
```

### 3.2 Morphemebene (innerhalb eines Wortes)

```ebnf
zahlwort_m        = tausender_m , [ hunderter_m ] , [ unter_hundert_m ]
                  | hunderter_m , [ unter_hundert_m ]
                  | unter_hundert_m ;
tausender_m       = [ faktor_m ] , "tausend" ;                         (* bis 999 999 [neu]; B6 bis 999 *)
faktor_m          = hunderter_m , [ unter_hundert_m ] | unter_hundert_m ;
hunderter_m       = [ einer_praefix_m ] , "hundert" ;                  (* "hundert", "zweihundert" [B6] *)
unter_hundert_m   = einer_m | zehn_bis_19_m | zehner_m | einer_praefix_m , "und" , zehner_m ;
einer_m           = "null" | "eins" | "ein" | "zwei" | "zwo" | "drei" | "vier" | "fuenf" | "sechs" | "sieben"
                  | "acht" | "neun" ;
einer_praefix_m   = "ein" | "zwei" | "drei" | "vier" | "fuenf" | "sechs" | "sieben" | "acht" | "neun" ;
zehn_bis_19_m     = "zehn" | "elf" | "zwoelf" | "dreizehn" | "vierzehn" | "fuenfzehn" | "sechzehn"
                  | "siebzehn" | "achtzehn" | "neunzehn" ;
zehner_m          = "zwanzig" | "dreissig" | "vierzig" | "fuenfzig" | "sechzig" | "siebzig" | "achtzig" | "neunzig" ;
kompositum_mass   = ( "eins" | einer_praefix_m ) , ( zehn_bis_19_m | zehner_m | einer_praefix_m , "und" , zehner_m ) ;
                  (* "einsachtzig" = 1,80; "zweifuenfzig" = 2,50; nicht bei "einundzwanzig" (Zahlwort 21 hat Vorrang, D11) *)
```

### 3.3 Einheiten und Faktoren

| Dimension | Einheiten | Basis | Faktoren | Status |
|---|---|---|---|---|
| Länge | mm, cm, m (auch ausgeschrieben) | m | 0,001; 0,01; 1 | [B6] |
| Fläche | m², qm, Quadratmeter | m² | 1 | [B6] |
| Winkel | Grad, ° | ° | 1 | [B6] |
| Anteil | Prozent, % | % | 1 | [neu] |
| Leistung | kW, kWp, Kilowatt (Peak) | kW bzw. kWp | 1 | [neu] |
| Energie | kWh, Kilowattstunden | kWh | 1 | [neu] |
| Volumen | l, Liter, m³, Kubikmeter | m³ | 0,001; 1 | [neu] |
| Farbtemperatur | K, Kelvin | K | 1 | [neu] |
| U-Wert | Watt pro Quadratmeter Kelvin | W/(m²K) | 1 | [neu] |
| Anzahl | Zählnomen des Slots | 1 | 1 | [neu] |

## 4 Disambiguierungsregeln

| Nr. | Regel | Beispiel | Ergebnis | Status |
|---|---|---|---|---|
| D1 | Ein Punkt mit **genau drei** Ziffern danach ist ein Tausendertrenner; ein Punkt mit einer oder zwei Ziffern ist ein Dezimaltrenner (Transkripte schreiben Dezimalzahlen teils englisch). | „2.500 mm“; „1.20m“ | 2,500 m; 1,20 m | [neu]; B6 liest „2.500 mm“ als 0,0025 m |
| D2 | Muster C (Einer + Zahl) gilt nur für Slots der Dimension Länge und nur, wenn keine Einheit folgt. | „eins zwanzig“ im Slot Breite | 1,20 m | [B6] |
| D3 | Ist in Muster C die zweite Zahl kleiner als 10, ist der Wert mehrdeutig: Kandidaten x,0y und x,y0. Liegt nur ein Kandidat im Wertebereich des Slots, gilt er; sonst Rückfrage. | „eins fünf breiter“ | {1,05; 1,50} → Rückfrage | [B6] Rückfrage; Filter über Wertebereich [neu] |
| D4 | Eine Zahl ohne Einheit erhält die Einheit des Slots, wenn sie im Wertebereich liegt. Liegt sie nur als Zentimeterwert im Bereich eines Längenslots, wird sie als cm gelesen und in der Interpretationsanzeige ausgewiesen. | „Dachneigung auf fünfunddreißig“; „Brüstung auf achtzig“ | 35°; 0,80 m | [neu]; B6 liefert dim „ohne“ |
| D5 | Eine Ziffer oder Ordinalzahl direkt nach einem Raumnomen gehört zur Referenz, nicht zum Wert. | „Kinderzimmer 2 auf 3,20 m“ | Referenz Nr. 2; Wert 3,20 m | [B6] Referenz; Ausschluss aus den Werten [neu] |
| D6 | Unbestimmte Artikel sind nur vor Einheit oder Bruch eine Zahl. | „Mach ein Fenster“; „einen halben Meter“ | kein Wert; 0,50 m | [B6] |
| D7 | „a mal b“ mit Einheit am Ende gibt beiden Faktoren diese Einheit; ohne Einheit im Slot „format“ gilt cm. | „vier mal sechs Meter“; „sechzig mal sechzig“ | (4 m; 6 m); 60 × 60 cm | [neu]; B6 liest nur den zweiten Wert |
| D8 | Dialektartikel „an“, „oan“, „a“ zählen als „ein“, aber nur vor einer Einheit. | „an Meter hoch“ | 1,00 m | [neu, U] |
| D9 | Komparativ oder „um“ macht den Wert relativ; das Vorzeichen folgt der Richtung des Komparativs. Bei Widerspruch („auf zwanzig Zentimeter breiter“) gewinnt der Komparativ, die Interpretationsanzeige zeigt beide Lesarten. | „zwanzig Zentimeter schmaler“ | −0,20 m relativ | [B6] Komparativ; Widerspruchsanzeige [neu] |
| D10 | Relative Angaben ohne Zahl („etwas“, „ein bisschen“, „deutlich“) ergeben keinen Wert. Die Stärke kommt aus der score-Frage `s.staerke`; die Schrittweite je Stufe steht in der Konfiguration. Ergebnis ist immer eine Vorschau. | „a bissl größer“ | Stufe 1 → Vorschau | [neu] |
| D11 | Ein vollständiges Zahlwort hat Vorrang vor dem Kompositum-Maß. | „einundzwanzig“ | 21, nicht 1,21 | [neu] |
| D12 | Himmelsrichtungen werden auf acht Sektoren abgebildet; „Garten-“ und „Straßenseite“ sind keine Himmelsrichtung, sondern Referenzen auf Grundstückskanten aus dem State-JSON. | „an die Ostseite“; „zur Gartenseite“ | O; Referenz | [neu] |
| D13 | Werte außerhalb des Wertebereichs des Slots werden nie abgeschnitten, sondern zurückgefragt; physikalisch unmögliche Werte (Länge ≤ 0) werden abgelehnt. | „Kniestock auf zwölf Meter“ | Rückfrage | [neu] |
| D14 | Mehrere Werte gleicher Dimension werden in Satzreihenfolge den Slots des Intents in Katalogreihenfolge zugeordnet (z. B. `breite`, dann `hoehe`); bleibt eine Zuordnung offen, folgt eine Rückfrage. | „ein Fenster eins zwanzig breit und eins vierzig hoch“ | breite 1,20 m, hoehe 1,40 m | [neu] |

## 5 Slotzuordnung

1. Für jeden Slot des erkannten Intents mit Quelle `parser` werden die Messwerte passender Dimension gesammelt (Slottyp in `intents.yaml`, Abschnitt `slot_typen`).
2. Messwerte ohne Einheit (Muster D) werden nach D4 und D5 zugeordnet oder verworfen.
3. Jeder Wert wird gegen `wertebereich` des Slots geprüft (D13).
4. Das Ergebnis ist ein Slotwert mit Herkunft: `quelle_text` (Textausschnitt), `muster`, `einheit_herkunft` (`text`, `slot` oder `konvention`), `mehrdeutig` und `kandidaten`.
5. Ein Pflichtslot ohne Wert löst die Rückfrage des Intents aus (`rueckfrage` in `intents.yaml`).

## 6 Referenzfälle

Die Spalte „B6 heute“ ist das tatsächliche Ergebnis von `parse_masse` am 27.09.2026 (Python 3.11.15). Die Spalte „Soll“ ist die Vorgabe für die App.

| Eingabe | Soll | B6 heute | Regel |
|---|---|---|---|
| eins zwanzig | 1,20 m (C) | 1,20 m (C) | D2 |
| einen Meter zwanzig | 1,20 m (A) | 1,20 m (A) | – |
| 1,20 m / 1.20m / 120 cm | 1,20 m (B) | 1,20 m (B) | D1 |
| 35 Grad / 35° / fünfunddreißig Grad | 35° (B) | 35° (B) | – |
| zwölf Quadratmeter / 12 m² | 12 m² (B) | 12 m² (B) | – |
| drei komma fünf Meter | 3,50 m (B) | 3,50 m (B) | – |
| anderthalb Meter / einen halben Meter | 1,50 m / 0,50 m | 1,50 m / 0,50 m | D6 |
| zweihundertzwanzig Zentimeter | 2,20 m | 2,20 m | – |
| eins fünf (Slot Breite) | Rückfrage {1,05; 1,50} | mehrdeutig 1,05 | D3 |
| ein Meter fünf | 1,05 m (A) | 1,05 m (A) | – |
| einsachtzig | 1,80 m | kein Wert | 3.2 `kompositum_mass` |
| eins null fünf | 1,05 m | 1,00 m mehrdeutig und 5 ohne Einheit | Muster C |
| 2.500 mm | 2,50 m | 0,0025 m | D1 |
| 1.250 mm | 1,25 m | 0,0013 m | D1 |
| tausendzweihundert Millimeter | 1,20 m | kein Wert | 3.2 `tausender_m` |
| fünfunddreißig (Slot Dachneigung) | 35° | 35, ohne Einheit | D4 |
| zehn Prozent / 5 kWp / sechs Kilowatt | 10 % / 5 kWp / 6 kW | Zahl ohne Einheit | 3.3 |
| vier mal sechs Meter | (4 m; 6 m) | 4 ohne Einheit; 6 m | D7 |
| an Meter (bairisch) | 1,00 m | kein Wert | D8 |
| Mach ein Fenster | kein Wert | kein Wert | D6 |

## 7 Prüfung

Die Datei wird mit `spezifikation/pruefe_sprache.py` geprüft: Die EBNF-Blöcke werden in Regeln zerlegt; jede Regel ist genau einmal definiert, jedes verwendete Nichtterminal ist definiert, Klammern und Anführungszeichen sind ausgeglichen.
