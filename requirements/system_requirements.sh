#!/bin/bash

apt update

# general dependencies
apt install -y curl python3 python3-pip nano

# arm64 compiler and emulator
apt install -y gcc-aarch64-linux-gnu qemu-user-static

# risc-v compiler
apt install -y gcc-riscv64-linux-gnu
