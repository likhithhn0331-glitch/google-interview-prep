def buy_sell_stock_two_pointer(array):
    left = 0
    right = 1
    max_profit = 0

    while right < len(array):
        current_profit = array[right] - array[left]
        if array[left] < array[right]:
            max_profit = max(max_profit, current_profit)
        else:
            left = right
        right += 1

    return max_profit