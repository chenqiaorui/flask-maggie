class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('正在学习%s' % course_name)


if __name__ == '__main__':
    stu = Student('ricky', 12)
    stu.study('java')
    print(stu.name)
    print(stu.age)
