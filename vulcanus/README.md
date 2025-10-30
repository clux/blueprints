# Vulvanus Tungsten Upcyclers

**Beats silo+recycler based upcycling by >30% when disabling car particles.**

**[blueprint](./train-voider-1.txt)**

## Setup
Scaled for mining prod >5700.
Highly specific mining patch setup. You'll probably need to adjust the train/rail setup in your base. This is a mostly a POC to show it's good, but it also reflects my actual use on my 3 best patches.

Works best with @MRX8024 UPS mods; [disable-vehicle-particles](https://mods.factorio.com/mod/disable-vehicles-particles) + [disable-vehicles](https://mods.factorio.com/mod/disable-vehicles) (the particle one being the important one).

## Benchmark

![train setup vulcanus](./train-voider.png)

comparing to abuc's old ore recyclers tuned to 7k for tungsten.

![recycler setup vulcanus](./recycler.png)

### Caveats
- including car production costs but excluding q5 rocketfuel costs (get from fulgora islands) and molten iron
- excluding space platform costs on recycler setup

### Benchmark Results
![ups breakdown](./results.png) + [report](./results.md).

### breakdowns
recycler setup:
![recycler breakdown](recycler-7k-breakdown.png)

trains without particles (mods on)
![train breakdown](train-voider-breakdown.png)

trains with particles (no mods)
![train breakdown](train-voider-particles-breakdown.png)
