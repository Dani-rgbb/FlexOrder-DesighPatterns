class DescontoPedidoGrande:
    def __init__(self, pedido):
        self.pedido = pedido

    def calcular_valor(self):
        valor = self.pedido.calcular_valor()
        if valor > 500:
            print("Aplicando 10% de desconto para pedidos grandes.")
            return valor * 0.90
        return valor