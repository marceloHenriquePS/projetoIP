
from Controlador import *
from Menus import *


def main():
    while True:
        opcaoMenu = menu()

        if opcaoMenu == 1:
            cadastroMembro()

        elif opcaoMenu == 2:
            menuLivros()
            op_livros = int(input("Opção: "))
            
            if op_livros == 1:
                adicionarLivro()
            
            elif op_livros == 2:
                deletarLivro()
            
            elif op_livros == 3:
                pesquisarLivro()

            elif op_livros == 4:
                break

            else:
                print("Opção inválida!")
            
        elif opcaoMenu == 3:
            menuComentarios()
            op_comentarios = int(input("Opção: "))
            
            if op_comentarios == 1:
                comentarLivro()
            
            elif op_comentarios == 2:
                listarComentarios()

            elif op_comentarios == 3:
                break

            else:
                print("Opção inválida!")

        elif opcaoMenu == 4:
            print("Volte sempre!")
            break
        
        else:
            print("Opção inválida!")

main()
