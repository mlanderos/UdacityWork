

def easy_mode2():
    print "you made it to easymode 2"

def easy_mode():
    easy_paragraph = """
__1__ programs can be written using any text editor and should have the extention __2__.
"""
    max_tries = 5
    while max_tries > 0:
        print easy_paragraph
        selection = raw_input('What is the answer to question 1: ').lower()
        if selection == "python":
            easy_paragraph = easy_paragraph.replace('__1__', selection)
            print easy_paragraph
            break
        else:
            max_tries -= 1
            print 'wrong answer! Try again. You have ' + str(max_tries) + ' left.'
    else:
        print "You failed! Max Attempt is met. Game Over!"
        quit()
    easy_mode2()

easy_mode()
            