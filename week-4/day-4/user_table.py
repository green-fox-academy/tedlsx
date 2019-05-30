import psycopg2 as psy
import json
import re

con = psy.connect(
    host = 'localhost',
    database = 'slack',
    user = 'postgres',
    password = 'xsl121924'
)

# print(con.get_dsn_parameters())
cur = con.cursor()

cur.execute("""
create table if not exists users(
    id serial primary key,
    user_id varchar(100),
    name varchar(128) default
)
""")

def user_table_create():
    file_thank = open("gfa-team-thanks.json")
    file_random = open("gfa-team-random.json")

    random_data = json.load(file_random)
    thank_data = json.load(file_thank)

    random_thank_data = random_data + thank_data

    user_in_mention = re.findall("\<\@(.+)\>", str(random_thank_data[0]))
    for user in user_in_mention:
        cur.execute("insert into users (user_id) values (%s)", user)
        con.commit()
    for message in random_thank_data:
        if "user" in message:
            user = message["user"]
            cur.execute("insert into users (user_id) values (%s)", list(user))
            con.commit()
        if "reactions" in message:
            for line in message["reaction"]:
                for user in line["users"]:
                    cur.execute("insert into users (user_id) values (%s)", list(user))
                    con.commit()

            
user_table_create()

cur.execute("select * from users")
print(cur.fetchall())

cur.close()
con.close()