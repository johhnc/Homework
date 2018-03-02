cluesDictionary = {1: {"whale": "This is the largest mammal type"},
                       2: {"eagle": "This is the US national bird"},
                       3: {"football": "This popular sport is played with helmets and pads"},
                       4: {"hawaii": "This state is a collection of islands"},
                       5: {"moon": "This satellite helps control the tides"}}



def getQuestionNumber(introMessage):
    return input(introMessage + "\n")
def isCorrect(userGuess, questionAnswer):
    if userGuess.lower == questionAnswer.lower():
        return True
    return False

introMessage = "Enter as question number from 1 to 5, and you will play that clue. Enter -1 to quit:"
keepGoing = True
while keepGoing:
    try:
        questionNumber = int(getQuestionNumber(introMessage))
    except:
        continue
    if questionNumber == int("-1"):
        print("Goodbye!")
        keepGoing = False
        break
    if questionNumber not in range(1,6):
        continue
    questionMessage = list(cluesDictionary[questionNumber].values())[0] + ". What is it?"
    questionAnswer = list(cluesDictionary[questionNumber].keys())[0].lower()
    userGuess = input(questionMessage + "\n").lower()
    print(isCorrect(userGuess, questionAnswer))

for i in questionAnswer:

    if index == 0:
        print("The first letter is:", i)
        index += 1
        userGuess = tryAnswer("Try Again!\n")
        if isCorrect(userGuess, questionAnswer):
            print(correctMessage(userGuess, questionAnswer))
            break

            elif index == len(questionAnswer) - 1:
            print("the last letter was", i)
            print(gameOver(questionAnswer))