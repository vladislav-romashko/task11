def fib(k):
    """Повертає список перших n чисел Фібоначчі."""
    fibonacci_numbers = [0, 1]

    while len(fibonacci_numbers) < k:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers[:k]


def main():
    try:
        k = int(input("Введіть кількість чисел Фібоначчі (k): "))
        if k <= 0:
            raise ValueError("Кількість чисел повинна бути додатньою.")

        result = fib(k)
        print(f"Перші {k} числа Фібоначчі: {result}")

    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()

