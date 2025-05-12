#=================
# INDEX OF DESIGN PATTERNS
#=================

# CREATIONAL PATTERNS:
# 1. Factory Design Pattern
# 2. Abstract Factory Design Pattern
# 3. Singleton Design Pattern
# 4. Builder Design Pattern
# 5. Prototype Design Pattern

# STRUCTURAL PATTERNS:
# 6. Adapter Design Pattern
# 7. Bridge Design Pattern
# 8. Composite Design Pattern
# 9. Decorator Design Pattern
# 10. Facade Design Pattern
# 11. Flyweight Design Pattern
# 12. Proxy Design Pattern

# BEHAVIORAL PATTERNS:
# 13. Chain of Responsibility Pattern
# 14. Command Pattern
# 15. Interpreter Pattern
# 16. Iterator Pattern
# 17. Mediator Pattern
# 18. Memento Pattern
# 19. Observer Pattern
# 20. State Pattern
# 21. Strategy Pattern
# 22. Template Method Pattern
# 23. Visitor Pattern


#=================
#=================
# Factory Design Pattern
#=================
#=================

class FrenchLocalizer:

    """ it simply returns the french version """

    def __init__(self):

        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg

def Factory(language ="English"):

    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()

f = Factory("French")
e = Factory("English")
s = Factory("Spanish")

message = ["car", "bike", "cycle"]

for msg in message:
    print(f.localize(msg))
    print(e.localize(msg))
    print(s.localize(msg))


#=================
#=================
# Abstract Factory Design Pattern
#=================
#=================

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

class WinButton(Button):
    def paint(self):
        return "Rendering Windows button"

class MacButton(Button):
    def paint(self):
        return "Rendering Mac button"

class WinCheckbox(Checkbox):
    def check(self):
        return "Checking Windows checkbox"

class MacCheckbox(Checkbox):
    def check(self):
        return "Checking Mac checkbox"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

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
            cls._instance.value = "Initial Value"
        return cls._instance

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

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

    def show(self):
        return f"Car with parts: {', '.join(self.parts)}"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_engine(self):
        self.car.add("Engine")
        return self

    def add_wheels(self):
        self.car.add("Wheels")
        return self

    def add_body(self):
        self.car.add("Body")
        return self

    def add_airbags(self):
        self.car.add("Airbags")
        return self

    def build(self):
        return self.car

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_sports_car(self):
        return self.builder.add_engine().add_body().add_wheels().add_airbags().build()

#=================
#=================
# Prototype Design Pattern
#=================
#=================

import copy

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        return f"Drawing Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        return f"Drawing Rectangle with width {self.width} and height {self.height}"

class ShapeRegistry:
    def __init__(self):
        self._shapes = {}

    def register(self, name, shape):
        self._shapes[name] = shape

    def get_clone(self, name):
        shape = self._shapes.get(name)
        return shape.clone() if shape else None

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

class Laptop:
    def __init__(self, socket):
        self.socket = socket

    def charge(self):
        v = self.socket.voltage()
        if v == 120:
            return "Charging..."
        else:
            return "Cannot charge: Incompatible voltage"


#=================
#=================
# Bridge Design Pattern
#=================
#=================

class Device(ABC):
    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

class TV(Device):
    def __init__(self):
        self._on = False

    def is_enabled(self):
        return self._on

    def enable(self):
        self._on = True

    def disable(self):
        self._on = False

class Remote:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

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
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"Leaf {self.name}"

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite {self.name} contains: " + ", ".join(results)

#=================
#=================
# Decorator Design Pattern
#=================
#=================

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class BasicNotifier(Notifier):
    def send(self, message):
        return f"Sending message: {message}"

class NotifierDecorator(Notifier):
    def __init__(self, wrappee: Notifier):
        self.wrappee = wrappee

    def send(self, message):
        return self.wrappee.send(message)

class SMSDecorator(NotifierDecorator):
    def send(self, message):
        base = super().send(message)
        return f"{base}\nSending SMS: {message}"

class EmailDecorator(NotifierDecorator):
    def send(self, message):
        base = super().send(message)
        return f"{base}\nSending Email: {message}"

class SlackDecorator(NotifierDecorator):
    def send(self, message):
        base = super().send(message)
        return f"{base}\nSending Slack message: {message}"

#=================
#=================
# Facade Design Pattern
#=================
#=================

class CPU:
    def freeze(self):
        return "CPU Freezing..."

    def jump(self, position):
        return f"CPU jumping to position {position}"

    def execute(self):
        return "CPU Executing"

class Memory:
    def load(self, position, data):
        return f"Memory loading data '{data}' at position {position}"

class HardDrive:
    def read(self, lba, size):
        return f"HardDrive reading {size} bytes from {lba}"

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        steps = [
            self.cpu.freeze(),
            self.memory.load("0x00", self.hard_drive.read("100", "512")),
            self.cpu.jump("0x00"),
            self.cpu.execute()
        ]
        return "\n".join(steps)

#=================
#=================
# Flyweight Design Pattern
#=================
#=================

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        return f"Drawing {self.name} tree at ({x}, {y}) with color {self.color}"

class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        return self.tree_type.draw(self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        type_ = TreeFactory.get_tree_type(name, color, texture)
        self.trees.append(Tree(x, y, type_))

    def draw(self):
        return [tree.draw() for tree in self.trees]

#=================
#=================
# Proxy Design Pattern
#=================
#=================

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename} from disk...")

    def display(self):
        return f"Displaying {self.filename}"

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        return self.real_image.display()

#=================
#=================
# Chain of Responsibility Pattern
#=================
#=================

class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass

class AuthHandler(Handler):
    def handle(self, request):
        if request.get("authenticated"):
            return self.next_handler.handle(request) if self.next_handler else "Request handled"
        return "Authentication Failed"

class LogHandler(Handler):
    def handle(self, request):
        print("Logging request...")
        return self.next_handler.handle(request) if self.next_handler else "Request logged"

class DataHandler(Handler):
    def handle(self, request):
        return f"Data processed for {request.get('user')}"

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
        return "Light is ON"

    def off(self):
        return "Light is OFF"

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        return self.light.on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        return self.light.off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        return self.command.execute()


#=================
#=================
# Interpreter Pattern
#=================
#=================

class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class Number(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        return self.number

class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)

#=================
#=================
# Iterator Pattern
#=================
#=================

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class NameIterator(Iterator):
    def __init__(self, names):
        self._names = names
        self._index = 0

    def has_next(self):
        return self._index < len(self._names)

    def next(self):
        if self.has_next():
            name = self._names[self._index]
            self._index += 1
            return name
        raise StopIteration

class NameRepository:
    def __init__(self):
        self.names = ["Alice", "Bob", "Charlie"]

    def get_iterator(self):
        return NameIterator(self.names)

#=================
#=================
# Mediator Pattern
#=================
#=================

class ChatRoom:
    def show_message(self, user, message):
        return f"[{user.name}]: {message}"

class User:
    def __init__(self, name, chatroom: ChatRoom):
        self.name = name
        self.chatroom = chatroom

    def send_message(self, message):
        return self.chatroom.show_message(self, message)


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
        self._state = ""

    def set_state(self, state):
        self._state = state

    def save_state_to_memento(self):
        return Memento(self._state)

    def get_state_from_memento(self, memento):
        self._state = memento.get_state()

    def get_state(self):
        return self._state

class Caretaker:
    def __init__(self):
        self._memento_list = []

    def add(self, state):
        self._memento_list.append(state)

    def get(self, index):
        return self._memento_list[index]

#=================
#=================
# Observer Pattern
#=================
#=================

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(f"{self.name} received update: {state}")

#=================
#=================
# State Pattern
#=================
#=================

class State(ABC):
    @abstractmethod
    def do_action(self, context):
        pass

class StartState(State):
    def do_action(self, context):
        print("Player is in start state")
        context.set_state(self)

    def __str__(self):
        return "Start State"

class StopState(State):
    def do_action(self, context):
        print("Player is in stop state")
        context.set_state(self)

    def __str__(self):
        return "Stop State"

class Context:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state


#=================
#=================
# Strategy Pattern
#=================
#=================

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b

class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class ContextStrategy:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

#=================
#=================
# Template Method Pattern
#=================
#=================

class DataProcessor(ABC):
    def process(self):
        self.read_data()
        self.transform_data()
        self.save_data()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def transform_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading CSV data")

    def transform_data(self):
        print("Transforming CSV data")

    def save_data(self):
        print("Saving CSV data")

class JSONDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading JSON data")

    def transform_data(self):
        print("Transforming JSON data")

    def save_data(self):
        print("Saving JSON data")

#=================
#=================
# Visitor Pattern
#=================
#=================

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Book(Element):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        visitor.visit_book(self)

class Fruit(Element):
    def __init__(self, name, weight, price_per_kg):
        self.name = name
        self.weight = weight
        self.price_per_kg = price_per_kg

    def accept(self, visitor):
        visitor.visit_fruit(self)

class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book: Book):
        pass

    @abstractmethod
    def visit_fruit(self, fruit: Fruit):
        pass

class PriceVisitor(Visitor):
    def visit_book(self, book: Book):
        print(f"Book: {book.title}, Price: ${book.price}")

    def visit_fruit(self, fruit: Fruit):
        cost = fruit.weight * fruit.price_per_kg
        print(f"Fruit: {fruit.name}, Cost: ${cost:.2f}")
