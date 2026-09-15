def product_of_array_except_self_brute_force(array):
    n = len(array)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= array[j]
        result.append(product)
    return result
