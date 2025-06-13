def fizz_buzz(n):
  """
  Печатает числа от 1 до n, заменяя кратные 3 на "Fizz", кратные 5 на "Buzz" и кратные 3 и 5 на "FizzBuzz".

  Args:
    n: Целое число, до которого нужно печатать.
  """
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

# Пример использования:
fizz_buzz(17)