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
| hobbit-21x-230k-q1 | 1.692 | 1.457 | 24.846 | 591 | 91337 | 0.00% |
| abuc-3x-119k | 1.321 | 1.143 | 23.537 | 757 | 71325 | 28.06% |
| mrx-1.5-119k-3x-quadrants | 1.201 | 1.032 | 17.342 | 832 | 64835 | 40.88% |
| clux-v3-8x-115k-6s5s | 1.139 | 0.791 | 17.665 | 877 | 61530 | 48.44% |
| clux-v5.22-115k-8s8s | 0.897 | 0.577 | 11.601 | **1115** | 48420 | 88.64% |

## Conclusion