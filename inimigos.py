import random as r

def gerarinimigo(dificuldade):
    # Definindo as raças e classes disponíveis para os inimigos
    racas = ["Goblin", "Orc", "Lobo", "Esqueleto"]
    classes = ["Guerreiro", "Mago", "Arqueiro", "Berserker"]

    # Escolhendo uma raça e classe aleatoriamente
    raca = r.choice(racas)
    classe = r.choice(classes)

    # Gerando atributos baseados na dificuldade
    if classe == "Guerreiro" or classe == "Arqueiro" or classe == "Berserker":
       HP = r.randint(10 + dificuldade * 2, 15 + dificuldade * 3)
       DEF = r.randint(3 + dificuldade, 5 + dificuldade * 2)
       ATK = r.randint(2 + dificuldade, 5 + dificuldade)
       MAG = 0

    if classe == "Mago":
       HP = r.randint(10 + dificuldade * 2, 15 + dificuldade * 3)
       DEF = r.randint(3 + dificuldade, 5 + dificuldade * 2)
       ATK = 0
       MAG = r.randint(2 + dificuldade, 5 + dificuldade)

    # Criando o dicionário do inimigo
    inimigo = {
        "Nome": f"{raca} {classe}",
        "Raça": raca,
        "Classe": classe,
        "Atributos": {
            "HP": HP,
            "DEF": DEF,
            "ATK": ATK,
            "MAG": MAG  # Para simplicidade, não estamos usando magia aqui
        }
    }

    return inimigo


print(gerarinimigo(1))
print(gerarinimigo(1))
print(gerarinimigo(1))
print(gerarinimigo(1))

print(gerarinimigo(2))
print(gerarinimigo(2))
print(gerarinimigo(2))
print(gerarinimigo(2))

print(gerarinimigo(3))
print(gerarinimigo(3))
print(gerarinimigo(3))
print(gerarinimigo(3))

print(gerarinimigo(4))
print(gerarinimigo(4))
print(gerarinimigo(4))
print(gerarinimigo(4))
