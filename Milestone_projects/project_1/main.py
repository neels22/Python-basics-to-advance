

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


row1= [' ',' ',' ']
row2= [' ',' ',' ']
row3= [' ',' ',' ']


display(row1,row2,row3)

print('\n')

row2[1]='x'

display(row1,row2,row3)

result = int(input("please enter a value : "))

display(row1,row2,row3)

def user_input():

    choice = ''
    acceptable_values = range(0,10)
    within_range = False

    while choice.isdigit() ==False or within_range==False:

        choice = input("enter your choice string: ")

        if choice.isdigit() ==False:
            print('sorry that is not a digit')

        if choice.isdigit():
            if int(choice) in acceptable_values:
                within_range ==True
            else:
                print('sorry out of range')
                within_range ==False

    return int(choice)

user_input()




