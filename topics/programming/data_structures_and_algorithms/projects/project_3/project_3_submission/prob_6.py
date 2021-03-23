def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return (None, None)

    if len(ints)  == 1:
        return (ints[0], ints[0])

    curr_min = 0
    curr_max = 0

    for el in ints:
        if el < curr_min:
            curr_min = el
        if el > curr_max:
            curr_max = el

    return curr_min, curr_max


if __name__ == '__main__':

    import random
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    test_cases = [
        ([0], (0, 0)),
        ([1, 0], (0, 1)),
        (random.sample(list(range(0, 10)), 9), (0, 9))
    ]

    for test_case in test_cases:
        test_input = test_case[0]
        expected_result = test_case[1]
        actual_result = get_min_max(test_input)

        if expected_result == actual_result:
            print("Pass")
        else:
            print("Fail")
        print(f"Expected: {expected_result}\nActual:  {actual_result}\n\n")



#
#

# In[ ]:
