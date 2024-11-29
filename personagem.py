import random as r  # Importa a biblioteca random e a renomeia como r para gerar números aleatórios
from colorama import Fore # Importa a função Fore do módulo colorama
# Função para solicitar e retornar o nome do personagem
def nome():
    nomepersonagem = input(Fore.GREEN + "Digite o Nome do Personagem: ")  # Pede ao usuário para digitar o nome
    return nomepersonagem  # Retorna o nome digitado

# Função para escolher a raça do personagem
def raca():
    racas = {1: "Humano", 2: "Elfo", 3: "Anão", 4: "Hobbit"}  # Dicionário de raças disponíveis
    print(Fore.GREEN + "Escolha a Raça do Seu Personagem: ")
    print(Fore.GREEN + "Digite: ")
    print(Fore.GREEN + "1 - Humano")
    print(Fore.GREEN + "2 - Elfo")
    print(Fore.GREEN + "3 - Anão")
    print(Fore.GREEN + "4 - Hobbit")
    
    escolharaca = int(input("Digite o Número da Raça: "))  # Pede ao usuário para escolher uma raça
    racapersonagem = racas.get(escolharaca)  # Obtém a raça correspondente ao número escolhido
    print(Fore.GREEN + f"A raça Escolhida foi: {racapersonagem}")  # Exibe a raça escolhida
    return racapersonagem  # Retorna a raça escolhida

# Função para escolher a classe do personagem
def classe():
    classes = {1: "Guerreiro", 2: "Feiticeiro", 3: "Ladino", 4: "Guardião"}  # Dicionário de classes disponíveis
    print(Fore.GREEN + "Escolha a Classe do Seu Personagem: ")
    print(Fore.GREEN + "Digite: ")
    print(Fore.GREEN + "1 - Guerreiro")
    print(Fore.GREEN + "2 - Feiticeiro")
    print(Fore.GREEN + "3 - Ladino")
    print(Fore.GREEN + "4 - Guardião")
    
    escolhaclasse = int(input("Digite o Número da Classe: "))  # Pede ao usuário para escolher uma classe
    classepersonagem = classes.get(escolhaclasse)  # Obtém a classe correspondente ao número escolhido
    print(f"A classe Escolhida foi: {classepersonagem}")  # Exibe a classe escolhida
    return classepersonagem  # Retorna a classe escolhida

# Função para calcular os atributos do personagem com base na raça e classe escolhidas
def atributos(raca, classe):
    # Atributos base para cada raça
    atributosraca = {
        "Humano": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 1, "Sabedoria": 0, "Carisma": 1},
        "Elfo": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 0, "Sabedoria": 1, "Carisma": 1},
        "Anão": {"Força": 1, "Destreza": 0, "Constituição": 1, "Inteligência": 1, "Sabedoria": 0, "Carisma": 0},
        "Hobbit": {"Força": 0, "Destreza": 0, "Constituição": 0, "Inteligência": 1, "Sabedoria": 1, "Carisma": 1}
    }

    # Atributos base para cada classe
    atributosclasse = {
        "Guerreiro": {"Força": 1, "Destreza": 1, "Constituição": 1, "Inteligência": 0, "Sabedoria": 0, "Carisma": 0},
        "Feiticeiro": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 1, "Sabedoria": 0, "Carisma": 1},
        "Ladino": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 1, "Sabedoria": 1, "Carisma": 0},
        "Guardião": {"Força": 0, "Destreza": 1, "Constituição": 0, "Inteligência": 1, "Sabedoria": 1, "Carisma": 0}
    }

    atributostotais = {}  # Dicionário para armazenar os atributos totais
    # Calcula os atributos totais somando os atributos da raça e da classe
    for atributo in atributosraca[raca]:
        atributostotais[atributo] = atributosraca[raca][atributo] + atributosclasse[classe][atributo]

    # Cálculo dos atributos específicos para cada classe
    if classe == "Guerreiro":
        HP = r.randint(25, 30) + atributostotais["Constituição"]  # HP varia entre 20 e 25 mais a Constituição
        DEF = r.randint(25, 30) + atributostotais["Destreza"]  # DEF varia entre 25 e 30 mais a Destreza
        ATK = r.randint(4, 8) + atributostotais["Força"] + atributostotais["Destreza"]  # ATK baseado em Força e Destreza
        MAG = atributostotais["Inteligência"] + atributostotais["Carisma"]  # MAG baseado em Inteligência e Carisma
        atributosjogador = {"HP": HP, "DEF": DEF, "ATK": ATK, "MAG": MAG}  # Dicionário com atributos do jogador
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")  # Exibe os atributos

    elif classe == "Feiticeiro":
        HP = r.randint(20, 25) + atributostotais["Constituição"]  # HP varia entre 15 e 20
        DEF = r.randint(20, 25) + atributostotais["Destreza"]  # DEF varia entre 20 e 25
        ATK = atributostotais["Força"]  # ATK baseado apenas em Força
        MAG = r.randint(10, 15) + atributostotais["Inteligência"] + atributostotais["Carisma"]  # MAG varia entre 10 e 15
        atributosjogador = {"HP": HP, "DEF": DEF, "ATK": ATK, "MAG": MAG}  # Dicionário com atributos do jogador
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")  # Exibe os atributos

    elif classe == "Ladino":
        HP = r.randint(25, 30) + atributostotais["Constituição"]  # HP varia entre 20 e 25
        DEF = r.randint(20, 25) + atributostotais["Destreza"]  # DEF varia entre 20 e 25
        ATK = r.randint(4, 8) + atributostotais["Força"] + atributostotais["Inteligência"]  # ATK baseado em Força e Inteligência
        MAG = atributostotais["Inteligência"] + atributostotais["Carisma"] + atributostotais["Sabedoria"]  # MAG baseado em Inteligência, Carisma e Sabedoria
        atributosjogador = {"HP": HP, "DEF": DEF, "ATK": ATK, "MAG": MAG}  # Dicionário com atributos do jogador
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")  # Exibe os atributos

    elif classe == "Guardião":
        HP = r.randint(20, 25) + atributostotais["Constituição"]  # HP varia entre 15 e 20
        DEF = r.randint(15, 20) + atributostotais["Destreza"]  # DEF varia entre 15 e 20
        ATK = r.randint(4, 8) + atributostotais["Força"] + atributostotais["Destreza"]  # ATK baseado em Força e Destreza
        MAG = r.randint(8, 12) + atributostotais["Inteligência"] + atributostotais["Sabedoria"]  # MAG varia entre 8 e 12
        atributosjogador = {"HP": HP, "DEF": DEF, "ATK": ATK, "MAG": MAG}  # Dicionário com atributos do jogador
        print(f"HP: {HP}, DEF: {DEF}, ATK: {ATK}, MAG: {MAG}")  # Exibe os atributos

    return atributosjogador  # Retorna os atributos do jogador

# Função para criar a ficha do jogador com nome, raça, classe e atributos
def jogador(nome, raca, classe, atributos):
    fichajogador = {}  # Dicionário para armazenar a ficha do jogador
    # Adiciona informações à ficha com base na classe escolhida
    if classe == "Guerreiro":
        fichajogador = {"Nome": nome, "Raça": raca, "Classe": classe, "Atributos": atributos, "Arma": "Espada"}  # Ficha do Guerreiro

    elif classe == "Feiticeiro":
        fichajogador = {"Nome": nome, "Raça": raca, "Classe": classe, "Atributos": atributos, "Arma": "Missil Magico"}  # Ficha do Feiticeiro

    elif classe == "Ladino":
        fichajogador = {"Nome": nome, "Raça": raca, "Classe": classe, "Atributos": atributos, "Arma": "Adaga"}  # Ficha do Ladino

    elif classe == "Guardião":
        fichajogador = {"Nome": nome, "Raça": raca, "Classe": classe, "Atributos": atributos, "Arma": "Arco"}  # Ficha do Guardião

    return fichajogador  # Retorna a ficha do jogador

# Função para adicionar um item à mochila do jogador
def adicionarmochila(item, mochila):
    quantidade = 0  # Inicializa a quantidade do item
    for objeto in mochila:  # Verifica se o item já está na mochila
        if objeto[0] == item:
            quantidade += 1  # Incrementa a quantidade se o item já existe
            objeto[1] = quantidade  # Atualiza a quantidade
            break
    else:
        mochila.append([item, 1])  # Adiciona o item à mochila se não existir
        print(Fore.GREEN + f"{item} foi adicionado a sua mochila.")  # Mensagem de confirmação
    return mochila  # Retorna a mochila atualizada

# Função para mostrar os itens na mochila do jogador
def mostrarmochila(mochila):
    if mochila:  # Verifica se a mochila não está vazia
        print(Fore.GREEN + "Mochila:")
        for item in mochila:  # Exibe cada item na mochila
            print(Fore.GREEN + f"- {item[0]} (Quantidade: {item[1]})")
    else:
        print(Fore.GREEN + "Sua Mochila está vazia.")  # Mensagem se a mochila estiver vazia

# Função para usar um item da mochila
import random as r  # Certifique-se de importar o módulo random

def usaritem(item, mochila, atributos):
    if not isinstance(mochila, list):  # Valida se mochila é uma lista
        print(Fore.GREEN + "Erro: 'mochila' não é uma lista válida.")
        return atributos, mochila

    for objeto in mochila:
        if not isinstance(objeto, list) or len(objeto) < 2:  # Valida se cada item é uma lista com pelo menos dois elementos
            print(Fore.GREEN + f"Erro: Um dos itens na mochila não está no formato esperado: {objeto}")
            continue

        if objeto[0] == item:  # Verifica o nome do item
            if item == "Poção de Cura":  # Verifica se é uma Poção de Cura
                if objeto[1] > 0:  # Confirma se há quantidade suficiente
                    cura = r.randint(10, 20)  # Define o valor de cura aleatoriamente
                    atributos["HP"] = (atributos["HP"] + cura)  # Garante que o HP não ultrapasse o máximo
                    objeto[1] -= 1  # Decrementa a quantidade da poção
                    print(Fore.GREEN + f"Você usou uma Poção de Cura e restaurou {cura} pontos de vida!")
                    if objeto[1] == 0:  # Remove o item se sua quantidade chegar a zero
                        mochila.remove(objeto)
                else:
                    print(Fore.GREEN + f"Você não tem mais {item} disponível.")
            else:
                print(Fore.GREEN + f"O item '{item}' não pode ser usado ou não é funcional.")
            return atributos, mochila  # Retorna os valores atualizados

    print(Fore.GREEN + f"O item '{item}' não está na mochila.")  # Mensagem caso o item não seja encontrado
    return atributos, mochila  # Retorna os valores originais