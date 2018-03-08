cluesDictionary = {1: {"whale": "This is the largest mammal type"},
                       2: {"eagle": "This is the US national bird"},
                       3: {"football": "This popular sport is played with helmets and pads"},
                       4: {"hawaii": "This state is a collection of islands"},
                       5: {"moon": "This satellite helps control the tides"}}

# Create a method that accepts a string as a message
# and asks the user a question with that message (input).
# Then return the user's response as the return value
# of the method
# Name: getQuestionNumber
# Input: string
# Returns: string

def getQuestionNumber(introMessage):
    return input(introMessage + "\n")


# Create a method that accepts the word the
# user guessed, as well as the correct answer
# and compares the two. If they match, return a
# string that tells the user that they guesses correctly,
# and tells them the guess and the correct answer.
# Make sure the word they submitted as a guess appears
# to them wrapped in double quotes
# Name: correctMessage
# Input: string, string
# Returns: string

def correctMessage(userGuess, questionAnswer):
    return "Congratulations! You entered" + userGuess + "and the answer is" + questionAnswer + "1\n"

# Create a method that accepts the word the
# user guessed, as well as the correct answer
# and compares the two as lowercase strings.
# If they match, return True, otherwise return fFalse
# Name: isCorrect
# Input: string, string
# Returns: bool

def isCorrect(userGuess, questionAnswer):
    if userGuess.lower() == questionAnswer.lower():
        return True
    return False

# Create a method that accepts a string as a message
# and asks the user a question with that message (input).
# Then return the user's response as the return value
# of the method
# Name: tryAnswer
# Input: string
# Returns: string

def tryAnswer(userGuess, questionAnswer):
    list(cluesDictionary[1].value())[0]
    print(tryAnswer)