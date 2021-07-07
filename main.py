from random import randrange

a = int(input('Please enter minimum value: '))
b = int(input('Please enter maximum value:'))

c = randrange(a,b)

print('Your min its',a,'and your max its',b)

d = int(input('Please enter your number of choice between '))

if (d<c):print('Your number its to small ')
elif(d>c):print('Your number its to big ')
else : print('This is the exact number')

