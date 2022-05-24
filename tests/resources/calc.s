.text
.global calc
.type calc, %function

calc :
	stp X29, X30, [X29, -16]!

loop:
	cbz X0, end
	ldr S9, [X1], #4
	ldr S10, [X2], #4
	ldr X11, [X3], #1
	cmp X11, #43
	b.eq mais
	cmp X11, #42
	b.eq vezes
	cmp X11, #80
	b.eq pot

normal:
	fcvtns X9, S9
	str X9, [X4], #4
	sub X0, X0, #1
	b loop

mais:
	fadd S9, S9, S10
	b normal

vezes:
	fmul S9, S9, S10
	b normal

pot:
	bl power
	b normal

end:
	ldp X29, X30, [X29]
	ret
