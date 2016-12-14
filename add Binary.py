'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''





class Solution(object):
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		r,v,c = '',0,0
		for i in xrange(0,max(len(a),len(b))):
			if i<len(a): v += int(a[-(i+1)])
			if i<len(b): v += int(b[-(i+1)])
			v,c = v%2 , v//2 
			r+=str(v)
			v=c
		if c!=0:
			return (r+str(v))[::-1]
		return r[::-1]
