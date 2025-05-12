#single representation Principle

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    def addEntry(self,entry):
        self.count+=1
        self.entries.append(f'{self.count} : {entry}')
    def removeEntry(self,pos):
        self.count-=1
        del self.entries[pos-1]
    def __str__(self):
        return '\n'.join(self.entries)
    '''
    The methods that will voilet SDP

    def savetofile(self):
        pass 
        
    def loadFromFile(self):
        pass
    '''

j = Journal()
j.addEntry("Studied SDP")
j.addEntry("Went to Marine Drive")
j.addEntry("Played Cricket")

print(j)

j.removeEntry(2)

print(j)


#Open Closed Principle

from abc import ABC , abstractmethod
from math import pi

class Shape:
    def __init__(self,type):
        self.type = type
    @abstractmethod
    def calculate_are(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius
    
    def calculate_are(self):
        return pi * self.radius * self.radius 

class Square(Shape):
    def __init__(self, side):
        super().__init__('square')
        self.side = side
    
    def calculate_are(self):
        return self.side * self.side 

class Rectangle(Shape):
    def __init__(self, length , width):
        super().__init__('rectangle')
        self.length = length
        self.width = width
    
    def calculate_are(self):
        return self.length * self.width

r = Circle(10)
print(r.calculate_are())



#Liskov Substitution Principle (LSP) 

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

r = Rectangle(5,10)
print(r.calculate_area())

s = Square(5)
print(s.calculate_area())

#Interface Segritation Principle

from abc import ABC , abstractmethod

class Printer (ABC):
    @abstractmethod
    def printer(self):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class OldMachine(Printer):
    def printer(self):
        print(" It Prints")

class NewMachine(Printer,Scanner,Fax):
    def printer(self):
        print(" It Prints")
    def fax(self):
        print(" It Fax")
    def scan(self):
        print(" It Scan")

machine = OldMachine()

machine.printer()

print("------")

machine2 = NewMachine()

machine2.fax()
machine2.printer()
machine2.scan()


#Dependency Inversion Principle
from abc import ABC , abstractmethod

class DataSource(ABC):
    @abstractmethod
    def get_source(self):
        pass

class Database(DataSource):
    @abstractmethod
    def get_source(self,data):
        return "Data is From Database"
    

class API(DataSource):
    @abstractmethod
    def get_source(self,data):
        return "Data is From API"


class Data:
    def __init__(self,data):
        self.data = data
    
    def get_source(self):
        data = self.data.get_source()
        print(f'Display Data : {data}')
