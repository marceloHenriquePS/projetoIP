def menu():
    # Título
    print('=' * 60)
    print("Clube do livro!".center(55))
    print('=' * 60)
    print('')
    print("Opções:")
    print("[1] - Cadastro de membro")
    print("[2] - Menu Livros")
    print("[3] - Menu Comentários")
    print("[4] - Sair")
    opcao = int(input("Opção: "))
    return opcao

def menuLivros():
    print("\nOpções:")
    print("[1] - Adicionar livro")
    print("[2] - Deletar livro")
    print("[3] - Pesquisar livro por código")
    print("[4] - Sair")

def menuComentarios():
    print("\nOpções:")
    print("[1] - Fazer Comentário")
    print("[2] - Listar Comentário(s)")
    print("[3] - Sair")



