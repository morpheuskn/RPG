''' Importa o módulo Random como a variável r. '''
import random as r

''' Função nome é responsável por criar o nome do personagem do jogador '''

def nome():
    nomepersonagem = input("Digite o Nome do Personagem: ")
    return nomepersonagem

''' Função raça é responsável pela escolha da raça'''

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

''' Função classe é responsável pela escolha da classe do personagem '''

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

    atributostotais = {}
    for atributo in atributosraca[raca]:
        atributostotais[atributo] = atributosraca[raca][atributo] + atributosclasse[classe][atributo]

    if classe == "Guerreiro":
        HP = r.randint(20, 25) + atributostotais["Constituição"]
        DEF = r.randint(25, 30) + atributostotais["Destreza"]
        ATK = r.randint(4, 8) + atributostotais["Força"] + atributostotais["Destreza"]
        MAG = atributostotais["Inteligência"] + atributostotais["Carisma"]
        atributosjogador = {"HP": HP, "DEF": DEF, "ATK": ATK, "MAG": MAG}
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")

    elif classe == "Feiticeiro":
        HP = r.randint(15, 20) + atributostotais["Constituição"]
        DEF = r.randint(20, 25) + atributostotais["Destreza"]
        ATK = atributostotais["Força"]
        MAG = r.randint(10, 15) + atributostotais["Inteligência"] + atributostotais["Carisma"]
        atributosjogador = {"HP": HP, "DEF": DEF, "ATK": ATK, "MAG": MAG}
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")

    elif classe == "Ladino":
        HP = r.randint(20, 25) + atributostotais["Constituição"]
        DEF = r.randint(20, 25) + atributostotais["Destreza"]
        ATK = r.randint(4, 8) + atributostotais["Força"] + atributos_totais["Inteligência"]
        MAG = atributostotais["Inteligência"] + atributostotais["Carisma"] + atributostotais["Sabedoria"]
        atributosjogador = {"HP": HP, "DEF": DEF, "ATK": ATK, "MAG": MAG}
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")

    elif classe == "Guardião":
        HP = r.randint(15, 20) + atributostotais["Constituição"]
        DEF = r.randint(15, 20) + atributostotais["Destreza"]
        ATK = r.randint(4, 8) + atributostotais["Força"] + atributostotais["Destreza"]
        MAG = r.randint(8, 12) + atributostotais["Inteligência"] + atributostotais["Sabedoria"]
        atributosjogador = {"HP": HP, "DEF": DEF, "ATK": ATK, "MAG": MAG}
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")

    return atributosjogador

def jogador(nome, raca, classe, atributos):
    fichajogador = {}
    if classe == "Guerreiro":
        fichajogador = {"Nome": nome, "Raça": raca, "Classe": classe, "Atributos": atributos, "Arma": "Espada"}

    elif classe == "Feiticeiro":
        fichajogador = {"Nome": nome, "Raça": raca, "Classe": classe, "Atributos": atributos, "Arma": "Missil Magico"}

    elif classe == "Ladino":
        fichajogador = {"Nome": nome, "Raça": raca, "Classe": classe, "Atributos": atributos, "Arma": "Adaga"}

    elif classe == "Guardião":
        fichajogador = {"Nome": nome, "Raça": raca, "Classe": classe, "Atributos": atributos, "Arma": "Arco"}

    return fichajogador

def adicionarmochila(item):
    mochila = []
    quantidade = 0
    for objeto in mochila:
        if objeto[0] == item:
            quantidade += 1
            objeto[1] = quantidade
            break
    else:
        mochila.append([item, 1])
        print(f"{item} foi adicionado a sua mochila.")
    return mochila

def mostrarmochila():
    mochila = adicionarmochila(item)
    if mochila:
        print("Mochila:")
        for item in mochila:
            print(f"- {item}")
    else:
        print("Sua Mochila está vazio.")


def morte():
    print("Você Morreu")
    

def ataque(atacante, defensor):
    dano = max(atacante["Atributos"]["ATK"] - defensor["Atributos"]["DEF"], 0)
    defensor["Atributos"]["HP"] -= dano
    return dano

def combate(jogador, inimigo):
    print(f"Iniciando combate entre {jogador['Nome']} e {inimigo['Nome']}!")
    
    while jogador["Atributos"]["HP"] > 0 and inimigo["Atributos"]["HP"] > 0:
        dano = ataque(jogador, inimigo)
        print(f"{jogador['Nome']} ataca {inimigo['Nome']} causando {dano} de dano.")
        print(f"{inimigo['Nome']} tem {inimigo['Atributos']['HP']} HP restantes.")
        
        if inimigo["Atributos"]["HP"] <= 0:
            print(f"{inimigo['Nome']} foi derrotado!")
            break
        
        dano = ataque(inimigo, jogador)
        print(f"{inimigo['Nome']} ataca {jogador['Nome']} causando {dano} de dano.")
        print(f"{jogador['Nome']} tem {jogador['Atributos']['HP']} HP restantes.")
        
        if jogador["Atributos"]["HP"] <= 0:
            print(f"{jogador['Nome']} foi derrotado!")
            break
