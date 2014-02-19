from random import choice
from random import randint

def longestIncreasingSubsequence(HtWt):
  HtWt.sort(key=lambda x:x[0])
  sequences = []
  for i in range(0,len(HtWt)):
    bestSequence = None
    for sequence in sequences:
      if is_valid(sequence,HtWt[i]):
        bestSequence = longer(sequence,bestSequence)
    if bestSequence != None:
      bestSequence.append(HtWt[i])
    else:
      bestSequence = [HtWt[i]]
    sequences.append(bestSequence)
  sequences.sort(key=len,reverse=True)
  return sequences[0]

def is_valid(sequence,HtWt):
  if HtWt[0]>sequence[-1][0] and HtWt[1]>sequence[-1][1]:
    return True
  else:
    return False

def longer(A,B):
  if A == None:
    return B
  elif B == None:
    return A
  return A if len(A)>len(B) else B
  
#building testcases
HtWt = []
for i in range(0,10):
  htwt = (randint(0,10),randint(0,10))
  HtWt.append(htwt)

def is_valid_sequence(sequence):
  for i in range(0,len(sequence)-1):
    if sequence[i][0] >= sequence[i+1][0]:
      return False
  return True

#testing
print HtWt
sequence = longestIncreasingSubsequence(HtWt)
print sequence
assert(is_valid_sequence(sequence)==True)