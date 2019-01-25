
# quicksort is a non stable sorting algorithm
# quicksort : average and best: o(nlogn). worst: o(n*n) when array is already sorted. 
# reasons why quicksort is better that merge sort in some cases:
# 1) its space complexity is better than merge sort since its space complexity is o(1) [considering stack space for recusrion worst case
#    is o(n), average is o(logn)] 
# 2) if a randomized version of quicksort is used, the worst case can be avoided by choosing random pivot
# 3) quicksort has better cache locality, i.e, better locality of reference. 

def partition(a, l, h):
	
	i = l
	pivot = a[h]
	for j in range(l, h):
		if(a[j] <= pivot):
			a[i], a[j] = a[j], a[i]
			i += 1

	a[i], a[h] = a[h], a[i]
	return i					

def quicksort(a, l, h):

	if(l < h):

		pivot = partition(a, l, h)

		quicksort(a, pivot + 1, h)
		quicksort(a, l, pivot - 1)
		
if __name__ == '__main__':
	size = int(input('enter the size: '))
	a = list(map(int, input().split()))

	quicksort(a, 0, size - 1)	

	print(a)

