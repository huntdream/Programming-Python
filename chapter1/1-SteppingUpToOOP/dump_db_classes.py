import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key])
db.close()
