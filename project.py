from pickle import TRUE
import random

def game():
    GuessNumber=int(input("guess a number "))
    return GuessNumber


    

    
       
      


   
       
    

luckyNumber=random.randint(0,9)
chances=5
result=False
while(chances>0):
    p=game()
    if p==luckyNumber:
        print("CONGRATS U HAVE WON!")
        chances=0
        result=True

    elif luckyNumber > p :
        print("Guess a higher number")
        chances=chances-1    





    elif luckyNumber < p :
        print("Guess a lower Number")
        chances=chances-1


if(chances==0 and result!=True):
    print("you have lost")
