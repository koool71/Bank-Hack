from semantics3 import Products

sem3 = Products(
  api_key = "SEM3188CBEA0C536322303E7C24718D47A3B",
  api_secret = "ZDI1NWU4NTQ3M2M4MjJiZDdlMWNlNDBmMTM0MTQ4OGU"
)

userInputProduct = input("What product would you like to know about: ")

sem3.products_field("search", userInputProduct)

results = sem3.get_products()

print(results)