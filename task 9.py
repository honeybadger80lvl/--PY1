salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
increase += 1
for i in range(10):
    need_money += salary
    need_money -= spend
    spend *= increase
need_money *= -1
print(round(need_money))
