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


# Gera a cláusula SELECT para uma consulta SQL
generate_select = lambda fields: f"SELECT {', '.join(fields)} "

# Gera a cláusula FROM para uma consulta SQL
generate_from = lambda table: f"FROM {table} "

# Gera a cláusula INNER JOIN para a consulta SQL
generate_inner_join = lambda table, condition: f"INNER JOIN {table} ON {condition} "

# Gera a cláusula WHERE para uma consulta SQL
generate_where = lambda condition: f"WHERE {condition} " if condition else ""

# Gera a cláusula GROUP BY para uma consulta SQL
generate_group_by = lambda fields: f"GROUP BY {', '.join(fields)} " if fields else ""

# Gera a cláusula HAVING para uma consulta SQL
generate_having = lambda condition: f"HAVING {condition} " if condition else ""

# Gera a cláusula ORDER BY para uma consulta SQL
generate_order_by = lambda fields, order='ASC': f"ORDER BY {', '.join(fields)} {order} " if fields else ""

# Função para compor uma consulta SQL completa usando as funções acima
compose_query = lambda select, from_clause, joins=[], where="", group_by=[], having="", order_by=[]: (
    select +
    from_clause +
    ''.join(joins) +
    where +
    generate_group_by(group_by) +
    having +
    generate_order_by(order_by)
)

# Exemplo específico de uso: Consulta para jogos lançados por mais de uma empresa
def query_games_by_multiple_companies():
    select_clause = generate_select(['GAMES.title AS GameTitle', 'COUNT(DISTINCT COMPANY.id_company) AS NumberOfCompanies'])
    from_clause = generate_from('GAMES')
    joins = [
        generate_inner_join('VIDEOGAMES', 'GAMES.id_console = VIDEOGAMES.id_console'),
        generate_inner_join('COMPANY', 'VIDEOGAMES.id_company = COMPANY.id_company')
    ]
    group_by_clause = ['GAMES.title']
    having_clause = generate_having('COUNT(DISTINCT COMPANY.id_company) > 1')
    return compose_query(select_clause, from_clause, joins, group_by=group_by_clause, having=having_clause)

# Executar e imprimir a consulta SQL
if __name__ == '__main__':
    sql_query = query_games_by_multiple_companies()
    print(sql_query)
