countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Transformação
output = [
    {'country': item[0][0].upper(), 'city': item[0][1].upper()} 
    for item in countries
]

print(output)