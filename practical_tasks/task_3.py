print('Sides of a triangle: ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a <= 0 or b <= 0 or c <= 0:
  print('Error')
else:
  if a + b > c and a + c > b and b + c > a:
    print('Triangle exists')
  else:
    print('Triangle isn\'t exist')