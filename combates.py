# Define a função 'ataque' que calcula o dano causado por um atacante a um defensor
def ataque(atacante, defensor):
    dano = 0  # Inicializa a variável dano
    # Verifica se o atacante é Guerreiro ou Ladino
    if atacante["Classe"] == "Guerreiro" or atacante["Classe"] == "Ladino":
        # Calcula o dano como a diferença entre o ataque e a defesa, garantindo que não seja negativo
        dano = max(atacante["Atributos"]["ATK"] - defensor["Atributos"]["DEF"], 0)
        # Subtrai o dano do HP do defensor
        defensor["Atributos"]["HP"] -= dano
    # Verifica se o atacante é um Feiticeiro
    elif atacante["Classe"] == "Feiticeiro":
        # Calcula o dano usando o atributo MAG do atacante
        dano = max(atacante["Atributos"]["MAG"] - defensor["Atributos"]["DEF"], 0)
        defensor["Atributos"]["HP"] -= dano
    # Verifica se o atacante é um Guardião
    elif atacante["Classe"] == "Guardião":
        # Calcula o dano somando ATK e MAG do atacante
        dano = max(atacante["Atributos"]["ATK"] + atacante["Atributos"]["MAG"] - defensor["Atributos"]["DEF"], 0)
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
            print(f"{inimigo['Nome']} foi derrotado!")
            break  # Encerra o combate se o inimigo for derrotado
        
        # O inimigo ataca o jogador
        dano = ataque(inimigo, jogador)
        print(f"{inimigo['Nome']} ataca {jogador['Nome']} causando {dano} de dano.")
        print(f"{jogador['Nome']} tem {jogador['Atributos']['HP']} HP restantes.")
        
        # Verifica se o jogador foi derrotado
        if jogador["Atributos"]["HP"] <= 0:
            print(f"{jogador['Nome']} foi derrotado!")
            exit()  # Encerra o programa se o jogador for derrotado
            break  # Encerra o combate

# Define inimigos com suas respectivas classes e atributos
caomagico = {'Nome': 'Cão Magico', 'Raça': 'Cão Demoniaco', 'Classe': 'Mago', 'Atributos': {'HP': 12, 'DEF': 5, 'ATK': 0, 'MAG': 5}}
caoguerreiro = {'Nome': 'Cão Guerreiro', 'Raça': 'Cão Demoniaco', 'Classe': 'Guerreiro', 'Atributos': {'HP': 13, 'DEF': 6, 'ATK': 6, 'MAG': 0}}
caoberserker = {'Nome': 'Cão Berserker', 'Raça': 'Cão Demoniaco', 'Classe': 'Berserker', 'Atributos': {'HP': 20, 'DEF': 5, 'ATK': 5, 'MAG': 0}}
caoarqueiro = {'Nome': 'Cão Arqueiro', 'Raça': 'Cão Demoniaco', 'Classe': 'Arqueiro', 'Atributos': {'HP': 20, 'DEF': 11, 'ATK': 5, 'MAG': 0}}

goblinmago = {'Nome': 'Goblin Mago', 'Raça': 'Goblin', 'Classe': 'Mago', 'Atributos': {'HP': 22, 'DEF': 13, 'ATK': 0, 'MAG': 6}}

orcmmago = {'Nome': 'Orc Mago', 'Raça': 'Orc', 'Classe': 'Mago', 'Atributos': {'HP': 16, 'DEF': 7, 'ATK': 0, 'MAG': 5}}
orcberserker = {'Nome': 'Orc Berserker', 'Raça': 'Orc', 'Classe': 'Berserker', 'Atributos': {'HP': 16, 'DEF': 6, 'ATK': 4, 'MAG': 0}}
orcguerreiro = {'Nome': 'Orc Guerreiro', 'Raça': 'Orc', 'Classe': 'Guerreiro', 'Atributos': {'HP': 14, 'DEF': 6, 'ATK': 5, 'MAG': 0}}
orcarqueiro = {'Nome': 'Orc Arqueiro', 'Raça': 'Orc', 'Classe': 'Arqueiro', 'Atributos': {'HP': 24, 'DEF': 9, 'ATK': 9, 'MAG': 0}}

esqueletomago = {'Nome': 'Esqueleto Mago', 'Raça': 'Esqueleto', 'Classe': 'Mago', 'Atributos': {'HP': 19, 'DEF': 6, 'ATK': 0, 'MAG': 6}}
esqueletoarqueiro = {'Nome': 'Esqueleto Arqueiro', 'Raça': 'Esqueleto', 'Classe': 'Arqueiro', 'Atributos': {'HP': 16, 'DEF': 11, 'ATK': 7, 'MAG': 0}}