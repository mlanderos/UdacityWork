
def correct_answer(level, user_input, question):
    """<>"""
    if level == 'easy':
        answerlist = ['python', '.py', 'yes', 'no']
    if level == 'medium':
        answer_list = ['hi','hi']
    if question == 1 and user_input == answerlist[question - 1]:
        return True
    if question == 2 and user_input == answerlist[question - 1]:
        return True
    if question == 3 and user_input == answerlist[question - 1]:
        return True
    if question == 4 and user_input == answerlist[question - 1]:
        return True
    return False

def mode(level, n):
    """function to test each blank space from any mode"""
    [level]_paragraph = "__1__ programs can be written using any text editor and should have the extention __2__. Write Yes for __3__ and No for __4__."
    max_tries = n #expecting 5
    question = 1
    while question < 5: #expecting only 4 questions max
        print paragraph
        selection = raw_input('What is the answer to question ' + str(question) +': ').lower()
        if max_tries > 1: #expecting 5 max tries
            if correct_answer(level, selection, question):
                paragraph = paragraph.replace('__'+ str(question) + '__', selection)
                print "Correct!"
                print ""
                question += 1
                max_tries = n #resetting retries back to n for next question!
            else:
                max_tries -= 1
                print 'wrong answer! Try again. You have ' + str(max_tries) + ' left.'
        else:
            print "You Loss!! Game Over!!"
            quit()
    print "You WON YAY!!!"
    quit()

def chosen(mode, guesses):
    print "You have chosen " + mode `n
    print "You will get " + str(guesses) + " guesses per problem"
    print ""
    print "Your current paragraph reads as such:"

def game_start():
    modes = ['easy', 'medium', 'hard']
    print "Please select a game difficulty by typing it in"
    user_modeselect = raw_input('Possible choices include easy, medium & hard: ').lower()
    user_guessSelect = raw_input('Choose a number which will be how many quesses you will get per question: ')
    while user_modeselect in modes:
        if user_modeselect == 'easy':
            chosen(user_modeselect, user_guessSelect)
            mode('easy', user_guessSelect)
    else:
        print "Incorrect. Please check your spelling and try again."
        game_start()
        
        
game_start()