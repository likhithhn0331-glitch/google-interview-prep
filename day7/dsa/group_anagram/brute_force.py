# Given an array of strings strs, group the anagrams together.

def group_anagrams_brute_force(strs):
    """
    Groups anagrams together using a brute force approach.

    :param strs: List of strings
    :return: List of lists, where each sublist contains anagrams
    """
    result = []
    visited = [False] * len(strs)

    for i in range(len(strs)):
        if visited[i]:
            continue
        current_group = [strs[i]]
        visited[i] = True

        for j in range(i + 1, len(strs)):
            if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                current_group.append(strs[j])
                visited[j] = True

        result.append(current_group)

    return result
