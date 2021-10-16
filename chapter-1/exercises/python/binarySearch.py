def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

def createList(r1, r2):
    return list(range(r1, r2+1))

my_list = createList(0, 128)

print(binary_search(my_list, -2))
