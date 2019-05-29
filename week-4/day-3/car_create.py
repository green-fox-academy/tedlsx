import psycopg2 as psy
import json
# import io

con = psy.connect(
    host = 'localhost',
    database = 'day3sql',
    user = 'postgres',
    password = 'xsl121924'
)

# print(con.get_dsn_parameters())
cur = con.cursor()
cur.execute("""
CREATE TABLE if not exists car(
id integer PRIMARY KEY,
brand varchar(20),
model varchar(10),
year int,
condition varchar(10),
price int,
count int)
""")

def caradd():
    with open("cars.json") as file:
        # data = file.readlines()
        # cur.executemany("INSERT INTO car VALUES ('{0}')".format(data))
        data = json.load(file)
        for line in data:
                cur.execute("insert into car values (%s, %s, %s, %s, %s, %s, %s)", list(line.values()))
                con.commit()
        select_query = 'select * from car'
        cur.execute(select_query)
        rows = cur.fetchall()
        cur.close()
        con.close()
        return rows

