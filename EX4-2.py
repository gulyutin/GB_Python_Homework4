# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

from random import randint
max_val=100
k = randint(1, 100)

koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly=' + '.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])

poly=poly.replace('x^1 + ', 'x + ')
poly=poly.replace('x^0', '')
poly+=('','1')[poly[-1]==' + ']
poly=(poly, poly[:-2])[poly[-2:]=='^1']
print("k = ", k)
print(poly)

with open('EX4-2.txt', 'w') as data:
    data.write(poly)
