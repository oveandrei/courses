'''sys'''

import sys

# Command-line arguments
print(sys.argv) # List of args passed to the script (first is script name)

# Exit the program
if '--exit' in sys.argv:
    sys.exit("Exiting program...")

# Show Python version
print(sys.version)

# Modify import path at runtime
sys.path.append("/my/custom/modules") # Adds a new path for module search


'''argparse'''

import argparse

parser = argparse.ArgumentParser(description='Example CLI app')
parser.add_argument('--name', type=str, help='Your name')
args = parser.parse_args()

print(f"Hello, {args.name}!")


'''contextlib'''

from contextlib import contextmanager

# Custom context manager
@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

with open_file('sample.txt') as f:
    f.write('Hello with context!')


'''abc'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# a = Animal() # TypeError: Can't instantiate abstract class
d = Dog()
print(d.speak()) # Woof!


'''typing'''

from typing import List, Optional

def greet_all(names: List[str]) -> None:
    for name in names:
        print(f"Hello, {name}")

def get_user(id: int) -> Optional[str]:
    return "Alice" if id == 1 else None


'''dataclasses'''

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int = 0 # default value

p1 = Point(3, 4)
p2 = Point(3)

print(p1) # Point(x=3, y=4)
print(p2) # Point(x=3, y=0)


'''warnings'''

import warnings

# Emit a warning
warnings.warn("This feature is deprecated", DeprecationWarning)


'''importlib'''

import importlib

# Dynamically import a module
math_module = importlib.import_module('math')
print(math_module.sqrt(16)) # 4

# Reload a module (e.g., after code changes in development)
importlib.reload(math_module)


'''locale'''

import locale

# Set locale for number formatting (may vary by system)
locale.setlocale(locale.LC_ALL, '') # Use system default locale

# Format number with grouping
num = 1234567.89
formatted = locale.format_string("%n", num, grouping=True)
print(formatted) # e.g., '1,234,567.89' in en_US

# Get currency symbol
print(locale.localeconv()['currency_symbol'])


'''gettext'''

import gettext

# Set up translation
# Normally you'd use .mo files; here's a dummy fallback example
gettext.install('example', localedir='locale', names=['ngettext'])


'''codecs'''
import codecs

# Write text with a specific encoding
with codecs.open('example_utf16.txt', 'w', encoding='utf-16') as f:
    f.write("This is UTF-16 encoded text.")

# Read it back
with codecs.open('example_ut16.txt', 'r', encoding='utf-16') as f:
    content = f.read()
    print(content)