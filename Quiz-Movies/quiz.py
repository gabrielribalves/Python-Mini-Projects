"""Quiz Movies
$ python3 quiz.py

$ python3 quiz.py load

"""

import os
import random
import sys

argument = sys.argv[1:]

questions = ""

#Store the text in questions.txt in a variable
path = os.curdir
filePath = os.path.join(path, "questions.txt")
with open(filePath, "r") as questionsFile:
    questions = questionsFile.read()

#Divide all questions in an array
listQuestion = questions.split("\n----------\n")
questionNumbers = list(range(0,len(listQuestion)))

def startGame(listQuestion, questionNumbers):
    pointCount = 0
    questionNumbersArr = questionNumbers
    input(f"Seja bem-vindo ao Quiz Movies!!!😀\nPara iniciar, pressione Enter.\n")

    for index in range(5):
        numberChosenQuestion = random.choice(questionNumbersArr)
        phrase, alternativeA, alternativeB, alternativeC, alternativeD, questionAnswer = listQuestion[numberChosenQuestion].split("\n")
        userAnswer = input(f"{phrase}\n{alternativeA}\n{alternativeB}\n{alternativeC}\n{alternativeD}\n\nResposta: ")
        print("-"*30)

        if questionAnswer.lower() == userAnswer.lower():
            pointCount += 1

        questionNumbersArr.remove(numberChosenQuestion)

    if pointCount >= 3:
        print("#"*30)
        print("VOCÊ VENCEU!!! 🤑🤑🤑🥳🥳🥳")
        print("Total de pontos: ", pointCount)
        print("#"*30)
    else:
        print("#"*30)
        print("você perdeu. 💩💩💩")
        print("Total de pontos: ", pointCount)
        print("#"*30)

def writeQuestion():
    input("""\
Escreva a Pergunta, depois as alternativas a) até d) e por último, a resposta.
Pressione Enter para continuar""")
    
    phrase = input("Escreva a pergunta do Quiz: ")
    alternativeA = "a) " + input("Escreva a alternativa A : ")
    alternativeB = "b) " + input("Escreva a alternativa B : ")
    alternativeC = "c) " + input("Escreva a alternativa C : ")
    alternativeD = "d) " + input("Escreva a alternativa D : ")
    questionAnswer = input("Escreva com uma letra a alternativa correta: ")

    fullText = f"\n----------\n{phrase}\n{alternativeA}\n{alternativeB}\n{alternativeC}\n{alternativeD}\n{questionAnswer}"

    print(fullText)
    path = os.curdir
    filePath = os.path.join(path, "questions.txt")
    with open(filePath, "a") as questionsFile:
        questionsFile.write(fullText)

if len(argument) > 0:
    if argument[0] == "load":
        writeQuestion()
else:
    startGame(listQuestion, questionNumbers)