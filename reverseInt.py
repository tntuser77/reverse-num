def reverseInt(x):
    y = x
    z = 0
    while x > 0:
        a = x % 10
        z = z * 10 + a
        x = x // 10
    return z