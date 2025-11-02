# FlexOrder-DesighPatterns
Refatoração de Sistema Legado com Padrões de Projeto

# 🛒 E-Commerce Mágico (Refatorado)

Este projeto refatora um sistema monolítico de pedidos para um design modular e extensível.

## ✨ Padrões Aplicados

- **Strategy**: Pagamento e frete desacoplados e intercambiáveis.
- **Decorator**: Descontos e taxas aplicados dinamicamente.
- **Facade**: Checkout simplificado e orquestrado.

## 📦 Estrutura

- `pedido/`: lógica de valor, descontos e taxas.
- `pagamento/`: estratégias de pagamento (Pix, Crédito, Mana).
- `frete/`: estratégias de frete (Normal, Expresso, Teletransporte).
- `checkout/`: fachada que orquestra o processo de compra.
- `main.py`: cenários de uso e testes.

## 🚀 Como Executar

```bash
python main.py