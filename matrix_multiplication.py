# result Matrix
def main():
  result = []
  a_width, a_height = (input ('\nMatrix A\nwidth: ')), (input ('height: '))
  if not a_width.isnumeric() or not a_height.isnumeric():
    print ('Input must be a number (positive integer).') 
    exit()
  else:
    a_width, a_height = int(a_width), int(a_height)

  b_width, b_height = input ('\nMatrix B\nwidth: '), input ('height: ')
  if not b_width.isnumeric() or not b_height.isnumeric():
    print ('Input must be a number (positive integer).') 
    exit()
  else:
    b_width, b_height = int(b_width), int(b_height)
  
  r_width, r_height = b_width, a_height
  a_values = matrixA(a_height,a_width)
  b_values = matrixB(b_height,b_width)
  
  for i in range (r_height):
    result.append([])
    for j in range (r_width):
      result[i].append(0)

  for i in range(len(a_values)):
        for j in range(len(b_values[0])):
          for k in range(len(b_values)):
              result[i][j] += a_values[i][k] * b_values[k][j]
  
  print ('\nResult: ')    
  for line in result:
    l = ''
    for item in line:
      l = l + str(item) + ' '
    print(l)

# Matrix A
def matrixA(a_height,a_width):
  a_values = []
  print ('\nMatrix A values:')
  for i in range (a_height):
    a_values.append(input().split())
    if len(a_values[i])>a_width:
      print (f'Input must not exceed given Matrix A width i.e. {a_width} numbers!')
      exit()

    

  for i in range (a_height):
    for j in range (a_width):
      if not a_values[i][j].isnumeric():
        print ('Input must be a number(s)-positive integer(s), separated by space.')
        exit()
      else:
        a_values[i][j] = int(a_values[i][j])
  return a_values

# Matrix B
def matrixB(b_height,b_width):
  b_values = []
  print ('\nMatrix B values:')
  for i in range (b_height):
    b_values.append(input().split())
    if len(b_values[i])>b_width:
      print (f'Input must not exceed given Matrix B width i.e. {b_width} number(s)!')
      exit()


  for i in range (b_height):
    for j in range (b_width):
      if not b_values[i][j].isnumeric():
        print ('Input must be a number(s)-positive integer(s), separated by space.')
        exit()
      else:
        b_values[i][j] = int(b_values[i][j])
  return b_values


main()

