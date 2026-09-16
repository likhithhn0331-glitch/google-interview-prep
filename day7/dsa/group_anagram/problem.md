# Group Anagrams

## Problem Statement

Given an array of strings `strs`, group the anagrams together.

You may return the groups in any order.

Two strings are **anagrams** of each other if they contain exactly the
same characters with the same frequencies, but the characters may appear
in a different order.

For example:

-   `"eat"` and `"tea"` are anagrams.
-   `"eat"` and `"ate"` are anagrams.
-   `"tan"` and `"nat"` are anagrams.
-   `"bat"` is not an anagram of `"eat"`.

The task is to identify all strings that belong to the same anagram
group and return those groups together.

------------------------------------------------------------------------

## Formal Input

You are given:

``` text
strs: an array/list of strings
```

Each element of `strs` is a string.

Example:

``` text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

------------------------------------------------------------------------

## Expected Output

Return a collection of groups, where:

1.  Every input string appears in exactly one group.
2.  Strings in the same group are anagrams of one another.
3.  Strings that are not anagrams of one another belong to different
    groups.
4.  The order of the groups does not matter.
5.  The order of strings inside a group does not matter unless a
    particular implementation chooses to preserve input order.

For the input:

``` text
["eat", "tea", "tan", "ate", "nat", "bat"]
```

one valid output is:

``` text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

Another ordering of the groups is also valid:

``` text
[
    ["bat"],
    ["tan", "nat"],
    ["eat", "tea", "ate"]
]
```

The important requirement is that the grouping itself is correct.

------------------------------------------------------------------------

## What Does "Anagram" Mean?

Two strings are anagrams when they contain exactly the same characters
with exactly the same frequencies.

Consider:

``` text
"eat"
"tea"
```

Character frequencies for `"eat"`:

``` text
e → 1
a → 1
t → 1
```

Character frequencies for `"tea"`:

``` text
t → 1
e → 1
a → 1
```

The frequencies are identical, so the strings are anagrams.

Now consider:

``` text
"eat"
"bat"
```

Character frequencies for `"eat"`:

``` text
e → 1
a → 1
t → 1
```

Character frequencies for `"bat"`:

``` text
b → 1
a → 1
t → 1
```

The frequencies differ because one contains `e` while the other contains
`b`.

Therefore:

``` text
"eat" ≠ anagram of "bat"
```

------------------------------------------------------------------------

## Core Challenge

The main challenge is not simply determining whether two individual
strings are anagrams.

Instead, the problem asks you to group **all** strings that share the
same anagram structure.

For example:

``` text
["eat", "tea", "tan", "ate", "nat", "bat"]
```

contains three logical groups:

``` text
Group 1:
"eat"
"tea"
"ate"

Group 2:
"tan"
"nat"

Group 3:
"bat"
```

The key algorithmic question is:

> How can we create a representation, or **signature**, for every string
> such that all anagrams produce the same signature?

Once that representation is available, a hash map can be used to group
strings efficiently.

------------------------------------------------------------------------

## Pattern Classification

This problem belongs to the:

``` text
Hashing
```

pattern.

More specifically:

``` text
Hash Map + Canonical Representation
```

The important pattern-recognition clue is:

> **Group equivalent objects by converting each object into a common
> canonical key.**

For this problem:

``` text
String
   ↓
Canonical representation / signature
   ↓
Hash Map key
   ↓
Group of anagrams
```

------------------------------------------------------------------------

## Important Observation

Anagrams have the same character composition.

Therefore, the order of characters should not affect the representation.

For example:

``` text
eat
tea
ate
```

can all be transformed into the same sorted representation:

``` text
aet
```

Similarly:

``` text
tan
nat
```

can both become:

``` text
ant
```

Therefore:

``` text
eat → aet
tea → aet
ate → aet

tan → ant
nat → ant

bat → abt
```

The canonical representation can then be used as the key in a hash map.

Conceptually:

``` text
"aet" → ["eat", "tea", "ate"]
"ant" → ["tan", "nat"]
"abt" → ["bat"]
```

------------------------------------------------------------------------

## Example 1

### Input

``` text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

### Canonical representations

``` text
eat → aet
tea → aet
tan → ant
ate → aet
nat → ant
bat → abt
```

### Hash Map

``` text
{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

### Output

``` text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

------------------------------------------------------------------------

## Example 2

### Input

``` text
strs = [""]
```

There is only one string, and an empty string is an anagram of itself.

### Output

``` text
[[""]]
```

------------------------------------------------------------------------

## Example 3

### Input

``` text
strs = ["a"]
```

There is only one string.

### Output

``` text
[["a"]]
```

------------------------------------------------------------------------

## Example 4

### Input

``` text
strs = ["abc", "bca", "cab", "xyz"]
```

Canonical representations:

``` text
abc → abc
bca → abc
cab → abc
xyz → xyz
```

Therefore:

``` text
[
    ["abc", "bca", "cab"],
    ["xyz"]
]
```

------------------------------------------------------------------------

## Example 5

### Input

``` text
strs = ["a", "a", "a"]
```

All three strings have the same signature.

Therefore:

``` text
[
    ["a", "a", "a"]
]
```

The algorithm must preserve duplicate input strings.

------------------------------------------------------------------------

## Example 6

### Input

``` text
strs = ["listen", "silent", "enlist", "google"]
```

The first three strings are anagrams:

``` text
listen → eilnst
silent → eilnst
enlist → eilnst
```

while:

``` text
google → eggloo
```

Therefore:

``` text
[
    ["listen", "silent", "enlist"],
    ["google"]
]
```

------------------------------------------------------------------------

## Constraints and Assumptions

The exact platform-specific constraints should always be checked in the
version of the problem being solved.

For algorithm design, define:

-   `n` = number of strings.
-   `k` = average or representative string length.
-   `L` = total number of characters across all strings.

The solution should be designed around the relationship between:

``` text
number of strings
```

and:

``` text
total number of characters
```

rather than treating every string as having the same fixed length.

If the problem specifies a restricted character set, such as lowercase
English letters, a frequency-count representation may be used instead of
sorting.

------------------------------------------------------------------------

## Requirements

Your solution must:

1.  Process every input string.
2.  Determine the anagram class of each string.
3.  Place each string into the correct group.
4.  Preserve duplicate strings.
5.  Handle empty strings if allowed by the problem constraints.
6.  Return all groups.
7.  Avoid comparing every pair of strings unnecessarily if a more
    efficient hashing-based approach is possible.

------------------------------------------------------------------------

## What the Problem Is Testing

This problem tests several important concepts.

### 1. Hash Maps

You need to understand how a hash map can associate:

``` text
signature → collection of strings
```

------------------------------------------------------------------------

### 2. Canonical Representation

You need to recognize that objects that are logically equivalent can
often be transformed into a common representation.

For example:

``` text
eat → aet
tea → aet
ate → aet
```

The sorted string is a canonical representation.

------------------------------------------------------------------------

### 3. Pattern Recognition

When you see:

> "Group strings that are equivalent under rearrangement."

You should think:

``` text
Hash Map
+
Canonical Key
```

------------------------------------------------------------------------

### 4. Complexity Analysis

You should compare multiple approaches rather than immediately writing
code.

For example:

``` text
Brute Force pairwise comparison
        ↓
Sorting-based signature
        ↓
Frequency-count signature
```

Each has different complexity characteristics.

------------------------------------------------------------------------

## Important Edge Cases

Before implementing the solution, consider the following.

### Empty input

``` text
[]
```

Expected result:

``` text
[]
```

------------------------------------------------------------------------

### One string

``` text
["abc"]
```

Expected:

``` text
[["abc"]]
```

------------------------------------------------------------------------

### Empty string

``` text
[""]
```

Expected:

``` text
[[""]]
```

if empty strings are permitted by the problem.

------------------------------------------------------------------------

### Duplicate strings

``` text
["abc", "abc"]
```

Both must remain in the same group:

``` text
[["abc", "abc"]]
```

------------------------------------------------------------------------

### Same characters, different order

``` text
["abc", "bca", "cab"]
```

All belong together.

------------------------------------------------------------------------

### Different character frequencies

``` text
["aab", "abb"]
```

These are not anagrams.

Their frequencies are:

``` text
aab:
a → 2
b → 1

abb:
a → 1
b → 2
```

Therefore they must be placed in different groups.

------------------------------------------------------------------------

### Case sensitivity

Determine whether the problem treats uppercase and lowercase characters
as distinct.

For example:

``` text
"A"
"a"
```

should not automatically be considered equivalent unless the problem
explicitly defines case-insensitive behavior.

------------------------------------------------------------------------

## Questions to Answer Before Coding

Do not start by memorizing an implementation.

Answer these questions first:

1.  What exactly makes two strings anagrams?
2.  What information must be identical between two anagrams?
3.  Can the characters be sorted to create a common representation?
4.  What should the hash-map key be?
5.  What should the hash-map value be?
6.  Why does every anagram produce the same key?
7.  What happens with duplicate strings?
8.  What happens with an empty string?
9.  What is the time complexity of sorting each string?
10. What is the total character-processing cost?
11. Can character-frequency counting produce a key?
12. When would frequency counting be preferable to sorting?
13. Why is a hash map appropriate for this problem?
14. Why would comparing every pair of strings be less efficient?
15. What are the edge cases?

------------------------------------------------------------------------

## Expected Problem-Solving Process

Use the following sequence during the interview.

### Step 1 --- Understand the requirement

Identify:

``` text
Input:
array of strings

Output:
groups of anagrams
```

------------------------------------------------------------------------

### Step 2 --- Identify the equivalence relation

Two strings belong to the same group when:

``` text
their character frequencies are identical
```

------------------------------------------------------------------------

### Step 3 --- Find a canonical key

Possible representations include:

``` text
sorted characters
```

or:

``` text
character-frequency vector
```

------------------------------------------------------------------------

### Step 4 --- Select the data structure

Use:

``` text
Hash Map
```

because we need:

``` text
key → group
```

------------------------------------------------------------------------

### Step 5 --- Process each string

Conceptually:

``` text
for every string:
    create its signature
    use signature as hash-map key
    append string to corresponding group
```

------------------------------------------------------------------------

### Step 6 --- Return the groups

The values of the hash map represent the required groups.

------------------------------------------------------------------------

## Complexity Questions

You should be prepared to explain the complexity of at least two
approaches.

### Sorting-based signature

For a string of length `k`, sorting costs approximately:

``` text
O(k log k)
```

If there are `n` strings with comparable length:

``` text
O(n × k log k)
```

More generally, it is useful to think in terms of the total character
count and the individual string lengths.

------------------------------------------------------------------------

### Frequency-count signature

If the alphabet size is fixed, a frequency representation can be
constructed in:

``` text
O(k)
```

for a string of length `k`.

Across all strings:

``` text
O(total number of characters)
```

up to the cost of constructing and hashing the representation.

The exact practical trade-off depends on the character set and
representation used.

------------------------------------------------------------------------

## Interview Follow-Up Topics

After solving the basic problem, be ready for:

1.  Can you solve it without sorting?
2.  Can you use character frequencies as the key?
3.  What changes if the alphabet is very large?
4.  What changes if the strings contain Unicode characters?
5.  What happens if strings are extremely long?
6.  What is the memory complexity?
7.  Why is a hash map useful here?
8.  What happens if hash collisions occur?
9.  How would you implement the canonical signature?
10. Can the groups be returned in deterministic order?
11. How would you handle streaming input?
12. What if the data does not fit into memory?
13. How would you distribute this computation?
14. What if the same anagram group appears across multiple batches?
15. How would you test the implementation?

------------------------------------------------------------------------

## Common Mistakes to Avoid

### Mistake 1 --- Comparing every pair

A naive solution may compare every string with every other string.

This can become expensive as the number of strings increases.

------------------------------------------------------------------------

### Mistake 2 --- Forgetting duplicate strings

If:

``` text
["eat", "eat"]
```

is provided, both strings belong in the output group.

------------------------------------------------------------------------

### Mistake 3 --- Using only the set of characters

A set loses frequency information.

For example:

``` text
"aab"
"abb"
```

both contain:

``` text
{a, b}
```

but they are not anagrams.

Therefore a plain character set is not sufficient.

------------------------------------------------------------------------

### Mistake 4 --- Mutating the original strings unnecessarily

If sorting is used to generate the key, ensure the implementation does
not accidentally destroy information needed later.

------------------------------------------------------------------------

### Mistake 5 --- Ignoring the character model

A frequency-array solution that assumes 26 lowercase English letters is
not automatically valid for arbitrary Unicode input.

The implementation must match the problem's stated character
constraints.

------------------------------------------------------------------------

## Pattern Recognition Summary

When you see:

``` text
"Group strings that are rearrangements of one another."
```

think:

``` text
Anagram
   ↓
Same character frequencies
   ↓
Canonical representation
   ↓
Hash Map
   ↓
Group
```

The core reusable pattern is:

``` text
Object
   ↓
Canonical Key
   ↓
Hash Map
   ↓
Equivalent Objects Grouped Together
```

This pattern is useful beyond anagrams.

The same general idea can appear whenever multiple inputs need to be
grouped according to an equivalence relation.

------------------------------------------------------------------------

## Definition of Done

Before considering this problem complete, you should be able to:

-   [ ] State the problem clearly without looking at notes.
-   [ ] Define an anagram precisely.
-   [ ] Explain why character frequencies determine anagram equivalence.
-   [ ] Identify the Hash Map pattern.
-   [ ] Explain the idea of a canonical representation.
-   [ ] Explain the sorting-based signature approach.
-   [ ] Explain the frequency-count approach.
-   [ ] State the time complexity of the chosen approach.
-   [ ] State the space complexity.
-   [ ] Handle duplicates.
-   [ ] Handle empty strings when permitted.
-   [ ] Handle an empty input.
-   [ ] Explain why a plain set of characters is insufficient.
-   [ ] Answer interview follow-up questions.
-   [ ] Implement the solution independently without copying a memorized
    template.

------------------------------------------------------------------------

## Interview Prompt

> **Given an array of strings `strs`, group the anagrams together. You
> may return the answer in any order.**

Example:

``` text
Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

Your first task in an interview is **not to code immediately**.

Start by explaining:

1.  What an anagram is.
2.  What information uniquely identifies an anagram class.
3.  How you can construct a canonical key.
4.  Why a hash map is the appropriate data structure.
5.  The expected time and space complexity.
6.  Important edge cases.

Then implement the solution.
