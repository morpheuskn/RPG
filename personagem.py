import random

def nome():
    nomepersonagem = input("Digite o Nome do Personagem: ")
    return nomepersonagem

def raca():
    racas = {1: "Humano", 2: "Elfo", 3: "Anão", 4: "Hobbit"}
    print("Escolha a Raça do Seu Personagem: ")
    print("Digite: ")
    print("1 - Humano")
    print("2 - Elfo")
    print("3 - Anão")
    print("4 - Hobbit")
    
    escolharaca = int(input("Digite o Número da Raça: "))
    racapersonagem = racas.get(escolharaca)
    print(f"A raça Escolhida foi: {racapersonagem}")
    return racapersonagem

def classe():
    classes = {1: "Guerreiro", 2: "Feiticeiro", 3: "Ladino", 4: "Guardião"}
    print("Escolha a Classe do Seu Personagem: ")
    print("Digite: ")
    print("1 - Guerreiro")
    print("2 - Feiticeiro")
    print("3 - Ladino")
    print("4 - Guardião")
    
    escolhaclasse = int(input("Digite o Número da Classe: "))
    classepersonagem = classes.get(escolhaclasse)
    print(f"A classe Escolhida foi: {classepersonagem}")
    return classepersonagem

def atributos(raca, classe):
    
    atributosraca = {
        "Humano": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 1, "Sabedoria": 0, "Carisma": 1},
        "Elfo": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 0, "Sabedoria": 1, "Carisma": 1},
        "Anão": {"Força": 1, "Destreza": 0, "Constituição": 1, "Inteligência": 1, "Sabedoria": 0, "Carisma": 0},
        "Hobbit": {"Força": 0, "Destreza": 0, "Constituição": 0, "Inteligência": 1, "Sabedoria": 1, "Carisma": 1}
    }

    atributosclasse = {
        "Guerreiro": {"Força": 1, "Destreza": 1, "Constituição": 1, "Inteligência": 0, "Sabedoria": 0, "Carisma": 0},
        "Feiticeiro": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 1, "Sabedoria": 0, "Carisma": 1},
        "Ladino": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 1, "Sabedoria": 1, "Carisma": 0},
        "Guardião": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 1, "Sabedoria": 1, "Carisma": 0}
    }

    
    atributos_totais = {}
    for atributo in atributosraca[raca]:
        atributostotais[atributo] = atributosraca[raca][atributo] + atributosclasse[classe][atributo]

    if classe == "Guerreiro":
        HP = random.randint(20, 25) + atributostotais["Constituição"]
        DEF = random.randint(25, 30) + atributostotais["Destreza"]
        ATK = random.randint(4, 8) + atributostotais["Força"] + atributos_totais["Destreza"]
        MAG = atributos_totais["Inteligência"] + atributostotais["Carisma"]
        atributosjogador = {"HP":HP, "DEF":DEF, "ATK": ATK, "MAG":MAG}
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")
        

     if classe == "Feiticeiro":
        HP = random.randint(15, 20) + atributostotais["Constituição"]
        DEF = random.randint(20, 25) + atributostotais["Destreza"]
        ATK = atributos_totais["Força"]
        MAG = random.randint(10, 15) +  atributostotais["Inteligência"] + atributostotais["Carisma"]
        atributosjogador = {"HP":HP, "DEF":DEF, "ATK": ATK, "MAG":MAG}
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")


     if classe == "Ladino":
        HP = random.randint(20, 25) + atributostotais["Constituição"]
        DEF = random.randint(20, 25) + atributostotais["Destreza"]
        ATK = random.randint(4, 8) + atributostotais["Força"] + atributostotais["Inteligência"]
        MAG = atributos_totais["Inteligência"] + atributostotais["Carisma"] + atributostotais["Sabedoria"]
        atributosjogador = {"HP":HP, "DEF":DEF, "ATK": ATK, "MAG":MAG}
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")


     if classe == "Guardião":
        HP = random.randint(15, 20) + atributostotais["Constituição"]
        DEF = random.randint(15, 20) + atributostotais["Destreza"]
        ATK = random.randint(4, 8) + atributostotais["Força"] + atributostotais["Destreza"]
        MAG = random.randint(8, 12) + atributostotais["Inteligência"] + atributostotais["Sabedoria"]
        atributosjogador = {"HP":HP, "DEF":DEF, "ATK": ATK, "MAG":MAG}
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")

    return atributosjogador


def jogador(nome,raca,classe,atributos):
    fichajogador = {}
    atributos = atributosjogador
    if classe == "Guerreiro":
        fichajogador = {"Nome":nome,"Raça":raca,"Classe":classe,"Atributos":atributos,"Arma":"Espada"}

    if classe == "Feiticeiro":
        fichajogador = {"Nome":nome,"Raça":raca,"Classe":classe,"Atributos":atributos,"Arma":"Missil Magico"}

    if classe == "Ladino":
        fichajogador = {"Nome":nome,"Raça":raca,"Classe":classe,"Atributos":atributos,"Arma":"Adaga"}

    if classe == "Guardião":
        fichajogador = {"Nome":nome,"Raça":raca,"Classe":classe,"Atributos":atributos,"Arma":"Arco"}

    return fichajogador


def mochila(item):
    itens = []
    for lista in itens:
        lista = objeto,quantidade
        if item in itens:
            quantidade += 1
        elif item not in itens:
            itens.append([item,1])
    return itens



        
    










def morte():
    print ("Você Morreu")
    menu()



    


    
