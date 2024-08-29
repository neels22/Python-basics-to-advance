



arr =[ 1,2,2,3,4,3,4,5,6,3,4,5,7,8,5,4]

freq = {}
for num in arr:
    if num not in freq:
        freq[num] = 1
    else:
        freq[num]+=1
print(freq)

# tc o(n)

count = {}
for num in arr:
    count[num] = arr.count(num)
print(count)

# tc o(n^2)








arr = [1,1,1,2,2,0,0,1,2,1,2,0,0,0,2,1,2,0,0,2,2,1,1,0,0,1]
       #i                                               j


i =0 
j = len(arr) -1

max_left  = float('-inf')
max_right   = float('-inf')

max_all = 0

print(max_left)

while i <= j:

    if arr[i] > max_left:
        max_left = arr[i]
        i+=1
    else:

        max_right= arr[j]
        j -= 1

    if max_left > max_right:
        max_all = max_left
    else:
        max_all = max_right

print(max_all)
        



print(max(arr))
########################


#  0 1 2 

arr = [1,2,2,0,0,2,1]

    # low ==0and mid ==1                               high ==2


low = 0 
mid = 0
high = len(arr) -1


for i in range(len(arr)):

    if arr[mid] == 0:
        arr[low],arr[mid] = arr[mid] , arr[low]
        low+=1
        mid +=1
    elif arr[mid] == 1:
        mid +=1
    elif arr[mid] ==2:

        arr[high],arr[mid] = arr[mid] , arr[high]
        high -=1
        # mid +=1


print(arr)