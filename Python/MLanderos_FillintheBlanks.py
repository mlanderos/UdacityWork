def get_answerfor(mode):
    """function to return answer key for selected mode. easy, medium, hard are the only acceptable values. Returns list"""
    if mode == 'easy':
        answer_key = ['python', 'guido', '.py', 'print']
    elif mode == 'medium':
        answer_key = ['variable', 'assign', 'operand', 'operator']
    else: #mode hard
        answer_key = ['operators', 'arith', 'assign', 'ical']
    return answer_key

def verify_answer(mode, u_answer, question_num):
    """function to verify answer for any mode and any question. Returns bool value"""
    answers = get_answerfor(mode)
    if u_answer == answers[question_num - 1]:
        return True
    else:
        return False

def get_paragraphfor(mode):
    """function to return paragraph for selected mode: easy, medium, hard are the only acceptable values. Returns string"""
    if mode == 'easy':
        paragraph = """
At Udactiy we are learning how to program in __1__. The __1__ language was created by __2__ van Rossum during 1985-1990. __1__ files
 have the extention __3__. If you want to print something from Python use the __4__ command."""
    if mode == 'medium':
        paragraph = """
Python __1__s do not need explicit declaration to reserve memory space. The declaration happens automatically when you __2__ 
a value to a variable. The equal sign (=) is used to __2__ values to __1__s. The __3__ to the left of the = __4__ is the 
name of the variable and the __3__ to the right of the = __4__ is the value stored in the variable. """
    if mode == 'hard':
        paragraph = """
__1__ are the constructs which can manipulate the value of operands. Python language supports the following types of __1__:
__2__metric __1__, Comparison __1__, __3__ment __1__, Log__4__ __1__, Bitwise __1__, Membership __1__ & Identity __1__."""
    return paragraph

def play_game(game_level, chances):
    """logic for looping through all questions and ending game if max attempts are met. Prints string output for user"""
    paragraph = get_paragraphfor(game_level)
    question_overflow = 5 #expecting only 4 questions max per mode
    question = 1
    max_tries = chances
    min_tries = 1
    while question < question_overflow:
        print "The current paragraph reads as such:"
        print paragraph
        user_answer = raw_input('What is the answer to question ' + str(question) +': ').lower()
        if max_tries > min_tries:
            if verify_answer(game_level, user_answer, question):
                paragraph = paragraph.replace('__'+ str(question) + '__', user_answer)
                print "Correct!\n"
                question += 1
                max_tries = chances #resetting retries back to chances variable for next question!
            else:
                max_tries -= 1
                if max_tries > min_tries:
                    print 'That isn''t the correct answer! Lets try again; You have ' + str(max_tries) + ' trys left.'
                else:
                    print 'That isn''t the correct answer! Lets try again; You have ' + str(max_tries) + ' try left. Make it count!'
        else:
            print "You failed too many straight guesses. GAME OVER!\n"
            quit()
    print paragraph
    print "You WON YAY!!!"
    quit()

def guesses():
    """function for user to input a integer for how mnay guesses he/she has to play each question. Returns int"""
    try:
        tries = input('Type a number that is lower than 100 for how many guesses you receive for each problem: ')
    except:
        print "Your input does not appear to an integer. Please try again"
        guesses()
    else:
        max_limit = 100
        if type(tries) is int:
            if tries > max_limit:
                print "Sorry number is not lower than 100. Pick new number"
                guesses()
            else:
                print "You will get " + str(tries) + " guesses per problem.\n"
                return tries

def game_start():
    """function for game to begin and allows user to select level and # of quesses"""
    print "Please select a game difficulty by typing it in"
    user_mode = raw_input('Possible choices include easy, medium & hard: ').lower()
    modes = ['easy', 'medium', 'hard']
    if user_mode in modes:
        print "You chose game mode: " + user_mode
        user_guess = guesses()
        play_game(user_mode, user_guess)
    else:
        print "Incorrect. Please check your spelling and try again."
        game_start()

game_start()
