import itertools


# Арифметична прогресія
def arithmetic_progression(start, step):
    number = start

    while True:
        yield number
        number += step


# Геометрична прогресія
def geometric_progression(start, ratio, limit=float("inf")):
    number = start

    while number <= limit:
        yield number
        number *= ratio


# Числа Фібоначчі
def fibonacci(n=None):
    a = 0
    b = 1
    count = 0

    while n is None or count < n:
        yield a
        a, b = b, a + b
        count += 1


# Послідовність Коллатца
def collatz_sequence(n):
    while n > 0:
        yield n

        if n == 1:
            break

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


# Розгортання вкладених списків
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def main():
    # Арифметична прогресія
    ap = arithmetic_progression(2, 3)
    first_10 = list(itertools.islice(ap, 10))
    print("Арифметична прогресія:", first_10)

    # Геометрична прогресія
    gp = list(geometric_progression(1, 2, 1000))
    print("\nГеометрична прогресія:", gp)

    # Фібоначчі
    fib = list(fibonacci(15))
    print("\nЧисла Фібоначчі:", fib)

    # Коллатц
    coll = list(collatz_sequence(27))
    print("\nКоллатц (27):")
    print("Довжина:", len(coll))
    print("Максимальне число:", max(coll))

    # Вкладені списки
    nested = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
    flat = list(flatten(nested))

    print("\nРозгорнутий список:", flat)

    # Перше число Фібоначчі більше 10000
    for number in fibonacci(None):
        if number > 10000:
            print("\nПерше число Фібоначчі > 10000:", number)
            break


if __name__ == "__main__":
    main()

