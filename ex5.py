#functions(funções)
'''
print('ola Marcos')
print('temos 5 laptops em estoque')

def boas_vindas():
    print('Ola Marcos')
    print('temos 5 laptops em estoque')

boas_vindas()    


def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultados = numero1 + numero2
    print (resultados)

def somar_dois_numeros1():
    numero1 = 10
    numero2 = 2
    resultado = numero1 + numero2
    print(resultado)


somar_dois_numeros()
somar_dois_numeros1()    
'''

# functions (funções) parâmetros e argumentos

def boas_vindas(nome, quantidade):
    print(f'ola {nome}')
    print(f'temos {str(quantidade)} laptops em estoque')

boas_vindas('marcos',5)
boas_vindas('lucia',5)
boas_vindas('pedro',5)  


