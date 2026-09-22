#EX1

numeros = open('numeros.txt', 'w', encoding='utf-8')

try:
    for i in range(10):
        num = int(input('Digite um número: '))
        numeros.write(str(num) +"\n")
    numeros.close()
except ValueError as e:
    print(f"Digite um número inteiro! ({e})")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")


#EX2

numeros = open('numeros.txt', 'r')
soma = 0
for numero in numeros.readlines():
    soma += int(numero)
numeros.close()
print(f"Soma: {soma}")

#EX3

arquivo = open('arquivo.txt', 'w', encoding='utf-8')
try:
    while True:
        num = int(input('Digite um número inteiro. Ao digitar 0, o programa para: '))
        arquivo.write(str(num) +"\n")
        if num == 0:
            break
    arquivo.close()
except ValueError as e:
    print(f"Digite um número inteiro! ({e})")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

# EX4

num = open('num.txt', 'w', encoding='utf-8')
pares = open('pares.txt', 'w', encoding='utf-8')
impares = open('impares.txt', 'w', encoding='utf-8')

try:
    while True:
        n = int(input('Digite um número inteiro. Ao digitar 0, o programa para: '))
        num.write(str(n) + "\n")
        if n == 0:
            break
        elif n % 2 == 0:
            pares.write(str(n) + "\n")
        elif n % 2 == 1:
            impares.write(str(n) + "\n")
    num.close()
except ValueError as e:
    print(f"Digite um número inteiro! ({e})")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

#EX5
pares = open('pares.txt', 'r', encoding='utf-8')
impares = open('impares.txt', 'r', encoding='utf-8')

numerosOrdenados = open('numeros_ordenados.txt', 'w', encoding='utf-8')

numeros = []

for numero in pares:
    numeros.append(int(numero))

for numero in impares:
    numeros.append(int(numero))

numeros.sort()

for numero in numeros:
    numerosOrdenados.write(str(numero) + '\n')

pares.close()
impares.close()
numerosOrdenados.close()

#EX6
# (Revisão de Lista e .split())
# frase = "hoje, eu, vou, ir, ao, mercado"
# lista = frase.split(",")
# print(lista)

try:
    with open('notas.txt', 'r') as Notas:
        linhas = Notas.readlines()
        print(linhas)
        for linha in linhas:
            alunos = linha.strip().split(',')
            print(alunos)
            media = (float(alunos[2]) + float(alunos[3]) + float(alunos[4]) + float(alunos[5])) / 4
            print(f"A média do aluno(a) {alunos[1]} é: {media:.2f}")
except FileNotFoundError as erro:
    print(f"Erro: {erro}")


#EX1 COMPLEMENTAR

try:
    ips = set()
    with open("ips.txt", "r") as arquivoips:
        for linha in arquivoips.readlines():
            ips.add(linha.strip())
        ips = list(ips)
        ips.sort()
        print(ips)

        with open('ipsunicos.txt', 'w') as arquivoips:
            arquivoips.writelines([ip + "\n" for ip in ips])

except FileNotFoundError as erro:
    print(f"Erro: {erro}")
except Exception as e:
    print(f"Ocorreu um erro no arquivo ips.txt: ({e})")


#EX2 COMPLEMENTAR

ALIMENTO = 2

try:
    contagemAlimentos = {}
    with open("foods.txt", "r") as arquivofoods:
        linhas = arquivofoods.readlines()
        print(linhas)
        for linha in linhas:
            pesquisa = linha.strip().split(",")
            contagemAlimentos[pesquisa[ALIMENTO]] = contagemAlimentos.get(pesquisa[ALIMENTO], 0) + 1
        print(contagemAlimentos)
        alimento_preferido = max(contagemAlimentos, key=contagemAlimentos.get)
        print(alimento_preferido)

except FileNotFoundError as erro:
    print(f"Erro: {erro}")
except Exception as e:
    print(f"Ocorreu um erro no arquivo ips.txt: ({e})")