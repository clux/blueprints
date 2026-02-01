# Factorio Benchmark Results

**Platform:** linux-x86_64
**Factorio Version:** 2.0.73
**Date:** 2026-02-01

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
| clux-q2-blades-v1 | 0.537 | 0.389 | 4.977 | 1863 | 86918 | 0.00% |
| clux-q2-blades-v1-heatsep | 0.415 | 0.283 | 5.016 | 2407 | 67287 | 29.18% |
| clux-q2-blades-v3 | 0.378 | 0.246 | 4.938 | 2647 | 61200 | 42.02% |
| clux-q2-blades-v5-miniheat | 0.370 | 0.233 | 4.361 | 2701 | 59965 | 44.95% |
| clux-q2-blades-v5 | 0.364 | 0.225 | 4.544 | **2745** | 58999 | 47.32% |

## Conclusion