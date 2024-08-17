def bank(X, Y):
    years = Y // 12  # получаю количество лет из месяцев
    return X * (1.1 ** years)
addX = int(input("Введите сумму денег: "))
addY = int(input("Введите количество месяцев: "))

if addX <= 0 or addY <= 0:
    print("Неправильный ввод данных!")
else:
    print(bank(addX, addY))