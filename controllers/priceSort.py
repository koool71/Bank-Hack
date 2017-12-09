import os

transFile = open("../data sets/transactions/transaction log.txt", "r")
priceList = []
transName = transFile.readline()
for file in os.listdir("../data sets/prices"):
	file = file[:-4]
	if(file == transName):
		print(transName)

		priceFile = open("../data sets/prices/" + transName + ".txt")
		for price in priceFile:
			priceList.append(int(price))
			priceList.sort()
		print(priceList)