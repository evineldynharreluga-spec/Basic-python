import requests

url = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(url)

print(response)

for x in response:
    print(response['weight'])

