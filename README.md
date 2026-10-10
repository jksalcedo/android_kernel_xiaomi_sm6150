# Mayon Kernel for Xiaomi sweet device

![GitHub Release](https://img.shields.io/github/v/release/jksalcedo/android_kernel_xiaomi_sm6150?include_prereleases)

A performance-optimized, and thermally balanced custom kernel for the Redmi Note 10 Pro / Max (`sweet` / `sweetin`).

## Features

* **BakaSU & SuSFS**: Built-in BakaSU (v4.2.0-rc3) with
  non-GKI manual hooks and SuSFS (v2.3.0) for root integration
  and mount hiding.
* **CPU Scheduling**: WALT load tracking enabled, with scheduler
  capacity-margin adjustments for the Snapdragon 732G's
  six efficiency cores and two performance cores.
* **CPU Frequency Scaling**: `schedutil` selected as the kernel's
  default governor. ROM settings may override governor selection
  and tuning.
* **Memory**: ZRAM with LZ4 and ZSTD compression support, plus
  balanced anonymous/file-page reclaim. The ROM selects the active
  compressor and swap size.
* **Storage**: SCSI blk-mq enabled by default, with mq-deadline
  selected for single-hardware-queue devices. Boot parameters and
  ROM settings may override defaults.
* **Networking**: BBR selected as the default TCP congestion-control
  algorithm and FQ as the default queue discipline. Runtime settings
  may be overridden by the ROM.
* **Charging**: Device-specific voltage and current limits, with
  reduced routine charging-driver logging.
* **Android Compatibility**: `CAP_CHECKPOINT_RESTORE` backport
  addressing the reported Chromium/AppZygote startup failure
  on VoltageOS 6.1 / Android 17.
* **Optional Input Boost**: Configurable CPU frequency floors applied
  briefly after input events. Requires nonzero boost frequencies;
  effectiveness and power consumption depend on ROM configuration.

## Flashing

1. Download the `zip` from [Releases](../../releases) or GitHub Actions artifacts.
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
* [Baka-SU (ReSukiSU)](https://github.com/Baka-SU/BakaSU) team for root
* [SUSFS (susfs4ksu)](https://gitlab.com/simonpunk/susfs4ksu) by `@simonpunk`
* [Neutron Toolchains](https://github.com/Neutron-Toolchains) by `@beakthoven`
* [AnyKernel3](https://github.com/osm0sis/AnyKernel3) by `@osm0sis`
