from models.pizza import Pizza
from models.pizza_especial import PizzaEspecial

lista_pizzas = ['Calabresa', 'Portuguesa', 'Napolitana']
lista_adicionais = ['Muçarela', 'Pimentão', 'Ovo']
adicionais = []
pizzas = []
print('''
      Preços: P - 10, M - 20, G - 30
      1- Calabresa
      2- Portuguesa
      3- Napolitana
      ''')
op = input('Escolha a pizza: ')
tamanho = input('Tamanho [P, M, G]: ')

escolha = input('Deseja algum adicional [S - Sim, N - Não]?  ')
if escolha.upper() == 'S':
    while escolha.upper() == 'S':
        adicional = input('''Informe o adicional: 
                          1- Muçarela
                          2- Pimentão
                          3- Ovo
                          ''')
        lista_adicionais.append(adicional)
        escolha = input('Deseja mais algum adicional [S - Sim, N - Não]?  ')
    pizza = PizzaEspecial(pizzas[op-1], tamanho, lista_adicionais)
    pizza.calcular_preco()
else:
    pizza = Pizza(pizzas[op-1], tamanho)
    pizza.calcular_preco()



