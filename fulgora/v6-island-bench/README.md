# v6 island bench

compares the two variants of v6 to v5.

overview;

![overview](./overview.png)

entities;

![entity summary](./entity-summary.png)

run variance;
![box plot](./boxplot.png)


## Miner Effect
tests run at MP20k
this makes a marginal difference and reduces the amount of updates a silo receives (it is only bumped whenever the silo or inserters hit it, so it effectively clock the miners)

it was tested earlier here (follow the red graph);
![miner-clock](./miner-clock.png)

basically a linear decrease in mining time as you increase the inactivity of the miners.

note that not clocking is worse (10k-ON) even when the mining prod is higher than a low clock (vs 6k-2tick)
old chart version ate my titles. 20k uses 10ticks, 50k uses 20ticks.
marginal improvements beyond MP 20k.
