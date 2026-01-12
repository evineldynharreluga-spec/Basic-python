
""""thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red","white","blue"]
}"""
#print(thisdict["brand"])

""""thisdict = dict(name = "John", age = 36, country = "Norway")
x = thisdict.get("age")
print(x)"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)