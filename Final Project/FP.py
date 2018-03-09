def getQuestionNumber(introMessage):
    return input(introMessage + "\n")


def correctMessage(userGuess, questionAnswer):
    print("Congratulations! You entered", userGuess, "and the correct answer is", questionAnswer + "!\n")


def isCorrect(userGuess, questionAnswer):
    if userGuess.lower() == questionAnswer.lower():
        return True
    else:
        return False

def tryAnswer(message):
    return input(message)


def gameOver(questionAnswer):
    print("Sorry! the word was", questionAnswer + ".", "Please Play Again!\n")


def main():
    cluesDictionary = {1: {"whale": "This is the largest mammal type"},
                       2: {"eagle": "This is the US national bird"},
                       3: {"football": "This popular sport is played with helmets and pads"},
                       4: {"hawaii": "This state is a collection of islands"},
                       5: {"moon": "This satellite helps control the tides"}}

    introMessage = "Enter as question number from 1 to 5, and you will play that clue. Enter -1 to quit"
    keepGoing = True

    while keepGoing:
        try:
            questionNumber = int(getQuestionNumber(introMessage))

        except:
            continue

        if questionNumber == int("-1"):
            print("Goodbye, thanks for playing!")
            keepGoing = False
            break

        if questionNumber not in range(1, 6):
            continue

        questionMessage = "{0}. What is it?".format(list(cluesDictionary[questionNumber].values())[0])
        questionAnswer = list(cluesDictionary[questionNumber].keys())[0].lower()
        userGuess = tryAnswer(questionMessage + "\n")

        if isCorrect(userGuess, questionAnswer):
            print(correctMessage(userGuess, questionAnswer))
            continue
        else:
            print("that was incorrect!")

        index = 0

        for i in questionAnswer:

            if index == 0:
                print("The first letter is:", i)
                index += 1
                userGuess = tryAnswer("Try Again! \n")
                if isCorrect(userGuess, questionAnswer):
                    print(correctMessage(userGuess, questionAnswer))
                    continue

            elif index == len(questionAnswer) - 1:
                    print("the next letter is:", i)
                    print(gameOver(questionAnswer))
                    continue
            else:
                print("The next letter is:", i)
                index += 1
                break


            if isCorrect(userGuess, questionAnswer):
                print(correctMessage(userGuess, questionAnswer))
                break


main()



