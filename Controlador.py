#---------- Usuários ----------#
lista_usuarios = []
num_usuario = 0

#--------- Cadastro de Usuários --------#
def cadatrar_usuario():
    global num_usuario 

    print("\n===== Cadastrar Usuários =====")
    nome = input("Nome: ")
    cpf = int(input("CPF: "))
    contato = input("Contato: ")

    num_usuario += 1

    for usuario in lista_usuarios:
        if usuario["CPF"] == cpf:
            print("CPF já cadastrado.")
            return

    usuario = {"Nome":nome, "CPF":cpf, "Contato":contato, "Número":num_usuario}
    lista_usuarios.append(usuario)

    print(f"Usuário '{nome}' foi adicionado ao sistema.")

#--------- Listar Usuários ----------#
def listar_usuarios():
    print("===== Lista de Usuários Cadastrados =====\n")
    print("Total de Usuários Cadastrados: {}\n".format(len(lista_usuarios)))

    if len(lista_usuarios) == 0:
        print("Não há usuários cadastrados no sistema!")
    else:
        for usuario in lista_usuarios:
            print("Usuário {}: {}".format(usuario["Número"], usuario["Nome"]))

#---------- Buscar Usuários ---------#
def buscar_usuario():
    print("===== Buscando Usuário... =====")

    if len(lista_usuarios) == 0:
        print("Não há usuários cadastrados no sistema.")
    
    else:
        cpf = int(input("Informe o CPF do Usuário: "))

        for usuario in lista_usuarios:

            if usuario["CPF"] == cpf:
                print("\nUsuário: {}\nCPF: {}\nEmpréstimos:".format(usuario["Nome"], usuario["CPF"]))
                return True
                
        print("\nEste usuário não está cadastrado.")
        return False
    
#---------- LIVROS -------------#
lista_livros = []
num_livros = 0

#-------- CADASTRO DE LIVROS -----------#
def cadatrar_livros():
    global num_livros

    print("\n===== Cadastro de Livros =====")
    nome = input("Nome: ")
    isbn = int(input("ISBN: "))
    situacao = True

    num_livros += 1

    for livro in lista_livros:
        if livro["ISBN"] == isbn:
            print("Livro já cadastrado.")
            return

    livro = {"Nome":nome, "ISBN":isbn,  "Situação":situacao, "Número":num_livros}
    lista_livros.append(livro)

    print(f"O livro '{nome}' foi adicionado ao sistema.")

#--------- Listar Livros ----------#
def listar_livros():
    print("===== Lista de Livros Cadastrados =====\n")
    print("Total de Livros Cadastrados: {}\n".format(len(lista_livros)))

    if len(lista_livros) == 0:
        print("Não há livros cadastrados no sistema!")
    else:
        for livro in lista_livros:
            print("Livro {}: {}".format(livro["Número"], livro["Nome"]))

#---------- Buscar Livros ---------#
def buscar_livro():
    print("===== Buscando Livros... =====")

    if len(lista_livros) == 0:
        print("Não há livros cadastrados no sistema.")
    
    else:
        isbn = int(input("Informe o ISBN do Livro: "))

        for livros in lista_livros:

            if livros["ISBN"] == isbn:
                print("Livro: {}\nISBN: {}\nSituação: {}".format(livros["Nome"], livros["ISBN"], livros["Situação"]))
                return True
                    
        print("\nEste livro não está cadastrado.")
        return False
    
#--------- Empréstimo de Livros ---------#
lista_emprestimos = []
num_emprestimo = 0

#------------- Realizando Empréstimos -------------#
def emprestimo_livro():
    global num_emprestimo

    if len(lista_livros) == 0:
        print("\nNão a livros cadastrados no sistema.")
    
    else:
        print(("\nInforme o CPF do usuário ao qual o livro será emprestado: "))
        cpf = int(input("---> "))

        for usuario in lista_usuarios:

            if usuario["CPF"] == cpf:
                print("\nUsuário {}: {}\nCPF: {}".format(usuario["Número"], usuario["Nome"], usuario["CPF"]))

                print(("\nInforme o ISBN do Livro que será emprestado: "))            
                isbn = int(input("---> "))


                for livro in lista_livros:
                    if livro["ISBN"] == isbn:

                        if livro["Situação"] == True:
                            print("\nLivro {}: {}\nISBN: {}".format(livro["Número"], livro["Nome"], livro["ISBN"]))

                            print("\nO Empréstimo foi realizado com sucesso.")
                            
                            livro["Situação"] = False

                            num_emprestimo += 1

                            emprestimo = {"Nome Usuário":usuario["Nome"], "CPF":usuario["CPF"], "Número Usuário":usuario["Número"], 
                                          "Nome Livro":livro["Nome"], "ISBN":livro["ISBN"], "Número Livro":livro["Número"], 
                                          "Número Empréstimo":num_emprestimo}
    
                            lista_emprestimos.append(emprestimo)

                            return True

                        print("Livro não pode ser emprestado no momento")
                        return False
       
                print("ISBN não encontra-se cadastrado no sistema.")
                return False
        
        print("CPF não encontra-se cadastrado no sitema.")
        return False

#------------- Listando Empréstimos ---------------#
def listar_emprestimos():
    print("===== Lista de Empréstimos Ativos =====\n")
    print("Total de Empréstimos Ativos: {}\n".format(len(lista_emprestimos)))

    if len(lista_emprestimos) == 0:
        print("Não há empréstimos realizados no sistema!")
    else:
        for emprestimo in lista_emprestimos:
            print("Empréstimo {}:".format(emprestimo["Número Empréstimo"]))

            print("========== EMPRÉSTIMO {} ==========")
            print("Usuário {}: {}".format(emprestimo["Número Usuário"], emprestimo["Nome Usuário"]))
            print("CPF: {}".format(emprestimo["CPF"]))

            print("========== INFORMAÇÕES DO LIVRO ==========")
            print("Livro {}: {}".format(emprestimo["Número Livro"], emprestimo["Nome Livro"]))
            print("ISBN: {}\n".format(emprestimo["ISBN"]))

#--------- Devolução de Livros -------------------#
lista_devolucoes = []
num_devolucao = 1

#------------ Realizando Devoluções --------------#
def devolucao_livro():
    global num_devolucao

    lista_devolucoes = []

    print(("\nInforme o CPF do usuário ao qual o livro será feita a devolução: "))
    cpf = int(input("---> "))

    for emprestimo in lista_emprestimos:

        if emprestimo["CPF"] == cpf:
            print("\nUsuário {}: {}\nCPF: {}".format(emprestimo["Número Usuário"], emprestimo["Nome Usuário"], emprestimo["CPF"]))

            print(("\nInforme o ISBN do Livro que será emprestado: "))            
            isbn = int(input("---> "))
                    
            if emprestimo["ISBN"] == isbn:

                    print("\nLivro {}: {}\nISBN: {}".format(emprestimo["Número Livro"], emprestimo["Nome Livro"], emprestimo["ISBN"]))

                    from datetime import date
                    data = date.today()
                    
                    print("===== Data da devolução =====\nData: {}".format(data))

                    print("\nA devolução foi realizado com sucesso.")

                    for livro in lista_livros:
                        livro["Situação"] = True

                    devolucao = {
                        "Nome Usuário":emprestimo["Nome Usuário"],
                        "CPF":emprestimo["CPF"],
                        "Nome Livro":emprestimo["Nome Livro"], 
                        "ISBN":emprestimo["ISBN"],
                        "Data":data,
                        }

                    lista_devolucoes.append(devolucao)

                    print(lista_devolucoes)

                    with open("Lista de Devoluções.txt", "a", encoding="utf-8") as arquivo:
                        for devolucao in lista_devolucoes:
                            arquivo.write("=" * 10) 
                            arquivo.write("Devolução {}".format(num_devolucao)) 
                            arquivo.write("=" * 10)
                            arquivo.write("\n")

                            for valor1, valor2 in devolucao.items():
                                arquivo.write("{}: {}".format(valor1, valor2))
                                arquivo.write("\n")
                            arquivo.write("=" * 32)
                            arquivo.write("\n")

                    
                    num_devolucao += 1
                    lista_emprestimos.remove(emprestimo)

                    return True
     
            print("Livro não pode ser devolvido no momento, pois, encontra-se disponível.")
            return False
        
    print("Não há empréstimos realizados neste CPF.")
    return False

#------------ Listando Devoluções -------------#
def listar_devolucoes():
    print("\n===Lista de Devoluções===")
    with open("Lista de Devoluções.txt", "r", encoding="utf-8") as arquivo:
        leitura = arquivo.read()

        print(leitura)