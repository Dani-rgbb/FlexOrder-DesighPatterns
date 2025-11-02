class PedidoBase:
    def __init__(self, itens):
        self.itens = itens

    def calcular_valor(self):
        return sum(item['valor'] for item in self.itens)