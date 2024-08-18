def is_year_leap(year):
    return f'Год {year} високостный?: {year %4 == 0}'
print (is_year_leap (2024))
print (is_year_leap (2023))
print (is_year_leap(2022))

## True, если год високосный, и False— если иначе
# return year % 4 == 0