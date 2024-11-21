import historia as h
import personagem as p  # Presumindo que 'p' é um módulo que contém a função mostrarmochila
karma = 0
mochila = []  # Presumindo que mochila é uma lista que você vai usar

def atualizar_karma(valor):
    global karma
    karma += valor

def escolha1():
    print(h.capitulo1)
    print("1 - Eu aceito, irei e voltarei com a joia e a vitória em mãos.")
    print("2 - Fale-me mais sobre ?")
    print("3 - Nem fudendo, pelo menos não sem uma gorda recompensa.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha2()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha2()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha2()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha2()  # Chama a próxima escolha

def escolha2():
    print(h.capitulo2)
    print("1 - Um anunciante no porto, me guiou para cá. Me disse que há um trabalho para um mercenário errante como eu.")
    print("2 - Fale-me mais sobre tais audiências.")
    print("3 - Não porra, eu vim para papear com você. Não está na cara?")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha3()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha3()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha3()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha3()  # Chama a próxima escolha

def escolha3():
    print(h.capitulo3)
    print("1 - Vossa majestade, será uma honra por minha vida e minha habilidade ao ser dispor.")
    print("2 - Fale-me mais sobre tais recompensas.")
    print("3 - Bom, se as recompensas forem boas estou dentro.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha4()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha4()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha4()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha4()  # Chama a próxima escolha

def escolha4():
    print(h.capitulo4)
    print("1 - Tentar passar conversando.")
    print("2 - Tentar passar despercebido.")
    print("3 - Matar a todos.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha5()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha5()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha5()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha5()  # Chama a próxima escolha

def escolha5():
    print(h.capitulo5)
    print("1 - Investigar marcas no chão.")
    print("2 - Investigar pedaços de carne preta.")
    print("3 - Investigar os corpos dos soldados.")
    print("4 - Investigar as armas quebradas.")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha6()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha6()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha6()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha6()  # Chama a próxima escolha

def escolha6():
    print(h.capitulo6)
    print("1 - Lutar contra os demônios.")
    print("2 - Tentar se esconder.")
    print("3 - Tentar fugir.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha7()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha7()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha7()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha7()  # Chama a próxima escolha

def escolha7():
    print(h.capitulo7)
    print("1 - Seguir o Vulto.")
    print("2 - Ir para outro Corredor.")
    print("3 - Tentar fugir.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha8()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha8()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha8()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha8()  # Chama a próxima escolha

def escolha8():
    print(h.capitulo8)
    print("1 - Ir em Direção ao Livro.")
    print("2 - Tentar parar.")
    print("3 - Tentar ir na Direção Contrária.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha9()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha9()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha9()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha9()  # Chama a próxima escolha

def escolha9():
    print(h.capitulo9)
    print("1 - Então por que tudo isso?")
    print("2 - Então seu nome é Natasha, eu tive uma visão e isso é um livro?")
    print("3 - Se isso é verdade, eu sou o rei da Costa das Espadas.")
    print("4 - Você é um livro?")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            escolha10()  # Chama a próxima escolha
        case 2:
            atualizar_karma(0)
            escolha10()  # Chama a próxima escolha
        case 3:
            atualizar_karma(-1)
            escolha10()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha10()  # Chama a próxima escolha

def escolha10():
    print(h.capitulo10)
    print("1 - Seria uma honra.")
    print("2 - Por que?")
    print("3 - Não.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            atualizar_karma(1)
            # Aqui você pode decidir o que acontece após a última escolha
        case 2:
            atualizar_karma(0)
            # Aqui você pode decidir o que acontece após a última escolha
        case 3:
            atualizar_karma(-1)
            # Aqui você pode decidir o que acontece após a última escolha
        case 4:
            p.mostrarmochila(mochila)
            # Aqui você pode decidir o que acontece após a última escolha
