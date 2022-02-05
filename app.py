import csv
import pandas as pd

df = pd.read_csv("starFinal.csv")
df = df.dropna()
df["radius"] = 0.102763*df["radius"]

df["mass"] = df['mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["mass"] = 0.000954588*df["mass"]

#df.drop(["Unnamed:0"],axis = 1,inplace = True)

df.reset_index(drop = True , inplace = True)
df.to_csv("unitConvertedStars.csv")