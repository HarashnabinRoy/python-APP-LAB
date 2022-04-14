str1=input("enter string 1: ")
str2=input("enter string 2: ")
for i in range(len(str1)):
    if str1[i: ]+str1[ :i]==str2:
        print(True)
