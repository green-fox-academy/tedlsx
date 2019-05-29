import psycopg2 as psy

con = psy.connect(
    host = 'localhost',
    database = 'day3sql',
    user = 'postgres',
    password = 'xsl121924'
)

cur = con.cursor()

def carremove():
    remove_query = "delete from car where count = 0"
    cur.execute(remove_query)
    con.commit()
    select_query = "select * from car"
    cur.execute(select_query)
    rows = cur.fetchall()
    return rows
