def searchMinor(arr):
	minor = arr[0]
	minor_idx = 0
	for i in range(1, len(arr)):
		if arr[1] < minor:
			minor = arr[i]
			minor_idx = i
	return minor_idx


def selectedSorted(arr):
	newArr = []
	for i in range(len(arr)):
		minor = searchMinor(arr)
		newArr.append(arr.pop(minor))
	return newArr

print(selectedSorted([6, 8, 3, 10, 2]))
