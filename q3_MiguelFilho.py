import mysql.connector
from mysql.connector import Error

# Conectar ao banco de dados
connect_db = lambda: mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='popai2004',
    database='programaçãofuncional'
)

# Executar query
execute_query = lambda connection, query, params=(): (
    lambda cursor: (
        cursor.execute(query, params),
        list(cursor.fetchall()) if query.strip().lower().startswith('select') else None,
        cursor.close()
    )
)(connection.cursor())

# Funções lambda para operações de inserção, remoção e consulta
modify_data = lambda query, params=(): (
    (lambda connection: (
        execute_query(connection, query, params),
        connection.close()
    ))(connect_db())
)

# Exemplo de operações para todas as tabelas
insert_data = lambda table, columns, values: modify_data(
    f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(values))});",
    values
)

remove_data = lambda table, condition: modify_data(
    f"DELETE FROM {table} WHERE {condition};"
)

query_data = lambda table, condition: modify_data(
    f"SELECT * FROM {table} WHERE {condition};"
)

# Exemplo de uso
if __name__ == '__main__':
    # Operações com USERS
    print(insert_data('USERS', ['name', 'country', 'id_console'], ('Alice', 'USA', 1)))
    print(query_data('USERS', 'id = 1'))
    print(remove_data('USERS', 'id = 1'))

    # Operações com VIDEOGAMES
    print(insert_data('VIDEOGAMES', ['name', 'id_company', 'release_date'], ('Game Console', 1, '2022-01-01')))
    print(query_data('VIDEOGAMES', 'id_console = 1'))
    print(remove_data('VIDEOGAMES', 'id_console = 1'))

    # Operações com GAMES
    print(insert_data('GAMES', ['title', 'genre', 'release_date', 'id_console'], ('Epic Game', 'Adventure', '2023-01-01', 1)))
    print(query_data('GAMES', 'id_game = 1'))
    print(remove_data('GAMES', 'id_game = 1'))

    # Operações com COMPANY
    print(insert_data('COMPANY', ['name', 'country'], ('Game Studio', 'Canada')))
    print(query_data('COMPANY', 'id_company = 1'))
    print(remove_data('COMPANY', 'id_company = 1'))
