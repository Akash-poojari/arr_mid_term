def find_middle_positive(arr):
    # Filter out negative integers
    positive_numbers = []
    for i in arr:
        if i>=0:
            positive_numbers.append(i)

    # Check if there are positive numbers in the filtered list
    if not positive_numbers:
        print("No positive numbers found in the array.")
        return

    # Calculate the middle index
    middle_index = len(positive_numbers) // 2

    # Print the middle indexed term
    print("Middle indexed term in positive numbers:", positive_numbers[middle_index])

# Example usage:
input_array = [-5, 10, -3, 7, 2, -1, 8]
find_middle_positive(input_array)