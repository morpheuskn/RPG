from tkinter import *
from tkinter import messagebox, ttk
import random as r
import personagem as p
import salvamento as s
import historia  

# Classe principal do jogo
class Jogo:

    karma = 0
    
    def __init__(self):
        self.jogador = None  # Inicializa o jogador como None
        self.capituloatual = 1  # Define o capítulo atual do jogo

    def novojogo(self):
        # Limpa o conteúdo da janela principal
        for widget in janela.winfo_children():
            widget.destroy()
        
        # Cria um novo Frame para novo jogo
        framenovojogo = Frame(janela,bg="black")
        framenovojogo.pack(pady=20)

        # Campo para entrada do nome do jogador
        Label(framenovojogo, text="Nome:", bg="black", fg="green").pack()
        entrynome = Entry(framenovojogo)
        entrynome.pack()

        # Seleção de Raça
        Label(framenovojogo, text="Raça:", bg="black", fg="green").pack()
        racas = ["Humano", "Elfo", "Anão", "Hobbit"]
        comboraca = ttk.Combobox(framenovojogo, values=racas)
        comboraca.pack()

        # Seleção de Classe
        Label(framenovojogo, text="Classe:", bg="black", fg="green").pack()
        classes = ["Guerreiro", "Feiticeiro", "Ladino", "Guardião"]
        comboclasse = ttk.Combobox(framenovojogo, values=classes)
        comboclasse.pack()

        # Função para salvar o novo jogo
        def salvarnovojogo():
            nome = entrynome.get()  # Obtém o nome do jogador
            raca = comboraca.get()  # Obtém a raça selecionada
            classe = comboclasse.get()  # Obtém a classe selecionada
            atributos = p.atributos(raca, classe)  # Obtém os atributos baseados na raça e classe
            self.jogador = p.jogador(nome, raca, classe, atributos)  # Cria um novo objeto jogador
            s.salvarjogo(self.jogador)  # Salva o jogo
            confirmacao = messagebox.askyesno("Novo Jogo", f"Jogo salvo com sucesso! Jogador: {nome}, Raça: {raca}, Classe: {classe}, Atributos: {atributos}")  # Mensagem de sucesso
            if confirmacao:
                # Inicia a história após a criação do personagem
                self.iniciarhistoria()

        # Botão para salvar o jogo
        Button(framenovojogo, text="Salvar Jogo", command=salvarnovojogo, bg="black", fg="green",highlightbackground = "black").pack(pady=10)

    def iniciarhistoria(self):
        # Limpa a tela atual
        for widget in janela.winfo_children():
            widget.destroy()

        # Configurações da tela de história
        janela.title("A Aventura é Iniciada")
        janela.geometry("800x600")
        janela.configure(bg="black")

        self.exibircapitulo(self.capituloatual)  # Exibe o primeiro capítulo

    def exibircapitulo(self, capitulo):
        # Limpa a tela atual
        for widget in janela.winfo_children():
            widget.destroy()

        # Exibe o título do capítulo
        titulo = Label(janela, text=f"Capítulo {capitulo}", bg="black", fg="green", font=("Courier", 30))
        titulo.pack(pady=20)

        # Exibe o texto do capítulo importado do módulo historia
        textocapitulo = getattr(historia, f'capitulo{capitulo}', "Capítulo não encontrado.")
        texto = Label(janela, text=textocapitulo, bg="black", fg="green", font=("Courier", 12), wraplength=750, justify="center")
        texto.pack(pady=10)

        # Dicionário com opções de escolha para cada capítulo
        opcoes = {
            1: ["Eu aceito, irei e voltarei com a joia e a vitória em mãos.", 
                "Fale-me mais sobre?", 
                "Nem fudendo, pelo menos não sem uma gorda recompensa.", 
                "Inventário"],
            2: ["Um anunciante no porto , me guiou para cá. Me disse que há um trabalho para um mercenário errante como eu.", 
                "Fale-me mais sobre tais audiências.", 
                "Não porra, eu vim para papear com você. Não está na cara?", 
                "Inventário"],
            3: ["Vossa majestade, será uma honra por minha vida e minha habilidade ao ser dispor.",
                "Fale-me mais sobre tais recompensas.",
                "Bom, se as recompensas forem boas estou dentro.",
                "Inventário"],
            4: ["Tentar passar conversando.",
                "Tentar passar despercebido.",
                "Matar a todos.",
                "Inventário"],
            5: ["Investigar marcas no chão.",
                "Investigar pedaços de carne preta.",
                "Investigar os corpos dos soldados.",
                "Investigar as armas quebradas."],
            6: ["Lutar contra os demônios.",
                "Tentar se esconder.",
                "Tentar fugir.",
                "Inventário"],
            7: ["Seguir o Vulto.",
                "Ir para outro Corredor.",
                "Tentar fugir.",
                "Inventário"],
            8: ["Ir em Direção ao Livro.",
                "Tentar parar.",
                "Tentar ir na Direção Contrária.",
                "Inventário"],
            9: ["Então por que tudo isso?",
                "Então seu nome é Natasha, eu tive uma visão e isso é um livro?",
                "Se isso é verdade, eu sou o rei da Costa das Espadas.",
                "Você é um livro?"],
            10: ["Seria uma honra.",
                 "Por que?",
                 "Não.",
                 "Inventário"],
            11: ["Atacar na Surdina",
                 "Atacar frontalmente",
                 "Dar a Volta",
                 "Inventaro"],
            12: ["Nós Iremos Lutar",
                 "O quê Vocês irão Fazer ?",
                 "Eu me Juntarei a Vocês",
                 "Inventario"]
        }

        # Verifica se o capítulo existe nas opções
        if capitulo in opcoes:
            self.mostrarescolhas(opcoes[capitulo], self.getcallback(capitulo))  # Mostra as escolhas disponíveis
        else:
            messagebox.showwarning("Atenção", "Capítulo não encontrado.")  # Mensagem de aviso se o capítulo não existir

    def mostrarescolhas(self, opcoes, callback):
        # Cria botões para cada opção de escolha
        for i, opcao in enumerate(opcoes):
            button = Button(janela, text=opcao, command=lambda i=i: callback(i+1), bg="black", fg="green",highlightbackground = "black")
            button.pack(pady=5)

    def getcallback(self, capitulo):
        # Mapeia cada capítulo a sua respectiva função de callback
        callbacks = {
            1: self.escolha1,
            2: self.escolha2,
            3: self.escolha3,
            4: self.escolha4,
            5: self.escolha5,
            6: self.escolha6,
            7: self.escolha7,
            8: self.escolha8,
            9: self.escolha9,
            10: self.escolha10,
            11: self.escolha11,
            12: self.escolha12,
            13: self.escolha13
        }
        return callbacks.get(capitulo, self.defaultcallback)  # Retorna a função de callback correspondente

    def defaultcallback(self, opcao):
        # Função padrão para opções não disponíveis
        messagebox.showwarning("Atenção", "Opção não disponível.")

    def escolha1(self, opcao):
        self.processarescolha(opcao, 2)  # Processa a escolha e avança para o próximo capítulo

    def escolha2(self, opcao):
        self.processarescolha(opcao, 3)

    def escolha3(self, opcao):
        self.processarescolha(opcao, 4)

    def escolha4(self, opcao):
        self.processarescolha(opcao, 5)

    def escolha5(self, opcao):
        self.processarescolha(opcao, 6)

    def escolha6(self, opcao):
        self.processarescolha(opcao, 7)

    def escolha7(self, opcao):
        self.processarescolha(opcao, 8)

    def escolha8(self, opcao):
        self.processarescolha(opcao, 9)

    def escolha9(self, opcao):
        self.processarescolha(opcao, 10)

    def escolha10(self, opcao):
        self.processarescolha(opcao, 11)

    def escolha11(self, opcao):
        self.processarescolha(opcao, 12)

    def escolha12(self, opcao):
        self.processarescolha(opcao, 13)

    def escolha13(self, opcao):
        self.processarescolha(opcao, 14)

    def processarescolha(self, opcao, proximocapitulo):
        # Processa a escolha do jogador e atualiza o capítulo atual
        match opcao:
        
           case 1:
               karma += 2
               pass  # Exemplo: escolha.atualizar_karma(1 elif opcao == 2:
        
           case 2:
                karma += 0
                pass  # Exemplo: escolha.atualizar_karma(0)

           case 3:
                karma += -2
                pass  # Exemplo: escolha.atualizar_karma(-1)
           case 4:
                p.mostrarmochila(item)  # Mostra o inventário do jogador
        self.capituloatual = proximocapitulo  # Atualiza o capítulo atual
        self.exibircapitulo(self.capituloatual)  # Exibe o próximo capítulo

    def carregarjogo(self):
        # Função para carregar um jogo salvo
        try:
            self.jogador = s.carregarjogo()  # Tenta carregar o jogo salvo
            if self.jogador:
                messagebox.showinfo("Carregar Jogo", f"Jogo carregado: {nome}")  # Mensagem de sucesso
                self.iniciarhistoria()  # Inicia a história a partir do ponto salvo
            else:
                messagebox.showwarning("Carregar Jogo", "Nenhum jogo encontrado.")  # Mensagem de aviso se não houver jogo salvo
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar o jogo: {e}")  # Mensagem de erro

    def sair(self):
        janela.destroy()  # Fecha a janela do jogo

    def inicializartela(self):
        # Limpa a tela atual
        for widget in janela.winfo_children():
            widget.destroy()

        # Configurações da tela inicial
        janela.title("A Aventura")
        janela.geometry("800x600")
        janela.configure(bg="black")

        # Título do jogo
        titulo = Label(janela, text="Medieval Self Adventure", bg="black", fg="green", font=("Courier", 40))
        titulo.pack(pady=5)

        # Subtítulo do jogo
        subtitulo = Label(janela, text="An Izac de Paula Game", bg="black", fg="green", font=("Courier", 20))
        subtitulo.pack(pady=10)

        # Botão para iniciar um novo jogo
        botaonovojogo = Button(janela, text="Novo Jogo", command=self.novojogo, bg="black", fg="green",highlightbackground = "black")
        botaonovojogo.pack(pady=20)

        # Botão para carregar um jogo salvo
        botaocarregarjogo = Button(janela, text="Carregar Jogo", command=self.carregarjogo, bg="black", fg="green",highlightbackground = "black")
        botaocarregarjogo.pack(pady=20)

        # Botão para sair do jogo
        botaosair = Button(janela, text="Sair", command=self.sair, bg="black", fg="green",highlightbackground = "black")
        botaosair.pack(pady=20)

# Inicializa a janela
janela = Tk()
jogo = Jogo()  # Cria uma instância da classe Jogo
jogo.inicializartela()  # Inicializa a tela do jogo
