from tkinter import *
from tkinter import messagebox, ttk
import random as r
import personagem as p
import salvamento as s
import historia as h
import combates as c

class Escolha:
    def __init__(self, jogo):
        self.jogo = jogo
        self.karma = 0
        self.mochila = jogo.mochila

    def atualizarkarma(self, valor):
        self.karma += valor

    def exibir_escolha(self, capitulo):
        # Mapeia os capítulos para suas respectivas escolhas
        escolhas = {
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
            13: self.escolha13,
            14: self.escolha14,
            15: self.escolha15,
        }
        # Chama a escolha correspondente ao capítulo
        if capitulo in escolhas:
            escolhas[capitulo]()

    def escolha1(self):
        self.jogo.exibircapitulo(1)
        opcoes = [
            ("Eu aceito, irei e voltarei com a joia e a vitória em mãos.", self.acao_escolha1_1),
            ("Fale-me mais sobre?", self.acao_escolha1_2),
            ("Nem ferrando, pelo menos não sem uma gorda recompensa.", self.acao_escolha1_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha1_1(self):
        self.exibir_mensagem("Anunciante Real: Que discurso heroico, que suas palavras sejam verdades e que você volte com a vitória em mãos.", self.jogo.exibircapitulo, 2)

    def acao_escolha1_2(self):
        self.exibir_mensagem("Anunciante Real: Não há muito mais a se falar sobre. El'goroth era uma das nossas cidades mais belas, até um incidente que a deixou em ruínas.", self.jogo.exibircapitulo, 2)

    def acao_escolha1_3(self):
        self.exibir_mensagem("Anunciante Real: Aposte que haverá um mar de tesouros para aquele que completar a árdua tarefa.", self.jogo.exibircapitulo, 2)

    def escolha2(self):
        self.jogo.exibircapitulo(2)
        opcoes = [
            ("Um anunciante no porto, me guiou para cá.", self.acao_escolha2_1),
            ("Fale-me mais sobre tais audiências.", self.acao_escolha2_2),
            ("Não imagina, eu vim para papear com você.", self.acao_escolha2_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha2_1(self):
        self.exibir_mensagem("Guarda: Então venha comigo, mercenário.", self.jogo.exibircapitulo, 3)

    def acao_escolha2_2(self):
        self.exibir_mensagem("Guarda: Essas audiências são momentos em que vossa ilustríssima majestade ouve, delibera e atende a pedidos da população.", self.jogo.exibircapitulo, 3)

    def acao_escolha2_3(self):
        self.exibir_mensagem("Guarda: Um engraçadinho, talvez fique menos engraçado passando uns tempos nos calabouços.", self.jogo.exibircapitulo, 3)

    def escolha3(self):
        self.jogo.exibircapitulo(3)
        opcoes = [
            ("Vossa majestade, será uma honra por minha vida e minha habilidade ao ser dispor.", self.acao_escolha3_1),
            ("Fale-me mais sobre tais recompensas.", self.acao_escolha3_2),
            ("Bom, se as recompensas forem boas estou dentro.", self.acao_escolha3_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha3_1(self):
        self.exibir_mensagem("Rei Dio: Pois bem herói, lhe daremos um cavalo e a bênção real. Vá e traga minha filha.", self.jogo.exibircapitulo, 4)

    def acao_escolha3_2(self):
        self.exibir_mensagem("Rei Dio: Um castelo, um título ducal e muito ouro.", self.jogo.exibircapitulo, 4)

    def acao_escolha3_3(self):
        self.exibir_mensagem("Rei Dio: Um homem movido a ouro e glórias. Pois bem, lhe daremos um cavalo e a bênção real. Vá e traga minha filha.", self.jogo.exibircapitulo, 4)

    def escolha4(self):
        self.jogo.exibircapitulo(4)
        opcoes = [
            ("Tentar passar conversando.", self.acao_escolha4_1),
            ("Tentar passar despercebido.", self.acao_escolha4_2),
            ("Matar a todos.", self.acao_escolha4_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha4_1(self):
        self.exibir_mensagem("Esidisi: Pare. Entregue tudo ou perderá a sua vida.", self.jogo.exibircapitulo, 5)

    def acao_escolha4_2(self):
        self.exibir_mensagem("Você utiliza uma trilha em meio à floresta para contornar o cerco bandido e consegue.", self.jogo.exibircapitulo, 5)

    def acao_escolha4_3(self):
        self.exibir_mensagem("Você parte para cima dos quatro bandidos.", self.jogo.exibircapitulo, 5)

    def escolha5(self):
        self.jogo.exibircapitulo(5)
        opcoes = [
            ("Investigar marcas no chão.", lambda: self.investigar(1)),
            ("Investigar pedaços de carne preta.", lambda: self.investigar(2)),
            ("Investigar os corpos dos soldados.", lambda: self.investigar(3)),
            ("Investigar as armas quebradas.", lambda: self.investigar(4)),
        ]
        self.jogo.adicionaropcoes(opcoes)

    def investigar(self, tipo):
        if tipo == 1:
            self.exibir_mensagem("Você percebe que essas são marcas das carruagens, você percebe que essas marcas vêm de El'goroth.", self.jogo.exibircapitulo, 6)
        elif tipo == 2:
            self.exibir_mensagem("Você vê que os pedaços das criaturas mortas não se parecem com nada que você tenha visto.", self.jogo.exibircapitulo, 6)
        elif tipo == 3:
            self.exibir_mensagem("Você vasculha os restos mortais dos soldados e encontra as ordens de escoltarem a princesa e a joia de El'goroth para o castelo real.", self.jogo.exibircapitulo, 6)
        elif tipo == 4:
            self.exibir_mensagem("Você investiga as armas abandonadas e percebe que elas foram quebradas por magia poderosa e força imensa.", self.jogo.exibircapitulo, 6)

    def escolha6(self):
        self.jogo.exibircapitulo(6)
        opcoes = [
            ("Lutar contra os demônios.", self.acao_escolha6_1),
            ("Tentar se esconder.", self.acao_escolha6_2),
            ("Tentar fugir.", self.acao_escolha6_3),
            ("Inventário", self.mostrarinventario )
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha6_1(self):
        self.exibir_mensagem("Você os ataca.", self.jogo.exibircapitulo, 7)

    def acao_escolha6_2(self):
        self.exibir_mensagem("Você rapidamente se esconde no alto de uma árvore próxima, até que os cães vão embora.", self.jogo.exibircapitulo, 7)

    def acao_escolha6_3(self):
        self.exibir_mensagem("Você rapidamente corre, os cães correm atrás. Mas você consegue os despistar.", self.jogo.exibircapitulo, 7)

    def escolha7(self):
        self.jogo.exibircapitulo(7)
        opcoes = [
            ("Seguir o Vulto.", self.acao_escolha7_1),
            ("Ir para outro Corredor.", self.acao_escolha7_2),
            ("Tentar fugir.", self.acao_escolha7_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha7_1(self):
        self.exibir_mensagem("Você segue o vulto, mas ele desaparece em frente a uma estante.", self.jogo.exibircapitulo, 8)

    def acao_escolha7_2(self):
        self.exibir_mensagem("Você vai avançando por outro corredor e acaba em frente a uma estante.", self.jogo.exibircapitulo, 8)

    def acao_escolha7_3(self):
        self.exibir_mensagem("Você tenta fugir, mas acaba entrando mais na biblioteca.", self.jogo.exibircapitulo, 8)

    def escolha8(self):
        self.jogo.exibircapitulo(8)
        opcoes = [
            ("Ir em Direção ao Livro.", self.acao_escolha8_1),
            ("Tentar parar.", self.acao_escolha8_2),
            ("Tentar ir na Direção Contrária.", self.acao_escolha8_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha8_1(self):
        self.exibir_mensagem("Você chega mais e mais perto do livro. Você sente uma vontade irresistível de tocá-lo.", self.jogo.exibircapitulo, 9)

    def acao_escolha8_2(self):
        self.exibir_mensagem("Você não consegue se conter e chega mais e mais perto do livro.", self.jogo.exibircapitulo, 9)

    def acao_escolha8_3(self):
        self.exibir_mensagem("Você não consegue se conter e chega mais e mais perto do livro.", self.jogo.exibircapitulo, 9)

    def escolha9(self):
        self.jogo.exibircapitulo(9)
        opcoes = [
            ("Então por que tudo isso?", self.acao_escolha9_1),
            ("Então seu nome é Natasha, eu tive uma visão e isso é um livro?", self.acao_escolha9_2),
            ("Se isso é verdade, eu sou o rei da Costa das Espadas.", self.acao_escolha9_3),
            ("Você é um livro?", self.acao_escolha9_4)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha9_1(self):
        self.exibir_mensagem("Natasha: Finalmente você fez a pergunta correta.", self.jogo.exibircapitulo, 10)

    def acao_escolha9_2(self):
        self.exibir_mensagem("Natasha: Achei que tinha ficado óbvio já que eu acabei de dizer isso.", self.jogo.exibircapitulo, 10)

    def acao_escolha9_3(self):
        self.exibir_mensagem("Natasha: Ah é, vossa majestade senhor da comédia.", self.jogo.exibircapitulo, 10)

    def acao_escolha9_4(self):
        self.exibir_mensagem("Natasha: Você não é muito inteligente, né.", self.jogo.exibircapitulo, 9)

    def escolha10(self):
        self.jogo.exibircapitulo(10)
        opcoes = [
            ("Seria uma honra.", self.acao_escolha10_1),
            ("Por que?", self.acao_escolha10_2),
            ("Não.", self.acao_escolha10_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha10_1(self):
        self.exibir_mensagem("Natasha: Obrigada.", self.jogo.exibircapitulo, 11)

    def acao_escolha10_2(self):
        self.exibir_mensagem("Natasha: Eu vi isso começar, e quero ver como termina.", self.jogo.exibircapitulo, 11)

    def acao_escolha10_3(self):
        self.exibir_mensagem("Natasha: Você se arrependerá por isso.", self.jogo.exibircapitulo, 11)

    def escolha11(self):
        self.jogo.exibircapitulo(11)
        opcoes = [
            ("Atacar na Surdina", self.acao_escolha11_1),
            ("Atacar frontalmente", self.acao_escolha11_2),
            ("Dar a Volta", self.acao_escolha11_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha11_1(self):
        self.exibir_mensagem("Você ataca a criatura das sombras, um ataque meticulosamente calculado para acertar a cabeça.", self.jogo.exibircapitulo, 12)

    def acao_escolha11_2(self):
        self.exibir_mensagem("Você ataca a criatura frontalmente.", self.jogo.exibircapitulo, 12)

    def acao_escolha11_3(self):
        self.exibir_mensagem("Você se esconde da criatura, usando destroços como esconderijo. Até conseguir fugir dele.", self.jogo.exibircapitulo, 12)

    def escolha12(self):
        self.jogo.exibircapitulo(12)
        opcoes = [
            ("Nós Iremos Lutar", self.acao_escolha12_1),
            ("O quê Vocês irão Fazer?", self.acao_escolha12_2),
            ("Eu me Juntarei a Vocês", self.acao_escolha12_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha12_1(self):
        self.exibir_mensagem("Você: Então que assim seja.", self.jogo.exibircapitulo, 13)

    def acao_escolha12_2(self):
        self.exibir_mensagem("Anung Un Rama: Para libertar a nossa irmã e trazer nosso mundo para o seu.", self.jogo.exibircapitulo, 13)

    def acao_escolha12_3(self):
        self.exibir_mensagem("Anung Un Rama: Um homem que trai a sua própria espécie, não é digno da nossa.", self.jogo.exibircapitulo, 13)

    def escolha13(self):
        self.jogo.exibircapitulo(13)
        opcoes = [
            ("Lutar", self.acao_escolha13_1),
            ("Fazer os Bestas lutarem com o próprio mestre", self.acao_escolha13_2),
            ("Fugir", self.acao_escolha13_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha13_1(self):
        self.exibir_mensagem("Você: Então que assim seja.", self.jogo.exibircapitulo, 14)

    def acao_escolha13_2(self):
        self.exibir_mensagem("Você apaga a sua tocha, e faz barulhos atraindo as bestas.", self.jogo.exibircapitulo, 14)

    def acao_escolha13_3(self):
        self.exibir_mensagem("Você apaga a sua tocha, e sai correndo para trás de Zodd.", self.jogo.exibircapitulo, 14)

    def escolha14(self):
        self.jogo.exibircapitulo(14)
        opcoes = [
            ("Lutar", self.acao_escolha14_1),
            ("Por que?", self.acao_escolha14_2),
            ("Fugir", self.acao_escolha14_3),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha14_1(self):
        self.exibir_mensagem("Você: Então que assim seja.", self.jogo.exibircapitulo, 15)

    def acao_escolha14_2(self):
        self.exibir_mensagem("Khan: Porque sim. Você se questiona quando mata formigas.", self.jogo.exibircapitulo, 15)

    def acao_escolha14_3(self):
        self.exibir_mensagem("Anung Un Rama: Um homem que trai a sua própria espécie, não é digno da nossa.", self.jogo.exibircapitulo, 15)

    def escolha15(self):
        self.jogo.exibircapitulo(15)
        opcoes = [
            ("Nós Iremos Lutar", self.acao_escolha15_1),
            ("Inventário", self.mostrarinventario)
        ]
        self.jogo.adicionaropcoes(opcoes)

    def acao_escolha15_1(self):
        self.exibir_mensagem("Você: Eu vou terminar isso agora.", self.jogo.final, self.jogo.karma, self.mochila)

    def exibir_mensagem(self, mensagem, proxima_acao, *args):
        for widget in self.jogo.janela.winfo_children():
            widget.destroy()

        Label(self.jogo.janela, text=mensagem, bg="black", fg="green", font=("Courier", 12), wraplength=750, justify="center").pack(pady=20)

        Button(self.jogo.janela, text="Seguir", command=lambda: proxima_acao(*args), bg="black", fg="green").pack(pady=10)

    def mostrarinventario(self):
        inventariotexto = "Inventário:\n" + "\n".join(self.mochila) if self.mochila else "Inventário vazio."
        messagebox.showinfo("Inventário", inventariotexto)

class Jogo:
    def __init__(self):
        self.jogador = None
        self.capituloatual = 1
        self.karma = 0
        self.mochila = []
        self.escolha = Escolha(self)  # Inicializa o módulo de escolhas
        self.janela = Tk()  # Inicializa a janela do jogo
        self.inicializartela()

    def novojogo(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        framenovojogo = Frame(self.janela, bg="black")
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

        Button(framenovojogo, text="Iniciar Jogo", command=salvarnovojogo, bg="black", fg="green").pack(pady=10)

    def iniciarhistoria(self):
        self.exibircapitulo(self.capituloatual)

    def exibircapitulo(self, capitulo):
        for widget in self.janela.winfo_children():
            widget.destroy()

        titulo = Label(self.janela, text=f"Capítulo {capitulo}", bg="black", fg="green", font=("Courier", 30))
        titulo.pack(pady=20)

        textocapitulo = getattr(h, f'capitulo{capitulo}', "Capítulo não encontrado.")
        texto = Label(self.janela, text=textocapitulo, bg="black", fg="green", font=("Courier", 12), wraplength=750, justify="center")
        texto.pack(pady=20)

        self.escolha.exibir_escolha(capitulo)  # Chama a função para exibir as escolhas

    def adicionaropcoes(self, opcoes):
        for texto, acao in opcoes:
            Button(self.janela, text=texto, command=acao, bg="black", fg="green").pack(pady=5)

    def carregarjogo(self):
        try:
            self.jogador = s.carregarjogo()  # Tenta carregar o jogo salvo
            if self.jogador:
                messagebox.showinfo("Carregar Jogo", f"Jogo carregado: {self.jogador.nome}")  # Mensagem de sucesso
                self.iniciarhistoria()  # Inicia a história a partir do ponto salvo
            else:
                messagebox.showwarning("Carregar Jogo", "Nenhum jogo encontrado.")  # Mensagem de aviso se não houver jogo salvo
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar o jogo: {e}")  # Mensagem de erro

    def sair(self):
        self.janela.destroy()  # Fecha a janela do jogo

    def inicializartela(self):
        # Limpa a tela atual
        for widget in self.janela.winfo_children():
            widget.destroy()

        # Configurações da tela inicial
        self.janela.title("A Aventura")
        self.janela.geometry("800x600")
        self.janela.configure(bg="black")

        # Título do jogo
        titulo = Label(self.janela, text="Medieval Self Adventure", bg="black", fg="green", font=("Courier", 40))
        titulo.pack(pady=5)

        # Subtítulo do jogo
        subtitulo = Label(self.janela, text="An Izac de Paula Game", bg="black", fg="green", font=("Courier", 20))
        subtitulo.pack(pady=10)

        # Botão para iniciar um novo jogo
        botaonovojogo = Button(self.janela, text="Novo Jogo", command=self.novojogo, bg="black", fg="green", highlightbackground="black")
        botaonovojogo.pack(pady=20)

        # Botão para carregar um jogo salvo
        botaocarregarjogo = Button(self.janela, text="Carregar Jogo", command=self.carregarjogo, bg="black", fg="green", highlightbackground="black")
        botaocarregarjogo.pack(pady=20)

        # Botão para sair do jogo
        botaosair = Button(self.janela, text="Sair", command=self.sair, bg="black", fg="green", highlightbackground="black")
        botaosair.pack(pady=20)

janela = Tk()
jogo = Jogo()
jogo.inicializartela()
janela.mainloop()
