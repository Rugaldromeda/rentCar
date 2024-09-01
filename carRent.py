import os

dictCars = [ 
    {"Car":"Chevrolet Tracker ", "Valor":120},
    {"Car":"Chevrolet Onix ", "Valor":90},
    {"Car":"Chevrolet Spin ", "Valor":150},
    {"Car":"Hyundai HB20 ", "Valor":85},
    {"Car":"Hyundai Tuckson ", "Valor":120},
    {"Car":"Fiat Uno ", "Valor":60},
    {"Car":"Fiat Mobi ", "Valor":70},
    {"Car":"Fiat Pulse ", "Valor":130}
]

dictRentCars = []

def formatador (string): return string.replace("{","").replace("'","").replace(":","").replace("}","")

def continuar():
    cont = int(input("0 - CONTINUAR | 1 - SAIR \n"))
    if(cont == 0):
        main()
    else:
        os.system('cls') or None
        exit()    

def portfolio():   
    for i in range(len(dictCars)):
        port = "[{}] {} R$ {} /dia".format(i, dictCars[i]["Car"], dictCars[i]["Valor"])
        print(formatador(port))

def alugados():   
    for i in range(len(dictRentCars)):
        port = "[{}] {} R$ {} /dia".format(i, dictRentCars[i]["Car"], dictRentCars[i]["Valor"])
        print(formatador(port))

def rent():
    print( "[ALUGAR] Dê uma olhada em nosso portifólio")
    portfolio()

    carChoice = int(input("Escolha o código do carro: \n"))
    period = int(input("Escolha por quantos dias deseja alugar: \n"))

    calcValor = period*(dictCars[carChoice]["Valor"])

    message = "Você escolheu {} por {} dias".format(dictCars[carChoice]["Car"], period)
    print(formatador(message))
    print("O aluguel totalizaria R$ {}. Deseja alugar?".format(calcValor))

    rentChoice = int(input("0 -  SIM | 1 - NÃO \n"))

    if(rentChoice == 0):
        print("Parabéns você alugou o {} por {} dias. \n".format(dictCars[carChoice]["Car"], period))
        dictRentCars.append(dictCars.pop(carChoice))
        #del dictCars[carChoice]

        continuar()
    elif(rentChoice == 1):
        os.system('cls') or None
        exit()

def devolucao():
    print("Segue a lista de carros alugados. Qual você deseja devolver?")
    alugados()

    rentedCar = int(input("Escolha o código do carro que deeja devolver: \n"))
    dictCars.append(dictRentCars.pop(rentedCar))

    print("Obrigado por devolver o carro {} !".format(dictRentCars[rentedCar]["Car"]))
    #del dictRentCars[rentedCar]
    continuar()


def choice(esc):
    if(esc == 0):
        portfolio()
        continuar()
    elif(esc == 1):
        rent()
    elif(esc ==2):
        devolucao()

def main():

    os.system('cls') or None
    print("================== \nBem vindo à locadora de carros! \n==================")

    escolha = int(input("O que deseja fazer?\n0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro \n"))

    choice(escolha)

main()