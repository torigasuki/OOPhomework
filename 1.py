class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("동물의 울음소리")
        
class Dog(Animal):
    def speak(self):
        print("멍멍")
        
class Cat(Animal):
    def speak(self):
        print(self.name)
        print(self.age)
        print("야옹")
        
        
class Shape():
    def get_area(self):
        print('도형의 면적')
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        self.area = 3.14*self.radius**2
        print(self.area)
        
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def get_area(self):
        self.area = self.width*self.height
        print(self.area)



class Car():
    def __init__(self,model,color,speed):
        self.model = model
        self.color = color
        self.speed = speed
    def accelerate(self):
        self.speed += 10
        
    def slowdown(self):
        self.speed -= 10
        
    def get_speed(self):
        return self.speed
    