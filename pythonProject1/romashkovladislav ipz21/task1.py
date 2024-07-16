def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_between(a, b):
    if a > b:
        a, b = b, a  # Обміняти значення, якщо a > b

    print(f"Прості числа між {a} та {b}:")
    for num in range(a, b + 1):
        if is_prime(num):
            print(num)

# Зчитуємо введення користувача
a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))

# Виводимо прості числа між a та b
print_primes_between(a, b)

