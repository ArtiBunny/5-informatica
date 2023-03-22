setups = [
    {"procesador": "i7 11700k", "RAM": "fury 32GB", "GPU": "RTX 3070 TI", "price": 1699} , {"procesador": "ryzen 9 3900X", "RAM":"fury 32GB", "GPU": "Radeon Rx 6500", "price": 1899} , {"procesador": "ryzen 7 5700G", "RAM":"HyperX 16GB", "GPU": "Radeon Rx 6500", "price": 1199} , {"procesador": "i5 10400F" , "RAM":"HyperX 8GB" , "GPU": "RTX 2060" , "price": 1099}
]



if setups [0]["procesador"] == "i7 11700k":
    print ("el procesador que buscas es el primero")
    descuento = setups [0]["price"] * 0,15
    print (descuento)
elif setups [1]["procesador"] == "i7 11700k":
    print ("el procesador que buscas es el segundo")
    descuento1 = setups [1]["price"] * 0,15
    print (descuento1)
elif setups [2]["procesador"] == "i7 11700k":
    print ("el procesador que buscas es el tercero")
    descuento2 = setups [2]["price"] * 0,15
    print (descuento2)
elif setups [3]["procesador"] == "i7 11700k":
    print ("el procesador que buscas es el cuarto")
    descuento3 = setups [3]["price"] * 0,15
    print (descuento3)


"8GB" == 8

if setups [0]["RAM"] == 8:
    print ("el primer setup tiene igual o menor ram a 8GB")
elif setups [1]["RAM"] == 8:
    print ("el procesador que buscas es el segundo")
elif setups [2]["RAM"] == 8:
    print ("el procesador que buscas es el tercero")
elif setups [3]["RAM"] == 8:
    print ("el procesador que buscas es el cuarto")


suma= setups[0]["price"] + setups[1]["price"] + setups[2]["price"] + setups[3]["price"]
print (suma)


