function binarySearch(array, target) {
	let low = 0
	let high = array.length - 1

	while (low <= high) {
		let mid = parseInt((low + high) / 2)
		let guess = array[mid]

		if (guess === target) {
			return mid
		}

		if (guess > target) {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return null
}

const arr = [1, 3, 4, 5, 7, 8, 10, 12, 13, 15]

console.log(binarySearch(arr, 16))
