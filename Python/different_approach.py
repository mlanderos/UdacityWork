


def guesses():
    try:
        tries = input('Type a number that is lower than 100 for how many guesses you receive for each problem: ')
    except:
        print "Your input does not appear to an integer. Please try again"
        guesses()
    else:
        if type(tries) is int:
            if tries > 100:
                print "Sorry number is not lower than 100. Pick new number"
                guesses()
            else:
                print "You chose " + str(tries)
                return tries

def game_start():
    modes = ['easy', 'medium', 'hard']
    print "Please select a game difficulty by typing it in"
    user_mode = raw_input('Possible choices include easy, medium & hard: ').lower()
    if user_mode in modes:
        user_guess = guesses()
        print "user_mode = " + user_mode
        print "user_guess = " + str(user_guess)
    else:
        print "Incorrect. Please check your spelling and try again."
        game_start()

game_start()
