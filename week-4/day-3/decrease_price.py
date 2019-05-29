import psycopg2 as psy

con = psy.connect(
    host = 'localhost',
    database = 'day3sql',
    user = 'postgres',
    password = 'xsl121924'
)

cur = con.cursor()
def decreaseprice():
    decreaseprice_query = "update car set price = price * 0.8 where condition = 'wreck' order by id "
    cur.execute(decreaseprice_query)
    con.commit()
    select_query = "select * from car"
    cur.execute(select_query)
    rows = cur.fetchall()
    return rows