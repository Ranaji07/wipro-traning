
# #functions
# def add(n1, n2):
#     return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# def mul(n1, n2):
#     return n1 * n2
#
# def div():
#     pass
#
#
#
# #driver
# num1=int(input('enter a number'))
# num2=int(input('enter another number'))
#
# res = add (num1, num2)
# print('Add:', res)
#
# res = sub (num1, num2)
# print('Sub:', res)
#
# res = mul (num1, num2)
# print('Mul:', res)

#ARBITARY
# def add(nums):
#     sum=0
#     for n in nums:
#         sum += n
#     return sum
#
# numbers = list()
# count = int(input('how many ?'))
#
# for _ in range(1, count+1):
#     numbers.append(int(input('No')))
# print(numbers)
# print(add(numbers))
#
# def add(n1, n2, n3=10):
#     return n1 + n2 + n3
#
# #driver
# num1=int(input('enter a number'))
# num2=int(input('enter another number'))
#
#
# print(add(num1, num2))
# print(add(num1, num2, n3:100))

#lambds

# num1=int(input('enter a number'))
# num2=int(input('enter another number'))
#
# add = lambda n1, n2 : n1+n2
#
# print(add(num1, num2))

numbers = [1,2,3,4,5,6,7,8,9,10]

# sq = lambda nums : [num * num for num in nums]
# print(sq(numbers))


sq = lambda nums : [num * num for num in nums if num%2==0 ]
print(sq(numbers))
