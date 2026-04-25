# """
# Date:24-4-26
# desc: learining various if stmt format
# """

#big2
# num1 = int(input('enter a number'))
# num2 = int(input('enter another number'))
#
# if num1 == num2:
#     print(' both are equal')
# elif num1 > num2 :
#     print(num1 , ' is big. ')
# else:
#     print(num2, ' is big. ')

#big3
# num1 = int(input('enter a number'))
# num2 = int(input('enter another number'))
# num3 = int(input('enter another number'))
#
# if num1 == num2 == num3:
#     print('All values are equal')
# elif num1 > num2 and num1 > num3:
#     print(num1, ' num1 is biggest')
# elif num2 > num1 and num2 > num3:
#     print(num2, ' num2 is biggest')
# elif num3 > num1 and num3 > num1:
#     print(num3, ' num3 is biggest')
#

#weekday
ch = int(input('enter a number bet 1-7'))

match ch:
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')
    case _:
        print('invalid choice')
