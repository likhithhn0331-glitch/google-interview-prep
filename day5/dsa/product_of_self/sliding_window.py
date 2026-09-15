def product_of_array_except_self_sliding_window(array):
    n = len(array)
    result = [1] * n

    # Calculate left products
    for i in range(1, n):
        result[i] = result[i - 1] * array[i - 1]

    # Calculate right products and multiply with left products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= array[i]

    return result
