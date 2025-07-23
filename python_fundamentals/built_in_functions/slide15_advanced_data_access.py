# reversed(): iterates from end to start
for ch in reversed("Python"):
    print(ch, end=" ")            # n o h t y P

# slice(): reusable slicing logic
data = list(range(10))           # [0, 1, 2, ..., 9]
s = slice(2, 8, 2)
print(data[s])                   # [2, 4, 6]

# memoryview(): view byte data without copying
b = bytearray(b"abcde")
m = memoryview(b)
print(m[1])                      # 98 (ASCII for 'b')

# Modify through memoryview
m[1] = 122
print(b)                         # bytearray(b'azcde')
