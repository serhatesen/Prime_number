"""

Asal sayılar : 1'e ve kendisinden başka bir sayıya bölünmeyen sayılara denir

"""

def asalnumber(num):
    if num < 2:   # 1 ve daha küçük sayılar asal değil
        return "Asal sayı değildir"
    for i in range(2, num):
        if num % i == 0:
            return "Asal sayı değildir"
    return "Asal sayıdır"

