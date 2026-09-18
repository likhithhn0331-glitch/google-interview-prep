# Daily Temperatures

## Problem Statement

Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that:

- `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature.
- If there is no future day for which this is possible, keep `answer[i] = 0`.

Return the resulting array.

---

## Examples

### Example 1

**Input:**
```text
temperatures = [73,74,75,71,69,72,76,73]
```

**Output:**
```text
[1,1,4,2,1,1,0,0]
```

**Explanation:**

- Day 0: Wait 1 day for temperature 74.
- Day 1: Wait 1 day for temperature 75.
- Day 2: Wait 4 days for temperature 76.
- Day 3: Wait 2 days for temperature 72.
- Day 4: Wait 1 day for temperature 72.
- Day 5: Wait 1 day for temperature 76.
- Days 6 and 7: No warmer temperature ahead.

---

### Example 2

**Input:**
```text
temperatures = [30,40,50,60]
```

**Output:**
```text
[1,1,1,0]
```

---

### Example 3

**Input:**
```text
temperatures = [30,60,90]
```

**Output:**
```text
[1,1,0]
```

---

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

---

## Approach Hint

A brute-force approach checks every future day for each temperature, resulting in `O(n²)` time complexity.

A more efficient solution uses a **Monotonic Decreasing Stack**:

1. Store indices of temperatures in a stack.
2. Maintain the stack such that temperatures are in decreasing order.
3. For each new temperature:
   - While the current temperature is greater than the temperature at the stack's top index:
     - Pop the index.
     - Calculate the waiting days as `currentIndex - poppedIndex`.
4. Push the current index onto the stack.
5. Any indices left in the stack have no warmer future day, so their answers remain `0`.

---

## Complexity Analysis

### Monotonic Stack Solution

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

where `n` is the length of the `temperatures` array.

---

## Tags

`Array` `Stack` `Monotonic Stack`