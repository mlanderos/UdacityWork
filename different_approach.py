
def guesses():
    user_guess = raw_input('Type a number that is lower than 100 for how many guesses you receive for each problem: ')
    while user_guess.Type == int:
        if user_guess > 100:
            print "Sorry number is not lower than 100. Pick new number"
            guesses()
        else:
            print "You chose" + str(user_guess)
            return user_guess
    guesses()



def game_start():
    modes = ['easy', 'medium', 'hard']
    print "Please select a game difficulty by typing it in"
    user_mode = raw_input('Possible choices include easy, medium & hard: ').lower()
    user_guess = guesses()
    while user_mode in modes:
        print "user_mode = " + user_mode
        print "user_guess = " + user_guess
    else:
        print "Incorrect. Please check your spelling and try again."
        game_start()        
game_start()