from project.cadastrar import cadastrar
from project.gato_detalhes import consultar
from project.listar_todos_os_gatos import listar
from project.remover import remover
from project.listar_nomes import visualizar

print('===================================================')
print('BEM VINDO(A) A MIAUDITORIA - ESCOLHA UMA OPÇÃO')
print('===================================================')
print('[1] - Cadastrar Item')
print('[2] - Listar Itens')
print('[3] - Consultar Item')
print('[4] - Remover Item')
print('[5] - Sair')
print('===================================================')


while True:
    
  opcao = int(input('Opção Desejada >>> '))

  if opcao == 1:

    nome = input('Qual o nome do seu gatinho(a)? ').strip().lower()
    sexo = input('Qual o sexo? [M] - Macho | [F] - Fêmea ').strip().lower()
    cor = input('Qual a cor do gatinho(a)? ').strip().lower()
    cadastrar(nome,cor,sexo)


  elif opcao == 2:
    listar()

  elif opcao == 3:
    visualizar()
    print('========== GATINHO CONSULTADO ==========')

    consulta = input('Digite o nome do gatinho que deseja consultar: ').strip().lower()
    consultar(consulta)

    print('\n=====================================')

  elif opcao == 4:
    visualizar()

    removendo = input('Digite o nome do gatinho que deseja remover da lista: ').strip().lower()
    remover(removendo)

  elif opcao == 5:
    print('>>>>> SAINDO <<<<<')
    break

  else:
    print('==== OPÇÃO INVÁLIDA!! =====')