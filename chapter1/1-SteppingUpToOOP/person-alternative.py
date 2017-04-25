"""
Alternative implementation of person classer, with data, behavior,
and operator overloading ( not used for object stored persistently)
"""


class Person:
    """
    a general person: data + logic
    """

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return ('<%s => %s : %s, %s>' %
                (self.__class__.__name__, self.name, self.job, self.pay))


class Manager(Person):
    """
    a person with custom raise
    inherits general lastname, str
    """

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, job='Manager')

    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', '22')
    sue = Person("Sue Jones", '23', 47000, 'hardware')
    tom = Manager('Tom Head', '35', 50000)
    print(sue, sue.pay, sue.lastName())
    print(tom)
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)
