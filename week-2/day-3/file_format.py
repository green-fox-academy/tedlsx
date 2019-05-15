# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:22:02 2019

@author: Ted_Liu
"""

######### movie

movie = open("movies.txt", "r")

my_text = movie.readlines()
for line in my_text:
    new_line = line.split(";")    
    print(new_line[0])
    
movie.close()
    
######## election
    
election = open("election.txt", "r")

my_text = election.readlines()
for line in my_text:
    new_line = line.split(",")
    if len(new_line) < 4:
            print(",".join(new_line))
    for word in new_line:
        if word == "":
            
            print(",".join(new_line))
        
election.close()     
    
#### Post
    
import json

with open("posts.json", encoding='utf-8') as out_file:
    data = json.load(out_file)
    print(data)

my_list =[]
for i in range(0, len(data)):
    my_list.append(data[i]["like_count"]) 
    max_like = max(my_list)
print(max_like)

for i in range(0, len(data)):
    if data[i]["like_count"] == 130:
        print(i)

data[2]["id"]


## transaction

##  from xml.dom import minidom


import xml.etree.ElementTree as ET



tree = ET.parse('transactions.xml')  
root = tree.getroot()


        
i = 0
for elem in root:
    i = 0
    my_list = []
    for subelem in elem:
       
        my_list.append( subelem.attrib.get("currency"))    
    print(f"from {elem[i].text} to {elem[i + 1].text} with amount {elem[i + 2].text} {my_list[2]}")


        
##### exam
    
import csv
import re

with open('exams.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    
    my_list = []
    for row in readCSV:
        my_list.append(row)
    new_list = my_list[1:-1]
    for new_row in new_list: 
        if "h" in new_row[2] and "m" in new_row[2] and "s" in new_row[2]:
            hour = int(re.findall("(\d+)h", new_row[2])[0]) * 60
            minute = int(re.findall("(\d+)m", new_row[2])[0])
            second = int(re.findall("(\d+)s", new_row[2])[0]) / 60
            score = float(new_row[1])
            score_ratio = score / (hour + minute + second)
            print(score_ratio)
            
            
        elif ":" in new_row[2]:
            hour = int(re.findall("(\d+)\:", new_row[2])[0]) * 60
            minute = int(re.findall("(\d+)\:", new_row[2])[1]) 
            second = int(re.findall("\:(\d+)", new_row[2])[1]) / 60
            score = float(new_row[1])
            score_ratio = score / (hour + minute + second)
            print(score_ratio)
        
        elif "." in new_row[2] and "h" in new_row[2]:
            hour = int(re.findall("\\.(\d+)", new_row[2])[0]) * 60
            score = float(new_row[1])
            score_ratio = score / hour
            print(score_ratio)
        
        elif "m" in new_row[2]:
            minute = re.findall("(\d+)m", new_row[2])[0] 
            score = float(new_row[1])
            score_ratio = score / float(minute)
            print(score_ratio)


            
        elif "s" in new_row[2]:
            second = int(re.findall("(\d+)s", new_row[2])[0]) / 60
            score = float(new_row[1])
            score_ratio = score / second
            print(score_ratio)
            
        else:
            print (0)
            



##### csv to json
            
import csv
import json


csvfile = open('users.csv', 'r')
jsonfile = open('users.json', 'w')

fieldnames = ("id", "first_name", "last_name", "email", "gender", "ip_address")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')



### json to xml
    
from xml.dom.minidom import Document
with open("flowers.json", "r") as flower_json:
    json_dic = json.loads(flower_json.read())
    print(json_dic)
    
doc = Document()
root = doc.createElement("flowers")
doc.appendChild(root)

for flower in json_dic:
    elem_flower = doc.createElement("flower")
    root.appendChild(elem_flower)

    for key, val in flower.items():
        child = doc.createElement(key)
        child_text = doc.createTextNode(str(val))
        
        elem_flower.appendChild(child)
        child.appendChild(child_text)
        
with open("flowers.xml", "w") as f:
    f.write(doc.toprettyxml())        
    
    
    
    
    
    
    
    
    
    
#### Door entering

with open('logs.csv') as csvfile:
    readcsv = csv.reader(csvfile) 
          
    my_list  = []
    dic = {}

    
    for row in readcsv:
        time = re.findall("(\d+\\.\d+\\.\d+)\\.", row[1])
        description = row[-1]
        my_list.append(row)
    for i in range(0, len(my_list)):
        same_describ_list = []
        time_list = []
        unique_time_list = []
        count_list = []
        date = {}
        description = my_list[i][-1]
        time = re.findall("(\d+\\.\d+\\.\d+)\\.", my_list[i][1])
        for k in range(0, len(my_list)):
            if description == my_list[k][-1]: 
                same_describ_list.append(my_list[i])
                
        for j in range(0, len(same_describ_list)):
            time = re.findall("(\d+\\.\d+\\.\d+)\\.", same_describ_list[j][1])
            time_list.append(time)
            if time not in unique_time_list:
                unique_time_list.append(time)
                
        for m in range(0, len(unique_time_list)):
            count = time_list.count(unique_time_list[m])
            count_list.append(count) 
            
        for n in range(0, len(unique_time_list)):            
            date.update({unique_time_list[n][0] : count_list[n]})
        
        dic.update({description : date})

dic        
       
      






    
    
    
    
    
    