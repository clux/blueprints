# hiwashi / 火鷲

unstacked prometheum gathering ship in version order.

## Current Active Versions
6 is experimental, but is slightly better.

### [Hiwashi 6.2](./hiwashi6.txt)
1571 tons. 216k eggs.

- 36 tons lighter than hiwashi 5.
- added 6 inline bays, removed 6 bays on side
- carbonic shifted left with beacons (killed ~5 tons)
- better carbonic belt weave (-5 tons)
- 492.4km/s now top speed. (+0.8km/s)
- cut 250MW power (down 750MW -> 500MW); unused, some accumulators to even out
- cut 3 rocket beacons (3.3k/m still), 1fuel beacon
- shifted fuel in
- cut some turrets around center, shifted tesla top right
- -5 tiles by oxide
- more likely to get through 216k eggs now
- circuit layout tweaks

Probably last iteration of this type of ship I make. Diminishing return on speed improvement now.
Biggest improvement at this point is to have more cryos to take advantage of peak promethean grabbing in the deep field, but that would require a huge redesign.

If I come back to this, then big redesign to try:
- 6 cryos (to never allow promethean chunk belts to back up) and maintain current width would be ideal
- reduce rockets more. with legendary rails and low quality launchers, we can reduce to 2.9k/m rocket usage. with belt buffer we could scale to 2.5k/m given explosive 31.
- try to get 1 ship to produce the equivalent of 1 full belt (240/s) of promethean science (current 9/8 ratio feels bad).
  * this would require 720k science per trip over 50m (`720*1000science/(50*60s) = 240/s`) which means (incidentally) 240k eggs (`720/3=240`)

might try this in 2.1 since apparently there are breaking changes planned.

### [Hiwashi 5](./hiwashi5.txt)

1607 tons. 215k eggs.
**the one from the youtube video**.

- 6 tiles shorter in height than hiwashi 4
- moved venting up to the top. had to shift mid-section a little to the left
- extra weight reduction around carbonic
- lower quality turrets for less particle action and less duplicate targeting.

## Legacy Versions
All gathered in the [legacy.txt](./legacy.txt) blueprint.
Rough changelog between them here for posterity

### Hiwashi 4
1614 tons

- carbonic minor improvements.

### Hiwashi 3
1640 tons. ~210k eggs.

- DI carbonic + smelting. clocked collectors.
- astroid scaled for astroid prod 30. add beacons on ice if lower.
- speculative early load with prom, aborts if not researching

### Hiwashi 2
1800ish tons. 205k eggs.

- dropped central sushi belt
- closer venting (underneath)
- minimised carbonic site for EXPL31 and dropped lasers

### Hiwashi 1
~2000 tons. ~200k eggs.

- side spoilers (holes) for aerodynamic efficiency (less weight => more speed)
- documented all combinators

### Hiwashi 0
~2150 tons. ~195k eggs.
Basically Hobbit's 3-grab Pella but with;

- 3 extra grabbers on each side to supplement early gathering.
- token system shifted to fulgora/nauvis for less wait time.
- removes lasers

Uses horrible weaving were the lasers were to get nuclear fuel in place and the new belt of prom.
Bumped tick time by 40s and added bonus egg cycle.
