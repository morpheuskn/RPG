import random as r  # Importa a biblioteca random e a renomeia como r para gerar números aleatórios
from colorama import Fore # Importa a função Fore do módulo colorama
# Função para lidar com a morte do jogador
def morte():
    print(Fore.GREEN + "Você Morreu")
    print(Fore.GREEN + "Game Over")  # Mensagem de Game Over
    exit()  # Encerra o programa

# Define a função 'ataque' que calcula o dano causado por um atacante a um defensor
def ataque(atacante, defensor):
    dano = 0  # Inicializa a variável dano
    # Verifica se o atacante é Guerreiro ou Ladino
    if atacante["Classe"] == "Guerreiro" or atacante["Classe"] == "Ladino":
        # Calcula o dano como a diferença entre o ataque e a defesa, garantindo que não seja negativo
        dano = max(atacante["Atributos"]["ATK"] - defensor["Atributos"]["DEF"], 0)
    # Verifica se o atacante é um Feiticeiro
    elif atacante["Classe"] == "Feiticeiro":
        # Calcula o dano usando o atributo MAG do atacante
        dano = max(atacante["Atributos"]["MAG"] - defensor["Atributos"]["DEF"], 0)
    # Verifica se o atacante é um Guardião
    elif atacante["Classe"] == "Guardião":
        # Calcula o dano somando ATK e MAG do atacante
        dano = max(atacante["Atributos"]["ATK"] + atacante["Atributos"]["MAG"] - defensor["Atributos"]["DEF"], 0)

    # Emula um Dado de 20 lados (entre 1 e 20)
    Dado20 = r.randint(1, 20)
    dano += Dado20

    # Se o fator aleatório for 20, dobra o dano
    if Dado20 == 20:
        dano *= 2
        print(Fore.GREEN + f"Crítico! {atacante['Nome']} causou Double Damage !")

    # Subtrai o dano do HP do defensor
    defensor["Atributos"]["HP"] -= dano

    return dano  # Retorna o dano causado

# Define a função 'combate' que simula um combate entre um jogador e um inimigo
def combate(jogador, inimigo):
    # Continua o combate enquanto ambos, jogador e inimigo, tiverem HP maior que 0
    while jogador["Atributos"]["HP"] > 0 and inimigo["Atributos"]["HP"] > 0:
        # O jogador ataca o inimigo
        dano = ataque(jogador, inimigo)
        print(f"{jogador['Nome']} ataca {inimigo['Nome']} causando {dano} de dano.")
        print(f"{inimigo['Nome']} tem {inimigo['Atributos']['HP']} HP restantes.")
        
        # Verifica se o inimigo foi derrotado
        if inimigo["Atributos"]["HP"] <= 0:
            print(Fore.GREEN + f"{inimigo['Nome']} foi derrotado!")
            break  # Encerra o combate se o inimigo for derrotado
        
        # O inimigo ataca o jogador
        dano = ataque(inimigo, jogador)
        print(f"{inimigo['Nome']} ataca {jogador['Nome']} causando {dano} de dano.")
        print(f"{jogador['Nome']} tem {jogador['Atributos']['HP']} HP restantes.")
        
        # Verifica se o jogador foi derrotado
        if jogador["Atributos"]["HP"] <= 0:
            print(Fore.GREEN + f"{jogador['Nome']} foi derrotado!")
            morte()  # Encerra o programa se o jogador for derrotado
            break  # Encerra o combate

# Define inimigos com suas respectivas classes e atributos
caomagico = {'Nome': 'Cão Magico', 'Raça': 'Cão Demoniaco', 'Classe': 'Mago', 'Atributos': {'HP': 12, 'DEF': 5, 'ATK': 0, 'MAG': 6}}
caoguerreiro = {'Nome': 'Cão Guerreiro', 'Raça': 'Cão Demoniaco', 'Classe': 'Guerreiro', 'Atributos': {'HP': 13, 'DEF': 6, 'ATK': 6, 'MAG': 0}}
caoberserker = {'Nome': 'Cão Berserker', 'Raça': 'Cão Demoniaco', 'Classe': 'Berserker', 'Atributos': {'HP': 20, 'DEF': 5, 'ATK': 6, 'MAG': 0}}
caoarqueiro = {'Nome': 'Cão Arqueiro', 'Raça': 'Cão Demoniaco', 'Classe': 'Arqueiro', 'Atributos': {'HP': 20, 'DEF': 11, 'ATK': 6, 'MAG': 0}}

bandidomago = {'Nome': 'Bandido Mago', 'Raça': 'Orc', 'Classe': 'Mago', 'Atributos': {'HP': 16, 'DEF': 7, 'ATK': 0, 'MAG': 4}}
bandidoberserker = {'Nome': 'Bandido Berserker', 'Raça': 'Orc', 'Classe': 'Berserker', 'Atributos': {'HP': 16, 'DEF': 6, 'ATK': 4, 'MAG': 0}}
bandidoguerreiro = {'Nome': 'Bandido Guerreiro', 'Raça': 'Orc', 'Classe': 'Guerreiro', 'Atributos': {'HP': 14, 'DEF': 6, 'ATK': 4, 'MAG': 0}}
bandidoarqueiro = {'Nome': 'Bandido Arqueiro', 'Raça': 'Orc', 'Classe': 'Arqueiro', 'Atributos': {'HP': 24, 'DEF': 9, 'ATK': 4, 'MAG': 0}}

astaorth = {'Nome': 'Astaroth', 'Raça': 'Demonio Superior', 'Classe': 'Mago', 'Atributos': {'HP': 50, 'DEF': 7, 'ATK': 0, 'MAG': 10}}
kladu = {'Nome': 'Kladu', 'Raça': 'Demonio', 'Classe': 'Berserker', 'Atributos': {'HP': 45, 'DEF': 6, 'ATK': 8, 'MAG': 0}}
anungunrama = {'Nome': 'Anung Un Rama', 'Raça': 'Demonio', 'Classe': 'Guerreiro', 'Atributos': {'HP': 40, 'DEF': 5, 'ATK': 8, 'MAG': 0}}
zodd = {'Nome': 'Zodd', 'Raça': 'Demonio', 'Classe': 'Guardião', 'Atributos': {'HP': 35, 'DEF': 9, 'ATK': 4, 'MAG': 4}}
khan = {'Nome': 'Khan', 'Raça': 'Demonio', 'Classe': 'Ladino', 'Atributos': {'HP': 30, 'DEF': 10, 'ATK': 8, 'MAG': 0}}