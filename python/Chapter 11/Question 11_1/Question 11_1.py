from random import choice
from random import randint

def merge(A,B,lastA,lastB):
  a = lastA-1
  b = lastB-1
  index = lastA+lastB-1
  while b>=0:
    if a>=0 and A[a] > B[b]:
      A[index] = A[a]
      a -= 1
    else:
      A[index] = B[b]
      b -= 1
    index -= 1
  return A

#building testcases
lenA = randint(1,10)
A = [0]*lenA
lenB = randint(1,10)
B = [0]*lenB
elems = range(0,20)
for i in range(0,len(B)):
  B[i] = choice(elems)
B.sort()
for i in range(0,lenA):
  A[i] = choice(elems)
A.sort()
for i in range(0,lenB):
  A.append(0)

#testing
def check_sorted(array):
  for i in range(0,len(array)-1):
    if array[i]>array[i+1]:
      return False
  return True
  
print A
print B
result = merge(A,B,lenA,lenB)
print result
assert(check_sorted(result) == True)