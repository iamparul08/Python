class Class1:
    def __init__(self):
        self.a = 1
        self.b = 11

    def showdata(self):
        print(self.a, self.b)

class Class2(Class1):
    def __init__(self):
        self.c = 2
        self.d = 22
        super().__init__() #calling parent constructor

    def showdata(self):
        print(self.c, self.d)


class Class4:
    def __init__(self):
        self.g = 4
        self.h = 44

    def showdata(self):
        print(self.g, self.h)

class Class3(Class2, Class4):
    def __init__(self):
        self.e = 3
        self.f = 33
        super().__init__()

    def showdata(self):
        print(self.e, self.f)

ob1 = Class1() #ob created for class1
ob2 = Class2() #for class 2
ob3 = Class3() #for class 3
ob4 = Class4() #for class4

ob1.showdata() #1 11
ob2.showdata() #2 22
ob3.showdata() #3 33
ob4.showdata() #4 44

Class1.showdata(ob2) #1 11
Class2.showdata(ob3) #2 22
