# Fulgora Q2 Islands

q2 science island that exports enough aquilo components for equal parts q2 cryo and q1 promethean for aquilo.

**[youtube](https://www.youtube.com/watch?v=NC3HJzfywt4) for version 3**

## [Train Island 5.13](./fulgora-train5.txt)
full redesign.

- 4 silos per island (down from 20)
- common items/fluids produced on the main bus and shared across halves
  * quartered cryos for sulfur/sulfuric (shared sulfuric + light oil)
  * quartered oil, light oil
  * halved supercaps EMs
  * halved number of battery cryos
  * halved number of ice chem plants (shared water)
  * quartered engine production
  * quartered pipe production
- wagon tech for sorting
- shared bus tick clock
- design around holmium ore; don't recycle more if we don't need it (less q1 recyclers)
- input gated stack inserters on q2 holmium, electrolyte, batteries
- recycler optimization (4 less Q1 recyclers, but they run more frequently)
- sorting optimization
  * less shuffling Q1 scrap, most taken from first wagon
  * less blue/lds crushing activity (we wasted outputs before, lds circuit was also wrong)
  * all q2 waste circuit filtered into one car per quadrant
  * almost zero wakelists around q2 silos, output/input circuitry for battery
  * better silo limits for battery silo
  * significantly less thrown away useful items
- 20 trash cars per island (down from 31 in v4 or 43 in v3) => ~3800 cars per hour
- 350 stack inserters, 66 bulk. lots of inserter selector logic to minimize inserters. (saved ~130 total)
- 49 recyclers (down 10)
- science clocking;
  * global output clock on science (green wire)
  * global lead follower clock on science input (red wire)
- belt latch on accumulators (overbeaconed so they are active 60% of the time)
- hibernation system; hibernating when 9m since last science request && export buffers full
  * caveat; checks one quadrant only, if you pull q1 holmium without q2 holmium it might not hibernate (but this should only happen for rocket prod)
  * hibernation wire sent down to bus to shut down bus inserter networks
- tank buffer removal everywhere except science (wakelists bad when the tank was full)
- dynamic train schedule (with new network name)
  * regular service; train tuned to 6s + 7s wait (max for sustained battery uptime)
  * rapid service; train tuned to 5s +5s wait (increased holmium ore for q2 holmium export)
- scrap; now Q1 109k/m and Q2 32k/m (12% reduction)

caveats:
- not compatible with v3/v4. tear down old island and replant.
- ensure accumulator inserters are going. sometimes they need replanting (only planted in stage 3 atm to try to counteract it)
- ensure accumulator EMs are not output stuck initially (we pull 16 at a time, and this should always work unless belt backs up, and the belt should never back up with the measurement)
- do NOT place any vehicles twice. ensure no bots are stuck trying to place any more vehicles (otherwise the vehicles might not be insertable and everything will backlog)
- car production cannot exceed [84 cars/m](https://factoriolab.github.io/spa/list?z=eJw1jzEOgzAMRW-TIUNFCrQsXpxWYqASQ09A1QHUQBsQlRh89n5XYbD.c75tORONtirMk6w3HVU2Q3aaKkSBOOnD0US6ZNbCBtx2WAEO4CNAe3wLyNX6AgqFGVAqLHvz528F4kaHoLnOQIdU10nHpDHpQRf084K7wjtSaUKItMlZcuFGeBMGDMK18Cgche.Cq3ArfDBd6PGvLDOv6UEs3l7NSs79ABXuRJE_&v=11) (roughly 5000 cars/h) with the single 8 beacon engine assembler (do not lower train waits too much, check usage)

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
