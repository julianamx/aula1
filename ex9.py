#LISTAS

#ARMAZENAR MAIS DE UMA INFORMAÇÃO EM VARIAVEIS
#MANTER A SEQUENCIA DOS DADOS EM UMA VARIAVEL

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'
                          #itens
cidades = ['Rio de Janeiro','São Paulo','Salvador']
#               0               1           2
#cidades.append('Santa Catarina')
#cidades.remove('Salvador')
#cidades.insert(2,'Manaus')
#cidades.pop(0)
#cidades.sort()

print(cidades)

numeros = [2,3,4,5]
letras = ['a','b','c','d']

#final = numeros + letras
numeros.extend(letras)

print(numeros)

itens = [['item1','item2'],['item3','item4']]
print(itens[0][1])