# ==========================================
# EXERCÍCIO 1 - Função de Soma
# ==========================================

def soma(a, b):
    return a + b

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Resultado:", soma(numero1, numero2))


# ==========================================
# EXERCÍCIO 2 - Função de Média
# ==========================================

def media(lista):
    return sum(lista) / len(lista)

numeros = input("Digite os números separados por espaço: ")

lista = []
for numero in numeros.split():
    lista.append(float(numero))

print("Média:", media(lista))


# ==========================================
# EXERCÍCIO 3 - Verificação de Paridade
# ==========================================

def verifica_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número: "))

print(verifica_paridade(numero))


# ==========================================
# EXERCÍCIO 4 - Soma de Matrizes
# ==========================================

def soma_matrizes(matriz1, matriz2):

    resultado = []

    for i in range(len(matriz1)):
        linha = []

        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j] + matriz2[i][j])

        resultado.append(linha)

    print("Matriz resultante:")

    for linha in resultado:
        print(linha)


matriz1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

soma_matrizes(matriz1, matriz2)


# ==========================================
# EXERCÍCIO 5 - Verificação de Primo
# ==========================================

def verifica_primo(numero):

    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


numero = int(input("Digite um número: "))

if verifica_primo(numero):
    print("É primo.")
else:
    print("Não é primo.")


# ==========================================
# EXERCÍCIO 6 - Calculadora Simples
# ==========================================

def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

valor1 = float(input("Primeiro número: "))
valor2 = float(input("Segundo número: "))
operacao = input("Operação (+,-,*,/): ")

if operacao == "+":
    print(soma(valor1,valor2))
elif operacao == "-":
    print(subtracao(valor1,valor2))
elif operacao == "*":
    print(multiplicacao(valor1,valor2))
elif operacao == "/":
    print(divisao(valor1,valor2))
else:
    print("Operação inválida.")


# ==========================================
# EXERCÍCIO 7 - Desafio Temperaturas
# ==========================================

import math

medicoes = [16, -25, 9, -36, 49]

medicoes_corrigidas = []

for valor in medicoes:
    medicoes_corrigidas.append(abs(valor))

print("Medições corrigidas:", medicoes_corrigidas)

menor = min(medicoes_corrigidas)
maior = max(medicoes_corrigidas)

print("Menor valor:", menor)
print("Maior valor:", maior)

print("Raiz quadrada do maior valor:", math.sqrt(maior))


# ==========================================
# EXERCÍCIO 8 - Sistema de Notas
# ==========================================

alunos = {}

while True:

    resposta = input("Deseja adicionar um aluno? (S/N): ")

    if resposta.upper() == "N":
        break

    nome = input("Digite o nome do aluno: ")

    entrada = input(f"Digite as notas de {nome} separadas por espaço: ")

    notas = []

    for nota in entrada.split():
        notas.append(float(nota))

    alunos[nome] = notas

print("\nMédias dos alunos:")

maior_media = -1
melhor_aluno = ""

for nome, notas in alunos.items():

    media = sum(notas) / len(notas)

    print(f"{nome}: {media:.2f}")

    if media > maior_media:
        maior_media = media
        melhor_aluno = nome

print(f"\nA maior média é de {melhor_aluno}: {maior_media:.2f}")
