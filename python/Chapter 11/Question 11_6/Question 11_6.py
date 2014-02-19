def findElement(matrix,elem):
  col = len(matrix[0])
  row = 0
  while col>=0 and row<= len(matrix)-1:
    if matrix[col][row] == elem:
      return True
    elif matrix[col][row] > elem:
      col -= 1
    else:
      row += 1
  return False