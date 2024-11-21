from tkinter import *
from tkinter import messagebox, ttk
import random as r
import personagem as p
import salvamento as s
import historia  # Importando o módulo historia

# Classe principal do jogo
class Jogo:
    def __init__(self):
        self.jogador = None  # Inicializa o jogador como None
        self.capitulo_atual = 1  # Define o capítulo atual do jogo

    def novojogo(self):
        # Limpa o conteúdo da janela principal
        for widget in janela.winfo_children():
            widget.destroy()
        
        # Cria um novo Frame para novo jogo
        frame_novo_jogo = Frame(janela, bg="black")
        frame_novo_jogo.pack(pady=20)

        # Campo para entrada do nome do jogador
        Label(frame_novo_jogo, text="Nome:", bg="black", fg="green").pack()
        entry_nome = Entry(frame_novo_jogo)
        entry_nome.pack()

        # Seleção de Raça
        Label(frame_novo_jogo, text="Raça:", bg="black", fg="green").pack()
        racas = ["Humano", "Elfo", "Anão", "Hobbit"]
        combo_raca = ttk.Combobox(frame_novo_jogo, values=racas)
        combo_raca.pack()

        # Seleção de Classe
        Label(frame_novo_jogo, text="Classe:", bg="black", fg="green").pack()
        classes = ["Guerreiro", "Feiticeiro", "Ladino", "Guardião"]
        combo_classe = ttk.Combobox(frame_novo_jogo, values=classes)
        combo_classe.pack()

        # Função para salvar o novo jogo
        def salvar_novo_jogo():
            nome = entry_nome.get()  # Obtém o nome do jogador
            raca = combo_raca.get()  # Obtém a raça selecionada
            classe = combo_classe.get()  # Obtém a classe selecionada
            atributos = p.atributos(raca, classe)  # Obtém os atributos baseados na raça e classe
            self.jogador = p.jogador(nome, raca, classe, atributos)  # Cria um novo objeto jogador
            s.salvarjogo(self.jogador)  # Salva o jogo
            messagebox.showinfo("Novo Jogo", f"Jogo salvo com sucesso! Jogador: {nome}")  # Mensagem de sucesso

            # Inicia a história após a criação do personagem
            self.iniciar_historia()

        # Botão para salvar o jogo
        Button(frame_novo_jogo, text="Salvar Jogo", command=salvar_novo_jogo, bg="black", fg="green").pack(pady=10)

    def iniciar_historia(self):
        # Limpa a tela atual
        for widget in janela.winfo_children():
            widget.destroy()

        # Configurações da tela de história
        janela.title("História Iniciada")
        janela.geometry("800x600")
        janela.configure(bg="black")

        self.exibir_capitulo(self.capitulo_atual)  # Exibe o primeiro capítulo

    def exibir_capitulo(self, capitulo):
        # Limpa a tela atual
        for widget in janela.winfo_children():
            widget.destroy()

        # Exibe o título do capítulo
        titulo = Label(janela, text=f"Capítulo {capitulo}", bg="black", fg="green", font=("Courier", 30))
        titulo.pack(pady=20)

        # Exibe o texto do capítulo importado do módulo historia
        texto_capitulo = getattr(historia, f'capitulo{capitulo}', "Capítulo não encontrado.")
        texto = Label(janela, text=texto_capitulo, bg="black", fg="white", font=("Courier", 12), wraplength=750, justify="left")
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
                 "Inventário"]
        }

        # Verifica se o capítulo existe nas opções
        if capitulo in opcoes:
            self.mostrar_escolhas(opcoes[capitulo], self.get_callback(capitulo))  # Mostra as escolhas disponíveis
        else:
            messagebox.showwarning("Atenção", "Capítulo não encontrado.")  # Mensagem de aviso se o capítulo não existir

    def mostrar_escolhas(self, opcoes, callback):
        # Cria botões para cada opção de escolha
        for i, opcao in enumerate(opcoes):
            button = Button(janela, text=opcao, command=lambda i=i: callback(i+1), bg="black", fg="green")
            button.pack(pady=5)

    def get_callback(self, capitulo):
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
            10: self.escolha10
        }
        return callbacks.get(capitulo, self.default_callback)  # Retorna a função de callback correspondente

    def default_callback(self, opcao):
        # Função padrão para opções não disponíveis
        messagebox.showwarning("Atenção", "Opção não disponível.")

    def escolha1(self, opcao):
        self.processar_escolha(opcao, 2)  # Processa a escolha e avança para o próximo capítulo

    def escolha2(self, opcao):
        self.processar_escolha(opcao, 3)

    def escolha3(self, opcao):
        self.processar_escolha(opcao, 4)

    def escolha4(self, opcao):
        self.processar_escolha(opcao, 5)

    def escolha5(self, opcao):
        self.processar_escolha(opcao, 6)

    def escolha6(self, opcao):
        self.processar_escolha(opcao, 7)

    def escolha7(self, opcao):
        self.processar_escolha(opcao, 8)

    def escolha8(self, opcao):
        self.processar_escolha(opcao, 9)

    def escolha9(self, opcao):
        self.processar_escolha(opcao, 10)

    def escolha10(self, opcao):
        self.processar_escolha(opcao, 11)

    def processar_escolha(self, opcao, proximo_capitulo):
        # Processa a escolha do jogador e atualiza o capítulo atual
        if opcao == 1:
            # Aqui você deve definir como atualizar o karma
            pass  # Exemplo: escolha.atualizar_karma(1 elif opcao == 2:
            # Aqui você deve definir como atualizar o karma
            pass  # Exemplo: escolha.atualizar_karma(0)
        elif opcao == 3:
            # Aqui você deve definir como atualizar o karma
            pass  # Exemplo: escolha.atualizar_karma(-1)
        elif opcao == 4:
            p.mostrarmochila(self.jogador.mochila)  # Mostra o inventário do jogador
        self.capitulo_atual = proximo_capitulo  # Atualiza o capítulo atual
        self.exibir_capitulo(self.capitulo_atual)  # Exibe o próximo capítulo

    def carregarjogo(self):
        # Função para carregar um jogo salvo
        try:
            self.jogador = s.carregarjogo()  # Tenta carregar o jogo salvo
            if self.jogador:
                messagebox.showinfo("Carregar Jogo", f"Jogo carregado: {self.jogador.nome}")  # Mensagem de sucesso
                self.iniciar_historia()  # Inicia a história a partir do ponto salvo
            else:
                messagebox.showwarning("Carregar Jogo", "Nenhum jogo encontrado.")  # Mensagem de aviso se não houver jogo salvo
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar o jogo: {e}")  # Mensagem de erro

    def sair(self):
        janela.destroy()  # Fecha a janela do jogo

    def inicializar_tela(self):
        # Limpa a tela atual
        for widget in janela.winfo_children():
            widget.destroy()

        # Configurações da tela inicial
        janela.title("A Aventura")
        janela.geometry("800x600")
        janela.configure(bg="black")

        # Título do jogo
        titulo = Label(janela, text="A Aventura", bg="black", fg="green", font=("Courier", 50))
        titulo.pack(pady=5)

        # Subtítulo do jogo
        subtitulo = Label(janela, text="An Izac de Paula Game", bg="black", fg="green", font=("Courier", 25))
        subtitulo.pack(pady=10)

        # Botão para iniciar um novo jogo
        botaonovojogo = Button(janela, text="Novo Jogo", command=self.novojogo, bg="black", fg="green")
        botaonovojogo.pack(pady=20)

        # Botão para carregar um jogo salvo
        botaocarregarjogo = Button(janela, text="Carregar Jogo", command=self.carregarjogo, bg="black", fg="green")
        botaocarregarjogo.pack(pady=20)

        # Botão para sair do jogo
        botaosair = Button(janela, text="Sair", command=self.sair, bg="black", fg="green")
        botaosair.pack(pady=20)

# Inicializa a janela
janela = Tk()
jogo = Jogo()  # Cria uma instância da classe Jogo
jogo.inicializar_tela()  # Inicializa a tela do jogo
