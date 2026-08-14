class User:
    # атрибуты
    user_count = 0
    default_pssword = "123456"
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.password = User.default_pssword
        self.role = "user"
        User.user_count += 1

    def change_password(self, new_password):
        self.password = new_password

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @classmethod
    def creater_admin(cls, name, phone_number):
        # альтернативный конструктор
        obj = User(name, phone_number)
        obj.role = "admin"
        obj.change_password("useradmin5656")
        return obj


user1 = User(name="login", phone_number="9965091000926")
print(user1.name, user1.phone_number)
print(User.get_user_count())
user2 = User(name="Imran", phone_number="996509100926")
print(user2.name, user1.phone_number)
print(User.get_user_count())

