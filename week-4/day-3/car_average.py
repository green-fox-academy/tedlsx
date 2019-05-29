import psycopg2 as psy

con = psy.connect(
    host = 'localhost',
    database = 'day3sql',
    user = 'postgres',
    password = 'xsl121924'
)

cur = con.cursor()

def caraverage():
    avg_query = "select extract(year from now()) - sum(year * count) / sum(count) as avg_year from car"
    cur.execute(avg_query)
    rows = cur.fetchall()
    return rows