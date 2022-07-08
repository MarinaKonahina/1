print("")
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = 100000
summ_money = {}
summ_money['ТКБ'] = (5.6*money)/100
summ_money['СКБ'] = (5.9*money)/100
summ_money['ВТБ'] = (4.28*money)/100
summ_money['СБЕР'] = (4.0*money)/100
print(summ_money)
print(list(summ_money.values()))
print(max(list(summ_money.values())))
