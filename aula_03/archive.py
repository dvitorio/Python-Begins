#Modos de arquivo
# r - read (leitura)
# a - append (Incrementa)
# w - write (escrita)
# x - criar arquivo 
# r+ - leitura + escrita


file = open("aula_03/text.txt", "r")

file.readable()

#print(file.readable()) Verifica se o arquivo pode ser lido

#print(file.read()) Lê um arquivo e imprime tudo dentro do mesmo
#print(file.readline()) Lê um arquivo e imprime tudo dentro do mesmo




lista = print(file.readlines())


file.close()

