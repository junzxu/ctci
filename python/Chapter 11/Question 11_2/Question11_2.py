from hashtable import HashMap
from random import *
from itertools import permutations

def sortAnagram(array):
  anagramHash = HashMap()
  for string in array:
    sortedString = [c for c in string]
    sortedString.sort()
    sortedString = "".join(sortedString)
    if anagramHash.has_key(sortedString):
      anagrams = anagramHash[sortedString]
      anagrams.append(string)
    else:
      anagramHash.add(sortedString,[string])
  array = []
  for entry in anagramHash:
    for string in entry.value:
      array.append(string)
  return array



#building testcases
def make_random_anagram(length):
  letters = range(ord('a'),ord('z')+1)
  letters = [chr(elem) for elem in letters]
  string = ''
  for i in range(0,length):
    c = choice(letters)
    string += c
  anagrams = list(map("".join, permutations(string)))
  index = randint(0,len(string)-1)
  anagram = anagrams[-index]
  return (string,anagram)

def make_anagram_array():
  array = []
  for i in range(0,5):
    anagrams = make_random_anagram(randint(3,6))
    array.append(anagrams[0])
    array.append(anagrams[1])
  array.sort(key=lambda x:hash(x))


#testing
for i in range(0,10):
  array = make_anagram_array()
  result = sortAnagram(array)
  print array
  print result
  assert(array.sort()==result.sort())
print 'passed all tests'