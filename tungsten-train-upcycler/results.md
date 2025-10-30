# Factorio Benchmark Results

**Platform:** linux-x86_64
**Factorio Version:** 2.0.72
**Date:** 2025-10-30

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
| recyclers | 0.531 | 0.436 | 2.515 | 1881 | 28702 | 0.00% |
| car-voider-particleson | 0.425 | 0.214 | 1.919 | 2350 | 22970 | 24.96% |
| car-voider | 0.352 | 0.161 | 1.680 | **2839** | 19019 | 50.91% |

## Conclusion