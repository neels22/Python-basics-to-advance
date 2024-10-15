


def reach_home(src,dest):

    if src == dest:
        print("reached home")
        return 

    reach_home(src+1, dest)


def fib(num):

    if num==0:
        return 0
    if num==1:
        return 1

    return fib(num-1) + fib(num-2)


def say_digits(num,map):


    if num ==0:
        return 

    digit = num%10
    num //=10

    say_digits(num,map)
    
    print(map[digit])





def main():

    src = 1
    dest = 10

    reach_home(src,dest)

    ans = fib(8)
    print(ans)

    map={
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        0:"zero"
    }

    ans = say_digits(412,map)
    print(ans)

main()