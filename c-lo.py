import random


def rolldice(): #this function generates three random numbers and returns them in an array
    values = []
    i = 0

    while i < 3:
        values.append(random.randrange(1,6))
        i = i + 1
    return values


#This is a mess off booleans that keeps calling rolldice() until a pair is noticed then returns the third number or tripples
def clo():
    roll = rolldice()
    n = 1
    while n < 2:
        #Here a 4,5,6 and a 1,2,3 are given huge and null values to make them game-dominant rolls
        if sorted(roll) == [4,5,6]:
            return 999
            n = n + 1
        elif sorted(roll) == [1,2,3]:
            return 0
            n = n + 1

        #Here is a likely inneficient combination of checks for a matching pair which returns the other number unless a triple is noticed
        elif roll[0] == roll[1]:
            if roll[0] == roll[2]:
                return roll[0]*111
            else:
                return roll[2]
            n = n + 1
        elif roll[0] == roll[2]:
            if roll[0] == roll[1]:
                return roll[0]*111
            else:
                return roll[1]
            n = n + 1
        elif roll[1] == roll[2]:
            if roll[1] == roll[0]:
                return roll[0]*111
            else:
                return roll[0]
            n = n + 1
        else:
            roll = rolldice()


p1 = clo()
p2 = clo()


print("You get :"+str(p1))
print("The computer gets :"+str(p2))

if p1 == 999:
    print ("You win with high straight!")
elif p2 == 999:
    print ("Computer wins with high straight!")
elif p1 == 0:
    print ("You lose with low straight.")
elif p2 == 0:
    print ("Computer loses with low straight!")
elif p1 > p2:
    print ("You win!")
elif p2 == p1:
    print("It's a tie.")
else:
    print ("The computer wins.")