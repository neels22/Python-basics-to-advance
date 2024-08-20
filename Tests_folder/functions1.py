
# write a function that returns the lesser of the two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def function1(a,b):
    if a %2==0 and b%2 ==0:
        return min(a,b)
    else:
        return max(a,b)
res=function1(10,31)
print(res)

# write a function that takes two strings and returns true if both of these strings start with same letter

def function2(str1):
    wordlist = str1.split()
    return wordlist[0][0] == wordlist[1][0]
res=function2('neel Neelay')
print(res)

# write a function that capitalizes the first and fourth letter 

def function3(name):
    st = ''

    first_letter = name[0].upper()
    fourth_letter = name[3].upper()

    return first_letter + name[1:3] + fourth_letter
res=(function3('neel'))
print(res)

# given a sentence return a sentence with words reversesd --- join method used 

def function4(st):
    words_list = st.split()
    words_list = words_list[::-1]
    st = ' '
    st = st.join(words_list)
    return st 
res=function4('i am home')
print(res)

# given an integer n return true if n is within 10 of 100 or 200 

def function5(n):
    return (abs(100-n) <=10) or (abs(200-n) <=10)
res= function5(100)
print(res)

# given a list of integers return true if 3 was next to a 3 anywhere

def function6(arr):
    for i in range(len(arr)-1):
        if arr[i] ==3 and  arr[i+1] ==3:  # nums[i:i+2] ==3 -- short form
            return True
    return False
res=function6([1,2,3,4,3,5])
print(res)

# given a string return string for every character make 3 character 

def function7(st):

    st1=''
    for ch in st:
        st1 += ch*3 

    return st1 
res = function7('hi')
print(res)

# given three integers between 1 and 11 if their sum is less than or equal to 21 return their sum however exceeds 21 and their is 11 reduce the sum by 10 finally if the sum after adjustment exceedds 21 return bust

def function8(a,b,c):

    if sum([a,b,c]) <=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])<=31:
        return sum([a,b,c]) -10
    else:
        return 'Bust'
res = function8(11,2,3)
print(res)

# return sum of list except ignore section from 6 to 9 and 6 is followed by 9

def function9(arr):

    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False

        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
res = function9([4,5,6,7,8,9])
print(res)

# write function that takes list of integers and return true if 007 contains in order not consecutive but order

def function10(arr):
    code = [0,0,7,'x']
    for num in arr:
        if num == code[0]:
            code.pop(0)
    return len(code) ==1
res = function10([1,2,3,0,0,7,23,3])
print(res)

# write a function that return number of prime numbers upto a certain number 

        

    


