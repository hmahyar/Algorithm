class RollingHash:
	def __init__(self, string, size):
		self.str  = string
		self.hash = 0
		self.prime_numner = 3
		for i in xrange(0, size):
			self.hash += ord(self.str[i])*(self.prime_numner**i)

		self.init = 0
		self.end  = size
		self.patern_size = size-1
		
	def update(self):
		if self.end <= len(self.str) -1:
			self.hash  = (self.hash - ord(self.str[self.init]))/self.prime_numner 
			self.hash += ord(self.str[self.end])*(self.prime_numner**self.patern_size)
			self.init += 1
			self.end  += 1
			
	def digest(self):
		return self.hash

	def text(self):
		return self.str[self.init:self.end]



def rabin_karp(substring, string):
	result = []
	if substring == None or string == None:
		return result
	if substring == "" or string == "":
		return result

	if len(substring) > len(string):
		return result

	hs 	 = RollingHash(string, len(substring))
	hsub = RollingHash(substring, len(substring))

		
	for i in range(len(string)-len(substring)+1):						
		if hs.digest() == hsub.digest():
			if hs.text() == substring:
				result.append(i)
		hs.update()
	return result
print rabin_karp('AB','ABACAB')