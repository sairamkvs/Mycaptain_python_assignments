def most_frequent(input_string):
    frequency = {}
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            frequency[char_lower] = frequency.get(char_lower, 0) + 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    print("Output:")
    for char, count in sorted_frequency:
        print(f"{char} = {count:02}")

input_string = input("Please enter a string: ") # Input string from user

most_frequent(input_string)# Call the function 
