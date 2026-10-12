# IRONBOUND — Ground Vehicle Records

Sixteen generated SVG records, 277 × 183 mm, matching the IRONBOUND Mech record layout. `IRONBOUND-Vehicles-Einfuegen.md` contains copyable Homebrewery insertion blocks using raw GitHub URLs.

## Rules and conversion

Tactical reference: supplied BattleTech: Override v5.3r1, MechWarrior: Destiny conversion rules, and the supplied IRONBOUND main rules. Weapons retain stock counts and mounting locations. Armor is TW/4, nearest integer; structure is TW tank structure/3, nearest integer; minimum one for a present location. Ground Move uses cruising MP; Sprint is ceil(1.5 × Ground). Base TMM sets the initiative bracket and is not reduced by motive damage.

TICs are newly grouped for IRONBOUND using Override limits, not transcriptions of the Dropbox cards. Missile TICs contain only like-type launchers. Damage is displayed as base + M dice (maximum). Ammunition capacities remain stock rounds per bin; spend one round per firing weapon. Only standard ammunition is included. Weapon destruction disables its entire TIC under IRONBOUND.

EV adopts standard BV2 at G4/P5 without rounding to hundreds. Apply IRONBOUND skill multipliers separately. CV adopts the stock catalogue price listed below. Vehicle operating costs are 10 C-bills/ton/day plus the separately hired shared crew's 500 C-bills/day; crew recruitment is 10,000. These campaign choices do not establish post-conversion playtest balance.

The diagram is schematic. Declare the actual miniature footprint before deployment and record it on the card. No passenger/cargo capability is conferred by this record. At six crew injury hits, the crew is incapacitated; survival follows Chapter 10. Classic engine/turret-lock statuses are omitted because the supplied IRONBOUND critical table does not generate them.

## Sources and adopted campaign values

Standard construction facts (armor, mass, engine, cruising MP, weapons, bins, introduction year) were checked against MegaMek's public mm-data stock BLK definitions. These are fan-maintained transcriptions of published BattleTech configurations. BV2 and stock CV were cross-checked with Master Unit List where indexed, and BattleTechWiki's published-price references otherwise. Conflicting older CV listings are not mixed into the catalogue: Condor 1,289,000; Demolisher Mk. II 2,079,000; Pegasus 865,725. Hetzer uses current MUL BV2 574 rather than the older 565 listing. AC/2 Carrier CV 1,086,400 uses the compiled stock-price reference; it was not independently confirmed against an accessible current MUL price field.

- [Master Unit List](https://www.masterunitlist.info/)
- [MegaMek mm-data](https://github.com/MegaMek/mm-data) — respect its upstream licensing and attribution for source data.
- [BattleTechWiki](https://www.sarna.net/wiki/Main_Page)
- [Override](https://dfawargaming.com/)

| Configuration | EV (G4/P5) | Adopted CV (C-bills) | Stock construction source |
|:--|--:|--:|:--|
| AC/2 Carrier Standard | 403 | 1,086,400 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/AC2%20Carrier.blk) |
| Bulldog Medium Tank Standard | 605 | 1,272,800 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Bulldog%20Medium%20Tank.blk) |
| Condor Heavy Hover Tank Standard | 653 | 1,289,000 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Condor%20Heavy%20Hover%20Tank.blk) |
| Demolisher Heavy Tank Mk. II | 981 | 2,079,000 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Demolisher%20Heavy%20Tank%20%28Mk.%20II%29.blk) |
| Hetzer Wheeled Assault Gun Standard | 574 | 664,000 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Hetzer%20Wheeled%20Assault%20Gun.blk) |
| J. Edgar Light Hover Tank Standard | 544 | 729,250 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/J.%20Edgar%20Light%20Hover%20Tank.blk) |
| LRM Carrier Standard | 833 | 1,872,000 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/LRM%20Carrier.blk) |
| Manticore Heavy Tank Standard | 993 | 2,640,800 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Manticore%20Heavy%20Tank.blk) |
| Pegasus Scout Hover Tank Standard | 640 | 865,725 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Pegasus%20Scout%20Hover%20Tank.blk) |
| Saladin Assault Hover Tank Standard | 596 | 911,625 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Saladin%20Assault%20Hover%20Tank.blk) |
| Savannah Master Hovercraft Standard | 215 | 91,667 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Savannah%20Master%20Hovercraft.blk) |
| Schrek PPC Carrier Standard | 935 | 3,829,500 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Schrek%20PPC%20Carrier.blk) |
| Scorpion Light Tank Standard | 306 | 327,083 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Scorpion%20Light%20Tank.blk) |
| SRM Carrier Standard | 816 | 1,932,800 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/SRM%20Carrier.blk) |
| Striker Light Tank Standard | 564 | 563,315 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Striker%20Light%20Tank.blk) |
| Vedette Medium Tank Standard | 475 | 725,750 | [BLK](https://github.com/MegaMek/mm-data/blob/main/data/mekfiles/vehicles/3039u/Vedette%20Medium%20Tank.blk) |

## Rebuild and verification

`stock-data.json` preserves extracted stock facts; `profiles.json` records converted values, groups and bins. Run `python3 build_cards.py` with Inkscape installed to regenerate cards and local PNG previews. Generation checks weapon-count preservation, TIC limits, ammunition links and per-location pip totals. All sixteen SVGs were parsed, rendered and visually inspected. No EV balance playtest was performed.

Unofficial fan project; BattleTech and MechWarrior belong to their respective rights holders.
