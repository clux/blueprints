# Fulgora Q2 Islands

q2 science island that exports enough aquilo components for equal parts q2 cryo and q1 promethean for aquilo.

**[youtube](https://www.youtube.com/watch?v=NC3HJzfywt4) for version 3**

## [Train Island 5.2](./fulgora-train5.txt)
full redesign.

- 4 silos per island (down from 20)
- reuse of fluid production on main bus
  * halved cryos for sulfur/sulfuric
  * halved oil, light oil
  * halved supercaps EMs (but streamlined)
  * halved number of battery cryos
  * halved number of ice chem plants (sharing water now)
  * halved engine production
  * quartered pipe production
- wagon tech for sorting
- bus optimization, shared output tick clock
- input gated stack inserters on q2 holmium, electrolyte, batteries
- recycler optimization (4 less Q1 recyclers, but they run more frequently)
- sorting optimization
  * less shuffling Q1 scrap, most taken from first wagon
  * less blue/lds crushing activity (we wasted outputs before, lds circuit was also wrong)
  * less wakelists chaos around silos, output/input circuitry for battery
  * significantly less thrown away items
- 24 trash cars per island (down from 31 in v4 or 43 in v3) => 5600 cars per hour
- 391 stack inserters, 66 bulk. lots of inserter selector logic to minimize inserters. (saved ~100 total)
- output clock on science (from precise production ratio)
- cheap input clock on science (one network per EM, not the best, but doesn't deadlock)
- belt latch on accumulators (overbeaconed so they are active 60% of the time)
- filtered stack inserters for Q3+ overflow from foundaries and cars
- hibernation system; hibernating when 9m since last science request && export buffers full (checking one quadrant only)
- tank buffer removal everywhere except science (wakelists bad when the tank was full)


## [Train Island 4.1](./fulgora-train4.txt)
minor tweaks on 3 and optimizations from feedback. cars and inserters are breaking changes.

- tweaked q2 trashing to use less inserters and circuits with thresholds
- removed 11 cars by q2 (less inserters now). => 6000 cars destroyed per hour.
- removed random combinator by q1 superconductors via MRX8024
- added very slow q5 holm export. unoptimized, mostly for fun. remove chest + inserter if unneeded.
- repositioned bus cars (not all were active despite showing up, and didn't notice because of leeway)
- removed unnecessary inserters around the bus
- made blueprint 3 stage to avoid stuck tanks; 1. crosshair, 2. everything except beacons, 3. everything except vehicles

if migrating from 3 -> 4.1;
- remove ALL inserters that target cars from top/bottom q2 recycling area (from q2 silos)
- remove ALL cars
- remove the middle bus area between the rails and between the chests with cars
- filter out trains/tanks from the blueprint (leave cars)
- force plant blueprint over
- fix stuck bots and repopulate bot networks if necessary

## [Train Island 3.0](./fulgora-train3.txt)

- 240.4 q2 em science / s
- 4.75k q2 holm / m (250/m excess for exports)
- 59 recyclers
- 4 quality miners
- 5 sorting silos per quadrant
- 124k q1 scrap / m
- 37k q2 scrap / m
- 8000 cars / hour
- Train setup; 6s wait + 5s wait

### Notes on operating
I didn't do multi-stage blueprints for this so some things can be set-up wrong on initial plant;

1. If science is blocked, replant beacon next to the tank
2. If center-south Q5 scrap inserter is looping scrap on the belt, replant belt to make the inserter target the tank

Additionally, some users reported microstarvations over extremely long periods with 11s train wait. You may need to set 10s (5+5).
