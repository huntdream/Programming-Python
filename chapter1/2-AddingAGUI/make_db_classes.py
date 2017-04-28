import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 3000, 'software')
sue = Person('Sue Jones', 43, 3500, 'hardware')
tom = Manager('Tom Kim', 35, 5000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
