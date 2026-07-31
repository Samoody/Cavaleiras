# ==========================================
# EXERCÍCIO 1 - Leitura de Dados
# ==========================================

import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df = pd.read_csv(url)

print(df.head())


# ==========================================
# EXERCÍCIO 2 - Manipulação de Colunas
# ==========================================

df["sepal_sum"] = df["sepal_length"] + df["sepal_width"]

df.rename(columns={"species": "especie"}, inplace=True)

print(df.head())


# ==========================================
# EXERCÍCIO 3 - Exclusão de Colunas e Linhas
# ==========================================

df.drop(columns=["sepal_sum"], inplace=True)

df.drop(index=0, inplace=True)

print(df.head())


# ==========================================
# EXERCÍCIO 4 - Tratamento de Valores Faltantes
# ==========================================

print("Valores faltantes:")
print(df.isna().sum())

df.fillna(0, inplace=True)

df.sort_values(by="petal_length", ascending=False, inplace=True)

print(df.head())


# ==========================================
# EXERCÍCIO 5 - Histograma
# ==========================================

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.hist(df["sepal_length"])

plt.title("Histograma do Comprimento da Sépala")
plt.xlabel("Sepal Length")
plt.ylabel("Frequência")

plt.show()


# ==========================================
# EXERCÍCIO 6 - Gráfico de Dispersão
# ==========================================

plt.figure(figsize=(8,5))

plt.scatter(df["sepal_length"], df["sepal_width"])

plt.title("Sepal Length x Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.savefig("scatter_iris.png")

plt.show()
