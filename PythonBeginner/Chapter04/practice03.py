# 3. Check that a tuple type cannot be changed in python.

mytuple = (1, 2, 3)
print(mytuple[2])
mytuple[2] = 4  # This will raise a TypeError because tuples are immutable  