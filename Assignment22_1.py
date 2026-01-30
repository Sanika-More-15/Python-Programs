class Demo:
    value=0

    def __init__(self,no1,no2):
        self.No1=no1
        self.No2=no2

    def Fun(self):
        print("Value of No1 from Fun() :",self.No1)
        print("Value of No2 from Fun() :",self.No2)

    def Gun(self):
        print("Value of No1 from Gun() :",self.No1)
        print("Value of No2 from Gun() :",self.No2)

obj1=Demo(11,21)
obj2=Demo(51,101)

obj1.Fun()
obj2.Gun()

obj1.Gun()
obj2.Fun()