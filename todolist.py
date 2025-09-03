def exibir_menu():
    """"Mostra a lista de opções"""
    print("-" * 50)
    print("Escolha uma opção:\n" \
          "1 - Inserir nova tarefa\n" \
            "2 - Listar tarefas\n" \
            "3 - Editar uma tarefa\n" \
            "4 - Deletar uma tarefa\n" \
            "5 - Sair"
        )
    print("-" * 50)

def adicionar_tarefa(lista_de_tarefas, tarefa):
    """Faz a verificação de espaço vazio na tarefa e adiciona a tarefa à lista"""
    tarefa = tarefa.strip()
    if tarefa:
        lista_de_tarefas.append(tarefa)
        print("-" * 50)
        print("Tarefa adicionada com sucesso")
        print("-" * 50)
    else:
        print("-" * 50)
        print("A tarefa cadastrada não pode estar vazia!")
        print("-" * 50)
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    """Primeiramente faz a verificação se existe tarefas na lista, caso tenha lista as tarefas, caso não mostra uma mensagem de erro"""
    print("\n")
    print("-" * 50)
    n = 1
    if not lista_de_tarefas:
        print("-" * 50)
        print("Nenhuma tarefa cadastrada! Tente novamente")
        print("-" * 50)
    else:
        print(f"{' ' * 15} Lista de Tarefas")
        print("-" * 50)
        for tarefa in lista_de_tarefas:
            print(f"{n} - {tarefa}")
            n += 1
    print("-" * 50)
    return lista_de_tarefas

def editar_tarefa(lista_de_tarefas, tarefa):
    """Verifica se há uma lista existente, verifica se o valor digitado é válido, verifica se a nova tarefa é válida e modifica uma tarefa existente"""
    tarefa -= 1
    if lista_de_tarefas:
        if 0 <= tarefa < len(lista_de_tarefas):
            print("-" * 50)
            print(f"Tarefa atual: {lista_de_tarefas[tarefa]}")
            print("-" * 50)
            nova_tarefa = input("Insira a nova descrição da tarefa: ").strip()
            if nova_tarefa:
                lista_de_tarefas[tarefa] = nova_tarefa
            else:
                print("-" * 50)
                print("A nova tarefa inserida não pode ser vazia!")
                print("-" * 50)
        else:
            print("-" * 50)
            print("Número de tarefa inválido")
            print("-" * 50)
    else:
        print("-" * 50)
        print("Não há nada na lista para deletar")
        print("-" * 50)
    return lista_de_tarefas

def deletar_tarefa(lista_de_tarefas, tarefa):
    """Verifica se há uma lista existente e deleta uma tarefa da lista"""
    tarefa -= 1
    if not lista_de_tarefas:
        print("-" * 50)
        print("Não existe nada para deletar! Tente novamente")
        print("-" * 50)
    else:
        lista_de_tarefas.pop(tarefa)
    return lista_de_tarefas

# Inicialização de variáveis
lista_de_tarefas = []
continuar = True

# Cabeçalho do programa
print("-" * 50)
print("Seja bem-vinde à sua lista de tarefas!")
print("-" * 50)

# Loop principal
while continuar == True:
    exibir_menu()
    print("-" * 50)
    opcao = input("Insira o que deseja fazer: ")
    print("-" * 50)

    if opcao == "1":
        print("-" * 50)
        tarefa = input("Insira uma nova tarefa: ")
        print("-" * 50)
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        # Verifica se o valor é numérico
        print("-" * 50)
        tarefa = input("Insira o número da tarefa que deseja editar: ")
        print("-" * 50)
        if not tarefa.isnumeric():
            print("-" * 50)
            print("Número inválido! Tente novamente")
            print("-" * 50)
        else:
            lista_de_tarefas = editar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == "4":
        # Verifica se o valor é numérico, se é menor que o limite da lista e se é maior do que zero
        print("-" * 50)
        tarefa = input("Insira o número da tarefa que deseja deletar: ")
        print("-" * 50)
        if not tarefa.isnumeric():
            print("-" * 50)
            print("Número inválido! Tente novamente")
            print("-" * 50)
        elif int(tarefa) > len(lista_de_tarefas):
            print("-" * 50)
            print("Número inválido! Tente novamente")
            print("-" * 50)
        elif int(tarefa) <= 0:
            print("-" * 50)
            print("Número inválido! Tente novamente")
            print("-" * 50)
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == "5":
        continuar = False
    else:
        print("-" * 50)
        print("Opção Inválida! Tente novamente")
        print("-" * 50)
    print("\n")