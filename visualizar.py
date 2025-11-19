from cadastrar import todos_os_gatos

def visualizar():
  print('====== ESCOLHA UM NOME NA LISTA ======')
  for gatos in todos_os_gatos.values():
    for gato in gatos:
      print(f'{gato[0]}')

visualizar()