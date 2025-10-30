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
| recyclers | 0.279 | 0.201 | 1.370 | 3579 | 9050 | 0.00% |
| car-voider-particleson | 0.255 | 0.149 | 0.965 | 3915 | 8274 | 9.38% |
| car-voider | 0.232 | 0.128 | 1.022 | **4312** | 7512 | 20.48% |

## Conclusion