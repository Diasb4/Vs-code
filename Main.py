# A = int(input())
# B = int(input())
# H = int(input())
# if H > B:
#     print("Пересып")
# elif H < A:
#     print("Недосып")
# else:
#     print("Это нормально")

# a=int(input())
# if a%400==0 and a%4==0:
#     print('Високосный')
# elif a%4==0 and a%100!=0:
#     print('Високосный')
# else:
#     print('Обычный')
#
# print(Surface(a,b,c))

# a = int(input())
#
# print((a > -15 and a <= 12) or (a > 14 and a < 17) or (a >= 19))
#
# a = float(input())
# b = float(input())
# c = input()
#
# def calculate(a, b, c):
#     if c == '+':
#         return a + b
#     elif c == '-':
#         return a - b
#     elif c == '*':
#         return a * b
#     elif c == '/':
#         if b == 0:
#             return 'Деление на 0!'
#         else:
#             return a / b
#     elif c == 'mod':
#         if b == 0:
#             return 'Деление на 0!'
#         else:
#             return a % b
#     elif c == 'pow':
#         return a ** b
#     elif c == 'div':
#         if b == 0:
#             return 'Деление на 0!'
#         else:
#             return a // b
# print(calculate(a, b, c))

# import math
#
# form = input()
#
# if form == "треугольник":
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = (a + b + c) / 2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(float(s))
#
# elif form == "прямоугольник":
#     a = float(input())
#     b = float(input())
#     print(float(a * b))
#
# elif form == "круг":
#     r = float(input())
#     print(float(3.14 * r * r))

# a = int(input())
# b = int(input())
# c = int(input())
#
# maximum = max(a, b, c)
# minimum = min(a, b, c)
# middle = a + b + c - maximum - minimum
#
# print(maximum)
# print(minimum)
# print(middle)

# n=int(input())

# if n%10==0 or 11<=n<=20:
#   print(str(n) + ' программистов')
# elif 111<=n<=114:
#   print(str(n) + ' программистов')
# elif n==1 or n%10==1 and n!= 111:
#   print(str(n) + ' программист')
# elif n%10==2 or n%10==3 or n%10==4 and n!=112 and n!=113 and n!=114:
#   print(str(n) + ' программиста')
# elif n%10==5 or n%10==6 or n%10==7 or n%10==8 or n%10==9:
#   print(str(n) + ' программистов')

# num = int(input())
# num_2 = num % 1000
# summa_1 = 0
# summa_2 = 0 
# for i in range(1,4):
#     summa_1 += num % 10
#     num = num // 10
# for i in range(1,4):
#     summa_2 += num_2 % 10
#     num_2 = num_2 // 10
# if summa_1 == summa_2:
#     print("Счастливый")
# else:
#     print("Обычный")

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# n = int(input())
# sum = 0
# while n != 0:
#     sum += n
#     n = int(input())
# print(sum)

# a = int(input())
# b = int(input())

# orig_a = a
# orig_b = b

# while b != 0:
#     a, b = b, a % b

# lcm = orig_a * orig_b // a

# print(lcm)

# n = int(input())
# while n <= 100:
#     if n >= 10:
#         print(n)
#     n = int(input())

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print('\t', end='')
# for j in range(c, d + 1):
#     print(j, end='\t')
# print()

# for i in range(a, b + 1):
#     print(i, end='\t')  
#     for j in range(c, d + 1):
#         print(i * j, end='\t')
#     print() 

# a = int(input())
# b = int(input())
# sum = 0
# count = 0 
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         sum = sum + i
#         count += 1
# print(sum / count)

# a = str(input().lower())
# count = 0
# for i in range(len(a)):
#     if a[i] == 'c' or a[i] == 'g':
#         count += 1
#         percent = (count / len(a)) * 100
# print(percent)

# s = input()
# count = 1

# for i in range(1, len(s)):
#     if s[i - 1] == s[i]:
#         count += 1
#     else:
#         print(s[i - 1] + str(count), end='')
#         count = 1

# print(s[-1] + str(count), end='')
# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)
# a = [1, 2, 3]
# b = a
# print(b)
# # значения списка b?

# a[1] = 10
# print(b)
# # значения списка b?

# b[0] = 20
# print(a)
# # значения списка a?

# a = [5, 6]
# print(b)
# # значения списка b?

# a = [int(i) for i in input().split()]
# summ = 0
# for i in range(len(a)):
#     summ += a[i]
# print(summ)
# a = [int(i) for i in input().split()]
# if len(a) == 1:
#     print(a[0])
# else:
#     for i in range(len(a)):
#         left = a[i - 1]
#         right = a[(i + 1) % len(a)]
#         print(left + right, end=' ')
# a = [int(i) for i in input().split()]
# a.sort()

# duplicates = []

# for i in range(1, len(a)):
#     if a[i] == a[i - 1] and a[i] not in duplicates:
#         duplicates.append(a[i])

# print(*duplicates)

numbers = []
total = 0

while True:
    n = int(input())
    numbers.append(n)
    total += n
    if total == 0:
        break

square_sum = sum(i ** 2 for i in numbers)
print(square_sum)
