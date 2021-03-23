
def rotated_array_search(arr, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not arr:
        # print("You have not provided an array with values.")
        return -1

    end_idx = len(arr) - 1
    pivot_idx = find_pivot(arr, start_idx=0, end_idx=end_idx)

    if pivot_idx == -1:
        return binary_search(arr, target, 0, end_idx)

    pivot_val = arr[pivot_idx]
    first_val = arr[0]

    if target == pivot_val:
        return pivot_idx

    elif target == first_val:
        return 0

    elif target < first_val: # upper partition of indices, lower half of sorted vals
        return binary_search(arr, target, pivot_idx + 1, end_idx)

    else: # lower partition of indices, upper partition of sorted values
        return binary_search(arr, target, 0, pivot_idx + 1)

    return result



def find_pivot(arr, start_idx, end_idx):
    if start_idx >= end_idx: # base case
        return -1

    mid_idx = (start_idx + end_idx) // 2

    if arr[mid_idx] > arr[mid_idx + 1]:
        return mid_idx

    elif arr[mid_idx] < arr[mid_idx - 1]:
        return (mid_idx - 1)

    elif arr[start_idx] >= arr[mid_idx]:
        return find_pivot(arr, start_idx=start_idx, end_idx=mid_idx - 1) # look from start up until the midpoint

    else:
        return find_pivot(arr, start_idx=mid_idx + 1, end_idx=end_idx) # look from midpoint til the end


def binary_search(array, target, start_idx, end_idx):
    if start_idx > end_idx:
        return -1 # element not found

    mid_idx = (start_idx + end_idx) // 2
    mid_element = array[mid_idx]

    if mid_element == target:
        return mid_idx
    elif target < mid_element:
        return binary_search(array, target, start_idx, mid_idx - 1)
    else:
        return binary_search(array, target, mid_idx + 1, end_idx)



if __name__ == '__main__':
    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

    def test_function(test_case):
        input_list = test_case[0]
        number = test_case[1]
        if linear_search(input_list, number) == rotated_array_search(input_list, number):
            print("Pass")
        else:
            print("Fail")

    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[], 10])


    def test_find_pivot(test_cases):
        for num, test_case in enumerate(test_cases):
            test_arr = test_case[0]
            print(f"TEST CASE {num + 1}", test_arr)
            actual_result = find_pivot(test_arr, 0, len(test_arr) - 1)
            expected_result = test_case[1]
            print(f"actual result:   {actual_result}")
            print(f"expected result: {expected_result}\n")
            assert actual_result == expected_result


    test_cases = [
        [[1, 2, 3, 4, 6, 7, 8, 9, 10, 11], -1], # no pivot
        [[6, 7, 7, 1, 2, 2, 4], 2], # pivot on duplicate
        [[9, 10, 11, 1, 2, 3, 4, 6, 7, 8], 2], #pivoted in bottom part
        [[3, 4, 6, 7, 8, 9, 10, 11, 1, 2], 7], # pivoted in top part
        [[9, 10, 11, 1, 2, 3, 4, 6, 7,], 2], #pivoted in bottom part, even count of elements
        [[3, 4, 6, 7, 8, 9, 10, 11, 1], 7], # pivoted in top part, even count of elements
        [[11, 12, 10],  1],
        [[11, 10], 0],
        [[10, 11], -1],
        [[], -1]
    ]

    test_find_pivot(test_cases)
