#Receba duas listas: uma com nomes e outra com idades. Converta para um dicionário onde cada nome é uma chave e a idade é o valor correspondente.

nomes = ["alan","marianna","pedro"]
idades = [22,19,25]

dic = {nomes:idades for nomes,idades in zip(nomes,idades)}