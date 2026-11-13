[← Back to list](List.md#sliding-window)


### 2.0 Subarray vs Subsequences vs Subsets
=== "**Subarray**"

    **arr = [1, 2, 1, 3, 2]**

    1. Contiguous part of an array,

    2. Order kept, Gaps **not** Allowed

    3. n(n+1)/2 non empty subarrays in total.

    - All valid subarrays:

         - [1], [2], [1], [3], [2]
    
         - [1,2], [2,1], [1,3], [3,2]
    
         - [1,2,1], [2,1,3], [1,3,2]
    
         - [1,2,1,3], [2,1,3,2]
    
         - [1,2,1,3,2]

    - Invalid: 
         - [1,1] (skips 2), 
    
         - [3,1] (order changed), 
    
         - [2,3] (skips 1)

    - Use: sliding window, Kadane's algorithm, prefix sums


=== "**Subsequence**"

    **arr = [1, 2, 1, 3, 2]**

    1. Non contigous part of array

    2. Order kept,gaps allowed

    3. 2^n (considering 1 empty subarray else 2^(n-1))
        = 32 by position, but only 26 distinct (including empty) because of the repeated values.

    - Valid Subsequences

        - [], [1], [2], [3]
    
        - [1,2], [1,1], [1,3], [2,1], [2,3], [2,2], [3,2]
    
        - [1,2,1], [1,2,3], [1,2,2], [1,1,3], [1,1,2], [1,3,2], [2,1,3], [2,1,2], [2,3,2]
    
        - [2,1,3,2], [1,1,3,2], [1,2,3,2], [1,2,1,2], [1,2,1,3]
    
        - [1,2,1,3,2]

    - Invalid:

        - [3,1] (3 comes after both 1s)
      
        - [3,2,1] (order broken), 
      
        - [1,1,1] (only two 1s exist)

    - Use: dynamic programming (LIS, LCS, distinct subsequences)


=== "**Subset(Mathematical one)**"

    **arr = [1, 2, 1, 3, 2]**
    
    1. No repeats, 

    2. Order ignored. 

    3. Values are {1,2,3}, so 2³ = 8 subsets including the empty set.

    - All valid: {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}

    - Order doesn't matter: {3,1} is the same subset as {1,3}

    - Invalid: 
    
         - {1,1,2} (repeat), 
    
         - {4} (not in the array),
    
         - {1,2,2} (repeat)

    - Use: backtracking, bitmasking, power set problems


### 2.1 Why Sliding Window ??

Sliding window is used to solve problems on contiguous subarrays or substrings
efficiently. 

Instead of recomputing the answer for every subarray from scratch,
in which every element inside overlapping windows gets included in the calculation
multiple times.

We maintain a window and update it incrementally as it moves: add the
new element entering the window and remove the element leaving it.


### 2.2 What Can Be Tracked Inside a Window??


- Sum/Product of elements (positive numbers only)


- Count of elements (or count of 0s, 1s, flips, etc.)


- Frequency map of characters or numbers


- Set of unique elements (for duplicate checks)


- Number of distinct elements


- Window maximum or minimum (using a monotonic deque)


- Window length (right - left + 1)


### 2.3 Complexity


Every element enters the window once and leaves it once, so each pointer moves
at most n steps. 

Time complexity is **O(n)**. 

### 2.x Template: 


### 2.4 Limitations:

Sliding Window can't be used when: 

1. If the solution needs to revisit or
re-check earlier positions, as both boundaries can move only forward.

2. Negative numbers are present as the logic assumes that adding an
element increases the sum and removing an element decreases it.

    Example: arr = [2, 4, -3, 1], find a subarray with sum = 3

    Fix: use prefix sum + hashmap.


3. When the condition is not monotonic.

    Sliding window needs a rule for when to shrink: once the window turns
    invalid, expanding further must never make it valid again (or vice versa).
    If validity flips back and forth, we cannot decide when to move left.
        
    Example: longest subarray with sum divisible by 3, arr = [1, 2, 4, 2].
    
    [1, 2] sum 3 is valid, [1, 2, 4] sum 7 is invalid, [1, 2, 4, 2] sum 9 is
    valid again. Valid -> invalid -> valid, so "shrink when invalid" gives wrong
    answers.
    
    Fix: use prefix sum with remainder hashmap.


### 2.5 FAQs

1. Which Approach to use??

| `for right in range(len(arr)):` | `while right < len(arr):` |
|---------------------------------|---------------------------|
| Use normally in almost every sliding window | Needed only in rare cases |
| `right` moves exactly once per iteration while expanding | `right` can move more than once, or conditionally, before the window is processed |
| `left` is handled by an inner `while` that shrinks the window | Need to write `right += 1` manually |
| No risk of forgetting to increment `right` | Forgetting `right += 1` causes an infinite loop |


2. My understanding of sliding window..

- Sliding window basic approach k alawa count wali approach (with 2 functions) tab lagana 
    jab pta nhi chale right expand/ left shrink se sahi ans ayega.

- both jaane se sahi ans aa rha hai tab use different approach.

- ya phir kuch subarrays beech mein skip ho rhe ho