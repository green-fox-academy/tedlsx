import psycopg2 as psy

con = psy.connect(
    host = 'localhost',
    database = 'day3sql',
    user = 'postgres',
    password = 'xsl121924'
)

# print(con.get_dsn_parameters())
cur = con.cursor()
cur.execute(
    """create table if not exists todo(
        id serial,
        task varchar(30)
        )"""
)


def todolist(task_list):
    select_query = 'select * from todo'
    cur.execute(select_query)
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows


