def valid_anagrams_frequency_counting(str_1, str_2):
    # Check if the lengths of the strings are equal
    if len(str_1) != len(str_2):
        return False

    # Create a frequency dictionary for characters in str_1
    char_count = {}
    for char in str_1:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrease the count for each character found in str_2
    for char in str_2:
        if char not in char_count or char_count[char] == 0:
            return False  # Character not found or count mismatch
        char_count[char] -= 1

    return True  # All characters matched
