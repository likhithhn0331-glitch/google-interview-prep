# Best Time to Buy and Sell Stock — Solution

## 1) Problem recap

We are given an array of stock prices. We must choose:

- one day to buy
- a later day to sell
- and maximize the profit

Rules:

- buy before sell
- only one transaction allowed
- cannot buy and sell on the same day
- if no profit is possible, return `0`

Example:

```python
prices = [7, 1, 5, 3, 6, 4]
# Best answer: buy at 1, sell at 6
# Profit = 6 - 1 = 5
```

---

## 2) Core idea

The best profit for any current day is:

```text
current_price - minimum_price_seen_so_far
```

So while scanning the list from left to right:

1. keep track of the minimum price seen so far
2. calculate profit if we sold today
3. update the best profit when needed

This is a greedy approach because at every step we keep the best possible buy choice for the current sell day.

---

## 3) Optimal solution (single pass)

```python
def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit
```

### Walkthrough

```text
prices = [7, 1, 5, 3, 6, 4]
```

- start: `min_price = 7`, `max_profit = 0`
- price = 1 -> `min_price = 1`
- price = 5 -> profit = 5 - 1 = 4
- price = 3 -> profit = 3 - 1 = 2
- price = 6 -> profit = 6 - 1 = 5, update max
- price = 4 -> profit = 4 - 1 = 3

Final result: `5`

---

## 4) Why this works

For any day `i`, the best buy price before that day is simply the minimum value seen up to index `i`.

So the profit for selling on day `i` is:

```text
prices[i] - min_price_so_far
```

We compare it with the best profit seen so far and keep the larger one.

This means we never need to check every pair of days; the minimum so far already gives the optimal buy for each sell day.

---

## 5) Big-O analysis

### Optimal solution

```text
Time:  O(n)
Space: O(1)
```

Reason:

- we iterate through the array once
- we store only a few variables: `min_price` and `max_profit`
- no extra array or nested loops

### Brute force

A basic brute-force solution checks every buying day and every selling day:

```python
def brute_force(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit
```

Complexity:

```text
Time:  O(n^2)
Space: O(1)
```

This works, but it is too slow for large arrays because it checks all pairs.

---

## 6) Brute force vs two-pointer (DSA perspective)

### Brute force

This means trying all possibilities.

- choose every buy day
- choose every sell day after it
- calculate difference
- keep the maximum

This is simple to reason about, but inefficient.

### Two-pointer method

A two-pointer version uses:

- `left` = current buying point
- `right` = current selling point

```python
def buy_sell_stock_two_pointer(prices):
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        current_profit = prices[right] - prices[left]

        if prices[left] < prices[right]:
            max_profit = max(max_profit, current_profit)
        else:
            left = right

        right += 1

    return max_profit
```

### DSA comparison

- brute force: tests all combinations, `O(n^2)`
- two-pointer: moves pointers forward, `O(n)`
- greedy/min-tracking: also `O(n)` and usually the clearest interview solution

In this problem, the greedy version is usually preferred because it is easier to explain:

```text
keep the lowest price seen so far
sell at current price
update max profit
```

The two-pointer version is valid too, but it is more about pointer movement than direct state tracking.

---

## 7) Answering the interview questions in problem.md

### 1. Why can't we simply find the minimum and maximum values in the array?

Because the minimum and maximum might not occur in the correct order.

Example:

```text
[7, 1, 5, 3, 6, 4]
```

Min = 1, Max = 7, but 7 comes before 1, so you cannot buy at 7 and sell at 1.

The sell must happen after the buy, so we need the minimum price before the current day, not just the global minimum and maximum.

---

### 2. Why must the minimum price be encountered before the selling price?

Because a stock must be bought before it can be sold.

So the profit must always be calculated as:

```text
sell_day_price - earlier_buy_price
```

A future lower price cannot be used as a buy after the current sell day.

---

### 3. Can you solve this using brute force? What is its time complexity?

Yes.

Try every pair `(buy_day, sell_day)` where `buy_day < sell_day`, and compute:

```text
prices[sell_day] - prices[buy_day]
```

There are `O(n^2)` pairs, so the complexity is:

```text
O(n^2)
```

It is correct but not efficient for large inputs.

---

### 4. Why is the single-pass solution considered a greedy approach?

Because at each step it chooses the locally optimal buy price:

- keep the lowest price seen so far
- check the current price as a selling candidate
- update the answer if profit improves

This greedy choice is enough to guarantee the global optimum for this problem.

---

### 5. Can you explain the solution without using an extra array?

Yes. We do not need an extra array at all.

We only track:

- `min_price`
- `max_profit`

That is enough to solve the problem because we only need the best profit, not the full history of prices.

---

## 8) Final takeaway

The most efficient and interview-friendly solution is:

- scan once from left to right
- store the minimum price seen so far
- compute profit for each price
- keep the maximum profit

This gives:

```text
Time:  O(n)
Space: O(1)
```

This is optimal for the problem and is the standard DSA solution expected in interviews.
