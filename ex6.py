# return calcula e retorna o valor
'''
def cliente1(nome):
    print(f'Olá {nome}')

def cliente2(nome):
    return f'Olá {nome}'

x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)

#criar uma função que soma varios numeros

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado
x = soma(2,3,4,7)
print(x)


#Define a função
def somador (valor1, valor2):
    soma = valor1 * valor2
    return soma

#Chama a função
res = somador (3,4)
print(f'valor e {res}')

#DEclaração da função
def imprime_msg(nomePessoa):
    print(f'O usuario {nomePessoa} escreveu uma mensagem')

#chamando a função 
nome = input('Digite seu nome: ')
imprime_msg(nome)   
'''
#criar um função que armazena numero e strings (dados)
#varios argumentos

def agencia(**carro):
    return carro

print(agencia(marca='gol', cor='branca', motor=1.0))
