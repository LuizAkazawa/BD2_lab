from database import Database
from writeAJson import writeAJson
from livroModel import LivroModel
from cli import PersonCLI

db = Database(database="relatorio5", collection="livros")
livroModel = LivroModel(database=db)

#create
#livroModel.create_livro(2, 'Fds', 'Eu', 2015, 34.5)
#livroModel.create_livro(3, 'Fds', 'fewaf', 2015, 34.5)

#read
#livroModel.read_livro_by_id(2)

#update
#livroModel.update_livro(2, 'diguidas', 'EuMesmo', 2010, 67.9)
#livroModel.delete_livro(2)

while True:
    print("1 - Create")
    print("2 - Read")
    print("3 - Update")
    print("4 - Delete")
    print("QUALQUER OUTRA TECLA PARA PARAR O PROGRAMA")
    op = int(input("Digite uma opção:"))


    if op==1:
        print("CRIANDO LIVRO")
        id = int(input("Id: "))
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        preco = float(input("Preco: "))
        livroModel.create_livro(id, titulo, autor, ano, preco)
    elif op == 2:
        print("PROCURANDO POR ID")
        id = int(input("Id: "))
        livroModel.read_livro_by_id(id)
    elif op == 3:
        print("ATUALIZANDO INFO PELO ID")
        id = int(input("Id: "))
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        preco = float(input("Preco: "))
        livroModel.update_livro(id, titulo, autor, ano, preco)
    elif op == 4:
        print('DELETANDO POR ID')
        id = int(input("Id: "))
        livroModel.delete_livro(id)
    else:
        print("PARANDO PROGRAMA ... ")
        break

