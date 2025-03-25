#Prática 04: Programação em Python
#1- Calculadora
def calculadora():
    while true:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação desejada(+,-,*,/): ")

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                resultado = num1 / num2
            else:
                raise ValueErro("Operação inválida")
            
            print(f"O resultado da operação é: {resultado}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
        except ZeroDivisionError:
            print(f"Erro: Divisão por zero não e permitida. Tente novamente.")

calculadora()

#2- Registre as notas
def notas():
    notas = []
    while true:
        try:
            entrada = float(input("Digite uma nota ou 'sair' para sair: "))
            if entrada.lower() == "sair":
                break

            nota = (entrada)
            if 0 <= nota <= 10:
#append() é um método que adiciona um item ao final da lista.
                notas.append(nota)
            else:
                print("Nota invalida. Digite uma nota entre 0 e 10.")
                continue

        except ValueError:
            print("Valor inválido. Digite uma nota entre 0 e 10.")

        if notas:
            media = sum(notas) / len(notas)
            print(f"A média das notas é: {media:.2f}")
            print(f"Total de notas válidas: {len(notas)}")
        else:
            print("Nenhuma nota válida digitada.")

notas()

#3- Senhas forte
def senha_forte():
    while true:
        senha = input("Digite uma senha ou 'sair' para encerrar o programa:")
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        if len(senha) < 8:
            print("Senha fraca: dever ter pelo menos 8 caracteres")
            continue

        if not any(caracter.isdigit() for caracter in senha):
            print("Senha fraca: deve ter pelo menos um número")
            continue

        print("A senha é válida!.")
        break
        
#4- Números Inteiros
def numeros_inteiros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar):")

        if entrada.lower() == 'fim':
            break
            
        try:
            numero = int(entrada)
            if numero / 2 ==0:
                print (f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é impar.")
                impares += 1
        except ValueError:
            print("Valor inválido. Digite apenas números inteiro.")
            continue
            
    print(f"\nResultado final:")
    print(f"Total de números pares: {pares}")
    print(f"Total de números impares: {impares}")

numeros_inteiros()