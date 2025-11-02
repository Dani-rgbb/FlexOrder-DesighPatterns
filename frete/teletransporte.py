from .estrategia import EstrategiaFrete

class FreteTeletransporte(EstrategiaFrete):
    def calcular(self, valor_base):
        print("Frete Teletransporte: R$50.00")
        return 50.00