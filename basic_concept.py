# About list
about = ['name', 'sex', 'age']
me = ['Yu Mao', 'Male', 21]

about_me = [about, me]

my_name = [name[0] for name in about_me]
print(my_name)

age = map((lambda x: x[2]), about_me)
print(list(age))

