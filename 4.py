num = int(input("Enter a number: "))
is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

if is_prime:
    print("It's a prime number!")
else:
    print("Not a prime number.")