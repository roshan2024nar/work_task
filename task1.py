def find_sum_list(input_list: list, target: int):
    """
    A function to find the starting and ending indices of a sublist from the given input list that sums up to the target value.

    Args:
            input_list (list) : The input list of integers.

            target (int) : The target value.

    Returns:

            list : A list containing the start and ending indices of the sublist that sums up to "target"
                   If no sublist is found, returns [-1,-1].

    Examples:

            >>> find_sum_list([4, 3, 5, 7, 8], 12)
            [0,2]

            >>> find_sum_list([1, 2, 3, 4], 17)
            [-1,-1] 

    """
    for start_index in range(len(input_list)):

        sum_values = 0

        for end_index in range(start_index, len(input_list)):

            sum_values += input_list[end_index]

            if sum_values == target:
                return [start_index, end_index]

    return [-1, -1]


input_list = [4, 3, 10, 2, 8]
target = 12

print(f"Input List: {input_list}\nTarget:{target}\nOutput: {find_sum_list(input_list, target)}")

input_list = [1, 2, 3, 4]
target = 15

print(f"\nInput List: {input_list}\nTarget:{target}\nOutput: {find_sum_list(input_list, target)}")