import math
def polar():
    z = a + b
    r = math.hypot(a, b)
    th = math.atan2(b, a)
    return r, th



a = int(input())
b = int(input())
print(polar())