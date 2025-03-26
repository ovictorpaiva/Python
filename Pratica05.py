#Prática 05: Programação em Python
#01- Calculadora de gorjetas
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round (gorjeta, 2)

    total_conta = 100.00
    porcentagem = 15
    gorjeta = calcular_gorjeta(total_conta, porcentagem)
    print(f"Para uma conta de R${total_conta:.2f} e uma gorjeta de {porcentagem}%, o valor da gorjeta é de R${gorjeta:.2f}")

#02-Palavra ou frase palídromo
def is_palindromo(texto):
    texto_limpo = ''.join(char.lower() 
        for char in texto 
        if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = "A cara rajada da jararaca"
resultado = is_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{frase}' é um palíndromo? {resposta}")

#03- Idade em dias
import datatime

def calculadora_idade_em_dias(ano_nascimento):

    ano_atual = datatime.datatime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nascimento = int(input("Digite seu ano de nascimento"))

idade_em_dias = calculadora_idade_em_dias(ano_nascimento)
print(f"Sua idade em dias aproximadamente é {idade_em_dias} dias")