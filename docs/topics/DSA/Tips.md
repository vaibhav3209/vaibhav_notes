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




### 2. Range vs Enumerate vs for ... in ??

|                                        | `for x in arr` | `enumerate(arr)`              | `range(n)`                                                     |
|----------------------------------------|---|-------------------------------|----------------------------------------------------------------|
| Gives you                              | Values | (index, value) pairs          | Indices only                                                   |
| **Traversal**                          | Sequential, all elements | Sequential, all elements      | Any start, stop, step                                          |
| **Access to neighbors (`i-1`, `i+1`)** | No | Not directly                  | Yes                                                            |
| Modify elements in place               | No (`x` is just a reference to the element) | Yes, `arr[i] = ...` using `i` | Yes, `arr[i] = ...`                                            |
| **Type returned**                      | The list itself (iterable) | Iterator (single use)         | Lazy sequence (reusable)                                       |
| **Best for**                           | Just values | Values and indices together   | Indexed Control <br> Start/skip Anywhere <br> Access neighbours |