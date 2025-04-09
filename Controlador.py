from FuncoesJSON import *

def cadastroMembro():
    carregarMEMBROS()

    membro = {'Nome': str(input("Informe seu nome completo: "))}

    contatos = []
    for i in range(1, 3):

        nomeContato = str(input(f"Nome do contato {i}: "))
        fone = int(input(f"Telefone {i}: "))
        
        contato = {'nomeContato':nomeContato, 'fone':fone}
        contatos.append(contato)

    membro['Contatos'] = contatos
    
    dadosMEMBROS['Membros'].append(membro)

    print("\nMembro adicionado com sucesso, Bem vindo ao clube!")

    gravarDadosMEMBROS()     

def adicionarLivro():
    carregarLIVROS()

    livro = {'Nome do Livro': str(input("Informe o livro que você está lendo no momento: "))}

    while True:
        livro['Código'] = int(input("Informe o código do livro de 0 a 50: "))
        
        if livro['Código'] > 50 or livro['Código'] < 0:
            print("Este código não existe, informe outro.")
            
        elif "Livros" in dadosLIVROS:           
            for i in dadosLIVROS['Livros']:

                if "Código" in i and i['Código'] == livro['Código']:
                    print("Código já cadastrado.")
                    break
            else:
                break

    livro['Gênero'] = str(input("Informe o gênero do livro: "))
    livro['Autor'] = str(input("Informe o autor do livro: "))

    dadosLIVROS['Livros'].append(livro)
    
    print("Livro adicionado com sucesso. Boa Leitura!")

    gravarDadosLIVROS()

def deletarLivro():
    carregarLIVROS()

    livroPesquisa = int(input("Digite o código do livro que deseja deletar: "))

    if len(dadosLIVROS["Livros"]) > 0:

        if "Livros" in dadosLIVROS:

            for livro in dadosLIVROS['Livros']:

                if "Código" in livro and livro['Código'] == livroPesquisa:
                    dadosLIVROS["Livros"].remove(livro)

                    print(f"Livro com código {livroPesquisa} removido com sucesso.")
                    return True
                
            print(f"Livro com código {livroPesquisa} não encontrado.")
            return False
    
    print("Base de dados vazia!")   
    return False

    
    gravarDadosLIVROS()

def comentarLivro():
    carregarLIVROS()

    while True:
        livroComentario = int(input("Digite o código do livro que deseja comentar: "))

        if len(dadosLIVROS["Livros"]) > 0:
            if "Livros" in dadosLIVROS:
            
                for livro in dadosLIVROS['Livros']:

                    if "Código" in livro and livro['Código'] == livroComentario:
                        if "Comentário" in livro:
        
                            comentario = input("Escreva o comentário: ")
                            print("Comentário adicionado com sucesso!")

                            livro['Comentário'].append(comentario)                        
                        
                        else:
                            livro["Comentário"] = [input("Escreva um comentário: ")]
                            print("Comentário adicionado com sucesso!")
                            break

                else:
                    print("Código não encontrado.\n")

                break
                    
        else:
            print("Não há livros na base.")
            break
    
    gravarDadosLIVROS()

def pesquisarLivro():
    carregarLIVROS()

    livroPesq = int(input("Digite o código para pesquisa: "))

    if len(dadosLIVROS["Livros"]) > 0:

        if "Livros" in dadosLIVROS:
            for livro in dadosLIVROS['Livros']:

                if "Código" in livro:

                    if livro["Código"] == livroPesq:

                        print("=" * 10, "DADOS DO LIVRO", "=" * 10)
                        print(f"Livro: {livro['Nome do Livro']}")
                        print(f"Autor: {livro['Autor']}")
                        print(f"Gênero: {livro['Gênero']} ")
                        print(f"Código: {livro['Código']}")
                        print("=" * 36)
                        print("\n")

                        return True
        
            print("Livro não cadastrado!")
            return False
        
    print("Base de dados vazia!")   
    return False

def listarComentarios():
    carregarLIVROS()

    cont_comentario = 1

    while True:
        livroComentar = int(input("Digite o código do livro que deseja ver os comentários: "))
        
        if "Livros" in dadosLIVROS:
            
            for livro in dadosLIVROS['Livros']:

                    if "Código" in livro and livro['Código'] == livroComentar:
                            
                            if len(livro['Comentário']) == 0:
                                print("Não há comentários registrado para esse livro.")
                                break
                            
                            else:
                                print("Lista de Comenários:\n")
                                for comentario in livro["Comentário"]:
                                    print("Comentário {}: {}".format(cont_comentario, comentario))
                                    cont_comentario += 1
                                break
                            
            else:
                print("Código não encontrado, tente novamente.")
            
            break
        
        else:
            print("Não há livros na base.")
    
    gravarDadosLIVROS()