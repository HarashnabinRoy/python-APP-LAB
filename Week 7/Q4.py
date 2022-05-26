dummy = tuple(map(int,input().split()))

avg = lambda tup: sum(tup)/len(tup)

print(avg(dummy))

# OR alterante one liner
print((lambda tup: sum(tup)/len(tup))(tuple(map(int,input('enter: ').split()))) )