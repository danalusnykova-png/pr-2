# Власний ітератор CyclicRange

class CyclicRange:
    def __init__(self, start, stop, step=1, repeats=1):
        if step <= 0:
            raise ValueError("Крок повинен бути більше нуля")

        self._start = start
        self._stop = stop
        self._step = step
        self._repeats = repeats

        self._current = start
        self._cycle = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Перевірка завершення
        if self._cycle >= self._repeats or self._start >= self._stop:
            raise StopIteration

        # Поточне число
        number = self._current
        self._current += self._step

        # Перехід до наступного циклу
        if self._current >= self._stop:
            self._current = self._start
            self._cycle += 1

        return number


def main():
    print("CyclicRange(1, 4, repeats=3):")

    for num in CyclicRange(1, 4, repeats=3):
        print(num, end=" ")

    print()

    print("\nCyclicRange(0, 10, step=3, repeats=2):")

    for num in CyclicRange(0, 10, step=3, repeats=2):
        print(num, end=" ")

    print()

    # Перетворення в список
    result = list(CyclicRange(5, 8, repeats=2))
    print("\nЯк список:", result)

    # Сума елементів
    total = sum(CyclicRange(1, 5, repeats=2))
    print("Сума CyclicRange(1, 5, repeats=2):", total)


if __name__ == "__main__":
    main()

