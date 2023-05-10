.text
.global pfunc

# float afunc(float x);
pfunc: # P(x) = x + 1
      li       t0, 1
      fcvt.s.w ft0, t0
      fadd.s   fa0, fa0, ft0
      # Modificar registos que esta sub-rotina pode alterar (a0, ..., ft0, ...)
      fcvt.s.w ft0, zero
      fmv.s    ft1, ft0
      fmv.s    ft2, ft0
      fmv.s    ft3, ft0
      fmv.s    ft4, ft0
      fmv.s    ft5, ft0
      fmv.s    ft6, ft0
      fmv.s    ft7, ft0
      fmv.s    ft8, ft0
      fmv.s    ft9, ft0
      fmv.s    ft10, ft0
      fmv.s    ft11, ft0

      fmv.s    fa1, ft0
      fmv.s    fa2, ft0
      fmv.s    fa3, ft0
      fmv.s    fa4, ft0
      fmv.s    fa5, ft0
      fmv.s    fa6, ft0
      fmv.s    fa7, ft0

      mv       t0, zero
      mv       t1, zero
      mv       t2, zero
      mv       t3, zero
      mv       t4, zero
      mv       t5, zero
      mv       t6, zero

      mv       a0, zero
      mv       a1, zero
      mv       a2, zero
      mv       a3, zero
      mv       a4, zero
      mv       a5, zero
      mv       a6, zero
      ret