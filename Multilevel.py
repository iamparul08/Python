class Class1:
    def __init__(self):
        self.a = 1
        self.b = 11

    def showData1(self):
        print(self.a, self.b)

class Class2(Class1):
    def __init__(self):
        self.c = 2
        self.d = 22
        super().__init__()

    def showData2(self):
        print(self.c, self.d)

class Class3(Class2):
    def __init__(self):
        self.e = 3
        self.f = 33
        super().__init__()

    def showData3(self):
        print(self.e, self.f)

ob1 = Class1() #object created for Class1
ob2 = Class2() #object created for Class2
ob3 = Class3() #object created for Class3

ob1.showData1() #1 11
ob2.showData2() #2 22
ob3.showData3() #3 33

ob3.showData2() #2 22
ob2.showData1() #1 11

Class1.showData1(ob3) #1 11
Class2.showData1(ob3) #1 11
Class3.showData1(ob3) #1 11

Class2.showData1(ob3) #1 11
Class3.showData2(ob3) #2 22
#Class3.showData2(ob1) #object of child class should be there to access members of parent class(MRT)
Class1.showData1(ob2)# 1 11
Class3.showData2(ob3) # 2 22
Class1.showData1(ob3) # 1 11