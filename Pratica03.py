#Prática 03: Programação em Python
#1- Classificador de Idade
idade =int(input('Digite sua idade: '))

if idade <= 0:
    print('Idade inválida')
elif idade <= 12:
    print('É uma Criança')
elif idade <= 17:
    print('É um Adolescente')
elif idade <= 59:
    print('É um Adulto')
else:
    print('É um Idoso')

#2- Calculadora de IMC
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = 'Abaixo do peso'
elif imc < 25:
    classificacao = 'Peso normal'
elif imc < 30:
    classificacao = 'Sobrepeso'
else:
    classificacao = 'Obeso'
print(f'Seu IMC é: {imc:.2f} e sua classificação é: {classificacao}')

#3- Conversor de Temperatura
print('Conversor de Temperatura')
temperatura = int(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F ou K): ").upper()

if unidade_origem == unidade_destino:
    resultado = temperatura
    print('A temperatura de origem e de destino são iguais')

elif unidade_origem == 'C':
    if unidade_destino == 'F':
        resultado = (temperatura * 9/5) + 32
    elif unidade_destino == 'K':
        resultado = temperatura + 273.15

elif unidade_origem == 'F':
    if unidade_destino == 'C':
        resultado = (temperatura - 32) * 5/9
    elif unidade_destino == 'K':
        resultado = (temperatura - 32) * 5/9 + 273.15

elif unidade_origem == 'K':
    if unidade_destino == 'C':
        resultado = temperatura - 273.15
    elif unidade_destino == 'F':
        resultado = (temperatura - 273.15) * 9/5 + 32
else:
    print('Unidade inválida')
    
print(f'A temperatura convertida é: {resultado:.2f} {unidade_destino}')

#4- Verificador de Ano Bissexto
ano = int(input('Digite um ano: '))
if ano % 4 ==0:
    if ano %100 ==0:
        if ano % 400 ==0:
            print(f'{ano} é um ano bissexto')
        else:
            print(f'{ano} não é um ano bissexto')
    else:
        print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')