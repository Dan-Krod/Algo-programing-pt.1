import math
x=0.5
while x <= 0.8:
   if x < 0.6:
        y = math.e**(x-math.sin(x))
        print(f"x={round(x,3)}|{y}")
        x += 0.02
   elif 0.6 <= x < 0.7:
        y = math.tan(abs(math.log(x)))
        print(f"x={round(x,3)}|{y}")
        x += 0.02
   else:    
        y = math.atan(x**7)
        print(f"x={round(x,3)}|{y}")
        x += 0.02
print('Done :)')