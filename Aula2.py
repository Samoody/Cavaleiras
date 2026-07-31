# ==========================================
# EXERCÍCIO 1 - Índice Pluviométrico
# ==========================================

soma = 0
indice_minimo = None
dia_minimo = 0

for dia in range(1, 8):
    indice = float(input(f"Qual o Índice Pluviométrico do dia {dia}? "))
    soma += indice

    if indice_minimo is None or indice < indice_minimo:
        indice_minimo = indice
        dia_minimo = dia

media = soma / 7

print(f"Índice Médio: {media:.2f}")
print(f"Índice Mínimo: {indice_minimo:.2f}")
print(f"Dia do Mínimo: {dia_minimo}")


# ==========================================
# EXERCÍCIO 2 - Teoria do Prof. Humberto
# ==========================================

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = numero1 + numero2
resultado = str(resultado)
resultado = resultado.replace("0", "")

print("Resultado:", resultado)


# ==========================================
# EXERCÍCIO 3 - Localizador de Vogais
# ==========================================

texto = input("Entrada: ")

vogais = "aeiouAEIOU"

for i in range(len(texto)):
    if texto[i] in vogais:
        print(i, texto[i])


# ==========================================
# EXERCÍCIO 4 - Tabuada
# ==========================================

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# ==========================================
# EXERCÍCIO 5 - Somatório
# ==========================================

soma = 0

while True:
    numero = int(input("Digite um número (negativo para sair): "))

    if numero < 0:
        break

    soma += numero

print("Soma dos números positivos:", soma)


# ==========================================
# EXERCÍCIO 6 - Validador de Senha
# ==========================================

senha_correta = "python123"

while True:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso Concedido!")
        break
    else:
        print("Senha Incorreta! Tente novamente.")


# ==========================================
# EXERCÍCIO 7 - Vetor em Ordem Inversa
# ==========================================

vetor = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

print("Vetor na ordem inversa:")

for i in range(4, -1, -1):
    print(vetor[i], end=" ")

print()


# ==========================================
# EXERCÍCIO 8 - Média da Turma
# ==========================================

notas = []
soma = 0

for i in range(6):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)
    soma += nota

media = soma / 6

print(f"Média da turma: {media:.2f}")
print("Notas iguais ou acima da média:")

for nota in notas:
    if nota >= media:
        print(f"- {nota:.2f}")


# ==========================================
# EXERCÍCIO 9 - Maior e Menor Valor
# ==========================================

vetor = []

for i in range(8):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]
indice_maior = 0
indice_menor = 0

for i in range(8):
    if vetor[i] > maior:
        maior = vetor[i]
        indice_maior = i

    if vetor[i] < menor:
        menor = vetor[i]
        indice_menor = i

print(f"Maior valor: {maior} (índice {indice_maior})")
print(f"Menor valor: {menor} (índice {indice_menor})")


# ==========================================
# EXERCÍCIO 10 - Soma da Diagonal Principal
# ==========================================

matriz = []

print("Preencha a matriz 3x3:")

for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)

    matriz.append(linha)

soma = 0

for i in range(3):
    soma += matriz[i][i]

print("Soma dos elementos da diagonal principal:", soma)


# ==========================================
# EXERCÍCIO 11 - Maior Elemento da Matriz
# ==========================================

matriz = []

print("Preencha a matriz 3x3:")

for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)

    matriz.append(linha)

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print("Maior valor encontrado:", maior)
print(f"Posição: Linha {linha_maior}, Coluna {coluna_maior}")


# ==========================================
# EXERCÍCIO 12 - Matriz Transposta
# ==========================================

matriz = []

print("Preencha a matriz 3x3:")

for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)

    matriz.append(linha)

transposta = []

for i in range(3):
    linha = []

    for j in range(3):
        linha.append(matriz[j][i])

    transposta.append(linha)

print("Matriz Transposta:")

for linha in transposta:
    for valor in linha:
        print(f"{valor:4}", end="")
    print()
