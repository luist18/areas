.data
cincos: .quad 0x5555555555555555

.text
.global power
.type power,"function"

// s0 = a
// s1 = b
// Calcula a^b (b>=0)
power:
    mov    x0, 1
    scvtf  s2, x0
    fabs   s1, s1
    fcvtnu w1, s1
_L1:
    cbz  w1, _L2
    fmul s2, s2, s0
    sub  w1, w1, 1
    b    _L1
_L2:
    fmov s0, s2
    // Altera x0 a x7 e x9 a x15
    ldr  x0, =cincos
    ldr  x1, [x0]
    mov  x2, x1
    mov  x3, x1
    mov  x4, x1
    mov  x5, x1
    mov  x6, x1
    mov  x7, x1
    mov  x9, x1
    mov  x10, x1
    mov  x11, x1
    mov  x12, x1
    mov  x13, x1
    mov  x14, x1
	mov  x15, x1
    ret
