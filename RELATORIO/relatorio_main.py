from cadastroRelatorio import *


def main():
    while True:
        print("\nMenu:")
        print("[1] - Apresentação")
        print("[2] - Relatório")
        print("[0] - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            apresentacao()
        elif opcao == '2':
            relatorio()
        elif opcao == '0':
            print("Aplicação finalizada. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamar main


main()
