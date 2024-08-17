def month_to_season(month):
    if month in [12,1,2]:
        return 'Winter'
    elif month in [3,4,5]:
        return 'Spring'
    elif month in [6,7,8]:
        return 'Summer'
    elif month in [9,10,11]:
        return 'Autumn'
    else: 
        return 'Неверный месяц'

print (month_to_season(2))
print (month_to_season(12))
print (month_to_season(6))
print (month_to_season(9))
print (month_to_season(13))