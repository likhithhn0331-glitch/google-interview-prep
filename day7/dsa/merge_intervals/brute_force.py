def merge_intervals_brute_force(intervals):
    """
    Merge all overlapping intervals using a direct O(n^2) comparison.

    Each interval is [start, end]. The result is sorted by start and contains
    the minimal set of non-overlapping merged intervals that cover the same
    ranges as the input.
    """
    if not intervals:
        return []

    normalized = []
    for start, end in intervals:
        if start > end:
            start, end = end, start
        normalized.append([start, end])

    normalized.sort(key=lambda interval: (interval[0], interval[1]))

    merged = []
    for current in normalized:
        if not merged:
            merged.append(current[:])
            continue

        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current[:])

    return merged
