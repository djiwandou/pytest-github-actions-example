class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def is_adult(self):
        return self.age >= 18