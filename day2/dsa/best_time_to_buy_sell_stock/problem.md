# Best Time to Buy and Sell Stock — DSA Problem Statement

## Problem

You are given an array `prices` where `prices[i]` represents the price of a stock on the **ith day**.

You want to maximize your profit by choosing **one day to buy** and a **different day in the future to sell**.

Return the **maximum profit** you can achieve.

If you cannot make any profit, return `0`.

### Important Rules

- You must **buy before you sell**.
- You can make **only one transaction**.
- You cannot buy and sell on the same day.

---

## Examples

### Example 1

```text
Input:  prices = [7,1,5,3,6,4]
Output: 5
```

**Explanation:**

Buy on day 2 at price `1` and sell on day 5 at price `6`.

```text
Profit = 6 - 1 = 5
```

---

### Example 2

```text
Input:  prices = [7,6,4,3,1]
Output: 0
```

**Explanation:**

The stock price keeps decreasing, so there is no profitable transaction.

```text
Maximum Profit = 0
```

---

### Example 3

```text
Input:  prices = [2,4,1,7]
Output: 6
```

**Explanation:**

Buy on day 3 at price `1` and sell on day 4 at price `7`.

```text
Profit = 7 - 1 = 6
```

---

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Expected Approach

Try solving this problem using a **single-pass / greedy approach**.

As you iterate through the array:

1. Keep track of the **minimum price seen so far**.
2. Treat the current price as a potential selling price.
3. Calculate the profit:

```text
profit = current_price - minimum_price
```

4. Keep track of the **maximum profit** found so far.
5. Update the minimum price whenever you encounter a lower price.

---

## Target Complexity

```text
Time:  O(n)
Space: O(1)
```

---

## Interview Follow-up Questions

1. Why can't we simply find the minimum and maximum values in the array?
2. Why must the minimum price be encountered **before** the selling price?
3. Can you solve this using brute force? What is its time complexity?
4. Why is the single-pass solution considered a greedy approach?
5. Can you explain the solution without using an extra array?
