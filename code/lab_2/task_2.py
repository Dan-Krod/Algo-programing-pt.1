import math
step = 0.5
x = -1
while x <= 1 :

    k = 1
    delta = 0.001
    sum = 0
    el = 10000

    while True :
        el = ((math.pow(-1, k) * x)/(k * (k+1))) * math.sin(2 * k+1)
        if abs(el) < delta :
            break
        sum += el
        k += 1

    print(f'x={round(x,3)} | sum={sum}')
    x += step
print('Done :)')

