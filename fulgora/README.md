# Fulgora Q2 Islands

q2 science island that exports enough aquilo components for equal parts q2 cryo and q1 promethean for aquilo.

**[youtube](https://www.youtube.com/watch?v=NC3HJzfywt4) for version 3**

## [Train Island 4.0](./fulgora-train4.txt)
minor tweaks and optimizations from feedback. cars and inserters are breaking changes.

- tweaked q2 trashing to use less inserters and circuits with thresholds
- removed 9 cars by q2 (less inserters now)
- removed random combinator by q1 superconductors via MRX8024
- added very slow q5 holm export. unoptimized, mostly for fun. remove chest + inserter if unneeded.

if migrating from 3->4;
- remove ALL inserters that target cars from top/bottom q2 recycling area (from q2 silos)
- filter out trains/tanks/cars from the blueprint
- force plant blueprint over
- remove 9 extranuous cars on the track not targeted by any inserters
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
