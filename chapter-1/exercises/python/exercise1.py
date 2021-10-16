Vector = list[str]

def binary_search(list: Vector, item: str):
	low = 0
	high = len(list) - 1
	counter = 0

	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]
		if guess == item:
			counter = counter + 1
			return counter
		if guess > item:
			counter = counter + 1
			high = mid - 1
		else:
			counter = counter + 1
			low = mid + 1
	return None

list_names = ['Jon', 'Bill', 'Maria', 'Jenny', 'Jack', 'Mary', 'Silver', 'Rob', 'Jason', 'Robisson']


print(binary_search(list_names, 'Jon'))
