n = int(input("Enter the number: "))

first, second = 0, 1
count = 0


if n <= 0:
   print("Please enter a positive number")

   print("Fibonacci series",n,":")
   print(first)

else:
   print("Fibonacci series:")
   while count < n:
       print(first)
       sum = first + second
       
       first = second
       second = sum
       count += 1