# Searching a 2D Sorted Matrix

matrix = [[1, 4, 7, 11,15]
	,[2, 5, 8, 12,19]
	,[3, 6, 9, 16,22]
	,[10,13,14,17,24]
	,[18,21,23,26,30]]
def step_wise_search(arr, key):
	X= len(arr)
	Y= len(arr[0])
	if key<arr[0][0] or key>arr[X-1][Y-1]:
		print 'Not Found'
		return (-1,-1)

	x = X-1
	y = 0

	while x>=0 and y<Y:
		print (arr[x][y]),
		if arr[x][y]<key:
			y+=1
		elif arr[x][y]>key:
			x-=1
		else:
			print
			return (x,y)

i,j = step_wise_search(matrix,162)
if (i>-1):
	m = 'We found {0} in {1},{2}'.format(matrix[i][j],i,j)
	print m