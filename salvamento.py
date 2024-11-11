import json
import os


def salvarjogo(jogador):
    with open('jogo_salvo.json', 'w') as f:
        json.dump(jogador, f)
    print("Jogo salvo com sucesso!")


def carregarjogo():
    if os.path.exists('jogo_salvo.json'):
        with open('jogo_salvo.json', 'r') as f:
            jogador = json.load(f)
        print("Jogo carregado com sucesso!")
        return jogador
    else:
        print("Nenhum jogo salvo encontrado.")
        return None
