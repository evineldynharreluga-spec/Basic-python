
company = 'Coding For All'
result = company.find('Coding')
print(company.find('Coding'))


if 'Coding' in company:
    print('There is "Company" in the string')
else:
    print('There is not "Company" in the string')

if result != -1:
    print('There is "Company" in the string')
else:
    print('There is not "Company" in the string')