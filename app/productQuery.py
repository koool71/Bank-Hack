from semantics3 import Products

class ProductQuery:

  def __init__(self):
    self.sem3 = Products(
      api_key = "SEM3188CBEA0C536322303E7C24718D47A3B",
      api_secret = "ZDI1NWU4NTQ3M2M4MjJiZDdlMWNlNDBmMTM0MTQ4OGU"
    )
    self.results = []

  def queryProduct(self):
    userInputProduct = input("What product would you like to know about: ")

    sem3.products_field("search", userInputProduct)

    results = sem3.get_products()

    return results

  def autoQueryProduct(self,product):
    self.results = []
    self.sem3.products_field("search", product)

    self.fullResults = self.sem3.get_products()
    self.fullResults = self.fullResults["results"]
    
    for item in self.fullResults:
      #get item name
      self.results.append(item["name"])
      self.siteDetailsResults = item["sitedetails"]
      for siteDetailItem in self.siteDetailsResults:
        self.latestOffersResults = siteDetailItem["latestoffers"]
        for latestOffersItem in self.latestOffersResults:
          self.results.append(latestOffersItem["seller"])
          self.results.append(latestOffersItem["price"])
        # print(self.latestOffersResults)
      # self.results.append(self.moneyResults["price"])

    # return self.fullResults
    return self.results
