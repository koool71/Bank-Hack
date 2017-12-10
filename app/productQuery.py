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
    self.sem3.products_field("search", product)

    results = self.sem3.get_products()

    return results
