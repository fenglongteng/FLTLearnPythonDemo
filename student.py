import people

class Student(people.People):

    def read_book(self):
        print(self.name,'在读书')

    def go_to_school(self):
        print('我的宝宝要去读书了')