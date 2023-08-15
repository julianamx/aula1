# operadores logicos
'''
renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')

# or
renda_acima_5mil = True
nome_limpo = False 

if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado') 


idade_Lucas = 21
idade_Carol = 17

# Operador or

if idade_Lucas >= 18 or idade_Carol >=18:
   print('Pelo menos um dois e maior de idade')
else:
    print('Lucas e Carol não são maiores de idade')  

if idade_Lucas >= 18 and idade_Carol >=18:
   print('Lucas e Carol são maiores de idade')
else:
    print('Pelos menos um dois é maior de idade') 

# Multiplos operadores de comparação

valor = 20

if 20 <= valor < 40:


#if valor >= 20 and valor < 40:
   print('produto foi aceito')
else:
    print('produto não aceito')    

    
# for numeros

# imprimir de 1 a 5

for numero in range(1,20, 2):
    print(numero)

lojas = ['rio', 'sampa', 'belo', 'curitiba'] 

for loja in lojas:
    print(lojas)
print('acabou for') 

for i in range(4):
    print(i) 
    print(lojas[i])

# for para strings

for letra in 'google':
    print(letra) 

palavra = 'google'

for  letra in palavra:
    print(letra + ' esta dentro da palavra google')    
'''

frutas = ['maça', 'banana', 'manga', 'uva']

for fruta in frutas:
    print(frutas)
    print(f'eu gosto de {fruta}')



for num in range(10):
    print(num + 1)


frutas = ['maça', 'banana', 'manga', 'uva']
vegetais = ['brocolis', 'cenoura','couve','alface']

for fruta in vegetais:
    print(frutas)
    print(vegetais)
    print(f'{frutas}'+ (f'{vegetais}'))


for num in range(1,11):  
    print(num)

print('Loop com break:')
for numero in range(1,11):
    if numero > 5:
        break 
    print(numero)
print('\nloop com o continue:')
for numero in range(1,11):
    if numero == 5:
        continue
    print(numero)    




