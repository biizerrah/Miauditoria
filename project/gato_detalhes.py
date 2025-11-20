from .cadastrar import todos_os_gatos

def consultar(consulta):
    for chave, gatos in todos_os_gatos.items():
        for gato in gatos:
            if consulta == gato[0]:
                sexo = 'Fêmea' if chave == 'f' else 'Macho'
                print(f'Nome: {gato[0]} | Cor: {gato[1]} | Sexo: {sexo}')
                return

    print('Gatinho não encontrado!! ')

