.text
.global afunc

afunc:	li a3, 7
	li a6, 2
	fcvt.s.w fa4, a6
	fcvt.s.w fa1, a3
	fdiv.s fa1, fa1, fa4
	li a4, 1
	fcvt.s.w fa2, a4
	li a5, 5
	fcvt.s.w fa3, a5
loop:	beq a1, zero, fim
	flw ft1, 0(a0)
	fabs.s ft1, ft1
	fle.s t0, ft1, fa3
	beq t0, a4, less
	fmul.s ft0, ft1, ft1
	fadd.s ft0, ft0, fa2
	fmul.s ft2, fa1, ft1
	fdiv.s ft0, ft2, ft0
	fsw ft0, 0(a2)
	addi a0, a0, 4
	addi a2, a2, 4
	addi a1, a1, -1
	j loop
less:	jal pfunc
	fadd.s ft0, ft1, fa0
	fsw ft0, 0(a2)
	addi a0, a0, 4
	addi a2, a2, 4
	addi a1, a1, -1
	j loop
fim:	fmv.s fa0, ft0
	ret