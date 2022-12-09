import random
options = ["Paper", "Rock", "Scissors"]
#player and computer scoreboard
p_score = 0
c_score = 0

def new_game():
    #ask if player wants to play again
    ng = input('New game?(Y/N)')
    if ng.upper() == 'Y':
        print('..........')
        game()
    elif ng.upper() == 'N':
        print('Good game.')
    else: 
        print('Response not recognized. Please choose Y or N')
        new_game()
        
def lose():
    #do this if player loses
    print('You lose!')
    global c_score
    c_score +=1
    
def win():
    #do this if play wins
    print('You win!')
    global p_score 
    p_score += 1
    
def choose():
    #player makes their choice of paper, rock, or scissors
    choice = input("Rock, Paper, or Scissors? ")
    if choice.upper() == 'ROCK' or choice.upper() == 'SCISSORS' or choice.upper() == 'PAPER':
        return choice
    else:
        print('Choose again. ')
        choose()
    
def game():
    #one full run through of a single game
    choice = choose()
    comp_choice = random.choice(options)
    print('You chose: ' + str(choice))
    print('Computer chose: ' + comp_choice)
    #determine who won
    if choice.upper() == comp_choice.upper():
        print('Tie Game!')
        #Both sides get half a point if it's a tie
        global p_score
        p_score +=0.5
        global c_score
        c_score +=0.5
    elif choice.upper() == 'ROCK':
        if comp_choice == 'Scissors':
            win()
        else:
            lose()
    elif choice.upper() == 'SCISSORS':
        if comp_choice == 'Paper':
            win()
        else:
            lose()
    else:
        if comp_choice == 'Rock':
            win()
        else:
            lose()
    #print scores after the game is over
    print("Your score: ", p_score)
    print("Computer score:", c_score)
    #ask if player wants to play again
    new_game()
            
      
game()



