from .estrategia import EstrategiaPagamento

class PagamentoCredito(EstrategiaPagamento):
    def pagar(self, valor):
        print(f"[Crédito] Processando R${valor:.2f}...")
        if valor < 1000:
            print("   -> Aprovado.")
            return True
        print("   -> Rejeitado (limite excedido).")
        return False