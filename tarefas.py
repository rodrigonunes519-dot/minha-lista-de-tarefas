tarefas = []

while True:
    print("\n=== MINHA LISTA DE TAREFAS ===")
    print("1 - Adiconar tarefa")
    print("2 - Ver tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")

    opcao = input("escolha: ")

    if opcao == "1":
        nova = input("Digite a tarefa: ")
        tarefas.append(nova)
        print(f"✅ '{nova}' adicionada com sucesso!")
    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa ainda!")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1}. {t}")

    elif opcao == "3":
        for i, t in enumerate(tarefas):
            print(f"{i+1}. {t}")
        num = int(input("Qual número concluiu? ")) - 1
        if 0 <= num < len(tarefas):
            print(f"✔️ Concluida: {tarefas.pop(num)}")
    elif opcao == "4":
        break
    