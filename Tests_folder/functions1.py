
# write a function that returns the lesser of the two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def function1(a,b):
    if a %2==0 and b%2 ==0:
        return min(a,b)
    else:
        return max(a,b)
res=function1(10,31)
print(res)

