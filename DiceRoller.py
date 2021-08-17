import random #imports the random module


def main():#main function
    player1 = 0#pyr1 base value
    player2 = 0#pyr2 base value
    player1score = 0#pyr1's score base value
    player2score = 0#pyr2's score base value
    
    
    
    print()
    print('''

     _   __           _____      __    _      __
    | \ /  \ |   |      |   | | |     | \  | |
    | | |  | |   |      |   | | |     |  | | |
    |_/ |  | |   |      |   |-| |-    |  | | |-
    | \ |  | |   |      |   | | |     |  | | |
    | | \__/ |__ |__    |   | | |__   |_/  | |__

                                 -By Ivan Heylen
    ''')#main logo

    player1name = input("Player 1's name: ")#input for pyr1's name
    player2name = input("Player 2's name: ")#input for pyr2' name
    roundsamount = int(input("Rounds to play: "))#input for amount of rounds to play
    cutoff = roundsamount * 2#the value that will be used to stop the while loop

    scores1 = list()#list of all roll values for player 1
    scores2 = list()#list of all roll values for player 2
    #loop take twice the roundsamount as the cutoff. Sice rounds amount has a value that isinputed, it is required that
    #the inputed value be multiplied by two in order that the while loop
    #will go through the same amount of times as the rounds amount that was inputed.
    
    while roundsamount != cutoff:#While loop that
        player1 = roll()#player 1 is assigned  random interger
        scores1.append(player1)#adds score to the score list for player 1
        print(player1name + " rolled a:")#print statement for player 1's score
        print(str(player1))
        player2 = roll()#player 2 is assigned  random interger
        scores2.append(player2)#adds score to the score list for player 2
        print("\n" +player2name + " rolled a:")#print statement for player 1's score
        print(str(player2))
        roundsamount = roundsamount + 1#adds 1 to the rounds amount so as to reach the cutoff.
        if player1 == player2:#draw statement
            print("\n---DRAW---\n")
        elif player1 > player2:#player 1 wins statement
            print("\n---" + player1name + " WINS!---\n")
        else:#player 2 wins statement
            print("\n---" + player2name + " WINS!---\n")

    
    Totalscoreplayer1 = sum(scores1)#sums the integers in the score list for player 1
    Totalscoreplayer2 = sum(scores2)#sums the integers in the score list for player 2
    if Totalscoreplayer1 == Totalscoreplayer2:#if player 1 and 2's summed value is equal than a draw is declared.
        print("Overall score was " + str(Totalscoreplayer1) + ". It's a draw!")
    elif Totalscoreplayer1 > Totalscoreplayer2:#if player 1's summed value is grater than player 2 than player 1 is declared winner.
        print("Overall Winner is " + player1name + "! SCORE: " + str(Totalscoreplayer1))
    else:#if player 1's summed value is not equal to or greater than player 2's summed value than the logical win goes to player 2.
        print("Overall Winner is " + player2name + "! SCORE: " + str(Totalscoreplayer2))



def roll():#random integer function using random module.
    randomroll = random.randint(1, 6)
    return randomroll


main()#excecution of the main function
 
