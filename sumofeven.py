n = int(input(" Please Enter the Maximum Value : "))
total = 0

print("Even numbers: ")
for number in range(1, n+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number

print("The Sum of Even Numbers:",  total)