#!/bin/bash

apt-get -y install autoconf automake autotools-dev curl python3 libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev ninja-build git

cd /usr/app

git clone https://github.com/riscv/riscv-gnu-toolchain

cd riscv-gnu-toolchain

./configure --prefix=/opt/riscv32 --with-arch=rv32gc --with-abi=ilp32d
make linux

export PATH=$PATH:/opt/riscv32/bin

cd /usr/app

rm -rf riscv-gnu-toolchain
