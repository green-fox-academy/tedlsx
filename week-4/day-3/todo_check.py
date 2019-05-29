import psycopg2 as psy

con = psy.connect(
    host = 'localhost',
    database = 'day3sql',
    user = 'postgres',
    password = 'xsl121924'
)

# print(con.get_dsn_parameters())
cur = con.cursor()

def todocheck(num):
    select_query = "select * from todo where id = (%(id_num)s)"
    cur.execute(select_query, {"id_num": num})
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows