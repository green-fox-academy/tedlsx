import psycopg2

con = connect(
    host = 'localhost',
    database = 'greenfox',
    username = 'postgres',
    password = 'xsl121924'
)

name = ''
class_name = ''

select_query = 'INSERT INTO students VALUES (%(name)s, %(class_name)s)'

select_query = 'SELEECT * from students WHERE name LIKE ''
cur = con.cursor()

cursor = connection.cursor()

rows = cur.fetchall()
for r in rows:
    print(f"")
    
# con.commit()

cur.close()
cur.execute(select_query, (name, class_name))

# print(cursor.rowcount)

con.close()