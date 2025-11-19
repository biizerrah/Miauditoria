from cadastrar import todos_os_gatos

def listar():

  total = len(todos_os_gatos['f']) + len(todos_os_gatos['m'])

  if total == 0:
    print('Não há gatos cadastrados!! ')

  else:

    for sexo,lista in todos_os_gatos.items():

      if sexo == 'f':
        print(">>>>>>>>>>>> FÊMEAS <<<<<<<<<<<<")

        for nome,cor in lista:
          print(f'Nome: {nome} | Cor: {cor}')

      elif sexo == 'm':
        print(">>>>>>>>>>>> MACHOS <<<<<<<<<<<<")

        for nome,cor in lista:
          print(f'Nome: {nome} | Cor: {cor}')
