class Pizza:
    def __init__(self, nome: str, tamanho: str):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = 0.0
    
    def calcular_preco(self):
        tamanho_preco = {
            'P': 10,
            'M': 20,
            'G': 30
        }
        self.preco = tamanho_preco.get(self.tamanho)
    
    def detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Preco: {self.preco}')
        
# pizza = Pizza('Calabresa', 'M')

# pizza.calcular_preco()

# pizza.detalhes()
    