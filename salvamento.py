import json
import os  # Adicionado para verificar a existência do arquivo



def salvarjogo(jogador):
    with open('jogosalvo.json', 'w') as f:
        json.dump(jogador, f)
    print("Jogo salvo com sucesso!")


def carregarjogo():
    if os.path.exists('jogosalvo.json'):
        with open('jogosalvo.json', 'r') as f:
            jogador = json.load(f)
        print("Jogo carregado com sucesso!")
        return jogador
    else:
        print("Nenhum jogo salvo encontrado.")
        return None
