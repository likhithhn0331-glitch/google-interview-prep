def binary_subarrays_with_sum_prefix_sum(nums, goal):
    count = 0
    prefix_sum = 0
    prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 having one occurrence

    for num in nums:
        prefix_sum += num
        # Check if there is a prefix sum that when subtracted from the current prefix sum equals the goal
        if (prefix_sum - goal) in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - goal]
        # Update the count of the current prefix sum in the dictionary
        if prefix_sum in prefix_sum_count:
            prefix_sum_count[prefix_sum] += 1
        else:
            prefix_sum_count[prefix_sum] = 1

    return count
