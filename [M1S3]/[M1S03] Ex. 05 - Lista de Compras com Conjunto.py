#Crie duas listas de compras: uma do João e outra da Maria. Use conjuntos para exibir: Itens em comum; Itens exclusivos de cada um; Todos os itens sem duplicatas.

joao_compras = {'arroz','farinha','coca-cola','feijao', 'sabonete'}
maria_compras = {'arroz','shampoo','coca-cola','feijao', 'sabao em pó'}

itens_em_comum = joao_compras.intersection(maria_compras)
itens_exclusivos_joao = joao_compras.difference(maria_compras)
itens_exclusivos_maria = maria_compras.difference(joao_compras)
itens_joao_e_maria = joao_compras.union(maria_compras)
