from Menu import *
from Controlador import *

def main():
    while True:
        menu_principal()
        op = int(input("---> "))

#---------- Menu De Usuários -------#
        if op == 1:
            menu_usuarios()
            op_usuario = int(input("---> "))

            if op_usuario == 1:
                cadatrar_usuario()

            elif op_usuario == 2:
                listar_usuarios()
            
            elif op_usuario == 3:
                buscar_usuario()
            
            elif op_usuario == 4:
                pass

            elif op_usuario == 0:
                break
            
            else:
                print("Opção Inválida.")

#--------- Menu De Livros ---------#       
        elif op == 2:
            menu_livros()
            op_livros = int(input("---> "))

            if op_livros == 1:
                cadatrar_livros()
            
            elif op_livros == 2:
                buscar_livro()

            elif op_livros == 3:
                listar_livros()

            elif op_livros == 4:
                menu_emprestimo()

                op_emprestimo = int(input("---> "))

                if op_emprestimo == 1:
                    emprestimo_livro()
                
                elif op_emprestimo == 2:
                    listar_emprestimos()

                elif op_emprestimo == 0:
                    continue

                else:
                    print("Opção inválida.")
                    break

            elif op_livros == 5:
                menu_devolucao()

                op_devolucao = int(input("---> "))

                if op_devolucao == 1:
                    devolucao_livro()
                
                elif op_devolucao == 2:
                    listar_devolucoes()

                elif op_devolucao == 0:
                    continue

                else:
                    print("Opção inválida.")
                    break

            elif op_livros == 0:
                break

            else:
                print("Opção Inválida.")

        elif op == 0:
            break

        else:
            print("Opção Inválida.")
            continue

main()