import requests
import json

url = "https://api-gateway.skymavis.com/graphql/marketplace"
headers = {
"Content-Type": "application/json",
"X-API-Key": "f2BkjPLpGG93RnjbDvtbBMQ2krqcmScR"
}


# def get_recent_sales():


def get_recent_auctions():
    query = """
    query MyQuery {
    settledAuctions {
        axies {
        total
        results {
            id
            genes
            class
            breedCount
            birthDate
            parts {
            name
            class
            }
            transferHistory {
            results {
                withPrice
                withPriceUsd
                timestamp
            }
            }
            stage
        }
        }
    }
    }
    """
    response = requests.post(url, headers=headers, json={"query": query})
    data = response.json()
    # print(data)
    results = data['data']['settledAuctions']['axies']['results']
    return(results)

results = get_recent_auctions()

#gets a list of 20 (index 0 to 19) of most recently sold axies
def get_auction_details(results):
    sold_list = []
    i = 0
    while i <= 19:
        stage = results[i]['stage']
        axie_details = []
        axieId = results[i]['id']
        saleDate = results[i]['transferHistory']['results'][0]['timestamp']
        birthDate = results[i]['birthDate']
        axie_details.append(axieId)
        axie_details.append(saleDate)
        axie_details.append(birthDate)
        if stage == 4:
            axieClass = results[i]['class']
            genes = results[i]['genes']
            breedCount = results[i]['breedCount']
            parts = results[i]['parts']
            eye = parts[0]['name']
            ear = parts[1]['name']
            back = parts[2]['name']
            mouth = parts[3]['name']
            horn = parts[4]['name']
            tail = parts[5]['name']
            eyeClass = parts[0]['class']
            earClass = parts[1]['class']
            backClass = parts[2]['class']
            mouthClass = parts[3]['class']
            hornClass = parts[4]['class']
            tailClass = parts[5]['class']
            usdPrice = results[i]['transferHistory']['results'][0]['withPriceUsd']
            ethPrice = results[i]['transferHistory']['results'][0]['withPrice']
            ethPrice = int(ethPrice)/1000000000000000000
            axie_details.append(axieClass)
            axie_details.append(genes)
            axie_details.append(breedCount)
            axie_details.append(mouth)
            axie_details.append(eye)
            axie_details.append(horn)
            axie_details.append(ear)
            axie_details.append(back)
            axie_details.append(tail)
            axie_details.append(mouthClass)
            axie_details.append(eyeClass)
            axie_details.append(hornClass)
            axie_details.append(earClass)
            axie_details.append(backClass)
            axie_details.append(tailClass)
            axie_details.append(usdPrice)
            axie_details.append(ethPrice)
        i = i + 1
        sold_list.append(axie_details)
    return(sold_list)









#query and get details given axie id
def get_axie_details(id):
    query = """
    query MyQuery($axieId: ID!) {
    axie(axieId: $axieId) {
        birthDate
        class
        genes
        breedCount
        image
        parts {
        name
        class
        }
        stage
    }
    }
    """
    variables = {"axieId": id}
    response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
    data = response.json()
    axieId = id
    birthDate = data['data']['axie']['birthDate']
    stage = data['data']['axie']['stage']
    if stage == 4:
        axieClass = data['data']['axie']['class']
        genes = data['data']['axie']['genes']
        breedCount = data['data']['axie']['breedCount']
        imageUrl = "https://axiecdn.axieinfinity.com/axies/" + str(axieId) + "/axie/axie-full-transparent.png"
        marketplaceUrl = "https://app.axieinfinity.com/marketplace/axies/" + str(axieId)
        eye = data['data']['axie']['parts'][0]['name']
        ear = data['data']['axie']['parts'][1]['name']
        back = data['data']['axie']['parts'][2]['name']
        mouth = data['data']['axie']['parts'][3]['name']
        horn = data['data']['axie']['parts'][4]['name']
        tail = data['data']['axie']['parts'][5]['name']
        eye_class = data['data']['axie']['parts'][0]['class']
        ear_class = data['data']['axie']['parts'][1]['class']
        back_class = data['data']['axie']['parts'][2]['class']
        mouth_class = data['data']['axie']['parts'][3]['class']
        horn_class = data['data']['axie']['parts'][4]['class']
        tail_class = data['data']['axie']['parts'][5]['class']
        details = []
        details.append(axieId)
        details.append(birthDate)
        details.append(axieClass)
        details.append(genes)
        details.append(breedCount)
        details.append(imageUrl)
        details.append(marketplaceUrl)
        details.append(mouth_class)
        details.append(eye_class)
        details.append(horn_class)
        details.append(ear_class)
        details.append(back_class)
        details.append(tail_class)
        details.append(mouth)
        details.append(eye)
        details.append(horn)
        details.append(ear)
        details.append(back)
        details.append(tail)
    else:
        details = []
        details.append(axieId)
        details.append(birthDate)
        details.append(marketplaceUrl)
        details.append("EGG")
    return(details)