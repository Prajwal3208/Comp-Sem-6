input_string = input("Enter a string: ")  # Asks the user to input a string
result = []  # Initializes an empty list to store results of AND operation
result1 = []  # Initializes another empty list to store results of XOR operation

for char in input_string:  # Iterates over each character in the input string
    a = ord(char)  # Gets the ASCII value of the character
    b = 127  # Represents the value to be used for bitwise operations
    k = a & b  # Performs bitwise AND operation
    j = a ^ b  # Performs bitwise XOR operation
    result.append(chr(k))  # Appends the character resulting from AND operation to result list
    result1.append(chr(j))  # Appends the character resulting from XOR operation to result1 list
    # Prints the binary representation, decimal value, and character representation of the results
    print("Converted value of", char, "in AND is:", bin(k)[2:], "and:", k, "and:", chr(k))
    print("Converted value of", char, "in XOR is:", bin(j)[2:], "and:", j, "and:", chr(j))

print(result)  # Prints the list of characters resulting from AND operation
print(result1)  # Prints the list of characters resulting from XOR operation
