from conectar import conexao
from prettytable import PrettyTable

def inserir_filmes():
    try:
        planos = ['basic', 'medium', 'premium']
        filme = input("Filme: ")
        print(planos)
        while True:
            plano = input("Plano: ")
            if plano not in planos:
                print("Plano inválido...")
            else:
                break
        desc = input("Descrição: ")
        classif = int(input("Classificação: "))

        inserir_filmes = f"""INSERT INTO filmes(filme, plano, descricao, class)
        values
        ('{filme}', '{plano}', '{desc}', {classif});"""
        cursor = conexao.cursor()
        cursor.execute(inserir_filmes)
        conexao.commit()

        # READ
        sql = "SELECT * from filmes"
        cursor.execute(sql)
        linhas = cursor.fetchall() # fetchall() => TRAGA TODAS AS LINHAS
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Filme", "Plano", "Descrição", "Classificação"]

        for linha in linhas:
            tabela.add_row(linha)

        print(tabela)

    except:
        print("Erro ao adicionar o filme...")

def inserir_usuarios():
    try:
        tipos = ['admin', 'user']
        planos = ['basic', 'medium', 'premium']
        usuario = input("Usuário: ")
        email = input("Email: ")
        print(planos)
        while True:
            plano = input("Plano: ")
            if plano not in planos:
                print("Plano inválido...")
            else:
                break

        print(tipos)
        while True:
            tipo = input("Tipo: ")
            if tipo not in tipos:
                print("Tipo inválido...")
            else:
                break
        idade = input("Idade: ")

        inserir_usuarios = f"""INSERT INTO usuarios(usuario, email, plano, tipo, idade)
        values
        ('{usuario}', '{email}', '{plano}', '{tipo}', {idade});"""
        cursor = conexao.cursor()
        cursor.execute(inserir_usuarios)
        conexao.commit()

        # READ
        sql = "SELECT * from usuarios"
        cursor.execute(sql)
        linhas = cursor.fetchall() # fetchall() => TRAGA TODAS AS LINHAS
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Usuário", "Email", "Plano", "Tipo", "Idade"]

        for linha in linhas:
            tabela.add_row(linha)

        print(tabela)

    except:
        print("Erro ao adicionar o filme...")