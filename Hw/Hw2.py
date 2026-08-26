class Person:
    def __init__(self, name, birth_date, profession):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я родился {self.birth_date}, "
            f"работаю {self.profession}"
        )


class Classmate(Person):
    def __init__(self, name, birth_date, profession, group_name):
        super().__init__(name, birth_date, profession)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я одноклассник Байэля, "
            f"я родился {self.birth_date}, "
            f"работаю {self.profession}, "
            f"учусь в группе {self.group_name}"
        )


class Friend(Person):
    def __init__(self, name, birth_date, profession, hobby):
        super().__init__(name, birth_date, profession)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я друг Байэля, "
            f"я родился {self.birth_date}, "
            f"работаю {self.profession}, "
            f"моё хобби — {self.hobby}"
        )



classmate1 = Classmate(
    "Бектур",
    "5.12.2000",
    "программистом",
    "ИТ-21"
)

classmate2 = Classmate(
    "Айбек",
    "10.03.2001",
    "дизайнером",
    "ИТ-21"
)


friend1 = Friend(
    "Алмаз",
    "5.12.2000",
    "программистом",
    "футбол"
)

friend2 = Friend(
    "Нурсултан",
    "20.07.2000",
    "врачом",
    "музыка"
)


classmate1.introduce()
classmate2.introduce()

friend1.introduce()
friend2.introduce()
