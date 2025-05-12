#=================
#=================
# Factory Design Pattern
#=================
#=================

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

#=================
#=================
# Abstract Factory Design Pattern
#=================
#=================

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinButton(Button):
    def paint(self):
        return "Rendering Windows button"

class MacButton(Button):
    def paint(self):
        return "Rendering Mac button"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

#=================
#=================
# Singleton Design Pattern
#=================
#=================

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

#=================
#=================
# Builder Design Pattern
#=================
#=================

class Car:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_engine(self):
        self.car.add("Engine")
        return self

    def add_wheels(self):
        self.car.add("Wheels")
        return self

    def build(self):
        return self.car

#=================
#=================
# Prototype Design Pattern
#=================
#=================

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def clone(self, name):
        return copy.deepcopy(self._objects.get(name))

#=================
#=================
# Adapter Design Pattern
#=================
#=================

class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 120

class SocketAdapter:
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def voltage(self):
        return self.european_socket.voltage() / 2

#=================
#=================
# Bridge Design Pattern
#=================
#=================

class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at {x},{y} radius {radius}")

class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

#=================
#=================
# Composite Design Pattern
#=================
#=================

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite({'+'.join(results)})"

#=================
#=================
# Decorator Design Pattern
#=================
#=================

class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

#=================
#=================
# Facade Design Pattern
#=================
#=================

class CPU:
    def freeze(self):
        print("Freezing CPU")

    def jump(self, position):
        print(f"Jumping to {position}")

    def execute(self):
        print("Executing")

class Computer:
    def __init__(self):
        self.cpu = CPU()

    def start(self):
        self.cpu.freeze()
        self.cpu.jump(1000)
        self.cpu.execute()

#=================
#=================
# Flyweight Design Pattern
#=================
#=================

class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class TreeFactory:
    _tree_types = {}

    def get_tree_type(self, name, color):
        key = (name, color)
        if key not in self._tree_types:
            self._tree_types[key] = TreeType(name, color)
        return self._tree_types[key]

#=================
#=================
# Proxy Design Pattern
#=================
#=================

class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load()

    def load(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

#=================
#=================
# Chain of Responsibility Pattern
#=================
#=================

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "Handled by A"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None

#=================
#=================
# Command Pattern
#=================
#=================

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

#=================
#=================
# Interpreter Pattern
#=================
#=================

class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        return self.data in context

#=================
#=================
# Iterator Pattern
#=================
#=================

class NameRepository:
    def __init__(self):
        self.names = ["John", "Jane", "Doe"]

    def __iter__(self):
        return iter(self.names)

#=================
#=================
# Mediator Pattern
#=================
#=================

class ChatRoom:
    def show_message(self, user, message):
        print(f"[{user}] {message}")

class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send(self, message):
        self.chatroom.show_message(self.name, message)

#=================
#=================
# Memento Pattern
#=================
#=================

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()

#=================
#=================
# Observer Pattern
#=================
#=================

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

class ConcreteObserver:
    def update(self, data):
        print(f"Received update: {data}")

#=================
#=================
# State Pattern
#=================
#=================

class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("Handling State A")

class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

#=================
#=================
# Strategy Pattern
#=================
#=================

class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Strategy A")

class ContextStrategy:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()

#=================
#=================
# Template Method Pattern
#=================
#=================

class Game(ABC):
    def play(self):
        self.initialize()
        self.start_play()
        self.end_play()

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def start_play(self):
        pass

    @abstractmethod
    def end_play(self):
        pass

class Football(Game):
    def initialize(self):
        print("Football Game Initialized")

    def start_play(self):
        print("Football Game Started")

    def end_play(self):
        print("Football Game Ended")

#=================
#=================
# Visitor Pattern
#=================
#=================

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        print("Visited A")
