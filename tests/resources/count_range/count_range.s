.text
.global count_range
count_range:
mv t1, zero
loop:
beq zero, a1, done
flw ft0, 0(a0)
flt.s t1, fa2, ft0
beqz t1, continue
flt.s t1, ft0, fa3 
beqz t1, continue
addi t1, t1, 1
continue:
addi a1, a1, -1
addi a0, a0, 4 
j loop
done:
mv a0, t1
ret