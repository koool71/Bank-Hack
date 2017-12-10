import os, csv

for file in os.listdir("../data sets/transactions"):
  transactionData = []
  with open("../data sets/transactions/" + file, "r") as csvFile:
    reader = csv.reader(csvFile, delimiter = ",")
    for row in reader:
      transactionData.append(row)
  for row in transactionData[1:]:
    transactionName = row[1]
    # print("Read" + transactionName + " transaction!")
    for file in os.listdir("../data sets/prices"):
      priceData = []
      priceList = []
      linkList = []

      fileName = file[:-4]
      if(fileName == transactionName):
        print(transactionName)

        with open("../data sets/prices/" + transactionName + ".csv") as csvFile:
          reader = csv.reader(csvFile, delimiter = ",")
          for row in reader:
            priceData.append(row)

        for row in priceData:
          price = row[0]
          link = row[1]
          linkList.append(link)
          priceList.append(int(price))
        lowIndex = priceList.index(min(priceList))
        lowLink = linkList[3]
        print(lowLink)
        print(priceList)