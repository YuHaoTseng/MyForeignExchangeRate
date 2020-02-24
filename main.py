import sys
import requests
import datetime
from ExchangeRate import MyExchangeRate

def Download(URL, FileName):
    with open(FileName, mode='wb') as file:
        file.write(requests.get(URL).content)
        file.close()

if __name__ == "__main__":
    # Initial Parameters
    sourceURL = "https://rate.bot.com.tw/xrt/flcsv/0/l6m/"
    currency = None

    if len(sys.argv) != 2:
        print("Number of Parameters is incorrect.")
        exit(0)
    else:
        currency = str(sys.argv[1])

    try:
        FilePath = str(datetime.date.today()) + "_" + currency + ".csv"
        # Download Exchange Rate CSV for Bank of Taiwan
        Download(sourceURL + currency + "?Lang=en-US", FilePath)

        mExchangeRate = MyExchangeRate(FilePath, currency);
        mExchangeRate.GenerateLineChart()
    except:
        print("Unexpected error: ", sys.exc_info()[0])

