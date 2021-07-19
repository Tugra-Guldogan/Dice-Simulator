import random

#ENJOY !!!!

start = input ("Do you want to roll the die ?")

def dice ():
    while True :
        print("The no: id " + str(random.randint(1,6)))
        global again
        again = input ("press any button to roll again")

if start=="yes":
    dice ()
