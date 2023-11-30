class Group_1012:
    def __init__(self, name, gen, age, evarage_mark):
        self.name = name
        self.gen = gen
        self.age = age
        self.evarage_mark = evarage_mark
        self.age += 1
    def study(self):
        print("гарно вчуся")
        if self.evarage_mark < 12:
            self.evarage_mark += 0.1
        else:
            print("Оцінку немає куди підвищувати")


student1 = Group_1012("Гончарук Олександр", "чол", 12, 12)
student2 = Group_1012("Трофимишин Владислав", "чол", 13,12)
student3 = Group_1012("Коваленко Макар", "чол", 13, 10)
student4 = Group_1012("Радомська Дарина",  "жін.",  13,  11)
student5 = Group_1012("Юраш Максим", "чол", 14, 10)
print("середні оцінки Владислава", student2.evarage_mark)
print("середні оцінки Владислава", student2.evarage_mark)
