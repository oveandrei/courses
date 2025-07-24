
'''Changing case'''
"hello".upper() # HELLO
"HELLO".lower() # hello
"hello world".title # Hello World

'''Stripping whitespace'''

"    Hello Wordld   ".strip() # 'Hello World'

'''Finding and Replacing'''

"text".find('x') # Returns the index of 'x' in 'text', or -1 if not found
"dog dog".replace("dog", "cat") # cat cat

'''Splitting and Joining'''
"one, two, three".split(",") # ['one', 'two', 'three']
"-".join(['one', 'two', 'three']) # 'one-two-three'

'''Checking Content'''
"hello".isalpha() # True, all characters are alphabetic
"123".isdigit() # True, all characters are digits
"hello123".isalnum() # True, all characters are alphanumeric