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
create table if not exists mentions(
    message_id int REFERENCES messages(id),
    user_id int REFERENCES users(id)
)
""")

def mention_table_create():
    file_thank = open("gfa-team-thanks.json")
    file_random = open("gfa-team-random.json")

    random_data = json.load(file_random)
    thank_data = json.load(file_thank)

    random_thank_data = random_data + thank_data

    m_id = 0
    for message in random_thank_data:
        if "user" in message and "client_msg_id" in message: 
            m_id += 1
        if "user" in message and "client_msg_id" in message and "text" in message: 
            user_in_mention = re.findall(r"\<\@([\d\w]{9})\>", message["text"])
            for user in user_in_mention:
                cur.execute('select id from users where user_id = (%s)', (user,))
                id_user = cur.fetchone()
                data = (m_id, id_user)
                cur.execute("insert into mentions values (%s, %s)", data)
                con.commit()

mention_table_create()
cur.execute("select * from mentions")
print(cur.fetchall())

cur.close()
con.close()