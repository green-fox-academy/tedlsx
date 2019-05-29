import psycopg2 as psy

con = psy.connect(
    host = 'localhost',
    database = 'day3sql',
    user = 'postgres',
    password = 'xsl121924'
)

# print(con.get_dsn_parameters())
cur = con.cursor()

def todoadd(new_task):
    add_query = "insert into todo (task) values  (%(new_todo)s)"
    cur.execute(add_query, {"new_todo": new_task})
    con.commit()
    select_query = 'select * from todo'
    cur.execute(select_query)
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows

