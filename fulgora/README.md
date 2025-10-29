# Fulgora Q2 Islands

q2 science island that exports enough aquilo components for equal parts q2 cryo and q1 promethean for aquilo.

**[youtube](https://www.youtube.com/watch?v=NC3HJzfywt4) for version 3**

## [Train Island 5.22](./fulgora-train5.txt)
full redesign. best performing variant. 240.9/s
34% more UPS than V3. See the [v5-island-bench folder](./v5-island-bench).

- 4 silos per island (down from 20)
- multi stage blueprint to help avoid placement errors
- common items/fluids produced on the main bus and shared across halves
  * quartered cryos for sulfur/sulfuric (shared sulfuric + light oil)
  * quartered oil, light oil, heavy oil
  * halved supercaps EMs
  * halved number of battery cryos
  * halved number of ice chem plants (shared water)
  * quartered engine production
  * quartered pipe production
- wagon tech for sorting (less silo costs, but worse symmetry)
- wagon balancing clock (quadrants have uneven q1 component pull)
- shared bus tick clock (40 tick)
- design around holmium ore; don't recycle more if we don't need it, but run train more if we run low on q2 exports.
- input gated stack inserters on q2 holmium, electrolyte, batteries, accumulators, super*
- sorting optimization
  * less shuffling Q1 scrap, most taken from first wagon
  * less blue/lds crushing activity (we wasted outputs before, lds circuit was also wrong)
  * all q2 waste circuit filtered into one car per quadrant
  * almost zero wakelists around q2 silos, output/input circuitry for battery
  * heavily tuned limits/circuitry around q2 silos
  * significantly less thrown away useful items, significantly lower train requirements
  * corner recycler on q2 fills up on q2 iron/copper/circuits during slow periods to allow longer hibernation
- 18 trash cars per island (down from 31 in v4 or 43 in v3) => ~3200 cars per hour. most fully utilized.
- `~350` stack inserters, `~80` bulk. lots of inserter selector logic to minimize inserters. (saved ~130 total)
- science EM clock; global tick output clock (green) + global lead follower input clock (red)
- belt latch on accumulators (overbeaconed so they are active 60% of the time)
- hibernation system; hibernating when 15m since last science request && export buffers full
- tank buffer removal everywhere except science (wakelists bad when the tank was full - science clock avoids this)
- dynamic train schedule (with new network name)
  * regular service; train tuned to 8s + 8s wait
  * rapid service; train tuned to 5s +5s wait (for more holmium for q2 holmium plate export)
- dynamic export system; capture excess q2 holmium if sufficient holmium fluid (will speed up the train until buffers are full)
- scrap use: dynamic based holmium exports; Q1 120k/m rapid, 109k/m regular. Q2 35k/m rapid, 32k/m regular
- holmium export; excess 625 q2 plates/m on rapid / 0 q2 plates/m on regular

caveats:
- not compatible with v3/v4. tear down old island and replant.
- do not replant vehicles twice (unless you remove the vehicles from stage blueprints; bots will get stuck, and some vehicles become non-insertable)
- plant blueprints in order with playtime between them (not editor paused)
  * inserters need to target correct vehicles before beacons or rails are placed
  * inserters by RF needs to target assembler before car is placed
  * beacons need to activate before ingredient flow in Q2 (otherwise accumulator EMs/supers can get soft-locked)
- for the last 9% performance consider using @MRX8024 UPS mods; [disable-vehicle-particles](https://mods.factorio.com/mod/disable-vehicles-particles) + [disable-vehicles](https://mods.factorio.com/mod/disable-vehicles). the particle mod is the most advantageous.

fixing broken deploys / softlocks:
- low batteries or science components?
  * inserters to outer cars stuck "waiting for train"? temporarily remove rails UNDER the car to force target the car.
  * accumulator inserters stuck? replant them. can happen if started before beacons were down with modules.
  * accumulator EMs stuck with 15 output? we pull 16 at a time, and this should always work unless belt backs up, and the belt should never back up with the given measurement. can also happen with early lack of beacons.
- bots stuck placing vehicles over other vehicles? manually fix, pick up bots, or place a yellow chest and cancel building requests. replant vehicles from blueprint (ideally not triggering the same issue)
- out of cars? car production cannot exceed [84 cars/m](https://factoriolab.github.io/spa/list?z=eJw1jzEOgzAMRW-TIUNFCrQsXpxWYqASQ09A1QHUQBsQlRh89n5XYbD.c75tORONtirMk6w3HVU2Q3aaKkSBOOnD0US6ZNbCBtx2WAEO4CNAe3wLyNX6AgqFGVAqLHvz528F4kaHoLnOQIdU10nHpDHpQRf084K7wjtSaUKItMlZcuFGeBMGDMK18Cgche.Cq3ArfDBd6PGvLDOv6UEs3l7NSs79ABXuRJE_&v=11) (roughly 5000 cars/h) with the single 8 beacon engine assembler (do not lower train waits too much - it doesn't help much beyond rapid == 5s + 5s anyway)
- some science EMs not outputting? replant the beacon next to the output inserter to force re-targeting of the buffer tank.
- q2 silos full / stuck? usually a symptom of the battery issues above. should go away after fixing those.

special thanks to @MRX8024 for beta testing + feedback + many improvements.

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

- 240.8 q2 em science / s
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
