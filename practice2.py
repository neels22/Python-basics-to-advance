


arr = [1, 2, 3, 4, 5]

size = 5

def issorted(arr, size):
    if size == 0 or size == 1:
        return True
    
    if arr[0] > arr[1]:
        return False
    else:
        # Use slicing to pass the remaining array
        ans = issorted(arr[1:], size - 1)
        return ans

ans = issorted(arr, size)
print(ans)

################



def countsum(arr, size, sum):
    if size == 0:
        return sum
    

    sum += arr[0]


    return countsum(arr[1:], size - 1, sum)

# Initial sum is 0
sum = countsum(arr, size, 0)
print(sum)


################

def linear(arr,size,target):

    if size==0:
        return False

    if arr[0]==target:
        return True
    else:
        remain = linear(arr[1:],size-1,target)    
        return remain


ans = linear(arr,size,4)
print(ans)


################
