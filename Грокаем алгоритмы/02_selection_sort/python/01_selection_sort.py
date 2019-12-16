# Finds the smallest value in an array
# Находим наименьшее значение в массиве
def findSmallest(arr):
  # Stores the smallest value
  # Хранит наименьше
  smallest = arr[0]
  # Stores the index of the smallest value
  # Хранит индекс наименьшего значения
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# Sort array
# Сортировка массива
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      # Находим наименьший элемент в массиве и добавляем его в новый массив
      smallest = findSmallest(arr)
      # добавляем наименьшее значение в новый массив, при этом удаляя это 
      # значение из старого, после чего начинаем поиск заново
      newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))
