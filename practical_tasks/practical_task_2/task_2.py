n = int(input('Enter the number: '))

factorial = 1
for i in range(2, n + 1):
  factorial *= i
 
print(f'Factorial: {factorial}')