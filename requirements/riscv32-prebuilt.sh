#!/bin/bash

wget -O toolchain.tar.gz https://github.com/luist18/areas/releases/download/areas-toolchain-riscv32/toolchain.tar.gz

mkdir /opt/riscv

tar -xzf toolchain.tar.gz -C /opt/riscv/

rm -rf toolchain.tar.gz

# Add to PATH inside Dockerfile or Dockerfile.dev
# echo "export PATH=$PATH:/opt/riscv/bin" >>~/.bashrc
