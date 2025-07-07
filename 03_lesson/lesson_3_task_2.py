from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79123456789"))
catalog.append(Smartphone("Nokia","N8","+79213453477"))
catalog.append(Smartphone("Realme","C75", "+79341522442"))
catalog.append(Smartphone("Honor","200","+79845675566"))
catalog.append(Smartphone("Motorolla","RAZR V3i","+79343423411"))
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")

