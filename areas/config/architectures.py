ARCHITECTURES = {
    'arm': {
        'compiler': 'aarch64-linux-gnu-gcc',
        'emulator': 'qemu-aarch64-static',
    },
    'riscv': {
        'compiler': 'riscv32-unknown-linux-gnu-gcc',
        'emulator': 'qemu-riscv32-static',
    },
    'riscv64': {
        'compiler': 'riscv64-linux-gnu-gcc',
        'emulator': 'qemu-riscv64-static',
    }
}
