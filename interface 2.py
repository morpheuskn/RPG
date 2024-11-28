from tkinter import *
from tkinter import messagebox, ttk
import random as r
import personagem as p
import salvamento as s
import historia as h
import escolha as e

class Jogo:

    def __init__(self):
        self.jogador = None
        self.capituloatual = 1
        self.karma = 0
        self.mochila = []

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
            atributos = p.atributos(raca, classe)
            self.jogador = p.jogador(nome, raca, classe, atributos)
            s.salvarjogo(self.jogador)
            messagebox.showinfo("Novo Jogo", f"Jogo salvo com sucesso! Jogador: {nome}, Raça: {raca}, Classe: {classe}")
            self.iniciarhistoria()

        Button(framenovojogo, text="Salvar Jogo", command=salvarnovojogo, bg="black", fg="green").pack(pady=10)

    def iniciarhistoria(self):
        for widget in janela.winfo_children():
            widget.destroy()
        self.exibircapitulo(self.capituloatual)

    def exibircapitulo(self, capitulo):
        for widget in janela.winfo_children():
            widget.destroy()

        titulo = Label(janela, text=f"Capítulo {capitulo}", bg="black", fg="green", font=("Courier", 30))
        titulo.pack(pady=20)

        textocapitulo = getattr(h, f'capitulo{capitulo}', "Capítulo não encontrado.")
        texto = Label(janela, text=textocapitulo, bg="black", fg="green", font=("Courier", 12), wraplength=750, justify="center")
        texto.pack(pady=20)

        self.adicionar_opcoes(capitulo)

    def adicionar_opcoes(self, capitulo):
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
        for texto, comando in opcoes.get(capitulo , []):
            Button(janela, text=texto, command=comando, bg="black", fg="green").pack(pady=5)


    def mostrar_inventario(self):
        inventario_texto = "Inventário:\n" + "\n".join(self.mochila) if self.mochila else "Inventário vazio."
        messagebox.showinfo("Inventário", inventario_texto)

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

janela = Tk()
jogo = Jogo()
jogo.inicializartela()
janela.mainloop()
