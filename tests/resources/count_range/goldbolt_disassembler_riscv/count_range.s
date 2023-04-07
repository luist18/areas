.text
.global count_range

count_range:
        ble     a1,zero,.L7
        slli    a1,a1,2
        mv      a5,a0
        add     a3,a0,a1
        li      a0,0
.L6:
        flw     fa5,0(a5)
        addi    a5,a5,4
        fge.s   a4,fa5,fa0
        beq     a4,zero,.L3
        fle.s   a4,fa5,fa1
        add     a0,a0,a4
.L3:
        bne     a5,a3,.L6
        ret
.L7:
        li      a0,0
        ret