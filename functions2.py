import requests
import json
from datetime import datetime
import os

axie_endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

#returns date
def get_current_date():
  now = datetime.now()
  current_date = now.strftime("%D")
  return current_date

#returns time
def get_current_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M")
  return current_time

#returns price, given token name
def get_price(token_name):
  coinreq = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + token_name + "&vs_currencies=usd",  headers = {"accept":"application/json"})
  coinname = token_name
  coinprice = coinreq.json()[token_name]['usd']
  return(coinprice)


def get_axie_details(id):
    axie_details = []
    payload1 = {
		"operationName": "GetAxieDetail",
    	"content-type" : "application/json",
		"variables": {
			"axieId": id
		},
		"query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\n"
	}
    r = requests.post(axie_endpoint, json=payload1)
    response1 = json.loads(r.text)
    data = response1["data"]["axie"]['parts']
    return(data)



def get_price_details(id):
	axie_details = []
	payload1 = {
		"operationName": "GetAxieDetail",
    	"content-type" : "application/json",
		"variables": {
			"axieId": id
		},
		"query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\n"
	}
	r = requests.post(axie_endpoint, json=payload1)
	response1 = json.loads(r.text)
	data1 = response1["data"]["axie"]
	
	payload2 = {
		"operationName": "GetAxieTransferHistory",
		"variables": {
			"axieId": id,
			"from": 0,
			"size": 5
		},
		"query": "query GetAxieTransferHistory($axieId: ID!, $from: Int!, $size: Int!) {\n  axie(axieId: $axieId) {\n    id\n    transferHistory(from: $from, size: $size) {\n      ...TransferRecords\n      __typename\n    }\n    ethereumTransferHistory(from: $from, size: $size) {\n      ...TransferRecords\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TransferRecords on TransferRecords {\n  total\n  results {\n    from\n    to\n    timestamp\n    txHash\n    withPrice\n    __typename\n  }\n  __typename\n}\n"
	}
	r2 = requests.post(axie_endpoint, json=payload2)
	response2 = json.loads(r2.text)
	data2 = response2['data']['axie']['transferHistory']['results']	
	if len(data2)==0:
		return 'null'
	saleDate = data2[0]['timestamp']
	priceEth = data2[0]['withPrice']
	priceEth = int(priceEth)/1000000000000000000
	parts = data1['parts']
	axieId = data1["id"]
	birthDate = data1['birthDate']
	axieClass = data1['class']
	genes = data1['genes']
	breedCount = data1['breedCount']
	mouth = parts[3]['name']
	eye = parts[0]['name']
	horn = parts[4]['name']
	ear = parts[1]['name']
	back = parts[5]['name']
	tail = parts[2]['name']
	mouthClass = parts[3]['class']
	eyeClass = parts[0]['class']
	hornClass = parts[4]['class']
	earClass = parts[1]['class']
	backClass = parts[5]['class']
	tailClass = parts[2]['class']
	axie_details.append(axieId)
	axie_details.append(saleDate)
	axie_details.append(birthDate)	
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
	axie_details.append(priceEth)
	return(axie_details)

def get_axie_owner(id):
	payload = {
		"operationName": "GetAxieDetail",
		"variables": {
			"axieId": id
		},
		"query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  level\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
	}
		
	r = requests.post(axie_endpoint, json=payload)
	# print(r.text)
	response = json.loads(r.text)
	
	owner = response["data"]["axie"]["owner"]
	return(owner)