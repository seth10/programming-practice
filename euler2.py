fib = [1, 2]
while fib[-1] < 4000000:
    fib.append(fib[-2] + fib[-1])
print sum(filter(lambda i: i%2==0, fib[:-1]))
