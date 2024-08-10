
mystring = "this is a test string"

#positive index positions
print(mystring[0])
print(mystring[3])
print(mystring[4])

# negative index positions 
print(mystring[-2])
print(mystring[-3])
print(mystring[-4])

print('Hello World'[8])  #also works

#######################
#slicing

mystring = 'abcdefghijk'

print(mystring[2:]) # from a index to end -2 to end 
print(mystring[:3]) # from 0 to upto that stop but not included -0 1 2 

print(mystring[3:6]) # 3 4 5 not 6 

# step size 
print(mystring[::])  
print(mystring[::2])  
print(mystring[::3])  
print(mystring[2::3])  

print('tinker'[1:4]) #also works

#using step size to reverse 
# explaination --> step is -1, which means the slice will move from right to left, effectively reversing the string.
print(mystring[::-1])  

#######################





