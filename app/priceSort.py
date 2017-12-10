import os, csv
from productQuery import ProductQuery

pq = ProductQuery()

#find transaction data
for file in os.listdir("../data sets/transactions"):
  transactionData = []

  #read transaction data
  with open("../data sets/transactions/" + file, "r") as csvFile:
    reader = csv.reader(csvFile, delimiter = ",")
    for row in reader:
      transactionData.append(row)

  for row in transactionData[1:]:
    transactionName = row[1]
    # print("Read" + transactionName + " transaction!")
    
    queryResults = pq.autoQueryProduct(transactionName)
    print(queryResults)

    # #find price data
    # for file in os.listdir("../data sets/prices"):
    #   priceData = []
    #   priceList = []
    #   linkList = []

    #   fileName = file[:-4]
      
    #   #compare price file name with current transaction name
    #   if(fileName == transactionName):
    #     print(transactionName)

    #     #read price data
    #     with open("../data sets/prices/" + transactionName + ".csv") as csvFile:
    #       reader = csv.reader(csvFile, delimiter = ",")
    #       for row in reader:
    #         priceData.append(row)

        #using a Semantic3 API to grab product data
        # queryResults = pq.autoQueryProduct(transactionName)
        # print(queryResults)

        #compare prices
        # for row in priceData:
        #   price = row[0]
        #   link = row[1]
        #   linkList.append(link)
        #   priceList.append(int(price))
        # lowIndex = priceList.index(min(priceList))
        # lowLink = linkList[3]
        # print(lowLink)
        # print(priceList)

# pq.queryProduct()