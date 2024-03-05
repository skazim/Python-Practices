class Pet:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def report_pet(self):
        print("Name: ",self.name)

    def check_age(self):
        if(self.age > 5):
            print("Pet need health insurance")
        else:
            print("Pets are in good age")


pet_object1 = Pet("Rover",1)
pet_object2 = Pet("Chower",10)


pet_object1.check_age()
pet_object2.check_age()