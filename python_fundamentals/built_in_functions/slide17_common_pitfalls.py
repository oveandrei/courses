
'''eval() Misuse - Security Warning'''
user_input = "2 + 2"
print(eval(user_input))         # Works, but dangerous!

# If user_input = "__import__('os').system('rm -rf /')"
# This could run arbitrary code — big security risk!

'''all() returns True'''
print(all([]))      # True
print(any([]))      # False


'''zip() Truncates to the shortest iterable'''
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))      # [(1, 'a'), (2, 'b')]
