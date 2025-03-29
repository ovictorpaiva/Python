#Prática 07: Programação em Python 
# 01- Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. 
# Calcule a média e o desvio padrão do tempo de execução constantes.
import numpy as np

def ler_log_e_calcular_estatisticas (nome_arquivo):
    tempos = []

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                try:
                    tempo = float(linha.strip())
                    tempos.append(tempo)
                except ValueError:
                    print(f"Aviso: Linha ignorada - '{linha.strip()}' não é um número valido.")

        if tempos:
            media = np.mean(tempos)
            desvio_padrao = np.std(tempos)
            print("Média do tempo de execução: (media:.2f) segundos")
            print("Desvio padrão do tempo de execução: (desvio_padrao:.2f) segundos")
        else:
            print(f"Nenhum dado válido encontrado no arquivo.")
    except FileNotFoundError:
        print("Erro: O arquivo especificado não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

        nome_arquivo = "log_treinamento.txt"
        ler_log_e_calcular_estatisticas(nome_arquivo)


#02- Crie um script em Python que escreva dados em um arquivo CSV. 
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""
import csv

nome_arquivo = 'pessoas.csv'

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', 25, 'São Paulo'],
    ['Maria', 32, 'Rio de Janeiro'],
    ['Pedro', 45, 'Belo Horizonte'],
    ['Ana', 22, 'Porto Alegre'],
    ['Carlos', 35, 'Curitiba'],
    ['Beatriz', 28, 'Recife'],
]

with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)"

"""

#03- Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. 
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""import csv 

def ler_csv(nome_arquivo):
    try:
        whith open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
                print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não foi encontrado")
        except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

ler_csv('pessoas.csv')"""

#04- Crie um script em Python que leia e escreva dados em um arquivo JSON. 
# O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
import json

def escrever_json(nome, idade, cidade, arquivo="pessoas.json"):
    dados = {
        "Nome": nome,
        "Idade": idade,
        "Cidade": cidade
        }

    with open(arquivo, mode='w') as f:
        json.dump(dados, f, indent=4)

def ler_json(arquivo="pessoas.json"):
    with open(arquivo, mode='r') as f:
        dados = json.load(f)
        return dados
nome = input("Esvreva seu nome: ")
idade = input("Esvreva sua idade: ")
cidade = input("Esvreva sua cidade: ")

escrever_json(nome, idade, cidade)

dados_pessoas = ler_json()
print("\nDados lidos do arquivo JSON: ")
print(dados_pessoas)