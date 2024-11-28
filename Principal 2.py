import personagem as p
import salvamento as s
import historia as h
import escolha as e

class Jogo:
    def __init__(self):
        self.jogador = None

    def menu(self):
        print("A Aventura")
        print("An Izac de Paula Game")
        print("Bem Vindo ao Menu inicial")
        
        while True:
            self.exibir_menu()
            escolha = self.obter_escolha()

            if escolha == 1:
                self.novo_jogo()
            elif escolha == 2:
                self.carregar_jogo()
            elif escolha == 3:
                print("Saindo do jogo. Até a próxima!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def exibirmenu(self):
        print("Escolha uma das Opções")
        print("1 - Novo Jogo")
        print("2 - Carregar Jogo")
        print("3 - Sair")

    def obter_escolha(self):
        while True:
            try:
                escolha = int(input("Digite a Opção Desejada: "))
                return escolha
            except ValueError:
                print("Por favor, digite um número válido.")

    def novojogo(self):
        nome = p.nome()
        raca = p.raca()
        classe = p.classe()
        atributos = p.atributos(raca, classe)
        self.jogador = p.jogador(nome, raca, classe, atributos)
        s.salvarjogo(self.jogador)
        e.escolha1(self.jogador)

    def carregar_jogo(self):
        self.jogador = s.carregarjogo()
        if self.jogador:
            print(f"Jogo carregado: {self.jogador}")
            e.escolha1(self.jogador)
        else:
            print("Nenhum jogo encontrado para carregar.")

if __name__ == "__main__":
    jogo = Jogo()
    jogo.menu()