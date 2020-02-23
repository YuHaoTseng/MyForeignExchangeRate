import sys
import requests
import datetime

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
        # Download Exchange Rate CSV for Bank of Taiwan
        Download(sourceURL + currency, str(datetime.date.today()) + "_" + currency + ".csv")
    except:
        print("Unexpected error: ", sys.exe_info()[0])

