class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def __str__(self):
        return f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, высшего образования {self.higher_education}"


Man_1 = Person(name="Nurlan",birth_date="26.09.2010",occupation="программист",higher_education="нет")
Man_2 = Person(name="Azamat",birth_date="15.04.2005",occupation="врач",higher_education="есть")
Man_3 = Person(name="Aibek",birth_date="08.12.2008",occupation="дизайнер",higher_education="нет")
Man_4 = Person(name="Bekzat",birth_date="21.07.2002",occupation="инженер",higher_education="есть")
Man_5 = Person(name="Timur",birth_date="03.02.2012",occupation="ученик",higher_education="нет")


print(Man_1)
print(Man_2)
print(Man_3)
print(Man_4)
print(Man_5)
