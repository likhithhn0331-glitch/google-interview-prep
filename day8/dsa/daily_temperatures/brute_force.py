def daily_temperatures_bruteforce(temperatures):
    """Return the number of days to wait for a warmer temperature for each day.

    Brute force approach: for every day, scan forward until a warmer temperature
    is found. This runs in O(n^2) time.
    """
    n = len(temperatures)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break

    return answer
