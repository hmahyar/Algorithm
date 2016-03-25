# Searching a 2D Sorted Matrix

a = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,15,24],[18,21,23,26,30]]
def search(arr, key):
	n= len(arr)
	m= len(arr[0])
	if key<arr[0][0] or key>arr[n-1][m-1]:
		return 'Not Found'

print search(a,32)