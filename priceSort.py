import os
import json

transFile = open("../data sets/transactions/transaction log.txt", "r")
priceList = []
linkList = []
data = json.load(open("../data sets/search results/iPhon.json"))
print(data)
low = 0
transName = transFile.readline()
for file in os.listdir("../data sets/prices"):
	file = file[:-4]
	if(file == transName):
		print(transName)

		priceFile = open("../data sets/prices/" + transName + ".txt")
		for item in priceFile:
			parse = item.split(" ")
			price = parse[0]
			link = parse[1]
			linkList.append(link)
			priceList.append(int(price))
		lowIndex = priceList.index(min(priceList))
		lowLink = linkList[3]
		print(lowLink)
		print(priceList)