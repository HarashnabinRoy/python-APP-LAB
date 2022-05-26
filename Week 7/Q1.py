import random
SORT = lambda x : x.sort()

a = [str(random.randint(1,i)) for i in range(10,100,10)]
print(a)

SORT(a)
print(a)