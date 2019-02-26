x = 58375
r = -1
while x > 10:
    d = x % 10
    x //= 10
    if d > r:
        r = d
print(r)