import random

options = ['s', 'w' , 'g']
print("hello, welcome to snake , gun , water game !!  please get ready !!")
n = int(input("enter your rounds which you want to play"))

round = 1

com_win = 0

usr_win = 0

while n >= round :

    print(f"round : {round} \nsnake - s \nwater - w \nGun - g\n ")

    try:
        player = input("choose your option")
    except EOFError as e:
        print(e)

    if player!='s' and player != 'w' and player != 'g':
        print("invalid entry ! plese check your input and try again")
        continue

    computer = random.choice(options)

    if computer == 's':
        if player == 'w' :
            com_win += 1
        elif  player == 'g':
            usr_win += 1





    elif computer == 'w':
        if player ==  'g':
            com_win += 1
        elif player == 's':
            usr_win += 1



    elif computer == 'g':
        if player ==  's':
            com_win += 1
        elif player == 'w':
            usr_win += 1



    if usr_win > com_win :
        print(f"usr won round{round}")

    elif usr_win < com_win :
        print(f"computer won {round}")

    else: print("draw")

    round += 1



if usr_win > com_win :
    print("congratulation usr you won")

elif com_win > usr_win:
    print("you lose usr ! sorry for your lose")

else :
    print("draw!!")
