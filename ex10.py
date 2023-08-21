#armazenar mais de uma informação em variaveis
# manter a sequencia dos dados em uma variavel
# O lower()metado retorna uma string onde todos os caracteres são minusculos.
#simbolos e numeros são ignorados.
'''
cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo','verde','azul','vermelho']
if cor_cliente.lower() in cores:
    print('sim')
else:
    print('Não temos esta cor em estoque')

#junta listas
 
cores =['amarelo', 'verde', 'azul', 'vermelho', 'roxo']
valores = [10,20,30,40,50] 
valor =[53.00,56.00]

duas_listas = zip(cores, valores, valor)
print(list(duas_listas))  

#crie uma lista de frutas a partir do input fornecidopo virgulas:

frutas_usuario = input('digite o nomes das frutas separados por vigula :')

frutas_lista = frutas_usuario.split(' , ')

print(frutas_lista)
'''
#Tuples
cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuples = ('amarelo', 'verde', 'azul', 'vermelho')

cores_list.append('roxo')

#print(type(cores_list))
#print(type(cores_tuples))

# duas_listas = cores_list *2
print(cores_list)