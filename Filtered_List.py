import unittest

def list_filter_function(list):
	if len(list) == 0 or len(list) % 10 != 0:
		print(“Error: List length is not a multiple of 10.”)
		return None

	final_list = []
	for i in range(len(list)):
		if (i+1)%2 != 0 and (i+1)%3 != 0:
			final_list.append(list[i])

	return final_list


def test_process_list():
    # test cases defined as tuples of (input_list, expected_output)
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 5, 7]),
        ([2, 4, 6, 8, 10], None),
        ([], None),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1]),
        ([2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647], [2147483647, 2147483647, 2147483647]),
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [10, 50, 70]),
        ([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [-10, -6, -4]),
    ]


    for input_list, expected_output in test_cases:
        try:
            result = list_filter_function(input_list)
            if result != expected_output:
                print(f"Test failed for input: {input_list}. Expected: {expected_output}, got: {result}")
                return False
        except Exception as e:
            if expected_output is not None:
                print(f"Test failed for input: {input_list}. Unexpected error: {e}")
                return False
            pass

    print("All tests passed.")
    return True


test_process_list()
