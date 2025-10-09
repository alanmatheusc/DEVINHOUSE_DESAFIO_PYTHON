"""
Criar um sistema simples de cadastro de alunos que permita:
Adicionar alunos com suas respectivas notas;
Calcular a média de cada aluno;
Exibir os alunos aprovados e reprovados com base na média.
Requisitos
  Listas para armazenar as notas dos alunos;
  Dicionários para associar cada aluno às suas notas;
  Laços de repetição para permitir múltiplos cadastros;
  Condicionais para verificar aprovação (média ≥ 7.

Instruções
  O programa deve perguntar quantos alunos serão cadastrados.
  Para cada aluno:
    Solicite o nome.
    Solicite 3 notas (valores entre 0 e 10).
    Armazene os dados em um dicionário no formato:
      {
        "João": [8.0, 7.5, 9.0],
        "Maria": [6.0, 5.5, 7.0]
      }
Após o cadastro, calcule a média de cada aluno.
Exibe uma lista com os alunos aprovados e reprovados, indicando suas médias.
Exemplo:
  Alunos cadastrados com sucesso!
  Aprovados:
  João: média 8.17
  Reprovados:
  Maria: média 6.17
"""
alunos = []

print("----------------------------------------------------------")
print("\n Bem vindo ao cadastro de Alunos!\n")
print("----------------------------------------------------------")

try:
  quantidade_alunos_para_cadastro = int(input("\nDigite a quantidade de alunos que você deseja cadastrar: "))
  print("----------------------------------------------------------")

  for i in range(quantidade_alunos_para_cadastro):
      nome = input("Digite o nome do aluno: ")
      notas = []
      calcula_media = lambda x: sum(x) / len(x)
      is_aluno_aprovado = lambda x: True if x >= 7 else False
      media_aluno = 0

      for j in range(3):
        notas_aluno = float(input(f"Digite a {j+1} nota do  {nome}: "))
        if notas_aluno < 0 or notas_aluno == "":
          print("Nota inválida")
          notas_aluno = float(input(f"Digite a {j+1} nota do  {nome}: "))
        else:
          notas.append(notas_aluno)
      
      media_aluno = round(calcula_media(notas),2)
      
      alunos.append({"nome":nome, "notas":notas, "media":media_aluno, "aprovado":is_aluno_aprovado(media_aluno)})

      print("----------------------------------------------------------")
      
      print(f"Aprovados: \n {nome}: média {media_aluno}") if is_aluno_aprovado(media_aluno) else print(f"Reprovados: \n {nome}: média {media_aluno}")

      print("----------------------------------------------------------")
except ValueError:
  print("Valor inválido")
print(alunos)
print("----------------------------------------------------------")