class CheckoutFacade:
    def __init__(self, pedido, estrategia_pagamento, estrategia_frete):
        self.pedido = pedido
        self.estrategia_pagamento = estrategia_pagamento
        self.estrategia_frete = estrategia_frete

    def concluir_transacao(self):
        print("=========================================")
        print("INICIANDO CHECKOUT REFORMADO...")

        valor_base = self.pedido.calcular_valor()
        frete = self.estrategia_frete.calcular(valor_base)
        total = valor_base + frete

        print(f"\nValor a Pagar: R${total:.2f}")
        sucesso = self.estrategia_pagamento.pagar(total)

        if sucesso:
            print("\nSUCESSO: Pedido finalizado e registrado no estoque.")
            print("Emitindo nota fiscal...")
        else:
            print("\nFALHA: Transação abortada.")