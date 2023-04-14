.text
.global transform

transform:
    lbu t1, (a0)
    sb t1, 1(a0)

end:
    ret