# Program to check if the difference between Sums of Odd and Even Digits is 0

def isDiff0(n):
    first = 0
    second = 0
    flag = True
    while(n > 0):
        digit = n % 10
        if(flag):
            first += digit
        else:
            second += digit
        if(flag):
            flag = False
        else:
            flag = True
        n = int(n/10)
    if(first-second == 0):
        return True
    return False
 
 
# driver code
n = 1243
if(isDiff0(n)):
    print("Yes")
else:
    print("No")
