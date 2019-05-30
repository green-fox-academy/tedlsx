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
create table if not exists messages(
    id serial primary key,
    user_id varchar(128),
    message text,
    channel varchar(128) default 'thanks_channel',
    sent_at timestamp 
)
""")

def messages_table_create():
    file_thank = open("gfa-team-thanks.json")
    file_random = open("gfa-team-random.json")

    random_data = json.load(file_random)
    thank_data = json.load(file_thank)

    random_thank_data = random_data + thank_data

    for message in random_thank_data:
        if "user" in message and "client_msg_id" in message: 
            time_find = re.match(r"\d+", message["ts"])
            time_stamp = time_find.group(0)
            message_value = [message["user"], message["text"], time_stamp]
            cur.execute("insert into messages (user_id, message, sent_at) values (%s,%s,to_timestamp(%s))", message_value)
            con.commit()
        else:
            continue

messages_table_create()

cur.execute("select * from messages")
print(cur.fetchall())

cur.close()
con.close()
    