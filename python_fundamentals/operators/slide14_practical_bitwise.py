# Example: Feature flags using bits

READ = 0b0001 # 1
WRITE = 0b0010 # 2
EXEC = 0b0100 # 4

user_permissions = READ | WRITE # 0b0011

# Check if WRITE is enabled
print(user_permissions & WRITE != 0) # True

# Add EXEC permission
user_permissions |= EXEC

# Remove READ permission
user_permissions &= ~READ

print(bin(user_permissions)) # 0b110 (WRITE + EXEC)