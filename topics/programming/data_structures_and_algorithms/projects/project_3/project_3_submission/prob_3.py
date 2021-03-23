def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not arr:
        return []
    heapsort(arr)
    return make_two_nums(arr)


def make_two_nums(arr):
    num_1 = ""
    num_2 = ""
    for ranking, digit in enumerate(arr):
        if ranking % 2:
            num_1 = str(digit) + num_1
        else:
            num_2 = str(digit) + num_2
    return [int(num_1), int(num_2)]


def heapify(arr, n, i):
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]  #swap parent node and child node
        heapify(arr, n, largest_index)

def heapsort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] #swap root node and current node
        heapify(arr, i, 0)

if __name__ == '__main__':


    def test_function(test_case):
        output = rearrange_digits(test_case[0])
        solution = test_case[1]
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

    test_cases = [
        [[4, 6, 2, 5, 9, 8], [964, 852]],
        [[1, 2, 3, 4, 5], [542, 31]],
        [[],[]],
        [[1, 2, 2, 0], [21, 20]]
    ]
    for test_case in test_cases:
        test_function(test_case)
