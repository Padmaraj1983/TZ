from faker import Faker

fakegen=Faker()

def populate(n):
    for i in range(n):
        num=fakegen.random_int(min=1,max=n)
        name=fakegen.name()
        sal=fakegen.random_int()
        print(num,name,sal)

populate(10)