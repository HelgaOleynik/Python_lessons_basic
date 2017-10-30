# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
  ost_number = (number%1) * (10**ndigits)
  okrugl_number = int((number%1) * (10**(ndigits+1))%10)

  x = int(number)
  y = float(x)
  ost_1 = int(ost_number)
  if okrugl_number <= 4:
    ost_2 = float(ost_1 / (10**ndigits))
    return(y+ost_2)
  else:
    ost_1 += 1 
    ost_2 = float(ost_1 / (10**ndigits))
    return(y+ost_2)
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
  

  a_part = 0 
  b_part = 0 


  for x in str (ticket_number // 1000):
    a_part += int(x)
  for y in str (ticket_number % 1000):
    b_part += int(y)
  if a_part == b_part:
    return True
  else:
    return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
