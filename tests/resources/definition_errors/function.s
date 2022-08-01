.text
.global func
.type func, %function

// multiply arg0 with arg1 and sum arg2
func:
    mul x0, x0, x1
    add x0, x0, x2
    ret
