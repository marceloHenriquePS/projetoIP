from datetime import date

dados = {'tarefas': []}
dataAtual = date.today()
data = dataAtual.strftime('%d/%m/%Y')


def apresentacao():
    print('-=' * 55)
    print("Projeto: Gestão de Clubes de Leitura".center(100))
    print('-=' * 55)
    print(f"Data: {data}")
    print("Equipe: Ingryd Rayla Nunes e Anna Priscila de Oliveira Gondim.")
    print('')
    print("Resumo:\nEste relatório documenta o desenvolvimento do código-fonte, implementado exclusivamente utilizando"
          "\n"
          "dicionários para armazenamento de dados, para o Sistema de Gestão de Clubes de Leitura em Python. O sistema"
          "\n"
          "tem como objetivo proporcionar uma plataforma interativa para os membros do clube, permitindo que eles adici"
          "\n"
          "onem livros à lista, compartilhem comentários e visualizem a lista de leitura coletiva, além de ter a capaci"
          "\n"
          "dade de remover livros da lista.")
    print('')
    print("Introdução:\nO Sistema de Gestão de Clubes de Leitura foi concebido como uma ferramenta centralizada para\n"
          "facilitar a interação entre os membros do clube.\nA aplicação utiliza conceitos de dados em dicionários pa"
          "ra criar uma estrutura modular e intuitiva.")
    print('')
    print("Tecnologias Utilizadas:\n• Linguagem de programação: Python 3.12.\n"
          "• Estrutura de Dados: Dicionários para armazenamento de informações sobre livros e membros.\n"
          "• Bibliotecas: datetime")
    print('')
    print("Estrutura do Código:\n"
          "O código está organizado em módulos para melhorar a manutenção e escalabilidade.\n"
          "A estrutura básica compreende:\n"
          "• 'clubeLivros_main.py': Arquivo responsável pela exibição do menu e interação com o usuário.\n"
          "• 'cadastroClubeLivros.py': Arquivo responsável por os dicionários e funções que armazenam as informações.\n"
          "• 'relatorio_main.py': Arquivo responsável pela exibição do menu do relatório e interação com o usuário.\n"
          "• 'cadastroRelatorio.py': Arquivo responsável por armazenar os dados do relatório.")
    print('')
    print("Funcionalidades Implementadas:\n"
          "• Adição, remoção e edição de livros na lista do clube de leitura utilizando dicionários.\n"
          "• Comentários associados a cada livro.\n"
          "• Visualização da lista de leitura coletiva.\n"
          "• Armazenamento persistente das informações utilizando estruturas de dicionários.")
    print('')
    print("Considerações Finais:")
    print("O Sistema de Gestão de Clubes de Leitura em Python foi desenvolvido com sucesso, proporcionando uma\n"
          "plataforma interativa para os membros do clube. A escolha de armazenar dados em dicionários demonstrou\n"
          "ser uma abordagem eficiente e facilitou a manipulação de informações no projeto.")


def relatorio():
    pass


apresentacao()
