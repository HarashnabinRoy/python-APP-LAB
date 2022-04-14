x=int(input("Enter a number: "))

def check_prime(num):
    flag=False
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                flag=True
                break
    if flag:
         print(x,"it's not a prime")
    else:
        print(x,"It's a prime")

check_prime(x)



