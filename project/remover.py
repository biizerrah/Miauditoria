from .cadastrar import todos_os_gatos

def remover(removendo):

    for gatos in todos_os_gatos.values():


        for gato in gatos:
            if removendo == gato[0]:


                gatos.remove(gato)
                print(f"Gatinho '{removendo}' removido(a) com sucesso!")
                return


    print('Gatinho não encontrado')
