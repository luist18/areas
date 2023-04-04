#!/bin/bash

wget -O toolchain.tar.gz https://github.com/stnolting/riscv-gcc-prebuilt/releases/download/rv32i-4.0.0/riscv32-unknown-elf.gcc-12.1.0.tar.gz

mkdir /opt/riscv

tar -xzf toolchain.tar.gz -C /opt/riscv/

export PATH=$PATH:/opt/riscv/bin
