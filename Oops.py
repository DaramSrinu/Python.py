#OOPS
class student:
    id=10
    name="Srinu"
    def display(self):
        print(self.id,self.name)
s=student()
s.display()

print()

#Default Constructor
class student:
    count=0
    def __init__(self):
        print("Non parametrized constructor")
    def display(self,name):
        print("Name",name)
s=student()
s.display("Srinu")

print()

#Parametrized Constructor
class student:
    #count=0
    def __init__(self,id,name):
        self.id=id
        self.name=name
        #student.count=student.count+1
    def display(self):
        print("Id & Name",self.id,self.name)
s=student(21,"Srinu")
s1=student(20,"Vamsi")
s.display()
s1.display()
#print("No of Students",student.count)

print()

#Encapsulation And Abstraction
class student:
    def __init__(self):
        self.__id=5
    def display(self):
        print("Id",self.__id)

  #  def setID(self,id):
   #     self.__id=id
s=student()
s1=student()
s1.__id=10  #same wii come no change we use set methods for change
#s1.setID(10)
s.display()
s1.display()

print()

#Inheritance
class Animal:   #multilevelInheritance
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is speaking")

class ChildDog(Dog):
    def eat(self):
        print("Child Dog is eating")

d=ChildDog()
d.speak()
d.bark()
d.eat()

print()

#Normal Inheritance
class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is speaking")

d=Dog()
d.speak()
d.bark()

print()

class Animal:   #multipleInheritance
    def speak(self):
        print("Animal is speaking")

class Dog:
    def bark(self):
        print("Dog is speaking")

class ChildDog(Animal,Dog):
    def eat(self):
        print("Child Dog is eating")

d=ChildDog()
d.speak()
d.bark()

print()

#Polymorphism
class Animal:   #MethodOverRidding
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def speak(self):
        print("Dog is speaking")

class Cat(Animal):
    def speak(self):
        print("Cat is speaking")

d=Cat()
d.speak()

print()

#Some More Functions
class RBI:
    def getRoi(self):
        return 10

class SBI:                #(RBI) remove means answer will be change
    def getRoi(self):
        return 7

class HDFC(RBI):
    def getRoi(self):
        return 8

d = RBI()
d.getRoi()
print(issubclass(SBI,RBI))
print(isinstance(d,SBI))


#Oops Assignment
class Area:
    def area1(self):
        AreaofRectangle=self.length * self.breadth
        print(AreaofRectangle)
class Area2:
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height

    def area1(self):
        triangle=0.5*self.breadth*self.height
        print("Area of triangle",triangle)

    def volume(self):
        volume=self.length*self.breadth*self.height
        print("Volume Of Rectangle",volume)

a=Area2(5,10,15)
a.area1()
a.volume()

#OOPS
id = 1
colour = "red"
capacity = 1
height = 10

def wash():
    print("washing")

def setCap():
    print('setCap')

def fillWater():
    print('fill water')

class bottle:
    # Attributes(properties/state)
    #Functions(Methods/Behavior)
    # static/class variable
    companyName = "Sirpa"
    id = 1
    colour = "red"
    capacity = 1
    height = 10

# Default Constructor
    def __init__(self):
        print('constructor')

    def wash(info):  # self not there means
        print(info)  # self manditary
        print("washing")

    def setCap(self):
        print('setCap')

    def fillWater(self):
        print('fill water')

# object Creation
bottle1 = bottle()
print(bottle1)
print(bottle1.colour)
bottle1.wash()

print()

class Bottle:
    # Attributes(properties/state)
    #Functions(Methods/Behavior)
    # static/class variable
    companyName = "Sirpa"
    id = 1
    colour = "red"
    capacity = 1
    height = 10

# Parameterized Constructor
    def __init__(self, colour, capacity):
        #self._colour=colour  using underscore(_) is turn to protected
        #self.__colour=colour using double underscore(__) is turn to private
        self.colour = colour
        self.capacity = capacity
        print('constructor')
    '''
#destructor
    def __del__(self):
        print('destructor')'''

    # functions/behaviour
    def wash(self):  # self not there means
        print(self)  # self manditary
        print("washing")  #self._wash,#self.__wash

    def setCap(self):
        print('setCap')

    def fillWater(self):
        print('fill water')


# object Creation
print(Bottle.companyName)
print(Bottle.colour)
Things = Bottle("green", 2)
Things1 = Bottle("pink", 3)
Things2 = Bottle("blue", 4)
print(Things)
print(Things.colour)   #
print(Things.capacity)
Things.wash()  # Takes 0 positional but 1 was given

print("========Child class Creation=======")

#Inheritance
class CopperBottle(Bottle):

   def morningWater(self):
       print('morningWater')

print(CopperBottle.companyName)
copper1 = CopperBottle("Yellow",5)
copper1.wash()

print()

class CopperBottle(Bottle):

   def __init__(self):
        print("child construtor")
   def morningWater(self):
       print('morningWater')

print(CopperBottle.companyName)
copper1 = CopperBottle()
copper1.wash()
#Object is the top class

class CopperBottle(Bottle):

   def __init__(self,colour,capacity):
       #Bottle.__init__(self,colour,capacity)
       #super().__init__(colour,capacity)
       print("child construtor")
   def morningWater(self):
       print('morningWater') #self._colour,#self.__colour

#method overriding
#   def setCap(self):
#      print('CopperBottle setCap')

print(CopperBottle.companyName)
copper1 = CopperBottle("Yellow",5)
copper1.wash()
print(Bottle.__bases__)   #parent of any class
print(CopperBottle.__bases__)
copper1.morningWater()
#copper1.setCap()

#Types of Inheritence
class Class1:
    def join(self):
        print('joined')

class Class2(Class1):
    def Subscribe(self):
        print('subscribed')

class Class3(Class2):
    def comment(self):
        print("commited")

cl3=Class3()
cl3.join()
cl3.Subscribe()
cl3.comment()

print()










