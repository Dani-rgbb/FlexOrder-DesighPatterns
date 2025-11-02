class DescontoPix:
    def __init__(self, pedido):
        self.pedido = pedido

    def calcular_valor(self):
        valor = self.pedido.calcular_valor()
        print("Aplicando 5% de desconto PIX.")
        return valor * 0.95