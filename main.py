#Vitor Pellegrino Macedo 202402694103#

import sqlite3

class MarcaRoupa:
    def __init__(self, nome, ramo):
        self.nome = nome
        self.ramo = ramo

    def __str__(self):
        return f"Marca: {self.nome}, Ramo: {self.ramo}"

def conectar():
    return sqlite3.connect("marcas.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marcas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ramo TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def inserir_marca():
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
            print("Nome inválido. Digite apenas letras e espaços.")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO marcas (nome, ramo) VALUES (?, ?)", (nome, ramo))
    conn.commit()
    conn.close()
    print("Marca inserida com sucesso!\n")

def exibir_marcas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, ramo FROM marcas")
    marcas = cursor.fetchall()
    conn.close()

    if not marcas:
        print("Nenhuma marca cadastrada.\n")
    else:
        print("\nLista de marcas:")
        for i, (id_, nome, ramo) in enumerate(marcas, start=1):
            print(f"{i}) Marca: {nome}, Ramo: {ramo}")
        print()

def excluir_todas():
    while True:
        confirm = input("Tem certeza que deseja excluir todas as marcas? (s/n): ").strip().lower()
        if confirm in ('s', 'n'):
            break
        else:
            print("Entrada inválida. Digite 's' para sim ou 'n' para não.")

    if confirm == 's':
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM marcas")
        conn.commit()
        conn.close()
        print("Todas as marcas foram excluídas.\n")
    else:
        print("Operação cancelada.\n")

def excluir_por_indice():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, ramo FROM marcas")
    marcas = cursor.fetchall()

    if not marcas:
        print("Nenhuma marca para excluir.\n")
        conn.close()
        return

    for i, (id_, nome, ramo) in enumerate(marcas, start=1):
        print(f"{i}) Marca: {nome}, Ramo: {ramo}")
    
    try:
        indice = int(input("Digite o número (índice) da marca a ser excluída: ").strip())
        if 1 <= indice <= len(marcas):
            id_marca = marcas[indice - 1][0]
            while True:
                confirm = input(f"Tem certeza que deseja excluir a marca {marcas[indice - 1][1]}? (s/n): ").strip().lower()
                if confirm in ('s', 'n'):
                    break
                else:
                    print("Entrada inválida. Digite 's' para sim ou 'n' para não.")
            if confirm == 's':
                cursor.execute("DELETE FROM marcas WHERE id = ?", (id_marca,))
                conn.commit()
                print("Marca excluída com sucesso.\n")
            else:
                print("Operação cancelada.\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")
    conn.close()

def menu():
    criar_tabela()
    while True:
        print("Menu Principal:")
        print("1) Inserir marca")
        print("2) Exibir todas as marcas")
        print("3) Excluir todas as marcas")
        print("4) Excluir marca pelo número")
        print("5) Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_marca()
        elif opcao == '2':
            exibir_marcas()
        elif opcao == '3':
            excluir_todas()
        elif opcao == '4':
            excluir_por_indice()
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
