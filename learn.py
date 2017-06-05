def create_multiple():
    return [lambda x: x * i for i in range(5)]


for multiple in create_multiple():
    print(multiple(2))
