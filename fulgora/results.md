# Factorio Benchmark Results

**Platform:** linux-x86_64
**Factorio Version:** 2.0.72
**Date:** 2025-10-23

## Scenario
* Each save was tested for 32400 tick(s) and 5 run(s)

## Results
| Metric            | Description                           |
| ----------------- | ------------------------------------- |
| **Mean UPS**      | Updates per second – higher is better |
| **Mean Avg (ms)** | Average frame time – lower is better  |
| **Mean Min (ms)** | Minimum frame time – lower is better  |
| **Mean Max (ms)** | Maximum frame time – lower is better  |

| Save | Avg (ms) | Min (ms) | Max (ms) | UPS | Execution Time (ms) | % Difference from base |
|------|----------|----------|----------|-----|---------------------|------------------------|
| fulgora-island-3-bench-6s5s | 1.294 | 0.882 | 17.794 | 772 | 209711 | 0.00% |
| fulgora-island-4-bench-5s5s | 1.257 | 0.920 | 17.942 | 795 | 203665 | 2.97% |
| fulgora-island-5.14-bench-7s7s | 0.994 | 0.683 | 11.147 | 1006 | 160946 | 30.30% |
| fulgora-island-5.19b-bench-7s7s | 0.968 | 0.617 | 12.538 | 1033 | 156777 | 33.77% |
| fulgora-island-5.20b-bench-8s8s | 0.962 | 0.619 | 12.640 | **1039** | 155916 | 34.50% |

## Conclusion