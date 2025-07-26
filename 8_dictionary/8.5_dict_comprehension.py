import random


city_names = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

city_temp = {city:random.randint(20, 30) for city in city_names}

above_25 = {city: temp for city, temp in city_temp.items() if temp > 25}

print("City Temperatures:", city_temp)
print("Cities with temperature above 25:", above_25)