import psycopg2 as psy

con = psy.connect(
    host = 'localhost',
    database = 'day3sql',
    user = 'postgres',
    password = 'xsl121924'
)

# print(con.get_dsn_parameters())
cur = con.cursor()

def todoremove(num):
    delete_query = "delete from todo where id = (%(id_num)s)"
    cur.execute(delete_query, {"id_num": num})
    con.commit()
    select_query = "select * from todo"
    cur.execute(select_query)
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows

