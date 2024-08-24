from subtask import address
from subtask import mailing

to_address = address("672000","Чита","Какая-то","10","1")
from_address = address("673497.","Зилово","Какая-то","99","1")
mailing = mailing(to_address, from_address, 666, "GAS444")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street},{mailing.from_address.house} - {mailing.from_address.appartament} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street},"
      f"{mailing.to_address.house} - {mailing.to_address.appartament}. Стоимость {mailing.cost} рублейю")