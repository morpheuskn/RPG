import personagem as p
import salvamento as s
import historia as h
import escolha as e

def menu():
    print("A Aventura")
    print("An Izac de Paula Game")
    print("Bem Vindo ao Menu inicial")
    print("Escolha uma das Opções")
    print("1 - Novo Jogo")
    print("2 - Carregar Jogo")
    print("3 - Sair")
    
    while True:
        try:
            escolha = int(input("Digite a Opção Desejada: "))
            break
        
        except ValueError:
            print("Por favor, digite um número válido.")

    match escolha:
        case 1:
            nome = p.nome()
            raca = p.raca()
            classe = p.classe()
            atributos = p.atributos(raca, classe)
            jogador = p.jogador(nome, raca, classe, atributos)
            s.salvarjogo(jogador)
            e.escolha1(jogador)
            menu()
        case 2:
            jogador = s.carregarjogo()
            if jogador:
                print(f"Jogo carregado: {jogador}")
                e.escolha1(jogador)
        
        case 3:
            print("Saindo do jogo. Até a próxima!")
            exit()
        
        case _:
            print("Opção inválida. Tente novamente.")

menu()