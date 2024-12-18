# Importa os módulos necessários para o jogo
import personagem as p  # Módulo que lida com a criação e manipulação de personagens
import salvamento as s   # Módulo que lida com salvar e carregar jogos
import escolha as e # Módulo que lida com as escolhas do jogador
from colorama import Fore # Importa a função Fore do módulo colorama
import time as t

# Função que exibe o menu principal do jogo
def menu():
    print(Fore.GREEN + "Medieval Self Adventure")  # Título do jogo
    print(Fore.GREEN +"An Izac de Paula Game")  # Nome do criador do jogo
    print(Fore.GREEN +"Bem Vindo ao Menu inicial")  # Mensagem de boas-vindas
    print(Fore.GREEN +"Escolha uma das Opções")  # Instrução para o jogador
    print(Fore.GREEN +"1 - Novo Jogo")  # Opção para iniciar um novo jogo
    print(Fore.GREEN +"2 - Carregar Jogo")  # Opção para carregar um jogo salvo
    print(Fore.GREEN +"3 - Sair")  # Opção para sair do jogo

    while True:  # Loop para garantir que o jogador insira uma opção válida
        try:
            escolha = int(input(Fore.GREEN +"Digite a Opção Desejada: "))  # Solicita a escolha do jogador
            break  # Sai do loop se a entrada for válida
        
        except ValueError:  # Se a entrada não for um número
            print(Fore.GREEN +"Por favor, digite um número válido.")  # Solicita uma nova entrada

    # Estrutura de controle para lidar com a escolha do jogador
    match escolha:
        case 1:  # Se o jogador escolher a opção 1
            nome = p.nome()  # Solicita o nome do personagem
            raca = p.raca()  # Solicita a raça do personagem
            classe = p.classe()  # Solicita a classe do personagem
            atributos = p.atributos(raca, classe)  # Define os atributos com base na raça e classe
            jogador = p.jogador(nome, raca, classe, atributos)  # Cria um objeto jogador
            s.salvarjogo(jogador)  # Salva o jogo
            print("\033c", end="") # Limpa o console
            t.sleep(2) # Cria um delay de 2 segundos
            e.escolha1(jogador)  # Chama a função de escolhas para o jogador
            menu()  # Retorna ao menu após a escolha
        case 2:  # Se o jogador escolher a opção 2
            jogador = s.carregarjogo()  # Tenta carregar um jogo salvo
            if jogador:  # Se o carregamento for bem-sucedido
                print(f"Jogo carregado: {jogador}")  # Exibe informações do jogador carregado
                print("\033c", end="") # Limpa o console
                t.sleep(2) # Cria um delay de 2 segundos
                e.escolha1(jogador)  # Chama a função de escolhas para o jogador
                menu()
        case 3:  # Se o jogador escolher a opção 3
            print(Fore.GREEN +"Saindo do jogo. Até a próxima!")  # Mensagem de despedida
            exit()  # Encerra o programa
        
        case _:  # Para qualquer outra opção inválida
            print(Fore.RED +"Opção inválida. Tente novamente.")  # Solicita que o jogador tente novamente

# Chama a função menu para iniciar o jogo
menu()