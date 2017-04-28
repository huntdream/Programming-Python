# interactive updates

import shelve
from person import Person

fieldnames = ('name', 'age', 'pay', 'job')
maxfield = max(len(item) for item in fieldnames)

db = shelve.open('../1-SteppingUpToOOP/class-shelve')
while True:
    key = input('\nKey? =>')
    if not key:
        break
    if key in db:
        record = db[key]  # update existing record
    else:  # or make/store new record
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tupdate=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
        db[key] = record
db.close()
