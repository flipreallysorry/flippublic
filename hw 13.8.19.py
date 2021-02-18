count = int(input("Введите кол-во билетов:"))
s = 0
for age in range(count):
    age = int(input("Введите возраст участников:"))
    for price in range(1):
        if 18 <= age <= 25:
            price = 990
        elif 0 <= age <= 18:
            price = 0
        elif 25 <= age <= 99:
            price = 1390
        else:
            print("Неверный возраст")
        s = s + price
if count >= 3:
    s = int(s * 0.9)
    i = int(s * 0.1)
    print("Вам скидосик 10%:", i)
print("Занесите в кассу:", s)






