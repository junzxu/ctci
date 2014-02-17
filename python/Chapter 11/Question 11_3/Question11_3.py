import random

def rotate(array,step):
    """ rotate array to right by step in the argument"""
    for i in range(0,step):
        tmp = array.pop()
        array.insert(0,tmp)

  
def Search(array,value,lo,hi):
    """ check which part of the array is sorted, for sorted part we can just apply binarySearch"""
    if lo >= hi:
      return -1
    mid = lo+(hi-lo)/2
    if array[mid] == value:
        return mid
    if array[lo] < array[mid]:
        if value in range(array[lo],array[mid]):
            return Search(array,value,lo,mid)
        else:
            return Search(array,value,mid+1,hi)
    elif array[lo] > array[mid]:
        if value in range(array[mid],array[hi-1]):
            return Search(array,value,mid+1,hi)
        else:
            return Search(array,value,lo,mid)
    elif array[lo] == array[mid]:
        if array[hi-1] != array[mid]:
            return Search(array,value,mid+1,hi)
        else:
          result = Search(array,value,mid+1,hi)
          if result != -1:
              return result
          else:
            return Search(array,value,lo,mid)

#building testcases
def generateRandomArray(size):
    elem = range(0,10)
    array = []
    for i in range(0,size):
        array.append(random.choice(elem))
    array.sort()
    return array

# gererate 10 random array of length 10, choose 1 random elem from each to search
arrays = []
query = []
for case in range(0,10):
    array = generateRandomArray(10)
    query.append(array[0])
    for i in range(0,random.randint(0, 10)):
        step = random.randint(0, 10)
        rotate(array,step)
    arrays.append(array)

#testing
#find index of minimum element in the array
for i,array in enumerate(arrays):
    q = query[i]
    print array
    print Search(array,q,0,10)
    assert(Search(array,q,0,10) != -1)
print 'all tests passed'