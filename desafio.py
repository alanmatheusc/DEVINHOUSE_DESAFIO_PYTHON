# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1TOdNiyz0nNFVE2Kf55B0xNWCl_JawpGa
"""

#Desafio da Aula

tabela_descontos = {"menor18":0.1, "maior18Emenor25":0.15,"maior60":0.2}

def isEstudante(input):
  if(input.lower() ==  "sim"):
    return True
  return False

def isPix(formaDePagamento):
  if(formaDePagamento.lower() == "pix"):
    return True
  return False

def aplicarDescontoPorIdade(valor_da_compra, idade):
  tabelaDesconto = 0
  desconto = 0
  if(idade < 18):
    tabelaDesconto = tabela_descontos["menor18"]
  elif(idade >= 18 and idade < 25):
    tabelaDesconto = tabela_descontos["maior18Emenor25"]
  elif(idade >= 60):
    tabelaDesconto = tabela_descontos["maior60"]

  desconto = valor_da_compra * tabelaDesconto
  valor_com_desconto = valor_da_compra - desconto
  return valor_com_desconto, tabelaDesconto


def aplicarDesconto(formaDePagamento, valor_da_compra, idade):
  valor_com_desconto_idade, tabelaDesconto = aplicarDescontoPorIdade(valor_da_compra, idade)

  if(isPix(formaDePagamento)):
    desconto_pix = valor_com_desconto_idade * 0.05
    valor_final = valor_com_desconto_idade - desconto_pix
    tabelaDesconto += 0.05
    return valor_final, tabelaDesconto
  return valor_com_desconto_idade, tabelaDesconto


nome_cliente = input("Digite seu Nome: ")
idade = int(input("Digite sua idade: "))
valor_da_compra = float(input("Digite o valor da compra: "))
is_estudante = isEstudante(input("Você é estudante? (Sim ou Não) "))
forma_de_pagamento = input("Digite a forma de pagamento: (cartão/pix) ")


print("------------------------------------------------------------------------")
print(f'Cliente: {nome_cliente}\n')
print(f'Idade: {idade}\n')
print(f'Forma de pagamento: {forma_de_pagamento}\n')
print(f'Valor original da compra: {valor_da_compra}\n')
print(f'Desconto \n')
valor_final, tabelaDesconto = aplicarDesconto(forma_de_pagamento,valor_da_compra, idade)
print(f'Valor da compra com desconto: {valor_final}\n')
print(f'Desconto total: {tabelaDesconto*100}%\n')


if(valor_da_compra > 500):
  print("Parabéns, João! Você ganhou um brinde especial!")