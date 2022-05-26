n=10
fib = lambda x: 1 if x in [0,1] else fib(x-1) + fib(x-2)

for i in range(n):
    print(fib(i))
