


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









def main():

    src = 1
    dest = 10

    reach_home(src,dest)

    ans = fib(8)
    print(ans)


main()