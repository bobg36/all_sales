import requests
import json
import functions as fn
import time
import pandas as pd
import csv

expensive = 0.007491
sleepTime = 46

def get_write_list_ids():
    #put all 20 id into a list
    f = open("recent20.txt", "r")
    old20id = []
    for axie in f:
        axie = axie.strip()
        old20id.append(axie)
    f.close()

    #write most recent 20 id to text file
    file = open("recent20.txt", "w")
    recent20id = []
    for axie in recent20:
        id = axie[0]
        file.write(str(id) + '\n')
        recent20id.append(id)
    file.close()

    #compare most recent 20 id to text file
    setOld = set(old20id)
    setRecent = set(recent20id)
    setDiffList = setRecent-setOld
    diffList = list(setDiffList)
    return(diffList)

count = 0
exp = 0
while True:
    try: 
        #get auctions from API
        results = fn.get_recent_auctions()
        #get recent 20 data from results
        recent20 = fn.get_auction_details(results)
        write_list_ids = get_write_list_ids()

        write_list = []
        if len(write_list_ids) > 0:
            i = 0
            i = len(write_list_ids)
            for item in write_list_ids:
                write_axieDetails = recent20[i]
                write_list.append(write_axieDetails)
                axieId = write_axieDetails[0]
                saleDate = write_axieDetails[1]
                axieClass = write_axieDetails[3]
                breedCount = write_axieDetails[5]
                mouth = write_axieDetails[6]
                eye = write_axieDetails[7]
                horn = write_axieDetails[8]
                ear = write_axieDetails[9]
                back = write_axieDetails[10]
                tail = write_axieDetails[11]
                usdPrice = write_axieDetails[18]
                ethPrice = write_axieDetails[19]
                marketplaceUrl = "https://app.axieinfinity.com/marketplace/axies/" + str(axieId)
                count = count + 1
                if ethPrice > expensive:
                    exp = exp + 1
                    print("$$$ ALL:" + str(count) + " EXP:" + str(exp) + " | " + marketplaceUrl + " $$$")
                # else:
                #     print("--- ALL:" + str(count) + " EXP:" + str(exp) + " | " + marketplaceUrl + " ---")
                    print(str("%.5f" % ethPrice) + " " + axieClass + "-" + str(breedCount) + "- |" + mouth + " | " + eye + " | " + horn + " | " + ear + " | " + back + " | " + tail + " | \n")
                
                i = i - 1

        with open("data.csv", "a", newline="") as f1:

            writer = csv.writer(f1)
            writer.writerows(write_list)
    except:
        print('error')


    time.sleep(sleepTime)




    # print(test)

