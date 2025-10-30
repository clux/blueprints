# Factorio Benchmark Results

**Platform:** linux-x86_64
**Factorio Version:** 2.0.72
**Date:** 2025-10-30

## Scenario
* Each save was tested for 10800 tick(s) and 3 run(s)

## Results
| Metric            | Description                           |
| ----------------- | ------------------------------------- |
| **Mean UPS**      | Updates per second – higher is better |
| **Mean Avg (ms)** | Average frame time – lower is better  |
| **Mean Min (ms)** | Minimum frame time – lower is better  |
| **Mean Max (ms)** | Maximum frame time – lower is better  |

| Save | Avg (ms) | Min (ms) | Max (ms) | UPS | Execution Time (ms) | % Difference from base |
|------|----------|----------|----------|-----|---------------------|------------------------|
| recyclers | 0.279 | 0.200 | 1.395 | 3580 | 9050 | 0.00% |
| car-voider | 0.232 | 0.120 | 0.978 | **4312** | 7513 | 20.45% |

## Conclusion