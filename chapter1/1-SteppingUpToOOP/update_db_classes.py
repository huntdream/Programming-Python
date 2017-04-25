import shelve

db = shelve.open('class-shelve')
tom = db['tom']
tom.giveRaise(0.5)
db['tom'] = tom

print(tom)
