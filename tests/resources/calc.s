.text
.global calc
.type calc, %function

calc:
        cmp     w0, 0
        ble     .L10
        stp     x29, x30, [sp, -64]!
        mov     x29, sp
        stp     x19, x20, [sp, 16]
        sxtw    x20, w0
        mov     x19, 0
        stp     x21, x22, [sp, 32]
        mov     x21, x1
        mov     x22, x2
        stp     x23, x24, [sp, 48]
        mov     x23, x3
        mov     x24, x4
        b       .L6
.L3:
        cmp     w0, 42
        beq     .L14
        cmp     w0, 80
        beq     .L15
.L4:
        str     s2, [x24, x19, lsl 2]
        add     x19, x19, 1
        cmp     x20, x19
        beq     .L16
.L6:
        ldrb    w0, [x22, x19]
        movi    v2.2s, #0
        ldr     s0, [x21, x19, lsl 2]
        ldr     s1, [x23, x19, lsl 2]
        cmp     w0, 43
        bne     .L3
        fadd    s2, s0, s1
        str     s2, [x24, x19, lsl 2]
        add     x19, x19, 1
        cmp     x20, x19
        bne     .L6
.L16:
        ldp     x19, x20, [sp, 16]
        ldp     x21, x22, [sp, 32]
        ldp     x23, x24, [sp, 48]
        ldp     x29, x30, [sp], 64
        ret
.L14:
        fmul    s2, s0, s1
        b       .L4
.L15:
        fcvt    d0, s0
        fcvt    d1, s1
        bl      power
        fcvt    s2, d0
        b       .L4
.L10:
        ret