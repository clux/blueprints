# Gleba Blades

gleba blueprints designed for constant megabase promethean research.

## [Agri V5](./agri-v5.txt)

Contains the V5 blades shown in the **[video](https://www.youtube.com/watch?v=7nK6PrSScFc)**.

- 66k/m agri science (4 blades +15% freshness overhead - cut a row/unit as appropriate)

Usage:
- 2 stage blueprints, place in order with time in between (if in editor)
- Bootstrap:
  * Place pentapod blueprint to get eggs from network to bootstrap
  * Bootstrap central nutrients (either via nutrient circuit, or manually first time)
  * Turn on bootstrap circuit to send nutrients up the top lane
  * Wait for everything to start
  * Disable nutrient bootstrap

Spoilage circuits can help cleanup. See the video's second half for instructions.

### Benchmark
Benchmark results
Ran a ~265k/m benchmark comparing

- 4x of these blades
- 3x4 of Konage blades
- 10x of Hobbit variant blades

and results gave basically

- Hobbit; baseline
- clux; +23% perf
- Konage; +24% perf

using a 4 run test over 108000 ticks (`30m`)

| save_name | run_index  | execution_time_ms | avg_ms | min_ms | max_ms  | effective_ups | percentage_improvement | ticks | factorio_version | platform |
| --------- | ---------- | ----------------- | ------ | ------ | ------- | ------------- | ---------------------- | ----- | ---------------- | -------- |
|    hobbit |         0  |     59954.903  |  0.555 |  0.400 |  7.352  |  1801.353928    |            0.000000 | 108000   |        2.0.76 |  linux-x86_64 |
|    hobbit |         2  |     59885.511  |  0.554 |  0.381 |  7.400  |  1803.441236    |            0.000000 | 108000   |        2.0.76 |  linux-x86_64 |
|    hobbit |         1  |     59857.247  |  0.554 |  0.396 |  7.208  |  1804.292804    |            0.000000 | 108000   |        2.0.76 |  linux-x86_64 |
|    hobbit |         3  |     59662.428  |  0.552 |  0.397 |  6.767  |  1810.184460    |            0.000000 | 108000   |        2.0.76 |  linux-x86_64 |
|    clux-v5 |        2  |     48503.789  |  0.449 |  0.312 |  5.789  |  2226.630171    |           24.111222 | 108000   |        2.0.76 |  linux-x86_64 |
|    clux-v5 |        3  |     48136.296  |  0.446 |  0.308 |  5.710  |  2243.629215    |           24.111222 | 108000   |        2.0.76 |  linux-x86_64 |
|    clux-v5 |        1  |     48030.456  |  0.445 |  0.307 |  5.900  |  2248.573280    |           24.111222 | 108000   |        2.0.76 |  linux-x86_64 |
|    clux-v5 |        0  |     48190.737  |  0.446 |  0.303 |  5.987  |  2241.094590    |           24.111222 | 108000   |        2.0.76 |  linux-x86_64 |
|    konage  |        1  |     47953.821  |  0.444 |  0.275 |  6.659  |  2252.166725    |           24.375754 | 108000   |        2.0.76 |  linux-x86_64 |
|    konage  |        0  |     48461.496  |  0.449 |  0.270 |  6.454  |  2228.573381    |           24.375754 | 108000   |        2.0.76 |  linux-x86_64 |
|    konage  |        2  |     47991.045  |  0.444 |  0.288 |  6.860  |  2250.419844    |           24.375754 | 108000   |        2.0.76 |  linux-x86_64 |
|    konage  |        3  |     48045.600  |  0.445 |  0.274 |  6.261  |  2247.864529    |           24.375754 | 108000   |        2.0.76 |  linux-x86_64 |


sanitize output;

- hobbit :: INFO belt::sanitize::parser:   - produced: normal-agricultural-science-pack (2586823.8)
- clux :: INFO belt::sanitize::parser:   - produced: normal-agricultural-science-pack (2645905.8)
- konage :: INFO belt::sanitize::parser:   - produced: normal-agricultural-science-pack (2671439.8)
