from ctypes import cdll
import pandas as pd
#ABSOLUTE DEVIATION
df = pd.read_pickle("pure_data.pkl")
AD = []
for eachRecord in df.to_dict(orient='records'):
    AD.append(round(abs(float(eachRecord["actual"].replace("%", "")) - float(eachRecord["forecast"].replace("%", ""))), 1))

df["AD"] = AD
print(df)

df.to_pickle("pure_data.pkl")

print("Added AD")