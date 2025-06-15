class MarcaRoupa:
    def __init__(self, nome, ramo):
        self.nome = nome
        self.ramo = ramo

    def __str__(self):
        return f"Marca: {self.nome}, Ramo: {self.ramo}"


def inserir_marca(lista_marcas):
    while True:
        nome = input("Digite o nome da marca: ").strip()
        if nome.replace(" ", "").isalpha():
            break
        else:
            print("Nome inválido. Digite apenas letras e espaços.")
    while True:
        ramo = input("Digite o ramo da marca: ").strip()
        if ramo.replace(" ", "").isalpha():
            break
        else:
            print("Nome inválido. Digite apenas letras e espaços")
    marca = MarcaRoupa(nome, ramo)
    lista_marcas.append(marca)
    print("Marca inserida com sucesso!\n")


def exibir_marcas(lista_marcas):
    if not lista_marcas:
        print("Nenhuma marca cadastrada.\n")
    else:
        print("\nLista de marcas:")
        for i, marca in enumerate(lista_marcas, start=1 ):
            print(f"{i}) {marca}")
        print()

def excluir_todas(lista_marcas):
    while True:
        confirm = input("Tem certeza que deseja excluir todas as marcas? (s/n): ").strip().lower()
        if confirm in ('s', 'n'):
            break
        else:
            print("Entrada inválida. Digite 's' para sim ou 'n' para não.")

    if confirm == 's':
        lista_marcas.clear()
        print("Todas as marcas foram excluídas.\n")
    else:
        print("Operação cancelada.\n")
1

def excluir_por_indice(lista_marcas):
    if not lista_marcas:
        print("Nenhuma marca para excluir.\n")
        return
    try:
        indice = int(input("Digite o número (índice) da marca a ser excluída: ").strip())
        if 1 <= indice < len(lista_marcas):
            while True:
                confirm = input(f"Tem certeza que deseja excluir a marca {lista_marcas[indice]}? (s/n): ").strip().lower()
                if confirm in ('s', 'n'):
                    break
                else:
                    print("Entrada inválida. Digite 's' para sim ou 'n' para não.")
            if confirm == 's':
                del lista_marcas[indice]
                print("Marca excluída com sucesso.\n")
            else:
                print("Operação cancelada.\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")


def menu():
    lista_marcas = []
    while True:
        print("Menu Principal:")
        print("1) Inserir marca")
        print("2) Exibir todas as marcas")
        print("3) Excluir todas as marcas")
        print("4) Excluir marca pelo número")
        print("5) Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_marca(lista_marcas) 
        elif opcao == '2':
            exibir_marcas(lista_marcas)
        elif opcao == '3':
            excluir_todas(lista_marcas)
        elif opcao == '4':
            excluir_por_indice(lista_marcas)
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()
