import random

userChoice = ""

input("Bem-Vindo ao Preda, Papel e Tesoura. Para continuar, pressione Enter...")

choicesArr = ["pedra", "papel", "tesoura"]

while True:
    computerChoice = random.choice(choicesArr)
    userChoice = input("Escolha pedra, papel ou tesoura: ").lower()

    if(userChoice == "Q"):
        break

    if(userChoice in choicesArr):
        msg = f"Escolha do Usuário: {userChoice.capitalize()}\nEscolha do Computador: {computerChoice.capitalize()}"
        if(userChoice == computerChoice):
            print("EMPATE!")
            print(msg)
        if(userChoice == "pedra" and computerChoice == "tesoura"):
            print("VITORIA!!! 🧠🧠🧠")
            print(msg)
        elif(userChoice == "tesoura" and computerChoice == "papel"):
            print("VITORIA!!! 🧠🧠🧠")
            print(msg)
        elif(userChoice == "papel" and computerChoice == "pedra"):
            print("VITORIA!!! 🧠🧠🧠")
            print(msg)
        else:
            print("DERROTA!!! 🤬🤬🤬")
            print(msg)
        print("-"*30)
        print("")
    else:
        print("Por favor, digite apena pedra, papel, tesoura ou Q para sair")