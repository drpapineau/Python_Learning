
#import of a library function
import random


#do not forget the style of the variable exempla str or int
NumberRandom = random.randrange(1,100)
Numberguess = 0
PlayerScore = 10
Proceed = True


print(NumberRandom)

while Proceed:
    PlayerScore -= 1
    try:
        Numberguess = int(input("guest the number between 1 and 100:  "))
        if Numberguess == NumberRandom:
            print(f"Good job you did {PlayerScore} Points/n")
            rejouer = input("voulez vous rejouer ? oui ou non ? ")
            if rejouer == "oui":
                NumberRandom = random.randrange(1,100)
                Numberguess = 0
                PlayerScore = 10
                Proceed = True
            elif rejouer == "non":
                print("byebye")
                Proceed = False
            else:
                print("mauvaix choix fuck you....")
                Proceed = False
        elif Numberguess > NumberRandom:
            print("the number you are looking for is smaller than the one you enter.... Try Again !\n")
        elif Numberguess < NumberRandom:
            print("the number you are looking for is bigger than the one you enter....Try Again !\n")
    except ValueError:
                print("not a number you retard fuck")  








