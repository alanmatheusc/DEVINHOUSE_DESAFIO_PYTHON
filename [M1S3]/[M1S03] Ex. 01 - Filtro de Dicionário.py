#Dado um dicionário com produtos e preços, exiba apenas os produtos com preço acima de R$ 100.

produtos = {"item1":110,"item2":115, "item3":40, "item4":50}
produto_acima_de_100 = {k:produtos[k] for k in produtos if produtos.get(k) > 100}


# Se for apenas para exibição em tela da para usar o for, se não a melhor opção é criar uma outra lista
for x in produtos:
  if(produtos.get(x)>100):
    print(f'{x}:{produtos.get(x)}')