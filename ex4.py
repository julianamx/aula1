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

#10
frutas = ['maça', 'banana', 'manga', 'uva']

for fruta in frutas:
    print(frutas)
    print(f'eu gosto de {fruta}')


#11
for num in range(10):
    print(num + 1)

#12
frutas = ['maça', 'banana', 'manga', 'uva']
vegetais = ['brocolis', 'cenoura','couve','alface']

for fruta in vegetais:
    
    print(frutas + vegetais)

#13
for num in range(1,11):  
    print(num)

#14
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

#15
lista = ['maçã', 'banana', 'morango','pera']
for frutas in range(1):
       print(frutas)
       if frutas == ('maçã'):
           continue
           print('frutas')

#16 
 
n= int (input('digite um numero'))
if n > 10:
    print('O numero é maior que 10')
else:
    print('O numero é igual ou menor que 10')

#17

a = input('Digite a sua idade: ') 
idade = int(a)
if idade  < 13 :
    print('Criança')
else:
    if idade >13 and idade <19:
        print('Adolescente')
    else:
        if idade >=20:
         print('Adulto')

#18
dados = ['BMW X6', 'BMW 15','BMW 18']
modelo = input('Qual modelo deseja comprar? ')

if modelo not in dados:
   print('modelo indisponivel')
else:
   print('disponivel')

#24
i = int(input('digite um numero: '))
retorno = i** 2
print(retorno)
'''
#25
def sum(num1, num2):
    return num1 + num2

print("\tSoma de dois números\n")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print ("")
print ("O resultado da soma é %d" %sum(num1, num2))

#26
def pontencia(base, expoente =2):
    return base ** expoente
user_number = int(input('Digite o numero base: '))
user_expoente = int(input('Digite um expoente(default2): '))

if user_expoente:
    print(f'O resultado é:{pontencia(user_number,int(user_expoente))}')
else:
    print(f'O resultado é:{pontencia(user_number)}')



    




  






       





