

index_count = 0
word = 'abcde'
for let in word:
    print(f'at index {index_count} the letter is {let}')
    index_count+=1

# we use enumerate function to replecate the above counter keeping function

for let in enumerate(word):
    print(let)

# below is output -- gives out tuples so we can also use unpacking 
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

# unpacking 
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('###')

