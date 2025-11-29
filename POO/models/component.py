from abc import ABC, abstractmethod

class Component(ABC):
    """
    CRC Card: Component
    Responsibility: Store properties, allow operations (move/rotate), manage points.
    """
    def __init__(self, id, name, x=0, y=0):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.rotation = 0
        self.voltage = 0.0
        self.current = 0.0

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Moved {self.name} to ({self.x}, {self.y})")

    def rotate(self):
        self.rotation = (self.rotation + 90) % 360
        print(f"Rotated {self.name} to {self.rotation}°")

    def rename(self, new_name):
        self.name = new_name

    @abstractmethod
    def get_type(self):
        pass