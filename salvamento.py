import json  # Importa a biblioteca json para manipulação de dados em formato JSON
import os  # Importa a biblioteca os para interagir com o sistema operacional, como verificar a existência de arquivos

def salvarjogo(jogador):
    # Função para salvar o estado do jogo em um arquivo JSON
    with open('jogosalvo.json', 'w') as f:  # Abre (ou cria) o arquivo 'jogosalvo.json' em modo de escrita
        json.dump(jogador, f)  # Converte o objeto 'jogador' em formato JSON e escreve no arquivo
    print("Jogo salvo com sucesso!")  # Mensagem de confirmação que o jogo foi salvo

def carregarjogo():
    # Função para carregar o estado do jogo a partir de um arquivo JSON
    if os.path.exists('jogosalvo.json'):  # Verifica se o arquivo 'jogosalvo.json' existe
        with open('jogosalvo.json', 'r') as f:  # Abre o arquivo em modo de leitura
            jogador = json.load(f)  # Lê o conteúdo do arquivo e o converte de JSON para um objeto Python
        print("Jogo carregado com sucesso!")  # Mensagem de confirmação que o jogo foi carregado
        return jogador  # Retorna o objeto 'jogador' carregado
    else:
        print("Nenhum jogo salvo encontrado.")  # Mensagem informando que não há jogos salvos
        return None  # Retorna None se não houver jogos salvos