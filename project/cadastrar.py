todos_os_gatos = { 'f':[],'m':[] }

def cadastrar(nome,cor,sexo):

  global todos_os_gatos
  novo_gato = (nome,cor)

  if sexo == 'f':
    todos_os_gatos['f'].append(novo_gato)
  elif sexo == 'm':
    todos_os_gatos['m'].append(novo_gato)

  return todos_os_gatos
