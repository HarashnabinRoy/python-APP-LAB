string = input("Enter the string: ")
def check_palin(str):
    return str == str[::-1]

ans = check_palin(string)
    
if ans:
    print("Yes")
else:
    print("No")