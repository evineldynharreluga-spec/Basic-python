def check_season(month):
    if month in ('April, January'):
        return 'Primavera'
    elif month == ('Marco'):
        return 'Outono'
    
month = str(input('Mes: '))
print(check_season(month))

