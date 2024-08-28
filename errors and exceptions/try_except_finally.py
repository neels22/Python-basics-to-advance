

# errors arise 
# we use error handling to let the script continue execution even if we encounter an error


# try --block of code to be attempted
  
# except -- in case error in try this will execute

# else -- you can else when try doesnt give error

# finally -- this code executes no matter what  -- not compulsory 

# many types of errors are their typerros , os errors etc



try:
    f = open('testfile','r')
    f.write('this is written')

except TypeError:
    print('type error') # for example 10 + '10'
except OSError:
    print('you have os error') # because it was opened in r mode 
except:
    print('all other errors')
finally:
    print('i always run')



##################################################


def ask_for_int():

    while True:
        try:
            res = int(input('enter a number'))
        except:
            print('oops its not a number')
            continue
        else:
            print('yes thank you')
            break
        # finally:
        #     print('finally ')

ask_for_int()