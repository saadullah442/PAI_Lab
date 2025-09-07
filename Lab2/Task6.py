countries = [
    {"country": "Mexico", "population": 129},
    {"country": "Indonesia", "population": 276},
    {"country": "Nigeria", "population": 211},
    {"country": "Russia", "population": 144},
    {"country": "India", "population": 1393},
    {"country": "Brazil", "population": 214},
    {"country": "Bangladesh", "population": 166},
    {"country": "United States", "population": 332},
    {"country": "Pakistan", "population": 225},
    {"country": "China", "population": 1412}
]

for x in range(0 , 10):
    for y in range(x , 10):
        if(countries[x]["population"] < countries[y]["population"]):
            temp = countries[x]
            countries[x] = countries[y]
            countries[y] = temp

for x in range(0 , 3):
    print(countries[x]["country"] , "\t" , countries[x]["population"])