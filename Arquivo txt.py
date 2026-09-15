# Muitas vezes precisamos acessar o conteúdo de um arquivo no file system
# Alguns tipos de arquivo, o Python lê naturalmente. Outros ele precisa de uma
# biblioteca especializada.
# O arquivo texto é NATURAL do Python.

print("Arquivo de Texto")
# Para acessar um arquivo precisamos informar ao Sistema Operacional que vamos
# manipular o arquivo. Isso é feito através do OPEN / CLOSE

# 'r' serve para ler
# 'w' serve para escrever
# 'a' serve para adicionar AO arquivo

arqAlunos = open('alunos.txt', 'r')
# Com o path completo:
# arqAlunos = open('D:\\1ESPI python\\PythonProject\\alunos.txt', 'r')

print("\nLendo e imprimindo o arquivo linha por linha:")
print(arqAlunos.readline())
print(arqAlunos.readline(), end='')    # end='' não deixa pular linha a mais
print(arqAlunos.readline(), end='')

#O texto lido do arquivo é um elemento iterável: UTILIZAÇÃO DE FOR
for linha in arqAlunos:
    print(linha, end='')

# Ao chegar ao fim do arquivo, ele não lê e nem imprime mais nada
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')

# Se eu quiser voltar e ler o arquivo desde o início, tenho que voltar o cursor para o início.
print("\nVoltando para o início do arquivo:")
arqAlunos.seek(0)
print(arqAlunos.readline(), end='')

print("\nLendo como uma lista de linhas:")
listaLinhas = arqAlunos.readlines()
print(listaLinhas)

# Desafio: Usando list comprehension, tirar o '\n' dos elementos da lista

def retirar(listaLinhas: list) -> list:
    return [linha.replace("\n", "") for linha in listaLinhas]
print(retirar(listaLinhas))


print("\nVoltando para uma posição qualquer do arquivo:")
arqAlunos.seek(12)
print(arqAlunos.readline(), end='')


print("\nLendo o arquivo inteiro:")  # Muito cuidado
print(arqAlunos.read())

print("\nFechando o arquivo:")
arqAlunos.close()

print("\nEscrevendo um arquivo:")
arqOlaMundo = open('arquivoOlaMundo.txt', 'w')
arqOlaMundo.write('Ola Mundo!')
arqOlaMundo.close()

# O modo 'w' sobrescreve o arquivo
arqOlaMundo = open('arquivoOlaMundo.txt', 'w')
arqOlaMundo.write('Bom dia Mundo!')
# Ele gruda as linhas! É necessário um '\n'
arqOlaMundo.write('\nO dia esta maravilhoso')
arqOlaMundo.close()

floricultura = ['rosa', 'gardenia', 'artemisia']
floricultura = [flor + '\n' for flor in floricultura ]
arqFloricultura = open('arquivoFloricultura.txt', 'w')
arqFloricultura.writelines(floricultura)
arqFloricultura.close()