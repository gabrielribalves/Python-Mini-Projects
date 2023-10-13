import os
import random

questions = ""
pointCount = 0

path = os.curdir
filePath = os.path.join(path, "questions.txt")

with open(filePath, "r") as questionsFile:
    questions = questionsFile.read()


listQuestion = questions.split("\n----------\n")
questionNumber = list(range(0,len(listQuestion)))

welcomeMsg = input(f"Seja bem-vindo ao Quiz Movies!!!😀\nPara iniciar, aperte Enter.\n")

for index in range(5):
    numberChosenQuestion = random.choice(questionNumber)
    phrase, alternativeA, alternativeB, alternativeC, alternativeD, questionAnswer = listQuestion[numberChosenQuestion].split("\n")
    userAnswer = input(f"{phrase}\n{alternativeA}\n{alternativeB}\n{alternativeC}\n{alternativeD}\n\nResposta: ")
    print("-"*30)

    if questionAnswer.lower() == userAnswer.lower():
        pointCount += 1

    questionNumber.remove(numberChosenQuestion)

if pointCount >= 2:
    print("#"*30)
    print("VOCÊ VENCEU!!! 🤑🤑🤑🥳🥳🥳")
    print("Total de pontos: ", pointCount)
    print("#"*30)
else:
    print("#"*30)
    print("você perdeu. 💩💩💩")
    print("Total de pontos: ", pointCount)
    print("#"*30)