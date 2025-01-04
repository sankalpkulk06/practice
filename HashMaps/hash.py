
city_map = {}

cities = ["BLR", "MUM", "DEL"]
city_map["India"] = []              # to avoid initilizing everytim we can use DefaultDict which is init on its own
city_map["India"] += cities

print(city_map)

from collections import defaultdict

city_map = defaultdict(list)

cities_India = ["BLR", "MUM", "DEL"]
city_map["India"] += cities_India

cities_USA = ["LA", "SF", "SJ"]
city_map["USA"] += cities_USA
print(city_map)

# Retrieving Data (hashmap.keys(), hashmap.values(), hashmap.items() - returns both)

city_list = city_map.values()
print("List of all the cities in the hashmap : ", city_list)