from fake_math import divide

result1 = divide(5, 7)
result2 = divide(3, 0)

print(f'Первый ответ: {result1}')
print(f'Второй ответ: {result2}')

from true_math import divide as de

result3 = de(89, 6)
result4 = de(56, 0)

print(f'Первый ответ: {result3}')
print(f'Второй ответ: {result4}')

