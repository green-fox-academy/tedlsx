import psycopg2 as psy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

con = psy.connect(
    host = 'localhost',
    database = 'slack',
    user = 'postgres',
    password = 'xsl121924'
)

# print(con.get_dsn_parameters())
cur = con.cursor()

def draw_max_post():
    x= []
    y =[]
    cur.execute("select distinct users.user_id, count(messages.user_id) as num_post from messages inner join users on users.id = messages.user_id group by users.user_id order by num_post desc limit 5")
    result = cur.fetchall()
    for res in result:
        x.append(res[0])
        y.append(res[1])

    sns.set_style("darkgrid")
    sns.barplot(x, y)
    plt.xlabel("user_id")
    plt.ylabel("num_post")
    plt.title("Frequency of posts for each user")
    plt.show()

def draw_activeday():
    x= []
    y =[]
    cur.execute("select extract(hour from  sent_at - interval '1h' * 6) as hour, count(id) as count_id from messages group by hour order by hour;")
    result = cur.fetchall()
    for res in result:
        x.append(res[0])
        y.append(res[1])

    sns.set_style("darkgrid")
    sns.barplot(x, y)
    plt.xlabel("hour")
    plt.ylabel("num of post")
    plt.title("Frequency of posts for each day")
    plt.show()

def draw_emoji():
    x= []
    y =[]
    cur.execute("select reaction, count(message_id) as count_id from reactions group by reaction order by count_id desc limit 10;")
    result = cur.fetchall()
    for res in result:
        x.append(res[0])
        y.append(res[1])

    sns.set_style("darkgrid")
    sns.barplot(x, y)
    plt.xlabel("emoji name")
    plt.ylabel("num of post")
    plt.title("Frequency of emoji for all posts")
    plt.show()

def user_table_create():
    file_thank = open("gfa-team-thanks.json")
    file_random = open("gfa-team-random.json")

    random_data = json.load(file_random)
    thank_data = json.load(file_thank)

    random_thank_data = random_data + thank_data