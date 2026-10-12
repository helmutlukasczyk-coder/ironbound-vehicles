# IRONBOUND — Fahrzeuge: einkopierbare Stellen

Alle 16 SVG-Karten liegen im Repo `helmutlukasczyk-coder/ironbound-vehicles` auf `main`. Sämtliche Bild-URLs unten verwenden **raw.githubusercontent.com**.

## 1. Hauptregelwerk — Appendix A

Den folgenden Block **nach der vollständigen Seite „Additional Unit Catalogues“ und unmittelbar vor `# Appendix B — Weapons and Equipment`** einfügen. Der bereits vorhandene `\page` vor Appendix B eröffnet die erste neue Seite; der neue Block endet mit `\page` für Appendix B. Bestehende Inhalte nicht ersetzen.

```markdown
{{pageNumber,auto}}
{{footnote APPENDIX A | GROUND VEHICLES}}

## Ground Vehicle Catalogue
<span id="ground-vehicle-catalogue"></span>

{{wide

Each row identifies one exact configuration. Complete profiles are in **IRONBOUND — Unit Records, Ground Vehicles**.

| Vehicle | Variant | Tons | Intro | Move | Role | EV | CV (M C-bills) |
|:--|:--|--:|--:|:--|:--|--:|--:|
| AC/2 Carrier | Standard | 60 | 2520 | 3t | Fire Support | 403 | 1.0864 |
| Bulldog Medium Tank | Standard | 60 | 2673 | 4t | Brawler | 605 | 1.2728 |
| Condor Heavy Hover Tank | Standard | 50 | 2564 | 8h | Skirmisher | 653 | 1.289 |
| Demolisher Heavy Tank | Mk. II | 80 | 2823 | 3t | Brawler | 981 | 2.079 |
| Hetzer Wheeled Assault Gun | Standard | 40 | 2887 | 4w | Brawler | 574 | 0.664 |
| J. Edgar Light Hover Tank | Standard | 25 | 2722 | 11h | Scout | 544 | 0.72925 |
| LRM Carrier | Standard | 60 | 2470 | 3t | Fire Support | 833 | 1.872 |
| Manticore Heavy Tank | Standard | 60 | 2575 | 4t | Brawler | 993 | 2.6408 |
| Pegasus Scout Hover Tank | Standard | 35 | 2791 | 8h | Skirmisher | 640 | 0.865725 |
| Saladin Assault Hover Tank | Standard | 35 | 2942 | 8h | Skirmisher | 596 | 0.911625 |
| Savannah Master Hovercraft | Standard | 5 | 3025 | 13h | Scout | 215 | 0.091667 |
| Schrek PPC Carrier | Standard | 80 | 2813 | 3t | Fire Support | 935 | 3.8295 |
| Scorpion Light Tank | Standard | 25 | 2807 | 4t | Brawler | 306 | 0.327083 |
| SRM Carrier | Standard | 60 | 2470 | 3t | Brawler | 816 | 1.9328 |
| Striker Light Tank | Standard | 35 | 3006 | 5w | Fire Support | 564 | 0.563315 |
| Vedette Medium Tank | Standard | 50 | 2943 | 5t | Brawler | 475 | 0.72575 |

**Move** lists base Ground Move in inches followed by movement type: **t** tracked, **w** wheeled, **h** hover. Sprint is Ground Move ×1.5, rounded up. Use the record for base TMM, initiative, armor, structure, and weapons.

**Variant:** Standard means the base configuration. Demolisher Mk. II is the 2823 configuration; it is not the later Demolisher II.

}}

\page

{{pageNumber,auto}}
{{footnote APPENDIX A | VEHICLE CAMPAIGN VALUES}}

## Vehicle Campaign Values

### Encounter Value

For these sixteen vehicle profiles, baseline EV equals the published standard **Battle Value 2 at Gunnery 4 / Piloting 5**, without rounding to hundreds.

Apply IRONBOUND's existing crew skill adjustments and round the resulting EV up:

| Crew | Gunnery / Piloting | EV multiplier |
|:--|:--:|--:|
| Green | 5 / 6 | ×0.8 |
| Regular | 4 / 5 | ×1.0 |
| Veteran | 3 / 4 | ×1.3 |
| Elite | 2 / 3 | ×1.6 |

EV is a campaign budgeting baseline. It is not recalculated from converted damage, armor, or TIC count.

### Catalogue Value

CV is the exact listed base purchase price. **CV (M C-bills)** expresses that price in millions; retain all shown digits.

Apply market, availability, condition, acquisition, and resale procedures normally. A catalogue entry does not include free crew, transport, or deployment permission.

\column

### Vehicle Operating Costs

The daily operating cost for these standard ground vehicles is:

**10 C-bills × vehicle tonnage per campaign day.**

This rate is separate from the standard hired crew's **500 C-bills per campaign day**. Recruiting that crew costs **10,000 C-bills**, as stated in Vehicle Support.

A 25-ton Scorpion therefore costs **250 C-bills/day** in vehicle upkeep plus **500 C-bills/day** in crew wages: **750 C-bills/day** while crew and vehicle are maintained.

A package that expressly includes crew wages must not charge the same wage twice. Repairs, replacement ammunition, transport, and acquisition remain separate expenses under their applicable procedures.

### Profile Use

Use only the exact record's installed weapons, mounting arcs, ammunition bins, and equipment. A turretless hull does not gain a turret firing arc.

Apply date, faction, eligible pool, and local availability restrictions. Vehicle Support and each mission's permissions remain necessary for company deployment.

These values adopt BV2 and stock purchase prices as IRONBOUND campaign references; their balance after tactical conversion remains subject to playtesting.

\page
```

## 2. Unit Records — Fahrzeugkapitel und Karten

Den folgenden Block **nach dem Assault-Mech-Abschnitt und unmittelbar vor dem Seitenkopf `{{pageNumber,auto}}` / `{{footnote PILOT DIRECTORY | RECRUITMENT}}` des Pilot Directory** einfügen. Der vorhandene Seitenwechsel eröffnet die Fahrzeugseite; der Block endet mit dem Seitenwechsel für Pilot Directory. Die vorhandene `.unitRecordPage`-CSS wird weiterverwendet.

```markdown
{{pageNumber,auto}}
{{footnote PART V | GROUND VEHICLES}}

# Ground Vehicles {#ground-vehicle-records}

These records cover sixteen standard Inner Sphere ground vehicle configurations.

Use the exact printed configuration and the Ground Vehicle Combat rules in the main rulebook. Company deployment requires Vehicle Support and mission permission.

EV uses standard BV2 at Gunnery 4 / Piloting 5. CV is the base purchase price before market and condition adjustments. Vehicle upkeep and crew wages are separate.

Declare and write the actual miniature footprint before deployment. The diagram is a damage tracker; it does not define scale or facing arcs.

Black circles track armor; red circles track structure. A turretless vehicle has four locations; a turreted vehicle has five. Each ammunition row is one physical bin, shared by its listed TICs.

## Record Index

| Vehicle | Configuration | EV | CV (C-bills) |
|:--|:--|--:|--:|
| AC/2 Carrier | Standard | 403 | 1,086,400 |
| Bulldog Medium Tank | Standard | 605 | 1,272,800 |
| Condor Heavy Hover Tank | Standard | 653 | 1,289,000 |
| Demolisher Heavy Tank | Mk. II | 981 | 2,079,000 |
| Hetzer Wheeled Assault Gun | Standard | 574 | 664,000 |
| J. Edgar Light Hover Tank | Standard | 544 | 729,250 |
| LRM Carrier | Standard | 833 | 1,872,000 |
| Manticore Heavy Tank | Standard | 993 | 2,640,800 |
| Pegasus Scout Hover Tank | Standard | 640 | 865,725 |
| Saladin Assault Hover Tank | Standard | 596 | 911,625 |
| Savannah Master Hovercraft | Standard | 215 | 91,667 |
| Schrek PPC Carrier | Standard | 935 | 3,829,500 |
| Scorpion Light Tank | Standard | 306 | 327,083 |
| SRM Carrier | Standard | 816 | 1,932,800 |
| Striker Light Tank | Standard | 564 | 563,315 |
| Vedette Medium Tank | Standard | 475 | 725,750 |

\page

{{unitRecordPage
![AC/2 Carrier Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-AC2-Carrier-Standard.svg)
}}

\page

{{unitRecordPage
![Bulldog Medium Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Bulldog-Standard.svg)
}}

\page

{{unitRecordPage
![Condor Heavy Hover Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Condor-Standard.svg)
}}

\page

{{unitRecordPage
![Demolisher Heavy Tank Mk. II](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Demolisher-Mk-II.svg)
}}

\page

{{unitRecordPage
![Hetzer Wheeled Assault Gun Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Hetzer-Standard.svg)
}}

\page

{{unitRecordPage
![J. Edgar Light Hover Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-J-Edgar-Standard.svg)
}}

\page

{{unitRecordPage
![LRM Carrier Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-LRM-Carrier-Standard.svg)
}}

\page

{{unitRecordPage
![Manticore Heavy Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Manticore-Standard.svg)
}}

\page

{{unitRecordPage
![Pegasus Scout Hover Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Pegasus-Standard.svg)
}}

\page

{{unitRecordPage
![Saladin Assault Hover Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Saladin-Standard.svg)
}}

\page

{{unitRecordPage
![Savannah Master Hovercraft Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Savannah-Master-Standard.svg)
}}

\page

{{unitRecordPage
![Schrek PPC Carrier Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Schrek-PPC-Carrier-Standard.svg)
}}

\page

{{unitRecordPage
![Scorpion Light Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Scorpion-Standard.svg)
}}

\page

{{unitRecordPage
![SRM Carrier Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-SRM-Carrier-Standard.svg)
}}

\page

{{unitRecordPage
![Striker Light Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Striker-Standard.svg)
}}

\page

{{unitRecordPage
![Vedette Medium Tank Standard](https://raw.githubusercontent.com/helmutlukasczyk-coder/ironbound-vehicles/main/IRONBOUND-Vedette-Standard.svg)
}}

\page

```

## 3. Inhaltsverzeichnis der Unit Records

Bei den Mech-Abschnitten vor Pilot Directory ergänzen; die vorhandene Formatierung des Inhaltsverzeichnisses beibehalten:

```markdown
[Ground Vehicles](#ground-vehicle-records)
```

## Profilabgleich

- Panzerung je Location: TW-Wert ÷4, normal gerundet; Mindestwert 1 bei vorhandener Panzerung.
- Struktur je Location: TW-Fahrzeugstruktur (`ceil(Tonnen/10)`) ÷3, normal gerundet; mindestens 1.
- Waffen: Override/Destiny-Konvertierung; identische Waffen nur innerhalb derselben Location gruppiert. TIC-Basis maximal 5 und Maximum maximal 14; größere einzelne Waffen auf eigenen TICs.
- Standard-Bins bleiben einzeln erhalten. Verbrauch: ein Schuss pro abgefeuerter Waffe, kompatible TICs teilen den Vorrat. Scorpion und Condor haben je einen halben MG-Bin mit 100 Schuss; Vedette einen vollen mit 200.
- Trefferdiagramme, Motive Damage, Crew Stunned und sechs Crew-Injury-Boxen folgen dem aktuellen IRONBOUND-Regelwerk. Sechs Treffer bedeuten **incapacitated**, nicht automatisch Tod.
- Keine VTOLs, Infantry, Battle Armor oder Aerospace Fighter in dieser Serie.
- EV und Unterhalt folgen der gewählten Kampagnenentscheidung: **BV2 G4/P5** sowie **10 C-bills/Tonne/Tag**, Crew separat.

Die TIC-Aufteilung wurde aus den Standardkonfigurationen mit Override erstellt. EV ist noch nicht durch IRONBOUND-Spieltests kalibriert. Quellen und Umrechnungsdaten sind zusätzlich im GitHub-Repo dokumentiert.
