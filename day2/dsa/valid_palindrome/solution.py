def valid_palindrome_two_pointer(s: str) -> bool:
    """
    Check if a string is a valid palindrome using the two-pointer technique.
    A valid palindrome reads the same forwards and backwards, ignoring non-alphanumeric characters and case.

    Args:
        s (str): The input string to check.
    """

    left, right = 0, len(s) - 1

    while left < right:
        # Move a left pointer to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move a right pointer to the previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters in a case-insensitive manner
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
