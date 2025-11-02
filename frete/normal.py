from .estrategia import EstrategiaFrete

class FreteNormal(EstrategiaFrete):
    def calcular(self, valor_base):
        frete = valor_base * 0.05
        print(f"Frete Normal: R${frete:.2f}")
        return frete