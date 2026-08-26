class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def introduce(self):
        education = (
            "У меня есть высшее образование."
            if self.__higher_education
            else "У меня нет высшего образования."
        )

        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.__occupation}. "
            f"{education}"
        )


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(
            name,
            birth_date,
            occupation,
            higher_education
        )
        self.group_name = group_name

    def introduce(self):
        education = (
            "У меня есть высшее образование."
            if self._Person__higher_education
            else "У меня нет высшего образования."
        )

        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self._Person__occupation}. "
            f"Я учился с Айсулуу в группе {self.group_name}. "
            f"{education}"
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(
            name,
            birth_date,
            occupation,
            higher_education
        )
        self.hobby = hobby

    def introduce(self):
        education = (
            "У меня есть высшее образование."
            if self._Person__higher_education
            else "У меня нет высшего образования."
        )

        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self._Person__occupation}. "
            f"Мое хобби {self.hobby}. "
            f"{education}"
        )



cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl2 = Classmate("Бектур", "15.05.2001", "программист", False, "11D")


fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr2 = Friend("Алмаз", "10.10.2000", "дизайнер", False, "музыка")


cl1.introduce()
cl2.introduce()

fr1.introduce()
fr2.introduce()
