# 0-add.py

a = 1
b = 2

# Use __import__ to import the function
add_module = __import__('add_0')
add = add_module.add

result = add(a, b)

print(f"{a} + {b} = {result}")
