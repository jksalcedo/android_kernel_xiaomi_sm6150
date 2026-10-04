# Mayon Kernel Architecture & Tuning Guide

This document explains the core optimizations and tuning choices made for the Snapdragon 732G (Sweet) device. The goal is to keep it simple: maximum UI smoothness, better battery life, and controlled thermals.

## 1. CPU Scheduling (WALT)
The Snapdragon 732G has 2 "Big" performance cores and 6 "Little" efficiency cores. We tuned the WALT scheduler specifically for this 2+6 layout. 
* **Strict Core Migration:** We raised the migration thresholds so that background tasks (like syncing or music playing) stay strictly on the Little cores. The power-hungry Big cores are only woken up when you actually need them (like gaming or heavy scrolling).
* **Touch Boost:** Instead of blindly locking the CPU to max frequency every time you touch the screen (which drains battery and causes heat), we use dynamic input boosting. It gives just enough power to render the screen smoothly without overheating.

## 2. CPU Governor (schedutil)
The CPU frequencies are managed by the `schedutil` governor, which scales the processor speed up and down based on real-time load.
* **No I/O Wait Boosting:** We disabled aggressive "I/O wait boosting". Normally, Android artificially spikes the CPU frequency every time it reads from storage. On fast UFS storage, this just causes unnecessary heat. Disabling it saves battery without hurting speed.

## 3. Thermal Management (Hardware LMH)
Instead of relying on slow software thermal engines that cause sudden lag spikes when the phone gets warm, we rely on **Hardware LMH (Limits Management Hardware)**.
* The hardware controls thermals directly, reacting in microseconds. It feathers the voltage smoothly, so if the phone gets hot during intense gaming, it will gently throttle down rather than suddenly lagging.

## 4. Memory & ZRAM
To keep more apps open in the background without aggressive app killing (LMK), we use ZRAM (compressed memory).
* **ZSTD Compression:** We recommend using the ZSTD algorithm for ZRAM. It compresses data much better than older algorithms like LZ4, effectively giving your phone more "virtual" RAM.
* **Smart Reclaim:** The kernel is tuned to preserve your app caches in RAM, so switching between recent apps is instant and doesn't force the phone to reload data from the slower storage.

## 5. Storage (I/O Scheduler)
We use the `mq-deadline` I/O scheduler. It is specifically designed for parallel solid-state storage (like the UFS 2.1 chip in the 732G). 
* It prioritizes "reads" (loading apps) over "writes" (saving data in the background), making app launch times noticeably faster.

## 6. GPU Tuning (Adreno 618)
The GPU shares heat and power with the CPU, so keeping it efficient is critical.
* **Deep Idle:** The GPU is forced to completely drop its voltage and go to sleep when the screen is on but static (like reading an article).
* **AdrenoBoost:** When the GPU detects a sudden heavy workload (like a 3D game rendering), it temporarily boosts itself to prevent frame drops, then immediately drops back down when the load passes.

## 7. Network Optimizations
* **TCP BBR:** We use Google's BBR network algorithm instead of the default CUBIC. BBR massively reduces lag and "bufferbloat" on weak 4G/LTE or congested Wi-Fi networks, making downloads and ping times much more stable.
* **TCP Fast Open:** Enabled for faster connections to modern websites and APIs, eliminating a round-trip of latency when loading web pages.

## 8. Compiler & Toolchain
The kernel is built using **Neutron Clang** (the latest LLVM compiler) instead of legacy GCC.
* **ThinLTO:** We use Link-Time Optimization (ThinLTO), which allows the compiler to analyze the entire kernel at once and strip out dead code. This makes the final kernel smaller, faster, and more efficient.
