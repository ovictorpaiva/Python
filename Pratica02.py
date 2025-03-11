#Prática 02: Programação em Python
#1- Conversor de Moeda
valor_reais = 100.00
valor_dolar = 5.20
valor_euro = 6.15
valor_convertido = valor_reais / valor_dolar
valor_convertido_euro = valor_reais / valor_euro
print(f"O valor convertido para reais é: {valor_convertido:.2f} em dólares e {valor_convertido_euro:.2f} em euros")

#2- Calculadora de Desconto
produto = "Camiseta"
preco = 50.00
desconto = 20
valor_desconto = preco * desconto/100
preco_final = preco - valor_desconto
print(f'O Produto: {produto} custa R$ {preco:.2f} com desconto de {desconto:.0f}%, o valor do desconto é R$ {valor_desconto:.2f} e o preço final é R$ {preco_final:.2f}')

#3- Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 2.5
nota_media = (nota1 + nota2 + nota3) / 3
print(f'As notas do aluno são: {nota1:.2f}, {nota2:.2f} e {nota3:.2f} e a média final é: {nota_media:.2f}')
'''
if nota_media >= 7:
    print('O aluno foi aprovado')
else:
    print('O aluno foi reprovado')
'''

#4- Calculadora de Consumo de Combustível
distancia = 300
combustivel = 25
consumo_medio = distancia / combustivel
print(f'A distância percorrida foi: {distancia}km o combustível gasto foi: {combustivel} litros e o consumo médio foi de: {consumo_medio:.2f} km/l')
