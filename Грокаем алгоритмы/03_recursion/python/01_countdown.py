def countdown(i):
  # base case
  # базовый вариант
  if i <= 0:
    return 0
  # recursive case
  # рекурсивный вариант
  else:
    print(i)
    return countdown(i-1)

countdown(5)
