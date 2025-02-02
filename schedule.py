class Teacher:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        email: str,
        can_teach_subjects: set,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()  # Множина призначених предметів

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def create_schedule(subjects: set, teachers: list) -> list:
    """
    Створює розклад занять використовуючи жадібний алгоритм.

    Args:
        subjects: Множина всіх предметів, які потрібно розподілити
        teachers: Список викладачів

    Returns:
        Список викладачів з призначеними предметами або None, якщо неможливо скласти розклад
    """
    remaining_subjects = subjects.copy()
    selected_teachers = []

    while remaining_subjects:
        # Знаходимо викладача, який може викладати найбільше з предметів, що залишились
        best_teacher = None
        max_subjects = 0

        for teacher in teachers:
            # Перевіряємо, скільки нерозподілених предметів може викладати цей викладач
            can_teach = len(teacher.can_teach_subjects.intersection(remaining_subjects))

            if can_teach > max_subjects:
                best_teacher = teacher
                max_subjects = can_teach
            elif can_teach == max_subjects and can_teach > 0:
                # Якщо можуть викладати однакову кількість предметів, обираємо молодшого
                if best_teacher is None or teacher.age < best_teacher.age:
                    best_teacher = teacher

        if best_teacher is None:
            # Якщо не знайшли викладача для предметів, що залишились
            return None

        # Призначаємо предмети вибраному викладачу
        subjects_to_assign = best_teacher.can_teach_subjects.intersection(
            remaining_subjects
        )
        best_teacher.assigned_subjects = subjects_to_assign
        remaining_subjects -= subjects_to_assign

        if subjects_to_assign:  # Додаємо викладача тільки якщо йому призначені предмети
            selected_teachers.append(best_teacher)

    return selected_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
