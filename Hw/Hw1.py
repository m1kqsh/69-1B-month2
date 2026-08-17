class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def __str__(self):
        return f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, высшего образования {self.higher_education}"


Man_1 = Person(name="Nurlan",birth_date="26.09.2010",occupation="программист",higher_education="нет")

print(Man_1)