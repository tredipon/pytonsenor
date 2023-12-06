import random
class Group_1012:
    def __init__(self, name, gen, age, evarage_mark, money, jobs, my_salary):
        self.my_salary = my_salary
        self.jobs = jobs
        self.money = money
        self.name = name
        self.gen = gen
        self.age = age
        self.evarage_mark = evarage_mark

    def study(self):
        print("гарно вчуся")
        if self.evarage_mark < 12:
            self.evarage_mark += 1
            self.age += 1
            self.money -= 1000
        else:
            print("Оцінку немає куди підвищувати")
    def nostudy(self):
        print("погано вчуся")
        if self.evarage_mark > 1:
            self.evarage_mark -= 1
            self.age += 1
            self.money -= 500

        else:
            print("Оцінку немає куди Занижувати")
    def work(self):
        print("Працюю")
        self.money = self.money + (self.my_salary * self.evarage_mark)
        self.age += 1
    def get(self):
        print("Одержую професію")
        if self.age > 18:
            if self.evarage_mark <= 4:
                self.jobs = plant.name
                self.my_salary = plant.salary
                self.age += 1
            if self.evarage_mark > 4:
                self.jobs = accountant.name
                self.my_salary = accountant.salary
                self.age += 1
            if self.evarage_mark > 7:
                self.jobs = programmer.name
                self.my_salary = programmer.salary
                self.age += 1
            if self.evarage_mark == 12:
                self.jobs = own_company.name
                self.my_salary = own_company.salary
                self.age += 1
        else:
            print("Не було отримано роботу за малий вік.")
            self.age += 1
    def nomoney(self):
        print("тратимо гроші")
        self.money -= 20000
        self.age += 1


student1 = Group_1012("Гончарук Олександр", "чол", 12, 10, 3500, "none", 0)
student2 = Group_1012("Трофимишин Владислав", "чол", 13,7, 3500, "none", 0)
student3 = Group_1012("Коваленко Макар", "чол", 13, 6, 3500, "none", 0)
student4 = Group_1012("Радомська Дарина",  "жін.",  13,  9, 3500, "none", 0)
student5 = Group_1012("Юраш Максим", "чол", 14, 11, 3500, "none", 0)

class Job:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

plant = Job("Завод", 150)
accountant = Job("Бугалтер",1000)
programmer = Job("Програміст",5500)
own_company = Job("Своя компанія",11500)

st1 = 0
st2 = 0
st3 = 0
st4 = 0
st5 = 0
for _ in range(60):
    st1 = int(random.randint(1, 5))
    st2 = int(random.randint(1, 5))
    st3 = int(random.randint(1, 5))
    st4 = int(random.randint(1, 5))
    st5 = int(random.randint(1, 5))
    if (st1 == 1):
        student1.study()
        print(student1.gen)
        print(student1.name)
        print(student1.age, "років")
        print("отримує оцінку", student1.evarage_mark)
        print("було витрачено на навчання 1000 й залишилося", student1.money)
    if (st2 == 1):
        student2.study()
        print(student2.gen)
        print(student2.name)
        print(student2.age, "років")
        print("отримує оцінку", student2.evarage_mark)
        print("було витрачено на навчання 1000 й залишилося", student2.money)
    if (st3 == 1):
        student3.study()
        print(student3.gen)
        print(student3.name)
        print(student3.age, "років")
        print("отримує оцінку", student3.evarage_mark)
        print("було витрачено на навчання 1000 й залишилося", student3.money)
    if (st4 == 1):
        student4.study()
        print(student4.gen)
        print(student4.name)
        print(student4.age, "років")
        print("отримує оцінку", student4.evarage_mark)
        print("було витрачено на навчання 1000 й залишилося", student4.money)
    if (st5 == 1):
        student5.study()
        print(student5.gen)
        print(student5.name)
        print(student5.age, "років")
        print("отримує оцінку", student5.evarage_mark)
        print("було витрачено на навчання 1000 й залишилося", student5.money)

    if (st1 == 2):
        student1.nostudy()
        print(student1.gen)
        print(student1.name)
        print(student1.age, "років")
        print("погано вчився й отримав оцінку", student1.evarage_mark)
        print("було витрачено на навчання 500 й залишилося", student1.money)
    if (st2 == 2):
        student2.nostudy()
        print(student2.gen)
        print(student2.name)
        print(student2.age, "років")
        print("погано вчився й отримав оцінку", student2.evarage_mark)
        print("було витрачено на навчання 500 й залишилося", student2.money)
    if (st3 == 2):
        student3.nostudy()
        print(student3.gen)
        print(student3.name)
        print(student3.age, "років")
        print("погано вчився й отримав оцінку", student3.evarage_mark)
        print("було витрачено на навчання 500 й залишилося", student3.money)
    if (st4 == 2):
        student4.nostudy()
        print(student4.gen)
        print(student4.name)
        print(student4.age, "років")
        print("погано вчився й отримав оцінку", student4.evarage_mark)
        print("було витрачено на навчання 500 й залишилося", student4.money)
    if (st5 == 2):
        student5.nostudy()
        print(student5.gen)
        print(student5.name)
        print(student5.age, "років")
        print("погано вчився й отримав оцінку", student5.evarage_mark)
        print("було витрачено на навчання 500 й залишилося", student5.money)

    if (st1 == 3):
        student1.work()
        print(student1.gen)
        print(student1.name)
        print(student1.age, "років")
        print("працював на", student1.jobs)
        print("з оцінкою", student1.evarage_mark)
        print("й заробив гроші тепер в нього", student1.money, "доларів")
    if (st2 == 3):
        student2.work()
        print(student2.gen)
        print(student2.name)
        print(student2.age, "років")
        print("працював на", student2.jobs)
        print("з оцінкою", student2.evarage_mark)
        print("й заробив гроші тепер в нього", student2.money, "доларів")
    if (st3 == 3):
        student3.work()
        print(student3.gen)
        print(student3.name)
        print(student3.age, "років")
        print("працював на", student3.jobs)
        print("з оцінкою", student3.evarage_mark)
        print("й заробив гроші тепер в нього", student3.money, "доларів")
    if (st4 == 3):
        student4.work()
        print(student4.gen)
        print(student4.name)
        print(student4.age, "років")
        print("працював на", student4.jobs)
        print("з оцінкою", student4.evarage_mark)
        print("й заробив гроші тепер в нього", student4.money, "доларів")
    if (st5 == 3):
        student5.work()
        print(student5.gen)
        print(student5.name)
        print(student5.age, "років")
        print("працював на", student5.jobs)
        print("з оцінкою", student5.evarage_mark)
        print("й заробив гроші тепер в нього", student5.money, "доларів")

    if (st1 == 4):
        student1.get()
        print(student1.gen)
        print(student1.name)
        print(student1.age, "років")
        print("отримав професію", student1.jobs)
        print("з оцінкою", student1.evarage_mark)
    if (st2 == 4):
        student2.get()
        print(student2.gen)
        print(student2.name)
        print(student2.age, "років")
        print("отримав професію", student2.jobs)
        print("з оцінкою", student2.evarage_mark)
    if (st3 == 4):
        student3.get()
        print(student3.gen)
        print(student3.name)
        print(student3.age, "років")
        print("отримав професію", student3.jobs)
        print("з оцінкою", student3.evarage_mark)
    if (st4 == 4):
        student4.get()
        print(student4.gen)
        print(student4.name)
        print(student4.age, "років")
        print("отримав професію", student4.jobs)
        print("з оцінкою", student4.evarage_mark)
    if (st5 == 4):
        student5.get()
        print(student5.gen)
        print(student5.name)
        print(student5.age, "років")
        print("отримав професію", student5.jobs)
        print("з оцінкою", student5.evarage_mark)

    if (st1 == 5):
        student1.nomoney()
        print(student1.gen)
        print(student1.name)
        print(student1.age, "років")
        print("потратив багато грошей й в нього залишилося", student1.money, "доларів")
    if (st2 == 5):
        student2.nomoney()
        print(student2.gen)
        print(student2.name)
        print(student2.age, "років")
        print("потратив багато грошей й в нього залишилося", student2.money, "доларів")
    if (st3 == 5):
        student3.nomoney()
        print(student3.gen)
        print(student3.name)
        print(student3.age, "років")
        print("потратив багато грошей й в нього залишилося", student3.money, "доларів")
    if (st4 == 5):
        student4.nomoney()
        print(student4.gen)
        print(student4.name)
        print(student4.age, "років")
        print("потратив багато грошей й в нього залишилося", student4.money, "доларів")
    if (st5 == 5):
        student5.nomoney()
        print(student5.gen)
        print(student5.name)
        print(student5.age, "років")
        print("потратив багато грошей й в нього залишилося", student5.money, "доларів")

print("Досягнення")
print(student1.gen)
print(student1.name)
print(student1.age, "років")
print("заробив за життя", student1.money, "доларів")
print("працюючи на", student1.jobs)
print("з оцінкою", student1.evarage_mark)

print("Досягнення")
print(student2.gen)
print(student2.name)
print(student2.age, "років")
print("заробив за життя", student2.money, "доларів")
print("працюючи на", student2.jobs)
print("з оцінкою", student2.evarage_mark)

print("Досягнення")
print(student3.gen)
print(student3.name)
print(student3.age, "років")
print("заробив за життя", student3.money, "доларів")
print("працюючи на", student3.jobs)
print("з оцінкою", student3.evarage_mark)

print("Досягнення")
print(student4.gen)
print(student4.name)
print(student4.age, "років")
print("заробив за життя", student4.money, "доларів")
print("працюючи на", student4.jobs)
print("з оцінкою", student4.evarage_mark)

print("Досягнення")
print(student5.gen)
print(student5.name)
print(student5.age, "років")
print("заробив за життя", student5.money, "доларів")
print("працюючи на", student5.jobs)
print("з оцінкою", student5.evarage_mark)




