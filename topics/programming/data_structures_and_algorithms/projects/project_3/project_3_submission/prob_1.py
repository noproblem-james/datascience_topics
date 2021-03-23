def sqrt(n):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    initial_guess = n
    updated_guess = (n + 1) // 2

    while updated_guess < initial_guess:
        initial_guess = updated_guess
        updated_guess = (initial_guess + n // initial_guess) // 2

    return initial_guess



if __name__ == '__main__':
    import math
    test_cases = [
        (0, 0),
        (1, 1),
        (9, 3),
        (10, 3),
        (16, 4)
    ]

    for x in range(2, 4):
        test_cases.append((x, math.sqrt(x) // 1))

    for test_case in test_cases:
        test_input = test_case[0]
        expected_result = test_case[1]
        actual_result = sqrt(test_input)

        if expected_result == actual_result:
            print("Pass")
        else:
            print("Fail")
        print(f"Expected: {expected_result}\nActual:  {actual_result}\n\n")
