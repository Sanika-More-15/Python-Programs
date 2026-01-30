class Circle:
    PI=3.14

    def __init__(self):
        self.Radious=0
        self.Area=0
        self.Circumference=0

    def Accept(self):
        self.Radious=int(input("Enter radious of circle :"))

    def CalculateArea(self):
        self.Area=Circle.PI * self.Radious * self.Radious
        print("Crea of Circle is :",self.Area)

    def CalcucalteCircunferrence(self):
        self.Circumference= 2 * Circle.PI * self.Radious
        print("Circumference of circle is :",self.Circumference)


obj1=Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalcucalteCircunferrence()
