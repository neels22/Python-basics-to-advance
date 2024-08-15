

# grab the words in the string that start with letter s 
s= "print out the words in the string that start with letter s "
# s.split()  returrn a list of words separated on white space 
for word in s.split():
    if word[0] =='s':
        print(word)


# use range to print out even numbers from 0 to 10
print(list(range(0,11,2)))
# method 2 
for num in range(0,11,2):
    print(num)


# list comprehension to list all numbers from 1 50 divisible by 3
print([x for x in range(1,51)if x%3==0 ])


# length of the words should be even 
s = 'print the if the lenght of the words is even'
evenwords= []
for words in s.split():
    if len(words) %2 == 0:
        print(words)
        evenwords.append(words)


# fizzbuzz
for num in range(1,101):

    if num %3 ==0 and num %5 == 0 :
        print('fizzbuzz')
    elif num % 3 ==0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)


# list comprehension for list of first letters of every words in string 
s= 'only take the first letter of the words in this string and ccreatea a list'

print([ word[0] for word in s.split() ])






