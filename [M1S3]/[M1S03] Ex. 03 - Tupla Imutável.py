#Crie uma tupla com 5 elementos. Tente alterar um dos elementos e explique o erro que ocorre. Use comentários no código para justificar

tup = (1,2,3,4,5)
tup[5] = 6
# Vai dar um erro, porque a tupla é do tipo imutavel, apartir do momento que a tupla é criada, ela não pode sofrer nenhum tipo de modificação.
# Porém, caso eu tenha um elemento que possa sofrer mutaçÕes como uma lista, dentro da tupla, eu consigo fazer alteração.
# Exemplo:
tup2 = (1,2,3,4,5,[1,2,3])
tup2[5][3] = 4
print(tup2)