from random import randint

def findElement(matrix,elem):
  col = len(matrix[0])-1
  row = 0
  while col>=0 and row<= len(matrix)-1:
    if matrix[row][col] == elem:
      return True
    elif matrix[row][col] > elem:
      col -= 1
    else:
      row += 1
  return False

#building testcase
def buildMatrix():
  row = randint(5,10)
  col = randint(5,10)
  matrix = []
  for i in range(0,row):
    matrix.append([0]*col)
    for j in range(0,col):
      if i==0 and j ==0:
        matrix[i][j] = randint(0,5)
      elif i==0:
        matrix[i][j] = matrix[i][j-1] + randint(1,5)
      elif j==0:
        matrix[i][j] = matrix[i-1][j] + randint(1,5)
      else:
        matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])+ randint(1,5)
  return matrix

def searchAll(matrix,x):
  for i in range(0,len(matrix)):
    if x in matrix[i]:
      return True
  return False

#testing
matrix = buildMatrix()
for i in range(0,len(matrix)):
  for j in range(0,len(matrix[0])):
    print matrix[i][j],
  print 

for i in range(0,20):
  x = randint(0,100)
  find = findElement(matrix,x)
  truth = searchAll(matrix,x)
  assert(find == truth)
print 'test passed'