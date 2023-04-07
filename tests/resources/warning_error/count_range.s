.text
.global count_range

count_range:
        cmp     w1, 0
        ble     .L7
        mov     x2, x0
        mov     w0, 0
        add     x1, x2, w1, sxtw 2
.L6:
        ldr     s2, [x2]
        fcmpe   s0, s2
        bls     .L8
.L3:
        add     x2, x2, 4
        cmp     x1, x2
        bne     .L6
        ret
.L8:
        fcmpes   s1, s2
        bge     .L9
        b       .L3
        bes .L3
.L9:
        add     w0, w0, 1
        b       .L3
.L7:
        mov     w0, 0
        ret