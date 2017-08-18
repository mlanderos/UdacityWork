def game_won(bool_result, paragraph):
    """Input a bool value. True for when user wins the game. False if not"""
    if bool_result:
        print paragraph
        print "You Won!! The force is strong with you!"
        quit()
    else:
        print "You failed too many straight guesses. GAME OVER!\n"
    quit()

def islast_chance(min_c, max_c):
    """Prints specific message dependent on how many chances remain to answer the question."""
    if max_c > min_c:
        print 'That isn''t the correct answer! Lets try again; You have ' + str(max_c) + ' trys left.'
    else:
        print 'That isn''t the correct answer! Lets try again; You have ' + str(max_c) + ' try left. Make it count!'

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

def ask_question(paragraph, question):
    """Prompts user for answer to question. Returns answer in string type"""
    print "The current paragraph reads as such:"
    print paragraph
    user_answer = raw_input('What is the answer to question ' + str(question) +': ').lower()
    return user_answer

def play_game(game_level, paragraph, max_chances, question_num):
    """Runs through logic of game. Prints out whether user Won or Lost."""
    question_overflow = 5
    min_tries = 1
    max_tries = max_chances
    while question_num < question_overflow:
        user_answer = ask_question(paragraph, question_num)
        if max_tries > min_tries:
            if verify_answer(game_level, user_answer, question_num):
                paragraph = paragraph.replace('__'+ str(question_num) + '__', user_answer)
                print "Correct!\n"
                question_num += 1
                max_tries = max_chances #resetting quesses for next question!
            else:
                max_tries -= 1
                islast_chance(min_tries, max_tries)
        else:
            game_won(False, paragraph)
    game_won(True, paragraph)

def get_paragraphfor(mode):
    """function to return paragraph for selected mode: easy, medium, hard are the only acceptable values. Returns string"""
    if mode == 'easy':
        paragraph = """
At Udactiy we are learning how to program in __1__. The __1__ language was created by __2__ van Rossum during 1985-1990. __1__ files
 have the extention __3__. If you want to print something from Python use the __4__ command.\n"""
    if mode == 'medium':
        paragraph = """
Python __1__s do not need explicit declaration to reserve memory space. The declaration happens automatically when you __2__ 
a value to a variable. The equal sign (=) is used to __2__ values to __1__s. The __3__ to the left of the = __4__ is the 
name of the variable and the __3__ to the right of the = __4__ is the value stored in the variable.\n"""
    if mode == 'hard':
        paragraph = """
__1__ are the constructs which can manipulate the value of operands. Python language supports the following types of __1__:
__2__metric __1__, Comparison __1__, __3__ment __1__, Log__4__ __1__, Bitwise __1__, Membership __1__ & Identity __1__.\n"""
    return paragraph

def get_gamedetails(game_level, chances):
    """logic for looping through all questions and ending game if max attempts are met. Prints string output for user\n"""
    paragraph = get_paragraphfor(game_level)
    max_chances = chances
    question_num = 1
    play_game(game_level, paragraph, max_chances, question_num)

def guesses():
    """function for user to input a integer for how mnay guesses he/she has to play each question. Returns int"""
    try:
        tries = input('Type a number that is lower than 100 for how many guesses you receive for each problem: ')
    except:
        print "Your input does not appear to an integer. Please try again"
        guesses()
    else:
        max_limit = 100
        if isinstance(tries, int):
            if tries > max_limit or tries == 0:
                print "Sorry number is not in the range of 1 to 99. Pick new number"
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
        get_gamedetails(user_mode, user_guess)
    else:
        print "Incorrect. Please check your spelling and try again."
        game_start()

game_start()
