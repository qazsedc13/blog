def binary_search(list, item):
  # low and high keep track of which part of the list you'll search in.
  # низкий и высокий следите за тем, какую часть списка вы будете искать в.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  # Пока вы не сузили это до одного элемента ...
  while low <= high:
    # ... check the middle element
    # ... проверить средний элемент
    mid = (low + high) // 2
    guess = list[mid]
    # Found the item.
    # Найден предмет.
    if guess == item:
      return mid
    # The guess was too high.
    # Предположение было слишком высоким.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    # Предположение было слишком низким.
    else:
      low = mid + 1

  # Item doesn't exist
  # Элемент не существует
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
# «Нет» означает ноль в Python. Мы используем, чтобы указать, что предмет не был найден.
print(binary_search(my_list, -1)) # => None
