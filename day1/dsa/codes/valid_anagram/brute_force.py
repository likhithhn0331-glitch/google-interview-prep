def valid_anagram_brute_force(str_1, str_2):
    # Check if the lengths of the strings are equal
    if len(str_1) != len(str_2):
        return False

    # Create a list to keep track of used characters in str_2
    used_indices = []

    # Iterate through each character in str_1
    for char in str_1:
        found = False
        # Check if the character exists in str_2 and hasn't been used yet
        for i in range(len(str_2)):
            if str_2[i] == char and i not in used_indices:
                used_indices.append(i)  # Mark this index as used
                found = True
                break
        if not found:
            return False  # Character not found or already used

    return True  # All characters matched
