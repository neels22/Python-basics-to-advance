
# __name__  ---> when you execute the script directly python assign main to name

# if __name__ == "__main__" ---> if name equals to main then i know i am this file directly and not importing its methods into another script


def funct():
    print('func in one.py')

print('top level in one.py')

if __name__ == "__main__": 
    # same thing as saying run the script
    funct()
else:
    print('one.py has been imported')