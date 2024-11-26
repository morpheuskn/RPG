from tkinter import *
from tkinter import messagebox, ttk
from random import *
from personagem import *
from salvamento import *
import historia  

# Classe principal do jogo
class Jogo:
    def __init__(self):
        self.jogador = None  # Inicializa o jogador como None
        self.capituloatual = 1  # Define o capítulo atual do jogo

    def novojogo(self):
        for widget in janela.winfo_children():
            widget.destroy()
        
        framenovojogo = Frame(janela, bg="black")
        framenovojogo.pack(pady=20)

        Label(framenovojogo, text="Nome:", bg="black", fg="green").pack()
        entrynome = Entry(framenovojogo)
        entrynome.pack()

        Label(framenovojogo, text="Raça:", bg="black", fg="green").pack()
        racas = ["Humano", "Elfo", "Anão", "Hobbit"]
        comboraca = ttk.Combobox(framenovojogo, values=racas)
        comboraca.pack()

        Label(framenovojogo, text="Classe:", bg="black", fg="green").pack()
        classes = ["Guerreiro", "Feiticeiro", "Ladino", "Guardião"]
        comboclasse = ttk.Combobox(framenovojogo, values=classes)
        comboclasse.pack()

        def salvarnovojogo():
            nome = entrynome.get()
            raca = comboraca.get()
            classe = comboclasse.get()
            atributos = atributos(raca, classe)
            self.jogador = jogador(nome, raca, classe, atributos)
            salvarjogo(self.jogador)
            messagebox.showinfo("Novo Jogo", f"Jogo salvo com sucesso! Jogador: {nome}, Raça: {raca}, Classe: {classe}, Atributos: {atributos}")
            self.iniciarhistoria()

        Button(framenovojogo, text="Salvar Jogo", command=salvarnovojogo, bg="black", fg="green", highlightbackground="black").pack(pady=10)

    def iniciarhistoria(self):
        for widget in janela.winfo_children():
            widget.destroy()

        janela.title("História Iniciada")
        janela.geometry("800x600")
        janela.configure(bg="black")

        self.exibircapitulo(self.capituloatual)

    def exibircapitulo(self, capitulo):
        for widget in janela.winfo_children():
            widget.destroy()

        titulo = Label(janela, text=f"Capítulo {capitulo}", bg="black", fg="green", font=("Courier", 30))
        titulo.pack(pady=20)

        texto_capitulo = getattr(historia, f'capitulo{capitulo}', "Capítulo não encontrado.")
        texto = Label(janela, text=texto_capitulo, bg="black", fg="green", font=("Courier", 12), wraplength=750, justify="center")
        texto.pack(pady=10)

        opcoes = {
            1: ["Eu aceito, irei e voltarei com a joia e a vitória em mãos.", 
                "Fale-me mais sobre?", 
                "Nem fudendo, pelo menos não sem uma gorda recompensa.", 
                "Inventário"],
            2: ["Um anunciante no porto, me guiou para cá. Me disse que há um trabalho para um mercenário errante como eu.", 
                "F ale-me mais sobre tais audiências.", 
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
                 "Inventário"]
        }

        if capitulo in opcoes:
            self.mostrarescolhas(opcoes[capitulo], self.getcallback(capitulo))
        else:
            messagebox.showwarning("Atenção", "Capítulo não encontrado.")

    def mostrarescolhas(self, opcoes, callback):
        for i, opcao in enumerate(opcoes):
            button = Button(janela, text=opcao, command=lambda i=i: callback(i+1), bg="black", fg="green", highlightbackground="black")
            button.pack(pady=5)

    def getcallback(self, capitulo):
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
        return callbacks.get(capitulo, self.defaultcallback)

    def defaultcallback(self, opcao):
        messagebox.showwarning("Atenção", "Opção não disponível.")

    def escolha1(self, opcao):
        self.processarescolha(opcao, 2)

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
        if opcao == 1:
            # Aqui você deve definir como atualizar o karma
            pass
        elif opcao == 2:
            # Aqui você deve definir como atualizar o karma
            pass
        elif opcao == 3:
            # Aqui você deve definir como atualizar o karma
            pass
        elif opcao == 4:
            if self.jogador:
               self.jogador.mostrarmochila()  # Mostra o inventário do jogador
               self.capituloatual = proximocapitulo
               self.exibircapitulo(self.capituloatual)

    def carregarjogo(self):
        try:
            self.jogador = carregarjogo()
            if self.jogador:
                messagebox.showinfo("Carregar Jogo", f"Jogo carregado: {self.jogador.nome}")  # Corrigido para usar self.jogador.nome
                self.iniciarhistoria()
            else:
                messagebox.showwarning("Carregar Jogo", "Nenhum jogo encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar o jogo: {e}")

    def sair(self):
        janela.destroy()

    def inicializartela(self):
        for widget in janela.winfo_children():
            widget.destroy()

        janela.title("A Aventura")
        janela.geometry("800x600")
        janela.configure(bg="black")

        titulo = Label(janela, text="Medieval Self Adventure", bg="black", fg="green", font=("Courier", 40))
        titulo.pack(pady=5)

        subtitulo = Label(janela, text="An Izac de Paula Game", bg="black", fg="green", font=("Courier", 20))
        subtitulo.pack(pady=10)

        botaonovojogo = Button(janela, text="Novo Jogo", command=self.novojogo, bg="black", fg="green", highlightbackground="black")
        botaonovojogo.pack(pady=20)

        botaocarregarjogo = Button(janela, text="Carregar Jogo", command=self.carregarjogo, bg="black", fg="green", highlightbackground="black")
        botaocarregarjogo.pack(pady=20)

        botaosair = Button(janela, text="Sair", command=self.sair, bg="black", fg="green", highlightbackground="black")
        botaosair.pack(pady=20)

# Inicializa a janela
janela = Tk()
jogo = Jogo()
jogo.inicializartela()
