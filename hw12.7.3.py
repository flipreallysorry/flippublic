per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("Внесити денюшку:"))
sbr=(per_cent['СБЕР'])/100
vtb=(per_cent['ВТБ'])/100
skb=(per_cent['СКБ'])/100
tkb=(per_cent['ТКБ'])/100
deposit=[money*tkb, money*skb, money*vtb, money*sbr]
print("Навар с капиталистов:", list(map(round, (deposit))))
print("Максимальный навар:", round(max(deposit)))