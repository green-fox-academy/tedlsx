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
CREATE TABLE if not exists employee(
id integer,
first_name varchar(20),
last_name varchar(10),
birth_date int,
nationality varchar(10),
gender varchar(10),
monthly_salary int,
university varchar(50))
""")

def employee_create():
    e1 = open("employees.csv", "r")
    e2 = open("employee.json", "r")    
    tree = ET.parse("emplyee.xml")
    root = tree.getroot()

    my_list = []

    data_csv = csv.reader(e1, delimiter=",")
    for row in data_csv:
        my_list.append(row)
    data_json = json.load(e2)
    for line in data_json:
            my_list.append(line)