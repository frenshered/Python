import random
import time
from math import trunc

maxLenPass = 99999999

password = random.randint(10000000, 100000000)
print(password)

a = input('Enter ok/no :')


def hack():
    startTime = trunc(time.time())
    p = 0
    genPass = '00000000'

    for i in range(maxLenPass + 1):
        if len(str(p)) == 1:
            genPass = '0000000' + str(p)
            print(genPass)
            if genPass == str(password):
                print('Password:', genPass)
                break
        elif len(str(p)) == 2:
            genPass = '000000' + str(p)
            print(genPass)
            if genPass == str(password):
                print('Password:', genPass)
                break
        elif len(str(p)) == 3:
            genPass = '00000' + str(p)
            print(genPass)
            if genPass == str(password):
                print('Password:', genPass)
                break
        elif len(str(p)) == 4:
            genPass = '0000' + str(p)
            print(genPass)
            if genPass == str(password):
                print('Password:', genPass)
                break
        elif len(str(p)) == 5:
            genPass = '000' + str(p)
            print(genPass)
            if genPass == str(password):
                print('Password:', genPass)
                break
        elif len(str(p)) == 6:
            genPass = '00' + str(p)
            print(genPass)
            if genPass == str(password):
                print('Password:', genPass)
                break
        elif len(str(p)) == 7:
            genPass = '0' + str(p)
            print(genPass)
            if genPass == str(password):
                print('Password:', genPass)
                break
        elif len(str(p)) == 8:
            genPass = str(p)
            print(genPass)
            if genPass == str(password):
                print('Password:', genPass)
                break

        p = p + 1

    endTime = trunc(time.time())
    print('Time:', endTime - startTime, 's')


if a == 'ok':
    hack()

