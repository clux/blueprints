# Factorio Benchmark Results

**Platform:** linux-x86_64
**Factorio Version:** 2.0.72
**Date:** 2025-10-28

## Scenario
* Each save was tested for 10800 tick(s) and 5 run(s)

## Results
| Metric            | Description                           |
| ----------------- | ------------------------------------- |
| **Mean UPS**      | Updates per second – higher is better |
| **Mean Avg (ms)** | Average frame time – lower is better  |
| **Mean Min (ms)** | Minimum frame time – lower is better  |
| **Mean Max (ms)** | Maximum frame time – lower is better  |

| Save | Avg (ms) | Min (ms) | Max (ms) | UPS | Execution Time (ms) | % Difference from base |
|------|----------|----------|----------|-----|---------------------|------------------------|
| v3-8x-115k-6s5s | 1.279 | 0.859 | 17.531 | 782 | 69043 | 0.00% |
| v4-8x-115k-5s5s | 1.246 | 0.926 | 18.538 | 802 | 67289 | 2.61% |
| v5.22-115k-8s8s | 0.951 | 0.599 | 11.755 | **1051** | 51377 | 34.38% |

## Conclusion