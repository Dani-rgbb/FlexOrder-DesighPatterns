class TaxaEmbalagemPresente:
    def __init__(self, pedido):
        self.pedido = pedido

    def calcular_valor(self):
        valor = self.pedido.calcular_valor()
        print("Adicionando R$5.00 de embalagem para presente.")
        return valor + 5.00