def find_middle_positive(arr):
    
    positive_numbers = []
    for i in arr:
        if i>=0:
            positive_numbers.append(i)

    if not positive_numbers:
        print("No positive numbers found in the array.")
        return

    middle_index = len(positive_numbers) // 2

    print("Middle indexed term in positive numbers:", positive_numbers[middle_index])

input_array = [-5, 10, -3, 7, 2, -1, 8]
find_middle_positive(input_array)
