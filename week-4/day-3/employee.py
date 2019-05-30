import psycopg2 as psy
import json, csv
import xml.etree.ElementTree as ET
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
CREATE TABLE if not exists employee1(
id integer,
first_name varchar(100),
last_name varchar(100),
birth_date date,
gender varchar(100),
monthly_salary int)
""")

cur.execute("""
CREATE TABLE if not exists employee2(
id integer,
name varchar(100),
birth_date date,
nationality varchar(100),
gender varchar(100),
monthly_salary int,
university varchar(100))
""")

cur.execute("""
CREATE TABLE if not exists employee3(
id integer,
name varchar(100),
birth_date date,
branch varchar(100),
gender varchar(100),
salary_by_year int,
position varchar(100))
""")

def employee_create():
    e1 = open("employees.csv", "r")
    e2 = open("employees.json", "r")    
    # tree = ET.parse("employees.xml")
    # root = tree.getroot()

    my_list = []

    data_csv = csv.reader(e1, delimiter=",")
    my_list = list(data_csv)[1:]
    for row in my_list:
        cur.execute("insert into employee1 values (%s, %s, %s, %s, %s, %s)", row)
        con.commit()

    data_json = json.load(e2)
    for line in data_json:
        dict_value = [line["id"], line["name"], line["birth_date"], line["nationality"], line["gender"], line["monthly_salary"], line["university"]]
        cur.execute("insert into employee2 values (%s, %s, %s, %s, %s, %s, %s)", dict_value)
        con.commit()

    e1.close()
    e2.close()

    # for elem in root:
    #     for subelem in elem:
    #         my_list.append(subelem.attrib.get())
    
