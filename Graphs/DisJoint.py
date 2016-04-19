class DisJoint(object):
	def __init__(self,N):
		self.id = range(N)
		self.rank= [0]* N
		self.count = N    
		self.N = N    
	def find(self,p):
		if isinstance(p,int) and p<self.N:
			id =self.id
			while id[p]!=p:
				p = id[p]
			return p

	def Union(self,a,b):
		_a = self.find(a)
		_b = self.find(b)
		print _a,_b,
		if _a == _b:
			return _a
		if self.rank[_a]>self.rank[_b]:
			self.id[_b] = _a	 
		else:
			self.id[_a] = _b
			if self.rank[_b] == self.rank[_a]:
				self.rank[_b]+=1
		print self.rank, self.id
d = DisJoint(12)
for i in range(11):
	d.Union(i,i+1)
