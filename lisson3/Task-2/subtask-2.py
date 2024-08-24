from subtask import Smartphone

catalog = []
phone1 = Smartphone("Apple","iPhone 14","89001234567")
phone2 = Smartphone("OnePlus","10 Pro","9165551234")
phone3 = Smartphone("Xiaomi","Mi 12","6666661234")
phone4 = Smartphone("Samsung","Galaxy S23","7777771234")
phone5 = Smartphone("Google ","Pixel 6","5551234567")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.mobel} - {phone.phone_namber}")