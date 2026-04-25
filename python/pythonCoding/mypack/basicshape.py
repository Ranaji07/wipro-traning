def areaofsquare(side):
    return side * side

def perimeterofsquare(side):
    return 4 * side

def areaofrevt(l, b):
    return l * b

print('Area : ', areaofcircle(rad=radius))
print('Peri : ', peerimeterofcircle(rad=radius))

si = int(input('enter side of sq'))
print('Area : ', areaofsquare(side=si))
print('Peri : ', areaofsquare(side=si))

l = int(input('enter lenght'))
b = int(input('enter breath'))
print('Area : ', areaofrect(l,b))