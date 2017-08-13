
def correct_answer(user_input, question):
    """<>"""
    easy_answerlist = ['python', '.py', 'yes', 'no']
    if user_input == easy_answerlist[question - 1]:
        return True
    else:
        return False

def mode(paragraph,n):
    """function to test each blank space from any mode"""
    max_tries = n #expecting 5
    question = 1
    while question < 5: #expecting only 4 questions max
        print paragraph
        selection = raw_input('What is the answer to question ' + str(question) +': ').lower()
        if max_tries > 0: #expecting 5 max tries
            if correct_answer(selection, question):
                paragraph = paragraph.replace('__'+ str(question) + '__', selection)
                print "Correct!"
                question += 1
                max_tries = n #resetting number back for next question!
            else:
                max_tries -= 1
                print 'wrong answer! Try again. You have ' + str(max_tries) + ' left.'
        else:
            print "You Loss!! Game Over!!"
            quit()
    print "You WON YAY!!!"
    quit()

easy_paragraph = """
__1__ programs can be written using any text editor and should have the extention __2__. Write Yes for __3__ and No for __4__.
"""
mode(easy_paragraph, 5)
