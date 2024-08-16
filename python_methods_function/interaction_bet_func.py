
from random import shuffle


def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("enter your guess 0,1,2: ")

    return int(guess)

def check_win(mylist , guess):

    if mylist[guess] =='o':
        return "you won"
    else:
        return "you lost"


# my original list
mylist = ['','o','']

# my shuffyles list
shuffle(mylist)
shuffled_list = mylist

# player guess
guess = player_guess()

# check_win
res = check_win(shuffled_list,guess)
print(res)