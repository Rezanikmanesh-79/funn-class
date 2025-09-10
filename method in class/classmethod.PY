class Person:
    instances = 0
    
    def __init__(self, name):
        self.name = name
        Person.instances += 1

    @classmethod  # این باعث میشه آرگومان اول به جای instance -> کلاس باشه
    def get_count(cls):
        return cls.instances


p1 = Person("Reza")
p2 = Person("Ali")
print(Person.get_count())  # 2
