repetir = 's'
total = 0
fatura = []

while(repetir == 's'):
     produto = input('Digite o nome do produto: ')
     preco = float(input('Digite o preço do produto: '))
     fatura.append([produto, preco])
     total += preco
     repetir = input('Deseja comprar mais algum produto? (S ou N)').lower()

for venda in fatura:
     print(venda[0], ':', venda[1]) 

print('O total da fatura é de: ', total)