from random import randint

maxCount = 8
setObj = {'title': 'Hello player!', 'text': 'Try to guess the number I guessed !)'}


def randomNum():
    return randint(0, 50)


def main(randNum):
    print('GameStart')
    count = 1

    while count <= maxCount:
        inpNum = input('Enter number:')

        if int(inpNum) == randNum:
            print('You win !!!!')
            print('Number of attempts:', count, '\n')
            break

        if int(inpNum) < randNum:
            print('You number is small')

        if int(inpNum) > randNum:
            print('Your number is big')

        print('Try again\n')
        count = count + 1

    if count > maxCount:
        print('The number of attempts has been reached!')


def setup():
    print(setObj['title'])
    print(setObj['text'])
    main(randomNum())


def loop():
    action = input('You ready to start game ? Enter y/n:')

    if action == 'y':
        setup()
        loop()

    else:
        print('Goodbye friend !)')


loop()
