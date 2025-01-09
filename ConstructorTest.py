class Calculator:
    class_variable=20
    #def __init__(self):
        #print("I'm a default onstructor")
    def __init__(self, a,b):
        self.a= a
        self.b=b
    def add_number(self):
        #return self.a+self.b + self.class_variable
        return self.a + self.b + Calculator.class_variable

obj = Calculator(a = 10, b = 5)
print(obj.add_number())
#obj.add_number(a = 10, b = 5)
#print("addition is ", addition)