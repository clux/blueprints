# Factorio Benchmark Results

**Platform:** linux-x86_64
**Factorio Version:** 2.0.76
**Date:** 2026-04-09

## Scenario
* Each save was tested for 108000 tick(s) and 20 run(s)

## Results
| Metric            | Description                           |
| ----------------- | ------------------------------------- |
| **Mean UPS**      | Updates per second – higher is better |
| **Mean Avg (ms)** | Average frame time – lower is better  |
| **Mean Min (ms)** | Minimum frame time – lower is better  |
| **Mean Max (ms)** | Maximum frame time – lower is better  |

| Save | Avg (ms) | Min (ms) | Max (ms) | UPS | Execution Time (ms) | % Difference from base |
|------|----------|----------|----------|-----|---------------------|------------------------|
| abuc-v1-12x-baseline | 0.508 | 0.345 | 9.022 | 1967 | 219523 | 0.00% |
| abuc-v3-12x | 0.397 | 0.207 | 8.830 | 2520 | 171402 | 28.08% |
| clux-twin-v7-6x_14beacon | 0.400 | 0.235 | 6.731 | 2499 | 172867 | 26.99% |
| clux-twin-v9-6x_15beacon-q5silo | 0.382 | 0.221 | 7.368 | **2615** | 165160 | 32.92% |
| geist-4x | 0.396 | 0.218 | 7.481 | 2527 | 170910 | 28.45% |

## Conclusion