## Desafio: Sistema de Avaliação de Compras em
uma Loja Online
Uma loja online deseja criar um programa em Python para avaliar os clientes e calcular o valor
final de suas compras. O sistema deve usar tipos de dados, entradas de usuário, operadores
aritméticos, lógicos e relacionais, e estruturas condicionais.
## Regras do Sistema
Entrada de dados obrigatórios:
- Nome do cliente (string)
- Idade (int)
- Valor da compra (float)
- Se é estudante (string: “sim” ou “não”)
- Forma de pagamento (string: “cartão” ou “pix”)
Descontos aplicados de acordo com as regras:
- Menor de 18 anos → 10% de desconto.
- Entre 18 e 25 anos e estudante → 15% de desconto.
- Mais de 60 anos → 20% de desconto.
- Caso contrário → sem desconto.
Promoção especial da loja:
- Se a forma de pagamento for pix, aplicar 5% de desconto adicional sobre o valor já calculado.
Condições adicionais:
- Se o valor final da compra for maior que R$ 500 e o cliente tiver pelo menos 2 condições de
desconto aplicadas, o cliente ganha um brinde especial.
- Caso contrário, mostrar apenas uma mensagem de agradecimento pela compra.
Saída esperada:
- Nome do cliente
- Idade
- Forma de pagamento
- Valor original da compra
- Percentual total de desconto aplicado
- Valor final da compra
- Mensagem sobre o brinde
## Exemplo de execução esperada
Digite seu nome: João
Digite sua idade: 20
Digite o valor da compra: 600
Você é estudante? (sim/não): sim
Forma de pagamento (cartão/pix): pix
Cliente: João
Idade: 20 anos
Forma de pagamento: pix
Valor original da compra: R$ 600.00
Desconto aplicado: 20%
Valor final da compra: R$ 480.00
Parabéns, João! Você ganhou um brinde especial! ■
