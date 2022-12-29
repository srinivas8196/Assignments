
# factorial of given number
def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while(n > 1):
			fact *= n
			n -= 1
		return fact

# Driver Code
n = int(input("Enter the number : "));
print("Factorial of",n,"is",factorial(n))

# Function for nth Fibonacci number

def fibo():
    n = int(input("Enter the total number: "))
    first, second = 0, 1
    count = 0

    if n <= 0:
        print("Please enter a positive number: ")

        print("Fibonacci series", n, ":")
        print(first)

    else:
        print("Fibonacci series:")
        while count < n:
            print(first)
            sum = first + second

            first = second
            second = sum
            count += 1

# palindrome or not


def Palindrome(str):

    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


# main function
s = input("Enter the any string: ")
ans = Palindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

def table():
    
    n1=1
    n2=int(input("Enter the number: "))
    for i in range(1,11):
        n3=n1*n2  
        print(n3)

while True:
    print("\nMAIN MENU")
    print("1. Factorial")
    print("2. Polyndrome")
    print("3. Fibonacci")
    print("4. Fibonacci")

    choice = int(input("Enter the function u want to perform:"))

    if choice == 1:
        factorial()
    if choice == 2:
        Palindrome()
    if choice == 3:
        fibo()
    if choice == 4:
        table()


    else:
        print("Please Provide a valid Input!")
