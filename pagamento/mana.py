from .estrategia import EstrategiaPagamento

class PagamentoMana(EstrategiaPagamento):
    def pagar(self, valor):
        print(f"[Mana] Transferência de R${valor:.2f} iniciada...")
        print("   -> Aprovado após 10 segundos.")
        return True