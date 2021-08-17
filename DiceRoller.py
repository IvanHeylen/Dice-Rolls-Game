import random 


def main():
    player1 = 0
    player2 = 0
    player1score = 0
    player2score = 0
    
    
    print('''

     _   __           _____      __    _      __
    | \ /  \ |   |      |   | | |     | \  | |
    | | |  | |   |      |   | | |     |  | | |
    |_/ |  | |   |      |   |-| |-    |  | | |-
    | \ |  | |   |      |   | | |     |  | | |
    | | \__/ |__ |__    |   | | |__   |_/  | |__

                                 -By Ivan Heylen
    ''')

    player1name = input("Player 1's name: ")
    player2name = input("Player 2's name: ")
    roundsamount = int(input("How many rounds:"))
    rounds = roundsamount
    roundstorun = rounds + 1
    print()
    
    while rounds != roundstorun + 1:
        player1 = roll()
        print(player1name + " rolled a:")
        print(str(player1))
        player2 = roll()
        print("\n" +player2name + " rolled a:")
        print(str(player2))
        rounds = rounds + 1

        if player1 == player2:
            print("\nDRAW")
        elif player1 > player2:
            print("\n" + player1name + " WINS!")
        else:
            print("\n" + player2name + " WINS!")


        Retry = input("Do you want to go again? (y or n): ")
        if Retry == "y":
            rounds = rounds - 2    
        elif Retry == "n":
            print("\nThanks for Playing :)")
            break
        else:
            print("Please type 'y' or 'n'")


def roll():
    randomroll = random.randint(1, 6)
    return randomroll



main()
    
