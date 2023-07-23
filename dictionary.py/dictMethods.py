
 #####CLEAR

car =	{"brand": "Ford","model": "Mustang","year": 1964}
car.clear()  
print(car)



###### COPY
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.copy()     
print(x)


###### FROM KEYS

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)


###### GET 

car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.get("model")
print(x)



car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.get("price", 15000)
print(x)



######ITEMS

car = {"brand": "Ford","model": "Mustang","year": 1964}

x = car.items()

print(x) 

car = {"brand": "Ford","model": "Mustang","year": 1964}

x = car.items()

car["year"] = 2018

print(x)


#######KEYS

car = {"brand": "Ford","model": "Mustang","year": 1964}

x = car.keys()

print(x)

print("KEYS")
car = {"brand": "Ford","model": "Mustang","year": 1964}

x = car.keys()

car["color"] = "white"

x = car.get("color")
print(x)

######POP

car = {"brand": "Ford","model": "Mustang","year": 1964}

car.pop("model")

print(car)


# SETDEFAULT
# GET 
# POPITEM









