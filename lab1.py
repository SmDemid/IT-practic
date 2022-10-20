a = float(input())
b = float(input())
c = float(input())

dis = b ** 2 - 4 * a * c

if dis < 0:
    print("корней нет")
elif dis == 0:
    print('x = ', - b / (2 * a))
else:
    print("x1 = ", (- b + (dis ** 0.5)) / (2 * a))
    print("x2 = ", (- b - (dis ** 0.5)) / (2 * a))