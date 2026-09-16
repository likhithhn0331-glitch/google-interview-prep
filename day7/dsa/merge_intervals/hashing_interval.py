def merge_intervals_hashing_interval(intervals):
    """
    Merge all overlapping intervals using a hash-based coverage approach.

    This version marks every integer point covered by the intervals in a set,
    then compresses consecutive covered points back into merged intervals.

    This is a valid hash-based alternative when we want to reason about the
    covered regions directly.
    """
    if not intervals:
        return []

    covered = set()
    for start, end in intervals:
        if start > end:
            start, end = end, start
        for value in range(start, end + 1):
            covered.add(value)

    if not covered:
        return []

    points = sorted(covered)
    merged = []
    start = points[0]
    prev = points[0]

    for value in points[1:]:
        if value == prev + 1:
            prev = value
            continue

        merged.append([start, prev])
        start = prev = value

    merged.append([start, prev])
    return merged
