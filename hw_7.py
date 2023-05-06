# 1) 
abcd = (lambda x: x*x - 10)(2)
print (abcd)

# 2) 
print (list(set(['Kuma', 'Nurtilek', 'Zina', 'Edzen', 'Kuma', 'Aitenur', 'Zina'])))

# 3) 
print(list(filter(lambda numbers: numbers %2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# 4) 
print(list(filter(lambda name: name == name[::-1], ['azat', 'zina', 'kuma', 'anna', 'sas'])))

# ДОП ЗАДАЧА:
# 5) 
import datetime
time1_str = input("Введите первую отметку времени в формате 'чч:мм:сс': ")
time1 = datetime.datetime.strptime(time1_str, "%H:%M:%S").time()
time2_str = input("Введите вторую отметку времени в формате 'чч:мм:сс': ")
time2 = datetime.datetime.strptime(time2_str, "%H:%M:%S").time()
difference = (datetime.datetime.combine(datetime.date.today(), time2) -
              datetime.datetime.combine(datetime.date.today(), time1)).total_seconds()
print("Разница между отметками времени: {} секунд".format(int(difference)))