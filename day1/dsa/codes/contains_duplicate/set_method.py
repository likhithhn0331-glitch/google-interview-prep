def contains_duplicate_set_method(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return True
        seen.add(num)
    return False
