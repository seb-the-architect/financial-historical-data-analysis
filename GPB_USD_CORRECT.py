import pandas as pd

#Percentage of tests that are correct after 1hr?
df = pd.read_pickle("pure_data.pkl")

correctArray = []
incorrectArray = []
unsureArray = []

for eachRecord in df.to_dict(orient='records'):
    #The actual value is less than the forecasted value
    #Price should fall...
    if float(eachRecord["actual"][:-1]) < float(eachRecord["forecast"][:-1]):
        #The opening price is larger than the closing price, price has fallen
        if eachRecord["candle_data"]["candles"][0]["mid"]["o"] > eachRecord["candle_data"]["candles"][0]["mid"]["c"]:
            correctArray.append(eachRecord)
        else:
            incorrectArray.append(eachRecord)
    
    #The actual value is larger than the forecasted value
    #Price should rise...
    elif float(eachRecord["actual"][:-1]) > float(eachRecord["forecast"][:-1]):
        #The opening price is less than the closing price, price has risen
        if eachRecord["candle_data"]["candles"][0]["mid"]["o"] < eachRecord["candle_data"]["candles"][0]["mid"]["c"]:
            correctArray.append(eachRecord)
        else:
            incorrectArray.append(eachRecord)

    else:
        unsureArray.append(eachRecord)

print("The percentage is", str(((len(correctArray) / 176) * 100)) + "%")

gbpUsdCorrectDF = pd.DataFrame(correctArray)
print(len(correctArray))
print(len(incorrectArray))
print(len(unsureArray))

gbpUsdIncorrectDF = pd.DataFrame(incorrectArray)
print(gbpUsdIncorrectDF)
gbpUsdIncorrectDF.to_pickle("GBP_USD_INCORRECT.pkl")
#gbpUsdCorrectDF.to_pickle("GBP_USD_CORRECT.pkl")

print("aight we good")

#df.to_pickle("pure_data.pkl")