
a = 5 # 0b0101
b = 3 # 0b0011

print(a & b) # Bits that are 1 in both operands -> # Out: 1 -> 0b0001
print(a | b) # OR # Out: 7 -> 0b0111
print(a ^ b) # XOR, bits that are 1 in one but not both  # Out: 6 -> 0b0110
print(~a) # NOT, Inverts all bits (1's complemented) # Out: -6 (inverted bits)
print(a << 1) # Left shift, shifts bits left (multiply by 2^n) # Out: 10 -> 0b1010
print(a >> 1) # Right shift, shifts bits right (divide by 2^n) # Out: 2 -> 0b0010
