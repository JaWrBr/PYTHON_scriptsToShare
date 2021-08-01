'''
Write a small interactive python utility that calculates matrix multiplication.
None of the variables are passed as arguments, everything will be handled at runtime

Write the utility in a way that you’d write a productiuon code, use python3 without any mathematical
libraries (like numpy), if you are familiar with pytest, use test driven development approach and attach all tests created during development.
'''

a_width, a_height = int(input ('\nMatrix A\nwidth: ')), int(input ('height: '))
b_width, b_height = int(input ('\nMatrix B\nwidth: ')), int(input ('height: '))
r_width, r_height = b_width, a_height
a_values, b_values = [], []
result = []

# Matrix A
print ('\nMatrix A values:')
for i in range ((a_height)):
  a_values.append(input().split())

for i in range (a_height):
  for j in range (a_width):
    a_values[i][j] = int(a_values[i][j])

# Matrix B
print ('\nMatrix B values:')
for i in range (b_height):
  b_values.append(input().split())

for i in range (b_height):
  for j in range (b_width):
    b_values[i][j] = int(b_values[i][j])

# result Matrix
for i in range (r_height):
  result.append([])
  for j in range (r_width):
    result[i].append(0)

for i in range(len(a_values)):
      for j in range(len(b_values[0])):
        for k in range(len(b_values)):
            result[i][j] += a_values[i][k] * b_values[k][j]
  
for r in result:
    print(r)
