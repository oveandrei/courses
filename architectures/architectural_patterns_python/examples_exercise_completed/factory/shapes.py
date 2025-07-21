# shapes.py
from abc import ABC, abstractmethod
import math

# Abstract base class defining the shape interface
class Shapes(ABC):
    @abstractmethod
    def draw(self, size: int) -> None:
        """
        Abstract draw method to be implemented by all shape subclasses.
        Takes a 'size' parameter (as string, validated before use).
        """
        pass


class Circle(Shapes):    
    def draw(self, size: int) -> None:
        """
        Draws an ASCII representation of a circle based on the given radius.
        Radius is converted from string to integer.
        """
        radius = int(size)
        aspect_ratio = 1  # Adjust this if terminal characters are not square

        for y in range(-radius, radius + 1):
            row = []
            for x in range(-radius, radius + 1):
                # Compensate x to maintain correct aspect in characters
                scaled_x = x * aspect_ratio
                distance = math.sqrt(scaled_x**2 + y**2)
                
                # Draw '*' if the distance is close to the radius (tolerance = 0.8)
                if abs(distance - radius) < 0.8:
                    row.append('*')
                else:
                    row.append(' ')
            print(''.join(row))


class Square(Shapes):
    def draw(self, size: int) -> None:
        """
        Draws an ASCII square of the given size.
        Borders are marked with '*', inside is blank.
        """
        size = int(size)
        for i in range(size):
            if i == 0 or i == size - 1:  # Top and bottom borders
                print('* ' * size)
            else:  # Hollow middle
                print('* ' + '  ' * (size - 2) + '*')


class Triangle(Shapes):
    def draw(self, size: int) -> None:
        """
        Draws a right-aligned triangle of height `size` in ASCII.
        """
        height = int(size)
        for i in range(1, height + 1):
            spaces = ' ' * (height - i)
            stars = '* ' * i
            print(spaces + stars)
