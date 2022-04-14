in_list = []
list1 = []
count=0
n= int(input("Enter no. of elements:  "))

for i in range(0,n):
    x=int(input("Enter elements: "))
    in_list.append(x)

for item in in_list:
    if item not in list1:
        count += 1
        list1.append(item)

print("No. of unique elements:",count)