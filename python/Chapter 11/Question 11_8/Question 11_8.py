from random import choice
from random import randint

class Tree(object):
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
    self.rank = 0

  
class Question(object):
  def __init__(self):
    self.tree = None
    
  def track(self,x):
    if self.tree == None:
      self.tree = Tree(x)
      return True
    node = self.tree
    count = 0
    while True:
      if x<= node.value:
        node.rank += 1
        if node.left == None:
          node.left = Tree(x)
          return True
        else:
          node = node.left
      else:
        if node.right == None:
          node.right = Tree(x)
          return True
        else:
          node = node.right

  def getRankOfNumber(self,x):
    node = self.tree
    count = 0
    while True:
      if x == node.value:
        return count + node.rank + 1
      elif x< node.value:
        if node.left == None:
          return -1
        else:
          node = node.left
      else:
        count += node.rank + 1
        if node.right == None:
          return -1
        else:
          node = node.right

#building testcases
def buildTestCase():
  q = Question()
  array = []
  for i in range(0,randint(0,20)):
    x = randint(0,100)
    q.track(x)
    array.append(x)
  array.sort()
  return q,array

def rank(array,x):
  return array.count(x)+array.index(x)
  
#testing
testcase,array = buildTestCase()
print array
for elem in array:
  r = rank(array,elem)
  print "rank of {0} is {1}".format(elem,r)
  assert(testcase.getRankOfNumber(elem)==r)
print "test passed"