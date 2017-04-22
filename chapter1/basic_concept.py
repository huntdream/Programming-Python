# About list
about = ['name', 'sex', 'age']
me = ['Yu Mao', 'Male', 21]

about_me = [about, me]

my_name = [name[0] for name in about_me]
print(my_name)

age = map((lambda x: x[2]), about_me)
print(list(age))

about_me.append(['You', 'And', 'Me'])

print(len(about_me))

name, sex, age = range(3)

print(me[name], me[sex], me[age])

# Dictionaries
me2 = {'name': 'Yu Mao', 'sex': 'Male', 'age': '21'}
you = dict(name='Life', sex='Dream', age='Future')
nothing = {}
nothing['You'] = 'Nothing'
nothing['And'] = 'Is'
nothing['Me'] = "True"

print(you, me, nothing, sep='\n')

print(list(zip(about, me)))
print(dict(zip(about, me)))

fields = ['name', 'sex', 'age']
record = dict.fromkeys(fields, '?')
print(record)

yumao = {
    'name': {"first": 'Yu', 'last': 'Mao'},
    'age': 21,
    'job': ['Student', 'Front End Programmer']
}
print(yumao['name'])
