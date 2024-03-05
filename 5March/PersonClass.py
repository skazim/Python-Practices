class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def greetMessage(self):
            print(f"Hello my name is {self.name} and I am {self.age} years old")

class Rectangle():
    def __init__(self,width, height):
        self.width = width
        self.height = height
    
    def calculateArea(self):
        area = self.width * self.height
        print(f"Area of Rectangle is {area}")
          
class BankAccount():
     
    def __init__(self, balance):
        self.balance = balance
    
    def depositMoney(self,amount):
        self.balance+=amount

    def withdrawMoney(self,amount):
        self.balance-=amount

    def showbalance(self):
        print(f"Current amount is your account is {self.balance}")



bankObject = BankAccount(1000)

bankObject.showbalance()

bankObject.depositMoney(100)

bankObject.showbalance()

bankObject.withdrawMoney(500)
bankObject.showbalance()


# person_object1 = Person("Kazim",30)
# person_object2 = Person("Hussain", 25)

# person_object1.greetMessage()
# person_object2.greetMessage()