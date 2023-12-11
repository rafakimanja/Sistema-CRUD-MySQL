import mysql.connector
from mysql.connector import Error


def create(cursor, conexao):

    usuario = {}

    usuario['nome'] = str(input('\nDigite o seu nome: '))
    usuario['tec'] = str(input('Digite a sua tecnologia: '))
    usuario['cargo'] = str(input('Digite o seu cargo: '))

    comando = ("insert into programadores (nome, tecnologia, cargo) values (%s, %s, %s)")
    valores = (usuario['nome'], usuario['tec'], usuario['cargo'])

    cursor.execute(comando, (valores))

    conexao.commit()


def read(cursor):

    query = ("select * from programadores")

    cursor.execute(query)

    result = cursor.fetchall()

    print('\nBanco de dados:')
    for a, b, c, d in result:
        print(f'ID: {a} | NOME: {b:<17}| TECNOLOGIA: {c:<12} | CARGO: {d}')


def update(cursor, conexao):

    read(cursor)

    id = int(input('\nDigite o id do usuario que deseja alterar: '))
    nome = str(input('Digite o nome: '))
    tec = str(input('Digite a tecnologia: '))
    cargo = str(input('Digite o cargo: '))

    comando = ("update programadores set nome = %s, tecnologia = %s, cargo = %s where id = %s")
    valores = (nome, tec, cargo, id)

    cursor.execute(comando, (valores))
    conexao.commit()


def delete(cursor, conexao):

    read(cursor)

    id = int(input('\nDigite o id do usuario que deseja apagar: '))
    esc = str(input(f'Você tem certeza que deseja \033[1;31mapagar\033[m o usuario ? [Y/N]: ')).upper()

    if esc == 'Y':

        comando = ("delete from programadores where id = %s")
        valores = (id,)

        cursor.execute(comando, (valores))
        conexao.commit()


if __name__ == '__main__':

    config = {
        'user': 'seu_usuario',
        'password': 'sua_senha',
        'host': 'localhost',
        'database': 'teste'
    }

    try:
        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor()

    except Error as erro:
        print(f'Erro na conexao: {erro}')

    while True:

        print('\n-----Sistema CRUD-----')
        print('0. Sair do sistema')
        print('1. Cadastrar usuario')
        print('2. Imprimir usuarios')
        print('3. Alterar usuario')
        print('4. Apagar usuario')
        esc = int(input(': '))

        match esc:

            case 0:
                cursor.close()
                conexao.close()
                break

            case 1:
                create(cursor, conexao)

            case 2:
                read(cursor)

            case 3:
                update(cursor, conexao)

            case 4:
                delete(cursor, conexao)

            case _:
                print('Erro! Opção inválida')