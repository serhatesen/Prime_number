"""

Asal sayılar : 1'e ve kendisinden başka bir sayıya bölünmeyen sayılara denir

"""

def asalnumber(num):
    if num < 2:   # 1 ve daha küçük sayılar asal değil
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while True:
    number = input('Sayı: ')
    if (number == 'q'):
        break
    else:
        number = int(number)
        if (asalnumber(number)):
            print(number, 'Asal Sayıdır')
        else:
            print(number, 'Asal sayı değildir')