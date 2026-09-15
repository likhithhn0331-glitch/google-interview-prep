def binary_subarrays_with_sum_brute_force(nums, goal):
    count = 0
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == goal:
                count += 1
    return count
