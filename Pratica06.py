#Prática 06: Programação em Python
#01- Gerador de senha
import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
nova_senha = gerar_senha(tamanho_senha)
print("Sua senha gerada é: {nova_senha}")

#02- Perfil de Usuário (API 'Random User Generator')
import random
import string
import requests

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}\n Email: {email}\n País: {pais}"
    except requests.RequestException as e:
        return f"Erro ao obter usuário aleatório: {e}"

def main():
    print("Gerando um usuário aleatório...")
    usuario = obter_usuario_aleatorio()
    print(usuario)

if __name__ == "__main__":
    main()

#03- Consultar CEP (API 'ViaCEP')
import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if "erro" in dados:
            return "CEP não encontrado."
        return f"""
        CEP: {dados['cep']}
        Logradouro: {dados['logradouro']}
        Bairro: {dados['bairro']}
        Cidade: {dados['localidade']}
        Estado: {dados['uf']}
        """
    except requests.RequestException as e:
        return f"Erro na consulta: {e}"

def main():
    cep = input("Digite um CEP para consulta (apenas números): ")
    print("\nConsultando CEP...")
    resultado = consultar_cep(cep)
    print(resultado)

if __name__ == "__main__":
    main()

#04- Consultar cotação USD, EUR, GBP (API 'AwesomeAPI')
import requests
from datetime import datetime

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
        Moeda: {moeda} para BRL
        Valor: R$ {float(cotacao['bid']):.2f}
        Máxima: R$ {float(cotacao['high']):.2f}
        Mínima: R$ {float(cotacao['low']):.2f}
        Data/Hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}
        """
    except requests.RequestException as e:
        return f"Erro ao obter cotação: {e}"
    except KeyError:
        return "Moeda não encontrada ou não suportada."

def main():
    moeda = input("Digite o código da moeda para cotação (ex: USD, EUR, GBP): ").upper()
    print("\nObtendo cotação...")
    resultado = obter_cotacao(moeda)
    print(resultado)

if __name__ == "__main__":
    main()