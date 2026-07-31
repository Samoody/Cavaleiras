numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2

print("O resultado é:", soma)


CALCULO SALARIO
numero1 = float(input("Valor da hora: "))
numero2 = float(input("Quantidade de horas por dia: "))

salario = numero1 * numero2 * 30

print("Salário final:", salario)
3. Verificar se um número é par ou ímpar
num_int = int(input("Digite um número inteiro: "))

paridade = num_int % 2

eh_par = (paridade == 0)

print(eh_par)
4- DIVISÃO POR CORES
cor1 = input("Digite a primeira cor: ")
cor2 = input("Digite a segunda cor: ")

if cor1 == "Amarelo" and cor2 == "Azul":
    print("Grupo 1")
elif cor1 == "Amarelo" and cor2 == "Vermelho":
    print("Grupo 2")
elif cor1 == "Rosa" and cor2 == "Verde":
    print("Grupo 1")
elif cor1 == "Rosa" and cor2 == "Roxo":
    print("Grupo 2")
else:
    print("Grupo inválido")
5- FOLHA DE PAGAMENTO
valor_hora = float(input("Digite o valor da hora de trabalho: "))
horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos

print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
print("IR: R$ {:.2f}".format(ir))
print("INSS: R$ {:.2f}".format(inss))
print("FGTS: R$ {:.2f}".format(fgts))
print("Total de descontos: R$ {:.2f}".format(total_descontos))
print("Salário Líquido: R$ {:.2f}".format(salario_liquido))
5.2
animacao = int(input("É de animação? (1 = Sim, 0 = Não): "))

if animacao == 1:
    disney = int(input("É da Disney? (1 = Sim, 0 = Não): "))

    if disney == 1:
        print("Frozen")
    else:
        print("Shrek")

else:
    terror = int(input("É de terror? (1 = Sim, 0 = Não): "))

    if terror == 1:
        comedia = int(input("É de comédia? (1 = Sim, 0 = Não): "))

        if comedia == 1:
            print("Todo Mundo em Pânico")
        else:
            print("Halloween")

    else:
        drama = int(input("É de drama? (1 = Sim, 0 = Não): "))

        if drama == 1:
            print("Diário de uma Paixão")
        else:
            print("Como se Fosse a Primeira Vez")


5.3
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):

    if lado1 == lado2 == lado3:
        print("Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Isósceles")
    else:
        print("Escaleno")

else:
    print("Os valores não formam um triângulo válido.")
EX PRA CASA
premio = 780000

primeiro = premio * 0.46
segundo = premio * 0.32
terceiro = premio - primeiro - segundo

print("Primeiro ganhador: R$", primeiro)
print("Segundo ganhador: R$", segundo)
print("Terceiro ganhador: R$", terceiro)
CONVERSÃO CELSIUS EM FAREN
celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * (9.0 / 5.0) + 32.0

print("Temperatura em Fahrenheit:", fahrenheit)
