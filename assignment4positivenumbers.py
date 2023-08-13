def get_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

input_str = input("Enter numbers separated by spaces: ") # Input list of numbers from the user
numbers = [int(num) for num in input_str.split()]

positive_numbers = get_positive_numbers(numbers) # Get positive numbers from the input list

print("Positive numbers:", positive_numbers) # Display the positive numbers
