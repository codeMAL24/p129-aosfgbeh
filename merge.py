import csv
import pandas as pd
dataset1 = []
dataset2 = []

with open("bright_stars.csv","r",encoding = "utf8")as f:
    c = csv.reader(f)
    for i in c:
        dataset1.append(i)

with open("unitConvertedStars.csv","r",encoding = "utf8") as f:
    c = csv.reader(f)
    for i in c:
        dataset2.append(i) 

header1 = dataset1[0]
starData1 = dataset1[1:]

header2 = dataset2[0]
starData2 = dataset2[1:]

header = header1 + header2
star_data = []
for i in starData1:
    star_data.append(i)

for i in starData2:
    star_data.append(i)  

with open("totalStars.csv","w",encoding = "utf8")as f:
    c = csv.writer(f)
    c.writerow(header)
    c.writerows(star_data)

df = pd.read_csv("totalStars.csv")    
df.tail(8)





