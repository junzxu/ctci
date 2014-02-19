def search(array,string,lo,hi):
  while lo<hi:
    mid = lo + (hi-lo)/2
    nonEmpty = mid
    if array[mid] == "":
      while nonEmpty <hi and array[nonEmpty]=="":
        nonEmpty += 1
    if array[nonEmpty] == string:
      return nonEmpty
    elif array[nonEmpty]<string:
      lo = nonEmpty+1
    else:
      hi = mid
  return -1

array = ['a','b','','d','','','g','','j','','z']
print array
print search(array,'z',0,11)