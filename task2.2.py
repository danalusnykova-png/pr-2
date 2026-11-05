from collections import defaultdict

# Дані студентів
SAMPLE_DATA = [
    "Настя,Математика,95",
    "Іван,Математика,78",
    "",
    "Дана,Фізика,92",
    "Петя,Математика,INVALID",
    "Анна,Фізика,88",
    "Настя,Фізика,90",
    "Іван,Програмування,85",
    "Дана,Програмування,91",
    "Петя,Фізика,76",
    "Анна,Математика,93",
    "Настя,Програмування,97",
    "",
    "Дана,Математика,89",
    "Іван,Фізика,72",
    "Петя,Програмування,80",
    "Анна,Програмування,86"
]


# Отримання записів
def data_source(records):
    for record in records:
        yield record


# Видалення порожніх рядків
def filter_empty(records):
    for record in records:
        if record.strip():
            yield record


# Перетворення записів у словники
def parse_records(records):
    for record in records:
        parts = record.split(",")

        if len(parts) != 3:
            continue

        try:
            grade = int(parts[2])
        except ValueError:
            continue

        yield {
            "student": parts[0],
            "subject": parts[1],
            "grade": grade
        }


# Відбір студентів за оцінками
def filter_passed(records, min_grade=60):
    for record in records:
        if record["grade"] >= min_grade:
            yield record


# Форматування результатів
def format_output(records):
    for record in records:
        yield f'[{record["subject"]}] {record["student"]}: {record["grade"]} балів'


# Обчислення суми та кількості оцінок
def aggregate_subjects(records):
    subject_grades = defaultdict(lambda: {"sum": 0, "count": 0})

    for record in records:
        subject = record["subject"]
        subject_grades[subject]["sum"] += record["grade"]
        subject_grades[subject]["count"] += 1

    for subject, grades in sorted(subject_grades.items()):
        average = grades["sum"] / grades["count"]
        yield f'{subject}: {average:.1f} (з {grades["count"]} оцінок)'


def main():
    # Перший конвеєр
    pipeline = format_output(
        filter_passed(
            parse_records(
                filter_empty(
                    data_source(SAMPLE_DATA)
                )
            ),
            min_grade=75
        )
    )

    print("=== Результати (від 75 балів) ===")

    for line in pipeline:
        print(line)

    # Другий конвеєр
    pipeline_avg = aggregate_subjects(
        parse_records(
            filter_empty(
                data_source(SAMPLE_DATA)
            )
        )
    )

    print("\n=== Середній бал по предметах ===")

    for line in pipeline_avg:
        print(line)


if __name__ == "__main__":
    main()

