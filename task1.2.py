from collections import namedtuple

# Студент з ім'ям та оцінкою
Student = namedtuple("Student", ["name", "grade"])


# Ітератор для студентів
class StudentGroupIterator:
    def __init__(self, students):
        self._students = students
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration

        student = self._students[self._index]
        self._index += 1
        return student


# Клас студентської групи
class StudentGroup:
    def __init__(self, group_name):
        self._group_name = group_name
        self._students = []

    # Додавання студента
    def add_student(self, name, grade):
        self._students.append(Student(name, grade))

    # Створення нового ітератора
    def __iter__(self):
        return StudentGroupIterator(self._students)

    def __len__(self):
        return len(self._students)

    # Найкращі студенти за оцінками
    def top_students(self, n=3):
        students = sorted(
            self._students,
            key=lambda student: student.grade,
            reverse=True
        )
        return iter(students[:n])


def main():
    # Створення групи
    group = StudentGroup("КІ-21")

    group.add_student("Олена", 95)
    group.add_student("Іван", 78)
    group.add_student("Марія", 92)
    group.add_student("Петро", 85)
    group.add_student("Анна", 88)

    print("Кількість студентів:", len(group))

    # Перший обхід
    print("\nПерший обхід:")
    for student in group:
        print(f"{student.name}: {student.grade}")

    # Другий обхід
    print("\nДругий обхід:")
    for student in group:
        print(f"{student.name}: {student.grade}")

    # Два незалежні ітератори
    iterator1 = iter(group)
    iterator2 = iter(group)

    print("\nПеревірка незалежних ітераторів:")
    print("Перший:", next(iterator1).name)
    print("Перший:", next(iterator1).name)
    print("Другий:", next(iterator2).name)

    # Вкладені цикли
    print("\nВсі пари студентів:")
    for s1 in group:
        for s2 in group:
            if s1.name < s2.name:
                print(f"{s1.name} та {s2.name}")

    # Топ-3 студенти
    print("\nТоп-3 студенти:")
    for student in group.top_students(3):
        print(f"{student.name}: {student.grade}")


if __name__ == "__main__":
    main()

