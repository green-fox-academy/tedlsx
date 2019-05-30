import psycopg2 as psy
import json
import re

con = psy.connect(
    host = 'localhost',
    database = 'slack',
    user = 'postgres',
    password = 'xsl121924'
)

cur = con.cursor()

cur.execute("""
CREATE TABLE if not exists reactions(
id serial PRIMARY KEY,
user_id varchar(100),
message_id varchar(100),
reaction varchar(128) 
)
""")

def reactions_table_create():
    file_thank = open("gfa-team-thanks.json")
    file_random = open("gfa-team-random.json")

    random_data = json.load(file_random)
    thank_data = json.load(file_thank)

    random_thank_data = random_data + thank_data

    for message in random_thank_data:
        if "user" in message and "client_msg_id" in message and "reactions" in message:
            for react in message["reactions"]:
                for user in react["users"]:
                    message_value = [user, message["client_msg_id"], react["name"]]
                    cur.execute("insert into reactions (user_id, message_id, reaction) values (%s,%s,%s)", message_value)
                    con.commit()
    
reactions_table_create()
cur.execute("select * from reactions")
print(cur.fetchall())

cur.close()
con.close()