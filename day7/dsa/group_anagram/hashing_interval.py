# Given an array of strings strs, group the anagrams together.

def group_anagrams_hashing_interval(strs):
    """
    Groups anagrams together using a hashing approach with interval optimization.

    :param strs: List of strings
    :return: List of lists, where each sublist contains anagrams
    """
    from collections import defaultdict

    anagram_map = defaultdict(list)

    for s in strs:
        # Create a hashable key based on character counts
        char_count = [0] * 26  # Assuming only lowercase letters
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        key = tuple(char_count)
        anagram_map[key].append(s)

    return list(anagram_map.values())
