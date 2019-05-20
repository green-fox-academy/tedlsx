#### Door entering
import csv
import json
import re
import numpy as np
import statistics
import seaborn as sns
import matplotlib.pyplot as plt


with open('logs.csv') as csvfile:
    my_list = []
    dic = {}
    readcsv = csv.reader(csvfile) 

    for row in readcsv:
        my_list.append(row)
    for i in range(0, len(my_list)): 
        id = my_list[i][-1]
        date = re.findall("(\d+\\.\d+\\.\d+)\\.", my_list[i][1])[0]
        
        if id in dic:
            if date in dic[id]:
                dic[id][date] += 1
            else:
                dic[id][date] = 1
        else:
            dic[id] = {date:1}

print(dic)

######### find the average arriving time
dic_arr_time ={}

my_new_list =[]

for i in range(0, len(my_list)):
    if "(F-1)" in my_list[i][5]:
        my_new_list.append(my_list[i])

def find_hours(times):
    time_hour =  re.findall("\.+\s(\d+)\:\d+\:\d+", times)[0]
    time_min = re.findall("\.+\s\d+\:(\d+)\:\d+", times)[0]
    time_sec = re.findall("\.+\s\d+\:\d+\:(\d+)", times)[0]
    return int(time_hour) + int(time_min) / 60 + int(time_sec) / 3600


dic_arr_time = {}

for i in range(0, len(my_new_list)): 
    id = my_new_list[i][-6]
    date = re.findall("(\d+\\.\d+\\.\d+)\\.", my_new_list[i][1])[0]
    hours = find_hours(my_new_list[i][1])

    if id in dic_arr_time:
        if date in dic_arr_time[id]:
            if hours < dic_arr_time[id][date]:
                dic_arr_time[id][date] = hours
        else:
            dic_arr_time[id][date] = hours
    else:
        dic_arr_time[id] = {date:hours}

dic_arr_time 


arrive_time = {}

for id in dic_arr_time:
    for date in dic_arr_time[id]:
        if date in arrive_time:
            arrive_time[date].append(dic_arr_time[id][date])

        else:
            arrive_time[date] = [dic_arr_time[id][date]] 

arrive_time

#### Total average time 
def hours_to_times(times):
    hour = int(times // 1)
    minute = int(times % 1 * 60 // 1)
    sec = int(times % 1 * 60 % 1 * 60)
    return f"{hour}:{minute}:{sec}"

sum_time = 0
sum_people = 0
for key in arrive_time:
    sum_time += sum(arrive_time[key])
    sum_people += len(arrive_time[key])

print("total average arriving time is ", hours_to_times(sum_time / sum_people))
        

###  average arrive time for each day
average_arrive_time = {}

for key in arrive_time:
    average_arrive_time[key] = float(sum(arrive_time[key]) / len(arrive_time[key]))
    
    average_arrive_time[key] =  hours_to_times(average_arrive_time[key])

average_arrive_time

def times_to_hours(times):
    time_hour =  re.findall("(\d+)\:\d+\:\d+", times)[0]
    time_min = re.findall("\d+\:(\d+)\:\d+", times)[0]
    time_sec = re.findall("\d+\:\d+\:(\d+)", times)[0]
    return int(time_hour) + int(time_min) / 60 + int(time_sec) / 3600



x = []
y = []
for key in sorted(average_arrive_time.keys()) :
    x.append(key)
    y.append(times_to_hours(average_arrive_time[key]))
    print(key , "has mean arriving time " , average_arrive_time[key])


sns.scatterplot(x, y)
plt.xlabel("date")
plt.ylabel("arriving time")
plt.title("Average arriving time")


####### meddian arriving time for each day

for key in arrive_time:
    med = statistics.median(arrive_time[key])
    time = hours_to_times(med)
    print(key, "has median arriving time ", time)

sns.relplot(x="date", y="median arriving time", data=tips)
plt.xlabel("Colors")
plt.ylabel("Values")
plt.title("Colors vs Values")

######## deviation 
for key in arrive_time:
    try:
        dev = statistics.stdev(arrive_time[key])
    except statistics.StatisticsError:
        dev = 0

    print(key, "arriving time has deviation ", dev)


