height = int(input("Enter diamond's height: "))

for x in range(height):
    print(" " * (height - x), "*" * (2*x + 1))
for x in range(height - 2, -1, -1):
    print(" " * (height - x), "*" * (2*x + 1))