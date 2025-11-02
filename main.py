import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pedido.base import PedidoBase
from pedido.desconto_pix import DescontoPix
from pedido.desconto_grande import DescontoPedidoGrande
from pedido.taxa_embalagem import TaxaEmbalagemPresente

from pagamento.pix import PagamentoPix
from pagamento.credito import PagamentoCredito
from frete.normal import FreteNormal
from frete.expresso import FreteExpresso

from checkout.facade import CheckoutFacade

# Cenário 1
itens1 = [{'nome': 'Capa da Invisibilidade', 'valor': 150.0},
          {'nome': 'Poção de Voo', 'valor': 80.0}]
pedido1 = PedidoBase(itens1)
pedido1 = DescontoPix(pedido1)
pagamento1 = PagamentoPix()
frete1 = FreteNormal()
checkout1 = CheckoutFacade(pedido1, pagamento1, frete1)
checkout1.concluir_transacao()

print("\n--- Próximo Pedido ---")

# Cenário 2
itens2 = [{'nome': 'Cristal Mágico', 'valor': 600.0}]
pedido2 = PedidoBase(itens2)
pedido2 = DescontoPedidoGrande(pedido2)
pedido2 = TaxaEmbalagemPresente(pedido2)
pagamento2 = PagamentoCredito()
frete2 = FreteExpresso()
checkout2 = CheckoutFacade(pedido2, pagamento2, frete2)
checkout2.concluir_transacao()