'''re'''

import re

text = "The rain in Spain"

# search: find first match anywhere
matchh = re.search(r"rain", text)
print(matchh.group()) # type: ignore # 'rain'

# match: only matches at the start
print(re.match(r"The", text)) # Match object

# findall: find all matching substrings
print(re.findall(r"\b\w{4}\b", text)) # ['rain', 'Spain']

# sub: replace texxt
print(re.sub(r"Spain", "France", text)) # 'The rain in France'

# compile: precompile pattern for reuse
pattern = re.compile(r"\b\w{4}\b")
print(pattern.findall(text)) # ['rain', 'Spain']


'''string and Template'''

import string
from string import Template

# Constants
print(string.ascii_letters) # abc....XYZ
print(string.digits) # 0123456789
print(string.punctuation) # !"#$%&*....

# Template usage (safe substitution)
template = Template("Hello, $name")
print(template.substitute(name="Alice")) # Hello, Alice

# Safer with user input (missing keys raise KeyError with substitute but not with save_substitute)
print(template.safe_substitute()) # Hello, $name


'''textwrap'''

import textwrap

text = "Python is an amazing programming language that emphasizes code readability."

# Wrap text into a list of lines
wrapped = textwrap.wrap(text, width=30)
print(wrapped)

# Fill: wrap and join into a single string
print(textwrap.fill(text, width=30))

# Dedent: remove common leading whitespace
raw = """\
    This is indented text.
    So is this."""
print(textwrap.dedent(raw))


'''unicodedata'''

import unicodedata

char = 'ñ'

# Unicode name
print(unicodedata.name(char)) # LATIN SMALL LETTER N WITH TILDE

# Normalize to composed form
s1 = 'ñ' # 'n' + combining tilde
s2 = unicodedata.normalize('NFC', s1)
print(s2 == 'ñ') # True

# Category
print(unicodedata.category('A')) # 'Lu' (Letter, uppercase)


'''difflib'''

import difflib

text1 = 'apple'
text2 = 'applesauce'

# Show diff in unified format
diff = difflib.unified_diff([text1], [text2], lineterm='')
print('\n'.join(diff))

# Fuzzy ration comparison
ratio = difflib.SequenceMatcher(None, text1, text2).ratio()

# Close matches
names = ['banana', 'bandana', 'cabana']
print(difflib.get_close_matches("banana", names)) # ["banana", "bandana", "cabana"]


'''stringprep'''

import stringprep

# Chec if character is in a prohibited list for networking input
print(stringprep.in_table_c12('\u0001')) # True (control character)

# Rarely used directly in apps - used internally for IDNA, LDAP, etc


'''html.parser'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start tage: {tag}")
    
    def handle_data(self, data):
        print(f"Data: {data}")

parser = MyHTMLParser()
html = "<html><body><h1>Hello!</h1></body></html>"
parser.feed(html)