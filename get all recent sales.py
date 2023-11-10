import functions2 as fn2
import requests
import json
from datetime import datetime
import os
import time
import csv

axie_endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

currentAxie = 11293116
while True:
        while currentAxie > 0:
            try:
                with open("scrapedata.csv", "a", newline="") as f1:

                    details = fn.get_price_details(currentAxie)
                    writer = csv.writer(f1)
                    if details != 'null':
                        writer.writerow(details)
                        print(str(details[0]) + " " + str(format(details[18], '.4f')) + ' ' + str(details[6]) + ' ' + str(details[7]) + ' ' + str(details[8]) + ' ' + str(details[9]) + ' ' + str(details[10]) + ' ' + str(details[11]) + ' ' + str(details[3]))
                    else:
                        details = fn.get_axie_details(currentAxie)
                        try:
                            print(str(currentAxie) + ' ' + str(details[0]['name']) + ' ' + str(details[1]['name']) + ' ' + str(details[2]['name']) + ' ' + str(details[3]['name']) + ' ' + str(details[4]['name']) + ' ' + str(details[5]['name']))
                        except:
                            print('still an egg')
                    time.sleep(0.01)
                    currentAxie = currentAxie - 1
            except:
                 print('error')
                 currentAxie = currentAxie - 1
    
