

class phone:

    def set_color(self , color):
        self.color = color
    
    def set_cost(self , cost):
        self.cost = cost
    
    def showColor(self ):
        return self.color
    
    def showCost(self ):
        return self.cost
    
    def make_call(self):
        print("makeing phone call")
    
    def playGame(self):
        print("Playing game")


person1 = phone()

person1.set_color('green')
clr = person1.showColor()
print(clr)

person1.set_cost(20000)
price = person1.showCost()
print(price)

person1.make_call()
person1.playGame()


class employes:
    def __init__(self,name,age,salery,gender):
        self.name = name
        self.age = age
        self.salery = salery
        self.gender = gender
    
    def emploY_details(self):
        print("Name: ",self.name)
        print("Age",self.age)
        print("Gender",self.gender)
        print("Salery: ",self.salery)

e1 = employes("Akash" , 19 , 0, "Male")

e1.emploY_details()


class veichel:
    def __init__( self , milage , cost ):
        self.milage = milage
        self.cost = cost

    def showDetails(self):
        print("Vehicle milage is", self.milage)
        print("Vehicle cost is", self.cost)

v1 = veichel(300,156700)
v1.showDetails()

class car(veichel):
    def schowCarDetails(self):
        print("i am a car")


car1 = car(200,10)

car1.schowCarDetails()
car1.showDetails()


