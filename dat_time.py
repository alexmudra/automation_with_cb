#лінк на лібу https://docs.python.org/3/library/datetime.html

import dat_time
from datetime import date

def time_counter (seconds): #записуємо секунди в перемінну
    print("Start")
    for i in range(1, seconds+1): #проходимось циклом по секундам +1
        print(f"{i}, привіт(ик) для Тані") #прінтаємо ітератор
        dat_time.sleep(2) #пауза на 1 секунду
    print("Finish")

time_counter(3)
#res: Start
# 1, привіт(ик) для Тані
# 2, привіт(ик) для Тані
# 3, привіт(ик) для Тані
# Finish
print("#####")

iso_date_format = date.fromisoformat(input("Input date like year-month-date ->"))
iso_date_format
