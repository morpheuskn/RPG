import historia as h
import personagem as p
import combates as c
import salvamento as s
jogador = s.carregarjogo()
karma = 0
mochila = []  

def atualizarkarma(valor):
    global karma
    karma += valor

def escolha1():
    print(h.capitulo1)
    print("1 - Eu aceito, irei e voltarei com a joia e a vitória em mãos.")
    print("2 - Fale-me mais sobre ?")
    print("3 - Nem ferrando, pelo menos não sem uma gorda recompensa.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Anunciante Real: Que discurso heroico, que suas palavras sejam verdades
                  e que você volte com a vitoria em mãos""")
            atualizarkarma(2)
            escolha2()  # Chama a próxima escolha
        case 2:
            print("""Anunciante Real: Não há muito mais a se falar sobre. El'goroth era uma das nossas cidades mais belas, até um incidente
que a deixou em ruinas. Porém o a noticia desse artefato é algo relativamente recente. Você está
pensando em aceitar a tarefa viajante ?
Você: Sim
Anunciante Real: Então que a sorte lhe acompanhe.""")
            atualizarkarma(0)
            escolha2()  # Chama a próxima escolha
        case 3:
            print("""Anunciante Real: Aposte que haverá um mar de tesouros para aquele que completar ardua tarefa.
Você: Então se é assim, que seja.""")
            atualizarkarma(-2)
            escolha2()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha1()  # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha1()

def escolha2():
    print(h.capitulo2)
    print("1 - Um anunciante no porto, me guiou para cá. Me disse que há um trabalho para um mercenário errante como eu.")
    print("2 - Fale-me mais sobre tais audiências.")
    print("3 - Não imagina, eu vim para papear com você. Não está na cara?")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Guarda: Então venha comigo, mercenario.""")
            atualizarkarma(2)
            escolha3()  # Chama a próxima escolha
        case 2:
            print("""Guarda: Essas audiencias, são momentos em que vossa ilustríssima majestade, ouve, delibera e
atende a pedidos da populacão. Veio para uma ?
Você: Eu vim me candidatar, para ir para El'goroth.
Guarda: Então venha comigo, mercenario.""")
            atualizarkarma(0)
            escolha3()  # Chama a próxima escolha
        case 3:
            print("""Guarda: Um engraçadinho, talvez fique menos engraçado passando uns tempos nos calabuços.
Você: Eu vim para falar sobre El'goroth.
Guarda: Venha mercenario.""")
            atualizarkarma(-2)
            escolha3()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha2()  # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha2()

def escolha3():
    print(h.capitulo3)
    print("1 - Vossa majestade, será uma honra por minha vida e minha habilidade ao ser dispor.")
    print("2 - Fale-me mais sobre tais recompensas.")
    print("3 - Bom, se as recompensas forem boas estou dentro.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Rei Dio: Pois bem heroi, lhe daremos um cavalo e a bensão real. Vá e traga minha filha.""")
            atualizarkarma(2)
            escolha4()  # Chama a próxima escolha
        case 2:
            print("""Rei Dio: Um castelo, um titulo ducal e muito ouro.
Você: Eu aceito.
Rei Dio: Pois bem, lhe daremos um cavalo e a bensão real. Vá e traga minha filha.""")
            atualizarkarma(0)
            escolha4()  # Chama a próxima escolha
        case 3:
            print("""Rei Dio: Um homem movido a ouro e glorias.
Pois bem, lhe daremos um cavalo e a bensão real. Vá e traga minha filha.""")
            atualizarkarma(-2)
            escolha4()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha3()  # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha3()

def escolha4():
    print(h.capitulo4)
    print("1 - Tentar passar conversando.")
    print("2 - Tentar passar despercebido.")
    print("3 - Matar a todos.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Esidisi: Pare. Entregue tudo ou perderá a sua vida.
Você: Eu posso matar todos vocês, ou posso voltar chamar a guarda real e aí eles vão matar a maioria
e prender o resto.
Esidisi: Quem é você ?
Você: Eu sou o mercenario enviado pelo rei, para resolver a questão de El'goroth.
Santana: Esidisi, deixe esse homem passar. Alguém que aceita uma tarefa dessas é muito poderoso
ou muito louco. De qualquer forma, não vale a pena.""")
            atualizarkarma(2)
            escolha5()  # Chama a próxima escolha
        case 2:
            print("""Você utiliza uma trilha em meio a floresta para contornar o cerco bandido e consegue.""")
            atualizarkarma(0)
            escolha5()  # Chama a próxima escolha
        case 3:
            print("""Você parte para cima dos quatro bandidos.""")
            c.combate(jogador, c.orcberserker)
            c.combate(jogador, c.orcguerreiro)
            c.combate(jogador, c.orcarqueiro)
            c.combate(jogador, c.orcmago)
            atualizarkarma(-2)
            escolha5()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha4()  # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha4()

def escolha5():
    print(h.capitulo5)
    repeticao = 0
    while repeticao <= 10:
        print("1 - Investigar marcas no chão.")
        print("2 - Investigar pedaços de carne preta.")
        print("3 - Investigar os corpos dos soldados.")
        print("4 - Investigar as armas quebradas.")
        resposta = int(input("O que Você Fará ? "))
        match resposta:
            case 1:
                print("""Você percebe que essas são marcas das carruagens,
você percebe que essas marcas vem de El'goroth.""")
                repeticao += 1
                atualizarkarma(1)
            case 2:
                print("""Você vê que os pedaços das criaturas mortas,
não se parecem com nada que você tenha visto.""")
                repeticao += 2
                atualizarkarma(1)
            case 3:
                print("""Você vasculha os restos mortais dos soldados,
e encontra as ordens de escoltarem a princesa e
a joia de El'goroth para o castelo real.""")
                repeticao += 3
                atualizarkarma(1)
            case 4:
                print("""Você investiga as armas abandonadas, e percebe
que elas foram quebradas por magia poderosa e força imensa.""")
                repeticao += 4
                atualizarkarma(1)
            case _:
                print("Opção inválida. Tente novamente.")
        if repeticao >= 10:
            print("""Você percebe que os adversarios dos soldados eram coisas
que não eram desse mundo, com magia e força fora do comum.
Tudo leva a crer que eles voltaram para El'goroth.""")
            break
    escolha6()

def escolha6():
    print(h.capitulo6)
    print("1 - Lutar contra os demônios.")
    print("2 - Tentar se esconder.")
    print("3 - Tentar fugir.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Você os ataca.""")
            c.combate(jogador, c.caomagico)
            c.combate(jogador, c.caoguerreiro)
            atualizarkarma(2)
            escolha7()  # Chama a próxima escolha
        case 2:
            print("""Você rapidamente se esconde no alto de uma arvore proxima,
até que os cães vão embora. Depois disso você desce e segue o seu caminho.""")
            atualizarkarma(0)
            escolha7()  # Chama a próxima escolha
        case 3:
            print("""Você rapidamente corre, os cães correm atrás. Mas você
consegue os despistar. Depois disso você desce e segue o seu caminho.""")
            atualizarkarma(-2)
            escolha7()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha6()  # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha6()

def escolha7():
    print(h.capitulo7)
    print("1 - Seguir o Vulto.")
    print("2 - Ir para outro Corredor.")
    print("3 - Tentar fugir.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Você segue o vulto, mas ele desaparece em frente uma estante.""")
            atualizarkarma(2)
            escolha8()  # Chama a próxima escolha
        case 2:
            print("""Você vai avançando por outro corredor e acaba em frente a uma estante.""")
            atualizarkarma(0)
            escolha8()  # Chama a próxima escolha
        case 3:
            print("""Você tenta fugir, mas acaba entrando mais na biblioteca.
E para em frente a uma estante.""")
            atualizarkarma(-2)
            escolha8()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha7()  # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha7()

def escolha8():
    print(h.capitulo8)
    print("1 - Ir em Direção ao Livro.")
    print("2 - Tentar parar.")
    print("3 - Tentar ir na Direção Contrária.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Você chega mais e mais perto do livro. Você sente uma vontade irresistivel de toca-lo.""")
            atualizarkarma(2)
            escolha9()  # Chama a próxima escolha
        case 2:
            print("""Você não consegue se conter e chega mais e mais perto do livro.
Você sente uma vontade irresistivel de toca-lo.""")
            atualizarkarma(0)
            escolha9()  # Chama a próxima escolha
        case 3:
            print("""Você não consegue se conter e chega mais e mais perto do livro.
Você sente uma vontade irresistivel de toca-lo.""")
            atualizarkarma(-2)
            escolha9()  # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha8()  # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha8()

def escolha9():
    print(h.capitulo9)
    print("1 - Então por que tudo isso?")
    print("2 - Então seu nome é Natasha, eu tive uma visão e isso é um livro?")
    print("3 - Se isso é verdade, eu sou o rei da Costa das Espadas.")
    print("4 - Você é um livro?")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Natasha: Finalmente você fez a pergunta correta.""")
            atualizarkarma(2)
            escolha10()  # Chama a próxima escolha
        case 2:
            print("""Natasha: Achei que tinha ficado obvio já que eu acabei de dizer isso.""")
            atualizarkarma(0)
            escolha10()  # Chama a próxima escolha
        case 3:
            print("""Natasha: Ah é, vossa majestade senhor da comedia.""")
            atualizarkarma(-2)
            escolha10()  # Chama a próxima escolha
        case 4:
            print("""Natasha: Você não é muito inteligente, né.""")
            atualizarkarma(0)
            escolha9()  # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha9()

def escolha10():
    print(h.capitulo10)
    print("1 - Seria uma honra.")
    print("2 - Por que?")
    print("3 - Não.")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Natasha: Obrigada""")
            p.adicionarmochila("Livro Magico", mochila)
            atualizarkarma(2) # Chama a próxima escolha
            escolha11()
        case 2:
            print("""Natasha: Eu vi isso começar, e quero ver como termina.
Você: Se é assim, sim.""")
            p.adicionarmochila("Livro Magico", mochila)
            atualizarkarma(0) # Chama a próxima escolha
            escolha11()
        case 3:
            print("""Natasha: Você se arrependerá por isso.""")
            atualizarkarma(-2) # Chama a próxima escolha
            escolha11()
        case 4:
            p.mostrarmochila(mochila) # Chama a próxima escolha
            escolha10()
        case _:
            print("Opção inválida. Tente novamente.")
            escolha10()

def escolha11():
    print(h.capitulo11)
    print("1 - Atacar na Surdina")
    print("2 - Atacar frontalmente")
    print("3 - Dar a Volta")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Você ataca a criatura da sombras, um ataque meticulosamente calculado para acertar a cabeça""")
            atualizarkarma(2) # Chama a próxima escolha
            escolha12()
        case 2:
            print("""Você ataca a criatura frontalmente.""")
            c.combate(jogador, c.orcberserker)
            atualizarkarma(0) # Chama a próxima escolha
            escolha12()
        case 3:
            print("""Você se esconde da criatura, usando destroços como esconderijo. Até conseguir fugir dele.""")
            atualizarkarma(-2) # Chama a próxima escolha
            escolha12()
        case 4:
            p.mostrarmochila(mochila) # Chama a próxima escolha
            escolha11()
        case _:
            print("Opção inválida. Tente novamente.")
            escolha11()

def escolha12():
    print(h.capitulo12)
    print("1 - Nós Iremos Lutar")
    print("2 - O quê Vocês irão Fazer ?")
    print("3 - Eu me Juntarei a Vocês")
    print("4 - Inventário")
    resposta = int(input("O que Você Fará ? "))
    match resposta:
        case 1:
            print("""Você: Então que assim seja.""")
            c.combate(jogador, c.orcguerreiro)
            atualizarkarma(2)
            escolha13() # Chama a próxima escolha
        case 2:
            print("""Anung Un Rama: Para libertar a nossa irmã e trazer nosso mundo para o seu.
Você: Por que ?
Anung Un Rama: Porque é a nossa natureza. Agora devemos lutar.""")
            c.combate(jogador, c.orcguerreiro)
            atualizarkarma(0)
            escolha13() # Chama a próxima escolha
        case 3:
            print("""Anung Un Rama: Um homem que traí a sua propria especie, não é digno da nossa.""")
            c.combate(jogador, c.orcguerreiro)
            atualizarkarma(-2)
            escolha13() # Chama a próxima escolha
        case 4:
            p.mostrarmochila(mochila)
            escolha12() # Chama a próxima escolha
        case _:
            print("Opção inválida. Tente novamente.")
            escolha12()
