from .estrategia import EstrategiaFrete

class FreteExpresso(EstrategiaFrete):
    def calcular(self, valor_base):
        frete = valor_base * 0.10 + 15.00
        print(f"Frete Expresso: R${frete:.2f}")
        return frete