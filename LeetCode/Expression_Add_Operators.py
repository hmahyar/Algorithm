'''

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

'''
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
	
	i = 0
	val = 0
	s, result = [],[]
        while i<len(num):
		val = val*10 + int(num[i])
		s.append(str(val))
		if str(val).startswith('0'):break
		self.expression(0,val,target,s,result,i+1,num)
		s.pop()
		i+=1
	return result

    def expression(self,o1,o2,target,s,result,p,num):
		if p == len(num) and o1+o2 == target:
			result.append(''.join(s))
		else:
			i=p
			val = 0
			val_s = ''
			while i < len(num):
				val = val*10+int(num[i])
			 	val_s = str(val)
				if val == 0:
					#continue 
			        	pass
				s.append('+'+val_s)
				self.expression(o1+o2,val,target,s,result,i+1,num)
				s.pop()
			
				s.append('-'+val_s)
				self.expression(o1+o2,-val,target,s,result,i+1,num)
				s.pop()
			
				s.append('*'+val_s)
				self.expression(o1,o2*val,target,s,result,i+1,num)
				s.pop()
	
				s.append('/'+val_s)
				self.expression(o1,o2/val,target,s,result,i+1,num)
				s.pop()

				i+=1

print Solution().addOperators('122',6)
