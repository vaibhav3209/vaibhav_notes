## 1. Arrays {#arrays}

[← Back to DSA list](DSAList.md#arrays)


## 2. Sliding Window { #sliding-window }

[← Back to DSA list](DSAList.md#sliding-window)


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

    3. 2^n = 32 by position, but only 26 distinct (including empty) because of the repeated values.

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


### 2.1 Why Sliding Window (Interview Explaination)??

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







## 4. LinkedLists {#linkedlist}

[← Back to DSA list](DSAList.md#linkedlist)

### 4.1 What are Linked Lists?

!!! danger "Don't Say"
    Linked Lists are linear Data Structures...... OR 
    Stored Linearly in memory.


!!! tip "Say"
    
    1. Linked Lists are Data structres that store data in form of Nodes,
        along with reference to the next node.

    2. It can only access data in sequential manner, forward for singly L.L.

    3. It has 2 components: 

        -> `val` : can store any data type [in PYTHON]

        -> `next` : pointer to next node



### 4.2 WHy was  Linked Lists developed ?

| Array limitation                                        | 	How linked list helps                              |
|---------------------------------------------------------|-----------------------------------------------------|
| Fixed size, or costly resizing (copy to a bigger block) | 	 Grows and shrinks one node at a time.             |
| Needs contiguous memory	                                | Nodes can be anywhere in memory, linked by pointers |
| Insert/delete in the middle shifts elements, O(n)       | 	O(1) once you have a reference to the position     |
| Wasted capacity from over-allocation                    | 	Allocates exactly what is needed                   |



### 4.3 Array vs Linked List (Python Specific)
| Arrays                                                                                                               | Linked List                                                           |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Elements stored in contigous memory locations and indexed access.                                                    | Elements stored in non contigous locations and accessed via pointers. |
| Linear and Binary Search possible.                                                                                   | Only linear search intuitively.                                       |
| Acessing : O(1)<br/>   Insert at end : O(1)<br/> Delete at end : O(1) <br/>Insert/Delete at start: O(n) [Ammortized] | O(1) if Position is known.<br/> O(n) from head pointer.               |
| Memory is allocated one time ==>> can need resizing                                                                  | Memory allocated upon creation ==>> No resiszing concept.             |
| Memory (per element) is **less**.                                                                                    | Memory (per element) is More.                                         |
| Bettter **Cache Locality**. ==>> Cache Friendly (since contigouus stored)                                            | Poor Cache locality. ==>> **Not** cache riendly.                      |




## Tips:

### 1. Python Assignments: 

=== "a, b = 0, 0 vs a = b = 0"

    | Tuple unpacking | Chained assignment |
    |---|---|
    | The right side 0, 0 is evaluated first into a tuple (0, 0), then that tuple is unpacked, with the first item going to a and the second to b. Each name gets its own separately evaluated value. | The value on the right is evaluated once, then assigned to each name from left to right. Both names point to the same object.<br>Right side is evaluated only once, and both names point to the same object (same ref). |
    | ✅ Safe for both mutable and immutable types. | ✅ Fine for Immutable types (int, str, tuple, None), since they can't change in place. |
    |  | ❌ Not safe for mutable types (list, dict, set), because a change through one name shows up in the other (the append problem). |
    | `a, b = [], []`<br>`a.append(1)`<br>`print(b)        # []  -> b is unaffected` | `a = b = []`<br>`a.append(1)`<br>`print(b)        # [1]  -> a and b are the same list`<br>`print(a is b)   # True` |
    |  | ?? When chained assignment is useful for mutable types<br>Use it only when you purposely want one shared object under two names:<br>- Aliasing the same state: `config = settings = load_config()`<br>- One shared resource: `db = conn = connect()`<br>- Calling an expensive function only once: `data = backup = fetch_data()` |


=== " += operator"
    
    - `x += y` calls `__iadd__`, which modifies the object in place. 



    - `x = x + y` calls `__add__`, which builds a new object and **REBINDS `x`**.
    Other names still point to the old object.

    ```python
    a = b = [1]
    a += [2]
    print(b)        # [1, 2]  -> modified in place, b sees it
    
    a = b = [1]
    a = a + [2]
    print(b)        # [1]     -> a got a new list, b is untouched
    ```


    - For lists, `+=` accepts any iterable, but `+` needs a list on both sides.

    ```python
    x = [1]
    x += "ab"       # [1, 'a', 'b']  -> works
    x = x + "ab"    # TypeError
    ```


=== "[[0]x3]x3 vs [[0 for _ in range(3)] for _ in range(3)]"




### 2. When to use Range vs Enumerate vs in ??

|                                        | `for x in arr` | `enumerate(arr)`              | `range(n)`                                                     |
|----------------------------------------|---|-------------------------------|----------------------------------------------------------------|
| Gives you                              | Values | (index, value) pairs          | Indices only                                                   |
| **Traversal**                          | Sequential, all elements | Sequential, all elements      | Any start, stop, step                                          |
| **Access to neighbors (`i-1`, `i+1`)** | No | Not directly                  | Yes                                                            |
| Modify elements in place               | No (`x` is just a reference to the element) | Yes, `arr[i] = ...` using `i` | Yes, `arr[i] = ...`                                            |
| **Type returned**                      | The list itself (iterable) | Iterator (single use)         | Lazy sequence (reusable)                                       |
| **Best for**                           | Just values | Values and indices together   | Indexed Control <br> Start/skip Anywhere <br> Access neighbours |