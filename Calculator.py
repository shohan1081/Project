

class Calculator:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def div(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "Error : Division by zero is not allowed"
        
    
    def mul(self,a,b):
        return a*b
    
    def mod(self,a,b):
        try:
           return a%b
        except ZeroDivisionError:
            return "Error : Modulation by zero is not allowed"
     
        
    
    def __init__(self,n,a,b):
        if n == 1:
            result = self.add(a, b)
            print(f"{a} + {b} = {result}")
        elif n == 2:
            result = self.sub(a, b)
            print(f"{a} - {b} = {result}")
        elif n == 3:
            result = self.mul(a, b)
            print(f"{a} * {b} = {result}")
        elif n == 4:
            result = self.div(a, b)
            print(f"{a} / {b} = {result}")
        elif n == 5:
            result = self.mod(a, b)
            print(f"{a} % {b} = {result}")
        

        
try:
    print("Select operation:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")
    n = int(input("Enter choise(1/2/3/4/5):"))
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    aa = Calculator(n,a,b) 
except ValueError:
    print("Invalid user input !")       
 

