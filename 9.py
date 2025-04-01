numbers = list(map(int, input("Enter numbers separated by space: ").split()))
unique_numbers = list(set(numbers))

print(f"List after removing duplicates: {unique_numbers}")