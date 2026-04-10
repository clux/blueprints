# Aquilo Blades

aquilo blueprints designed and benchmarked for 8 belts of prom science using q2 cryogenic.
q2 holmium prerequisite (assumed to come from something like the [fulgora islands](../fulgora)).

## [Fuel Blade V9](./fuel-v9.txt)
Fuel blade supplying cryo + quantum blade with hot fluro and RF.
Enough for 16 lane equivalent prom science.

- 880*3 hot fluro/s (extendible to 4x without modifications)
- ~50/s RF

Intended to be the only thing that needs oil and water on aquilo.
Clocks;
- LF on hot fluro + production latched operation
- Latch on amonia to ensure ice is going fully or not at all
- belt latch by measuring one tile of belt for outputs elsewhere.


## [Cryo V9](./science-v9.txt)

Contains the 15 beacon variant described in the **[blade update video](https://www.youtube.com/watch?v=8A15Uhcs6Ak)**.

## [Cryo V7/V8](./science-v8.txt)

Contains 3 Q2 blades described in the **[video](https://www.youtube.com/watch?v=0XLs3IbV2Ic)**.

- V7 Twin Blade 484/s :: 14 beacon main twin blade in video, most performant.
- V7 Twin Blade 503/s :: 15 beacon twin variant blade variant, performs slightly worse.
- V8 Solo Blade 242/s :: solo blade variant, performs slightly worse.

See the [v7-v8 cryo benchmark results](/aquilo/cryo-v7-v8-bench/README.md), or the video, for numbers.

## [Quantum 9.0](./quantum-v9.txt)

- back pressure detection to auto-shutdown

accidentally revved version number +2 in video so now it's standard
talked about in the
[blade update video](https://www.youtube.com/watch?v=8A15Uhcs6Ak)

## [Quantum 7.0](./quantum-v7.txt)
Optimization of V6;

- improved beaconing by `Geist` (`9` -> `12` beacons, so production increased from 4500/m -> 5400/m)
- crazy alternating car swing clock by `abuc` with hibernation system and backpressure toggle
- rocket parts sushied for `-300` heat pipes (i also helped :smile:)

## [Quantum 6.0](./quantum-v6.txt)

The quantum car blade from the **[video](https://www.youtube.com/watch?v=wCnDNrBy8-0)**.
