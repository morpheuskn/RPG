# Importa os módulos necessários para o jogo
import historia as h  # Importa o módulo 'historia' como 'h'
import personagem as p  # Importa o módulo 'personagem' como 'p'
import combates as c  # Importa o módulo 'combates' como 'c'
from colorama import Fore # Importa a função Fore do módulo colorama
import time as t

karma = 0  # Inicializa a variável karma com 0

mochila = []  # Inicializa a mochila como uma lista vazia

def atualizarkarma(valor):
    global karma  # Declara que vamos usar a variável global karma
    karma += valor  # Atualiza o karma com o valor recebido


def escolha1(jogador):
    print(Fore.GREEN + h.capitulo1)  # Exibe o primeiro capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Eu aceito, irei e voltarei com a joia e a vitória em mãos.")
    print(Fore.GREEN + "2 - Fale-me mais sobre ?")
    print(Fore.GREEN + "3 - Nem ferrando, pelo menos não sem uma gorda recompensa.")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha1(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Anunciante Real: Que discurso heroico, que suas palavras sejam verdades
e que você volte com a vitoria em mãos""")
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha2(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Anunciante Real: Não há muito mais a se falar sobre. El'goroth era uma das nossas cidades mais belas, até um incidente
que a deixou em ruinas. Porém o a noticia desse artefato é algo relativamente recente. Você está
pensando em aceitar a tarefa viajante ?
Você: Sim
Anunciante Real: Então que a sorte lhe acompanhe.""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha2(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Anunciante Real: Aposte que haverá um mar de tesouros para aquele que completar ardua tarefa.
Você: Então se é assim, que seja.""")
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha2(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.RED + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.RED + f"Erro relacionado aos atributos: {e}")
            except Exception as e:
                print(Fore.RED + f"Erro ao usar o item: {e}")
            finally:  # Exibe a mochila
                escolha1(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha1(jogador)  # Chama a próxima escolha

def escolha2(jogador):
    print(Fore.GREEN + h.capitulo2)  # Exibe o segundo capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Um anunciante no porto, me guiou para cá. Me disse que há um trabalho para um mercenário errante como eu.")
    print(Fore.GREEN + "2 - Fale-me mais sobre tais audiências.")
    print(Fore.GREEN + "3 - Não imagina, eu vim para papear com você. Não está na cara?")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha2(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Guarda: Então venha comigo, mercenario.""")
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha3(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Guarda: Essas audiências, são momentos em que vossa ilustríssima majestade, ouve, delibera e
atende a pedidos da população. Veio para uma ?
Você: Eu vim me candidatar, para ir para El'goroth.
Guarda: Então venha comigo, mercenario.""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha3(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Guarda: Um engraçadinho, talvez fique menos engraçado passando uns tempos nos calabouços.
Você: Eu vim para falar sobre El'goroth.
Guarda: Venha mercenario.""")
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha3(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.RED + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.RED + f"Erro relacionado aos atributos: {e}")
            except Exception as e:
                print(Fore.RED + f"Erro ao usar o item: {e}")
            finally:  # Exibe a mochila
                escolha2(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha2(jogador)  # Chama a próxima escolha

def escolha3(jogador):
    print(Fore.GREEN + h.capitulo3)  # Exibe o terceiro capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Vossa majestade, será uma honra por minha vida e minha habilidade ao ser dispor.")
    print(Fore.GREEN + "2 - Fale-me mais sobre tais recompensas.")
    print(Fore.GREEN + "3 - Bom, se as recompensas forem boas estou dentro.")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha3(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Rei Dio: Pois bem heroi, lhe daremos um cavalo e a bênção real. Vá e traga minha filha.""")
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha4(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Rei Dio: Um castelo, um título ducal e muito ouro.
Você: Eu aceito.
Rei Dio: Pois bem, lhe daremos um cavalo e a bênção real. Vá e traga minha filha.""")
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha4(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Rei Dio: Um homem movido a ouro e glórias.
Pois bem, lhe daremos um cavalo e a bênção real. Vá e traga minha filha.""")
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha4(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha3(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha3(jogador)  # Chama a próxima escolha

def escolha4(jogador):
    print(Fore.GREEN + h.capitulo4)  # Exibe o quarto capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Tentar passar conversando.")
    print(Fore.GREEN + "2 - Tentar passar despercebido.")
    print(Fore.GREEN + "3 - Matar a todos.")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha4(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Esidisi: Pare. Entregue tudo ou perderá a sua vida.
Você: Eu posso matar todos vocês, ou posso voltar chamar a guarda real e aí eles vão matar a maioria
e prender o resto.
Esidisi: Quem é você ?
Você: Eu sou o mercenário enviado pelo rei, para resolver a questão de El'goroth.
Santana: Esidisi, deixe esse homem passar. Alguém que aceita uma tarefa dessas é muito poderoso ou muito louco. De qualquer forma, não vale a pena.""")
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha5(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Você utiliza uma trilha em meio a floresta para contornar o cerco bandido e consegue.""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha5(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Você parte para cima dos quatro bandidos.""")
            try:
                c.combate(jogador, c.bandidoberserker)  # Inicia combate com o Bandido Berserker
                c.combate(jogador, c.bandidoguerreiro)  # Inicia combate com o Bandido Guerreiro
                c.combate(jogador, c.bandidoarqueiro)  # Inicia combate com o Bandido Arqueiro
                c.combate(jogador, c.bandidomago)  # Inicia combate com o Bandido Mago
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha5(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha4(jogador)
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha4(jogador)  # Chama a próxima escolha

def escolha5(jogador):
    print(Fore.GREEN + h.capitulo5)  # Exibe o quinto capítulo da história
    repeticao = 0  # Inicializa a contagem de repetições
    while repeticao <= 10:  # Loop até que a repetição atinja 10
        # Apresenta as opções para o jogador
        print(Fore.GREEN + "1 - Investigar marcas no chão.")
        print(Fore.GREEN + "2 - Investigar pedaços de carne preta.")
        print(Fore.GREEN + "3 - Investigar os corpos dos soldados.")
        print(Fore.GREEN + "4 - Investigar as armas quebradas.")
        
        try:
            resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
        except ValueError:
            print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
            continue  # Retorna ao início do loop

        match resposta:  # Verifica a resposta do jogador
            case 1:
                print(Fore.GREEN + """Você percebe que essas são marcas das carruagens,
você percebe que essas marcas vem de El'goroth.""")
                repeticao += 1  # Aumenta a contagem de repetições
                atualizarkarma(0)  # Não altera o karma
            case 2:
                print(Fore.GREEN + """Você vê que os pedaços das criaturas mortas,
não se parecem com nada que você tenha visto.""")
                repeticao += 2  # Aumenta a contagem de repetições
                atualizarkarma(0)  # Não altera o karma
            case 3:
                print(Fore.GREEN + """Você vasculha os restos mortais dos soldados,
e encontra as ordens de escoltarem a princesa e
a joia de El'goroth para o castelo real.""")
                repeticao += 3  # Aumenta a contagem de repetições
                atualizarkarma(0)  # Não altera o karma
            case 4:
                print(Fore.GREEN + """Você investiga as armas abandonadas, e percebe
que elas foram quebradas por magia poderosa e força imensa.""")
                repeticao += 4  # Aumenta a contagem de repetições
                atualizarkarma(0)  # Não altera o karma
            case _:
                print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro

        if repeticao >= 10:  # Se a contagem de repetições atingir 10
            print (Fore.GREEN + """Você percebe que os adversários dos soldados eram coisas
que não eram desse mundo, com magia e força fora do comum.
Tudo leva a crer que eles voltaram para El'goroth.""")
            break  # Sai do loop
    t.sleep(5)
    print("\033c", end="")
    escolha6(jogador)  # Chama a próxima escolha

def escolha6(jogador):
    print(Fore.GREEN + h.capitulo6)  # Exibe o sexto capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Lutar contra os demônios.")
    print(Fore.GREEN + "2 - Tentar se esconder.")
    print(Fore.GREEN + "3 - Tentar fugir.")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha6(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Você os ataca.""")
            try:
                c.combate(jogador, c.caomagico)  # Inicia combate com o cão mágico
                c.combate(jogador, c.caoguerreiro) # Inicia combate com o cão guerreiro
                c.combate(jogador, c.caoberserker) # Inicia combate com o cão berserker
                c.combate(jogador, c.caoarqueiro)  # Inicia combate com o cão arqueiro
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha7(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Você rapidamente se esconde no alto de uma árvore próxima,
até que os cães vão embora. Depois disso você desce e segue o seu caminho.""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha7(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Você rapidamente corre, os cães correm atrás. Mas você
consegue os despistar. Depois disso você desce e segue o seu caminho.""")
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha7(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha6(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha6(jogador)  # Chama a próxima escolha

def escolha7(jogador):
    print(Fore.GREEN + h.capitulo7)  # Exibe o sétimo capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Seguir o Vulto.")
    print(Fore.GREEN + "2 - Ir para outro Corredor.")
    print(Fore.GREEN + "3 - Tentar fugir.")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha7(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Você segue o vulto, mas ele desaparece em frente a uma estante.""")
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha8(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Você vai avançando por outro corredor e acaba em frente a uma estante.""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha8(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Você tenta fugir, mas acaba entrando mais na biblioteca.
E para em frente a uma estante.""")
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha8(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha7(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha7(jogador)  # Chama a próxima escolha

def escolha8(jogador):
    print(Fore.GREEN + h.capitulo8)  # Exibe o oitavo capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Ir em Direção ao Livro.")
    print(Fore.GREEN + "2 - Tentar parar.")
    print(Fore.GREEN + "3 - Tentar ir na Direção Contrária.")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha8(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Você chega mais e mais perto do livro. Você sente uma vontade irresistível de tocá-lo.""")
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha9(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Você não consegue se conter e chega mais e mais perto do livro.
Você sente uma vontade irresistível de tocá-lo.""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha9(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Você não consegue se conter e chega mais e mais perto do livro.
Você sente uma vontade irresistível de tocá-lo.""")
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha9(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha8(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha8(jogador)  # Chama a próxima escolha

def escolha9(jogador):
    print(Fore.GREEN + h.capitulo9)  # Exibe o nono capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Então por que tudo isso?")
    print(Fore.GREEN + "2 - Então seu nome é Natasha, eu tive uma visão e isso é um livro?")
    print(Fore.GREEN + "3 - Se isso é verdade, eu sou o rei da Costa das Espadas.")
    print(Fore.GREEN + "4 - Você é um livro?")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha9(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Natasha: Finalmente você fez a pergunta correta.""")
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha10(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Natasha: Achei que tinha ficado óbvio já que eu acabei de dizer isso.""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha10(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Natasha: Ah é, vossa majestade senhor da comédia.""")
            atualizarkarma(-2)  # Dimin ui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha10(jogador)  # Chama a próxima escolha
        case 4:
            print(Fore.GREEN + """Natasha: Você não é muito inteligente, né.""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha10(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha9(jogador)  # Chama a próxima escolha

def escolha10(jogador):
    print(Fore.GREEN + h.capitulo10)  # Exibe o décimo capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Seria uma honra.")
    print(Fore.GREEN + "2 - Por que?")
    print(Fore.GREEN + "3 - Não.")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha10(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Natasha: Obrigada""")
            p.adicionarmochila("Livro Mágico", mochila)  # Adiciona o livro mágico à mochila
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha11(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Natasha: Eu vi isso começar, e quero ver como termina.
Você: Se é assim, sim.""")
            p.adicionarmochila("Livro Mágico", mochila)  # Adiciona o livro mágico à mochila
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha11(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Natasha: Você se arrependerá por isso.""")
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha11(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha10(jogador)  # Chama a próxima escolha

        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha10(jogador)  # Chama a próxima escolha

def escolha11(jogador):
    print(Fore.GREEN + h.capitulo11)  # Exibe o décimo primeiro capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Atacar na Surdina")
    print(Fore.GREEN + "2 - Atacar frontalmente")
    print(Fore.GREEN + "3 - Dar a Volta")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha11(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Você ataca a criatura das sombras, um ataque meticulosamente calculado para acertar a cabeça""")
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha12(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Você ataca a criatura frontalmente.""")
            try:
                c.combate(jogador, c.kladu)  # Inicia combate com o Kladu
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha12(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Você se esconde da criatura, usando destroços como esconderijo. Até conseguir fugir dele.""")
            atualizarkarma (-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha12(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha11(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha11(jogador)  # Chama a próxima escolha

def escolha12(jogador):
    print(Fore.GREEN + h.capitulo12)  # Exibe o décimo segundo capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Nós Iremos Lutar")
    print(Fore.GREEN + "2 - O quê Vocês irão Fazer ?")
    print(Fore.GREEN + "3 - Eu me Juntarei a Vocês")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha12(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Você: Então que assim seja.""")
            try:
                c.combate(jogador, c.anungunrama)  # Inicia combate com o Anung Un Rama
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha13(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Anung Un Rama: Para libertar a nossa irmã e trazer nosso mundo para o seu.
Você: Por que ?
Anung Un Rama: Porque é a nossa natureza. Agora devemos lutar.""")
            try:
                c.combate(jogador, c.anungunrama)  # Inicia combate com o Anung Un Rama
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha13(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Anung Un Rama: Um homem que trai a sua própria espécie, não é digno da nossa.""")
            try:
                c.combate(jogador, c.anungunrama)  # Inicia combate com o Anung Un Rama
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha13(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha12(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha12(jogador)  # Chama a próxima escolha

def escolha13(jogador):
    print(Fore.GREEN + h.capitulo13)  # Exibe o décimo terceiro capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Lutar")
    print(Fore.GREEN + "2 - Fazer os Bestas lutarem com o próprio mestre")
    print(Fore.GREEN + "3 - Fugir")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha13(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Você: Então que assim seja.""")
            try:
                c.combate(jogador, c.zodd)  # Inicia combate com o Zodd
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha14(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Você apaga a sua tocha, e faz barulhos atraindo as bestas. Quando elas correm atrás de você.
Você começa a correr, atraindo as bestas em direção a Zodd""")
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha14(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Você apaga a sua tocha, e sai correndo para trás de Zodd. Quando ele parte para te atacar,
você derruba as paredes da caverna em cima de Zodd e suas bestas.""")
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha14(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha13(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha13(jogador)  # Chama a próxima escolha

def escolha14(jogador):
    print(Fore.GREEN + h.capitulo14)  # Exibe o décimo quarto capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Lutar")
    print(Fore.GREEN + "2 - Por que ?")
    print(Fore.GREEN + "3 - Fugir")
    print(Fore.GREEN + "4 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha14(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Você: Então que assim seja.""")
            try:
                c.combate(jogador, c.khan)  # Inicia combate com o Khan
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(2)  # Aumenta o karma
            t.sleep(5)
            print("\033c", end="")
            escolha15(jogador)  # Chama a próxima escolha
        case 2:
            print(Fore.GREEN + """Khan: Porque sim. Você se questiona quando mata formigas. Para nós vocês não passam
disso.""")
            try:
                c.combate(jogador, c.khan)  # Inicia combate com o Khan
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            p.adicionarmochila("Poção de Cura", mochila)
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            escolha15(jogador)  # Chama a próxima escolha
        case 3:
            print(Fore.GREEN + """Você corre, prestes a ser atacado por Khan, você ataca as paredes em volta dele, 
                  fazendo com que parte do túnel desabe o soterrando.""")
            atualizarkarma(-2)  # Diminui o karma
            t.sleep(5)
            print("\033c", end="")
            escolha15(jogador)  # Chama a próxima escolha
        case 4:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                # Verifica se o item está na mochila
                encontrado = False
                for pertence in mochila:
                    if pertence[0] == item:  # Confirma se o nome do item é encontrado
                        p.usaritem(item, mochila, jogador["Atributos"])  # Chama a função para usar o item
                        print(Fore.GREEN + f"Você usou o item: {item}")
                        encontrado = True
                        break  # Sai do loop após encontrar o item

                if not encontrado:  # Caso o item não seja encontrado
                    print(Fore.GREEN + "Item não encontrado na mochila.")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha14(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha14(jogador)  # Chama a próxima escolha

def escolha15(jogador):
    print(Fore.GREEN + h.capitulo15)  # Exibe o décimo quinto capítulo da história
    # Apresenta as opções para o jogador
    print(Fore.GREEN + "1 - Nós Iremos Lutar ")
    print(Fore.GREEN + "2 - Inventário")
    
    try:
        resposta = int(input(Fore.GREEN + "O que Você Fará ? "))  # Recebe a escolha do jogador
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
        escolha15(jogador)
        return

    match resposta:  # Verifica a resposta do jogador
        case 1:
            print(Fore.GREEN + """Você: Eu vou terminar isso agora.""")
            try:
                c.combate(jogador, c.astaorth)  # Inicia combate com o Astaroth
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro durante o combate: {e}")
                return
            atualizarkarma(0)  # Não altera o karma
            t.sleep(5)
            print("\033c", end="")
            final(jogador, karma, mochila)  # Chama a função final
        case 2:
            try:
                p.mostrarmochila(mochila)  # Exibe a mochila
                item = input(Fore.GREEN + "Digite o Nome do Item que quer Usar ou para sair digite Sair: ")
                for pertence in mochila:
                    if item not in pertence:
                        print(Fore.GREEN + "Item não encontrado na mochila.")
                        continue
                    else:
                        p.usaritem(item, mochila, jogador["Atributos"])
                        print(Fore.GREEN + f"Você usou o item: {item}")
            except AttributeError as e:
                print(Fore.GREEN + f"Erro relacionado a atributos: {e}")
            except Exception as e:
                print(Fore.GREEN + f"Ocorreu um erro ao usar o item: {e}")
            finally:
                escolha15(jogador)  # Chama a próxima escolha
        case _:
            print(Fore.RED + "Opção inválida. Tente novamente.")  # Mensagem de erro
            escolha15(jogador)  # Chama a próxima escolha

def final(jogador, karma, mochila):
    print(Fore.GREEN + f"Karma final: {karma}")  # Exibe o karma final
    for livro in mochila:  # Verifica os itens na mochila
        if "Livro Magico" in livro:  # Se o livro mágico estiver na mochila
            if karma > 14:
                print(Fore.GREEN + h.finalbomlivro)  # Exibe final bom com livro
            elif -14 <= karma <= 14:
                print(Fore.GREEN + h.finalmaisoumenoslivro)  # Exibe final mais ou menos com livro
            else:
                print(Fore.GREEN + h.finalruimlivro)  # Exibe final ruim com livro
        elif "Livro Magico" not in livro:
            if karma > 14:
                print(Fore.GREEN + h.finalbom)  # Exibe final bom sem livro
            elif -14 <= karma <= 14:
                print(Fore.GREEN + h.finalmaisoumenos)  # Exibe final mais ou menos sem livro
            else:
                print(Fore.GREEN + h.finalruim)  # Exibe final ruim sem livro

    print(Fore.GREEN + "Fim do jogo.")  # Mensagem de fim de jogo
    exit()  # Encerra o programa