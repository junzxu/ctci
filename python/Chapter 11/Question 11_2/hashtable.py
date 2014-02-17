#implementation of the hashmap with double hashing probe
class _MapEntry(object):
	def __init__(self,key,value):
		self.key = key
		self.value = value

class HashMap(object):
	UNUSED = None
	EMPTY = _MapEntry(None,None)

	def __init__(self,size=20):
		self._table = [None]*size
		self._count = 0
		self._maxCount = len(self._table)-len(self._table)//3 #max keys before exceeding load factor

	def __len__(self):
		return self._count

	def __contains__(self,key):
		slot = self._findSlot(key,False)
		return slot is not None

	def has_key(self,key):
		slot = self._findSlot(key,False)
		return slot is not None

	def add(self,key,value):
		if key in self:
			slot = self._findSlot(key,False)
			self._table[slot].value = value
			return False
		else:
			slot = self._findSlot(key,True)
			self._table[slot] = _MapEntry(key,value)
			self._count += 1
			if self._count == self._maxCount:
				self._rehash()
			return True

	def valueOf(self,key):
		slot = self._findSlot(key,False)
		assert slot is not None, "Invalid key"
		return self._table[slot].value

	def remove(self,key):
		assert key in self
		slot = self._findSlot(key,False)
		self._table[slot] = self.EMPTY


	def _findSlot(self,key,forInsert):
		slot = self._hash(key)
		step = self._doublehash(key)

		#probing
		M = len(self._table)
		while self._table[slot] is not None:
			if forInsert and (self._table[slot] is  self.EMPTY):
				return slot
			elif not forInsert and (self._table[slot] is  not self.EMPTY and self._table[slot].key == key):
				return slot
			else:
				slot = (slot+step)%M

		if forInsert and (self._table[slot] is  self.EMPTY or self._table[slot] is None):
			return slot


	def _rehash(self):
		#create a larger table
		origTable = self._table
		newSize = len(self._table)*2 +1
		self._table = [None]*newSize
		self._count = 0
		self._maxCount =  newSize - newSize//3
		for entry in origTable:
			if entry is not None and entry is not self.EMPTY:
				slot = self._findSlot(entry.key,True)
				self._table[slot] = entry
				self._count += 1

	def _hash(self,key):
		return abs(hash(key)) % len(self._table)

	def _doublehash(self,key):
		return 1+abs(hash(key)) % (len(self._table)-2)

	def __getitem__(self,key):
		return self.valueOf(key)

	def __iter__(self):
		return _HashIterator(self)

class _HashIterator(object):
	def __init__(self,hashMap):
		self.hashMap = hashMap
		self._table = hashMap._table
		self._index = 0

	def __iter__(self):
		return self

	def next(self):
		if self._index > len(self._table)-1:
			raise StopIteration
		while self._table[self._index] is None or self._table[self._index] is self.hashMap.EMPTY:
			self._index += 1
			if self._index > len(self._table)-1:
				raise StopIteration
		index = self._index
		self._index += 1
		return self._table[index]
