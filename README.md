# Mayon Kernel for Xiaomi sweet device

A performance-optimized, and thermally balanced custom kernel for the Redmi Note 10 Pro / Max (`sweet` / `sweetin`).

## Features

* **KernelSU & SUSFS**: Built-in KernelSU (v0.9.5) with non-GKI manual hooks and SUSFS (v1.5.5) for kernel-level root and mount hiding.
* **Modern LLVM Toolchain**: Compiled with **Neutron Clang** using Link-Time Optimization (**ThinLTO**).
* **WALT Scheduler Tuning**: Asymmetric 2+6 (Kryo 470 Gold/Silver) energy-aware load tracking with dynamic input boost.
* **Optimized Governors**: `schedutil` tuned with disabled artificial I/O wait boosting for better battery and lower heat.
* **Memory & Storage**: ZRAM with ZSTD compression, balanced page reclaim, and `mq-deadline` I/O scheduler.
* **Networking**: BBR TCP congestion control with FQ packet scheduling by default.

For an in-depth breakdown of our tuning decisions, read the [Comprehensive Architecture and Kernel Tuning Analysis](ARCHITECTURE.md).

## Flashing

1. Download `mayon-kernel-sweet.zip` from [Releases](../../releases) or GitHub Actions artifacts.
2. Boot into recovery (TWRP / OrangeFox).
3. Flash the zip and reboot.

## Building

This repository uses GitHub Actions for automated, clean compilation.

### Automated CI
Trigger the workflow via the **Actions** tab by selecting **build kernel** > **Run workflow**.

### Local Compilation Prerequisites
* **Toolchain**: Neutron Clang (via `antman`)
* **Cross-compilers**: `aarch64-linux-gnu-`, `arm-linux-gnueabi-`
* **Defconfig**: `vendor/sdmsteppe-perf_defconfig` merged with `arch/arm64/configs/vendor/sweet.config`

## Credits & Acknowledgements

* [LineageOS](https://github.com/LineageOS) team for the device kernel source tree
* [KernelSU](https://github.com/tiann/KernelSU) by `@tiann` & contributors
* [SUSFS (susfs4ksu)](https://gitlab.com/simonpunk/susfs4ksu) by `@simonpunk`
* [Neutron Toolchains](https://github.com/Neutron-Toolchains) by `@beakthoven`
* [AnyKernel3](https://github.com/osm0sis/AnyKernel3) by `@osm0sis`
