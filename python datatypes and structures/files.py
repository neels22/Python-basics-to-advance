

myfile = open('python datatypes and structures/test.txt')


# read method -- one giant string 
print(myfile.read()) #returns a string 
print(myfile.read()) # cursor is at the end of the file 

myfile.seek(0)  # resets the cursor 
# print(myfile.read()) # now you can print 


myfile.seek(0) 

#readlines --- to grab a list where each ele represents a line 
print(myfile.readline())

# closing your file
myfile.close()

# we have to manually close the file otherwise we may get errors if we kept open

##########
# best practices for opening files
# no need to worry about closing the file 

with open('python datatypes and structures/test.txt') as my_new_file:
    content = my_new_file.read()
    print(content)


# writing to files 
with open('python datatypes and structures/test.txt',mode='w') as my_new_file:
    pass
    # content = my_new_file.read() 

#modes on files
# w -- write 
# r -- reading
# a -- appending to files
# r+ -- reading and writing 
# w+ -- writing and reading ( overwrite the existing or create new one)


with open('python datatypes and structures/test.txt',mode='a') as my_new_file:
    my_new_file.write("\n four on fourth")


with open('python datatypes and structures/test.txt') as my_new_file:
    content = my_new_file.read()
    print(content)

with open('python datatypes and structures/test2.txt',mode='w') as f:
    f.write("i created this file") # will create new file for us and write in it






