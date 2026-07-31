# ==========================================
# PARTE 1 - TUPLAS
# ==========================================

# Exercício 1 - Desempacotando Dados do Sistema

computador = ("Intel Core i5", 16, 512)

processador, ram, armazenamento = computador

print("Processador:", processador)
print("Memória RAM:", ram, "GB")
print("Armazenamento:", armazenamento, "GB")


# ==========================================
# Exercício 2 - Notas da Competição
# ==========================================

notas = (8.5, 9.0, 7.5, 8.8, 9.2)

print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
print("Média:", sum(notas) / len(notas))


# ==========================================
# PARTE 2 - DICIONÁRIOS
# ==========================================

# Exercício 3 - Ficha de Matrícula

aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["idade"] = int(input("Digite a idade: "))
aluno["cidade"] = input("Digite a cidade: ")

print("\nFicha do Aluno")

for chave, valor in aluno.items():
    print(chave, ":", valor)


# ==========================================
# Exercício 4 - Consulta de Estoque
# ==========================================

estoque = {
    "coxinha": 15,
    "esfiha": 10,
    "refrigerante": 30
}

produto = input("Digite o produto: ")

if produto in estoque:
    print("Quantidade em estoque:", estoque[produto])
else:
    print("Produto não vendido ou indisponível.")


# ==========================================
# Exercício 5 - Contador de Letras
# ==========================================

palavra = input("Digite uma palavra: ")

contador = {}

for letra in palavra:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print(contador)
