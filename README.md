# Mayon Kernel for Xiaomi sweet device

A performance-optimized, thermally balanced custom for Xiaomi sweet device.

## Features
This kernel has been tuned to maximize sustained performance and UI fluidity without compromising battery life. Key optimizations include:

* **WALT Scheduler Tuning**: Asymmetric topology fixes for the 2+6 (Cortex-A76/A55) architecture.
* **Modern LLVM/Clang Toolchain**: Compiled with Neutron Clang, leveraging advanced ThinLTO.
* **KernelSU-Next**: Integrated legacy hooks for systemless root support.
* **Other**: Will be updated soon.


## Architectural Overview
If you want to understand the exact design philosophies, tuning decisions, and hardware limits of this kernel, please read the [Comprehensive Architecture and Kernel Tuning Analysis](ARCHITECTURE.md). 


## Building
This repo utilizes GitHub Actions for automated, clean compilation.
