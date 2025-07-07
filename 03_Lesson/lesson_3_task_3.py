from address import Address
from mailing import Mailing

from_address = Address("124456", "Москва", "Мира", "13", "25")
to_address = Address("654321", "Санкт-Петербург", "Репищева", "10", "5")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="ASDF12345678"
)

print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.building} - {mailing.from_address.apartment} в {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.building} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
