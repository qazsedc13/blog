def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
	# базовый случай, массивы с 0 или 1 элементом уже "отсортированы"
    return array
  else:
    # recursive case
	# рекурсивный случай
    pivot = array[0]
    # sub-array of all the elements less than the pivot
	# вложенный массив всех элементов меньше, чем pivot
    less = [i for i in array[1:] if i <= pivot]
    # вложенный массив всех элементов больше, чем pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
