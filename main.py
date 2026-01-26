from fib_while import fib as fib_while
from fib_for import fib as fib_for
from sum_digits import sum_digits
from is_prime import is_prime

# Проверь свои функции:

# 1. Фибоначчи (while): первые 10 чисел
print("Fib while:", [fib_while(i) for i in range(10)])

# 2. Фибоначчи (for): первые 10 чисел
print("Fib for:", [fib_for(i) for i in range(10)])

# 3. Сумма цифр
print("sum_digits(12345) =", sum_digits(12345))

# 4. Простые числа от 2 до 20
print("Primes:", [n for n in range(2, 21) if is_prime(n)])
