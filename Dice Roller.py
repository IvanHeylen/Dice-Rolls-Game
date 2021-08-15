import random 

def main():
    player1 = 0
    player2 = 0
    player1score = 0
    player2score = 0
    rounds = 1

    while rounds != 2:
        player1 = roll()
        print("Player 1 Score:")
        print(str(player1))
        player2 = roll()
        print("\nPlayer 1 Score:")
        print(str(player2))
        rounds = rounds + 1
        if player1 == player2:
            print("\nDRAW")
        elif player1 > player2:
            print("\nPLAYER 1 WINS!")
        else:
            print("\nPLAYER 2 WINS!")


def roll():
    randomroll = random.randint(1, 6)
    return randomroll

main()
    
