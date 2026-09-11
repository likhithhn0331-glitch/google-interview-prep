# valid palindrome DSA problem
from solution import valid_palindrome_two_pointer

# LeetCode-style test cases
test_strings = [
    "level",
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
    "abc",
    "Was it a car or a cat I saw?",
    "noon",
    "0P"
]

for text in test_strings:
    print(f"{text!r} -> {valid_palindrome_two_pointer(text)}")
