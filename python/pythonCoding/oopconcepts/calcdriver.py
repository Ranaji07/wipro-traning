
from oopconcepts.calc import Calc


calcobj = Calc()
print(calcobj.add( a:10, b:5))
print(calcobj.sub( a:10, b:5))
print(calcobj.mul( a:10, b:5))
numbres = [10, 20, 30]
count = len(numbres)

try:
    res = calcobj.fdiv( a:10, b:0)
except ZeroDivisionError:
    print('0 in denominator')
else:
    print(res)
finally:
    print('Done!!')
