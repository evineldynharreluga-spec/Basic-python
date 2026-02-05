import requests
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)

data = response.json()
print(len(data))
#pprint(data[:2])


average = []
for cat in data:
    print(cat['life_span'].split(' - '))
    lowest = round(int(cat['life_span'].split(' - ')[0]))
    highest = round(int(cat['life_span'].split(' - ')[1]))
    average.append(round((lowest + highest)/2))
print(sum(average)/len(average))