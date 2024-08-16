
def even_odd(num):
    if num % 2 == 0:
        return "number is even"
    else:
        return "number is odd"
res = even_odd(20)
print(res)

def even_check(num):
    return num % 2 ==0
print(even_check(3))

# retrun true if any number is even inside a list
def check_even_list(nums):
    for num in nums:
        if num % 2 ==0:
            return True
    return False
res = check_even_list([1,2,3,34,34])
print(res)

# return even numbers in list
def check_even_list(nums):
    even_list = []
    for num in nums:
        if num % 2 ==0:
            even_list.append(num)
    return even_list
res = check_even_list([1,2,3,34,34])
print(res)
