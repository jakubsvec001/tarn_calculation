import numpy as np


def tarn_calc(arr):
    """Calculate the tarns of a histogram of arrays

    Tarns are lakes created by rainfall within local minimums within
    mountain ranges. Given array representing values of a histogram at
    each unit along the x axis, determine the maximum units of water that the
    histogram can hold.

    Example 1:
    arr1 = [2, 1, 1, 1, 2, 1, 1, 4, 1] = 5
           |
           |
    |xxx|xx|
    |||||||||

    Example 2:
    arr2 = [1, 3, 4, 3, 2, 1, 5, 4, 7, 2, 1, 3, 5, 7] = 24

            |xxxx|
            |xxxx|
          |x|xxx||
      |xxx|||xxx||
     |||xx|||xx|||
     ||||x||||x|||
    ||||||||||||||

    Example 3:
    arr3 = [1, 2, 3, 1] = 0
      |
     ||
    ||||

    Example 4:
    arr4 = [7, 1, 1, 2, 1, 1, 1, 2, 1] = 5
    |
    |
    |xxx|xx|
    |||||||||

    Args:
        arr (list / np.array): list of ints or numpy array of integers or floats.

    Return:
        float: total tarn area contained
    """

    arr = np.array(arr)
    n = len(arr)
    past_max = np.zeros(n)
    future_max = np.zeros(n)
    past_max[0] = arr[0]
    for i in range(1, n):
        past_max[i] = max(past_max[i-1], arr[i])
    rev_arr = arr[::-1]
    future_max[0] = rev_arr[0]
    for i in range(1, n):
        future_max[i] = max(future_max[i-1], rev_arr[i])
    total = np.sum(np.minimum(past_max, future_max[::-1]) - arr)
    return total
