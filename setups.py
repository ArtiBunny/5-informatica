setups=[
    {"procesador": "i7 11700k" , "ram": "fury 32GB", "gpu": "rtx 3070 ti", "price": 1699},
    {"procesador": "ryzen 9 5900x" , "ram": "fury 32GB", "gpu": "radeon rx 6500", "price": 1899},
    {"procesador": "ryzen 7 5700g" , "ram": "hypeX 16GB", "gpu": "radeon rx 6500", "price": 1199},
    {"procesador": "i5 10400f" , "ram": "hypeX 8GB", "gpu": "rtx 2060", "price": 1099}
]
ram = setups[0]["ram"] , setups[1]["ram"] , setups[2]["ram"] , setups[3]["ram"]
#if "hypeX 8GB" in ram:
#   setups[3]["ram"] 
#   print ("Su memoria RAM se filtro en las menores o iguales a 8GB")
print (ram)
price = setups[0]["price"] + setups[1]["price"] + setups[2]["price"] + setups[3]["price"]
print (price)
    