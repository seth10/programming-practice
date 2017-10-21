s = 0
for i in range(1000):
    if 0 in [i%3, i%5]:
        s += i
print s
