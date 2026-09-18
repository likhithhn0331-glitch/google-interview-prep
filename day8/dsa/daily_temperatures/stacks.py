def daily_temperatures_stack(temperatures):
    """Return the number of days to wait for a warmer temperature using a stack.

    Strategy:
    - Keep indices in a monotonic decreasing stack of temperatures.
    - When a warmer temperature appears, pop smaller temperatures and calculate
      the gap in days.
    - This reduces the complexity to O(n) time.
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer
