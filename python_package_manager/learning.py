''''import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

for url in url_lists:
    webbrowser.open_new_tab(url)'''


import requests

url = 'https://openweathermap.org/api'

response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)