import json

def arquivo():
 produtos = {}
 soma = {}
 contador = 0
 with open('dados.csv', 'r',encoding='UTF-8') as arq:
  for linha in arq.readlines()[1:]:
    produto,quantidade,valor = linha.strip().split(',')
    if produto not in produtos:
     produtos["produto"] = produto
     produtos["quantidade"] = quantidade
     produtos["valor"] = valor
    with open('total_valor.csv', 'w', encoding='UTF-8') as w:
      for key,value in produtos.items():
        if key == 'valor':
          contador += int(value)
        soma['total'] = contador
      print(soma)
      json.dump(soma,w,indent=4, ensure_ascii=False)
        
arquivo()