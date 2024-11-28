# Importa os módulos necessários para o jogo
import personagem as p  # Módulo que lida com a criação e manipulação de personagens
import salvamento as s   # Módulo que lida com salvar e carregar jogos
import historia as h     # Módulo que pode lidar com a narrativa do jogo (não utilizado aqui)
import escolha as e      # Módulo que lida com as escolhas do jogador

# Função que exibe o menu principal do jogo
def menu():
    print("A Aventura")  # Título do jogo
    print("An Izac de Paula Game")  # Nome do criador do jogo
    print("Bem Vindo ao Menu inicial")  # Mensagem de boas-vindas
    print("Escolha uma das Opções")  # Instrução para o jogador
    print("1 - Novo Jogo")  # Opção para iniciar um novo jogo
    print("2 - Carregar Jogo")  # Opção para carregar um jogo salvo
    print("3 - Sair")  # Opção para sair do jogo

    while True:  # Loop para garantir que o jogador insira uma opção válida
        try:
            escolha = int(input("Digite a Opção Desejada: "))  # Solicita a escolha do jogador
            break  # Sai do loop se a entrada for válida
        
        except ValueError:  # Se a entrada não for um número
            print("Por favor, digite um número válido.")  # Solicita uma nova entrada

    # Estrutura de controle para lidar com a escolha do jogador
    match escolha:
        case 1:  # Se o jogador escolher a opção 1
            nome = p.nome()  # Solicita o nome do personagem
            raca = p.raca()  # Solicita a raça do personagem
            classe = p.classe()  # Solicita a classe do personagem
            atributos = p.atributos(raca, classe)  # Define os atributos com base na raça e classe
            jogador = p.jogador(nome, raca, classe, atributos)  # Cria um objeto jogador
            s.salvarjogo(jogador)  # Salva o jogo
            e.escolha1(jogador)  # Chama a função de escolhas para o jogador
            menu()  # Retorna ao menu após a escolha
        case 2:  # Se o jogador escolher a opção 2
            jogador = s.carregarjogo()  # Tenta carregar um jogo salvo
            if jogador:  # Se o carregamento for bem-sucedido
                print(f"Jogo carregado: {jogador}")  # Exibe informações do jogador carregado
                e.escolha1(jogador)  # Chama a função de escolhas para o jogador
        
        case 3:  # Se o jogador escolher a opção 3
            print("Saindo do jogo. Até a próxima!")  # Mensagem de despedida
            exit()  # Encerra o programa
        
        case _:  # Para qualquer outra opção inválida
            print("Opção inválida. Tente novamente.")  # Solicita que o jogador tente novamente

# Chama a função menu para iniciar o jogo
menu()