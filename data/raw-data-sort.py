import pandas as pd

#Puts the data into a more readable format and pickles it
rawFile = open("Data/Raw-MOM-history.txt", "r")
pureFile = open("Data/Purified.txt", "w")
fileLines = rawFile.readlines()
print(f"Purifying {len(fileLines)} lines...")

pure_data = [{"dates":[]}, {"time":[], "actual":[], "forecast":[], "previous":[], "AD": []}]

#Removing excess months
for eachLine in fileLines:
    for eachMonth in ["(Jan)", "(Feb)", "(Mar)", "(Apr)", "(May)", "(Jun)", "(Jul)", "(Aug)", "(Sep)", "(Oct)", "(Nov)", "(Dec)"]:
        if eachMonth in eachLine:
            fileLines[fileLines.index(eachLine)] = eachLine.replace(eachMonth, "")
    #print(eachLine)

#Splitting and appending
for eachLine in fileLines:
    #Date
    pure_data[0]["dates"].append(eachLine[0:12])
    #The rest
    pure_array = ([x for x in eachLine[13:].replace(" ", "").split("\t") if x not in ["", "\n"]])
    pure_data[1]["time"].append(pure_array[0])
    pure_data[1]["actual"].append(pure_array[1])
    pure_data[1]["forecast"].append(pure_array[2])
    pure_data[1]["previous"].append(pure_array[3])

df = pd.DataFrame(pure_data[1], index=pure_data[0]["dates"])

df.to_pickle("pure_data.pkl")