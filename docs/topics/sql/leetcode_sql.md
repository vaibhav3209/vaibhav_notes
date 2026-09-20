# SQL Revision List 

| Problem |  Link/Problem no. | Notes                  | Importance    |
|---------|---------------------------------|------------------------|---------------|
| Second Highest Salary            | [Leetcode 176](https://leetcode.com/problems/second-highest-salary/) | [Notes](#leetcode-176) | ⭐             |
| Rank Scores           | [Leetcode 178](https://leetcode.com/problems/rank-scores/)           | [Notes](#leetcode-178) | ⭐⭐⭐           |
| Consecutive Numbers                             | [Leetcode 180](https://leetcode.com/problems/consecutive-numbers/)   | [Notes](#leetcode180)  | ⭐⭐⭐           |
| Salary Greater than Manager's| [Leetcode 181](https://leetcode.com/problems/employees-earning-more-than-their-managers/)| -                      | ⭐             |

---

# Concepts

??? note "Second Highest Salary"
    <a id="leetcode-176"></a>


    | Approach            | Time Complexity | Handles Duplicates | Handles NULL |
    |---------------------|---|---|---|
    | 1. LIMIT/OFFSET     | O(N log N) | Only with `DISTINCT` | ❌ No |
    | 2. MAX() < MAX()    | O(N) + O(N) | ✅ Yes | ✅ Yes |
    | 3. DENSE_RANK()     | O(N log N) | ✅ Yes | ❌ No |
    | 4. Functional (UDF) | O(N log N) | ✅ Yes (via DISTINCT) | ⚠️ Depends on `WHERE` clause |
    
    
    !!! tip "Best Practice"
        Always add `WHERE salary IS NOT NULL` before ranking or ordering — every approach here can 
        be tripped up by NULLs. (EXCEPT 2nd).
    
    
    === "**Approach 1**: LIMIT AND OFFSET"
    
        ```sql
            SELECT DISTINCT salary
            FROM Employee 
            ORDER BY salary DESC 
            LIMIT 1 OFFSET 1;
        
            /*
                1. Time: O(N log N) .
                2. Handles Duplicates : only if you write `DISTINCT`.
                3. Handles Null: No — if NULLs sort first in your DB, the "first" row could be NULL,
                    throwing off the offset.
                "Why DISTINCT?"
                    If the top salary appears twice, the "2nd row" is just a duplicate of the 1st — 
                    not actually the second distinct salary.
            
                "What if there's only one salary and we OFFSET?"
                    The query just returns `NULL`.
            */
        ```
    
    === "**2**: MAX() < MAX()"
    
        ```sql
            SELECT MAX(salary) AS SecondHighestSalary
            FROM Employee
            WHERE salary < (SELECT MAX(salary) FROM Employee);
        
        /*
            1. Time: O(N) + O(N) — two table scans.
            2. Handles Duplicates : the `<` comparison naturally drops every row equal to
                the top value, ties or not.
            3. Handles Null:`MAX()` ignores NULLs automatically, so a NULL row
                    never "wins" as the max.
          
        */
        ```
    
    === "**3**: DENSE_RANK()"
    
        ```sql
            SELECT salary
            FROM (
                SELECT salary,
                       DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
                FROM Employee
                WHERE salary IS NOT NULL
            ) ranked
            WHERE rnk = 2;
            
            /*
                1. Time:   O(N log N) due to sorting.
                2. Handles Duplicates :Yes — assigns correct, gapless ranks.
                3. Handles Null: No — needs an explicit `WHERE salary IS NOT NULL`.
            
                 "Why not RANK() OVER()?"
                    Ties share a rank and the next rank is skipped (1, 1, 3, 4...).
                     If two people tie for 1st, there's no rank 2 at all — the query returns empty.
            */
        ```
    
    
    === "**4**: Functional (UDF)"
    
        ```sql
            CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
            BEGIN
                DECLARE val INT;
                SET val = N - 1;
                RETURN (
                    SELECT DISTINCT salary 
                    FROM Employee 
                    WHERE salary IS NOT NULL
                    ORDER BY salary DESC 
                    LIMIT 1 OFFSET val
                );
            END
    
        /*
            1. Time: O(N log N) due to sorting,
            2. Handles Duplicates : Yes, via `DISTINCT`.
            3. Handles Null: Only if you remember the `WHERE` clause — 
                easy to forget since it's buried inside a function body.
        */
        ```
    
    [[Trick Learned]](#print-null-in-select)    


    [(Back to topic)](#leetcode-176){: .back-to-list }
    [(Back to list)](#sql-revision-list){: .back-to-list }



---

??? note "Rank Scores"
    <a id="leetcode-178"></a>


**Implement Rankings without using Window()**

- A rank of a value is just: "how many distinct/total values are
greater than or equal to it?

  
    Given Table:

                        | id | score |
                        | --- | --- |
                        | 1  | 3.50 |
                        | 2  | 3.65 |
                        | 3  | 4.00 |
                        | 4  | 3.85 |
                        | 5  | 4.00 |
                        | 6  | 3.65 |


**Method 1**: Dense_rank()  equivalent

- Correlated Subquery + Without Group By + (>=) sign

```sql
SELECT s1.score, 
       (SELECT COUNT(DISTINCT s2.score) 
        FROM Scores s2 
        WHERE s2.score >= s1.score) AS denserank
FROM Scores s1
ORDER BY s1.score DESC;
```


-  Self JOIN + WIth Group by + (>=) sign + **with Distinct**

```sql
SELECT s1.score
    , COUNT(DISTINCT s2.score) AS denserank
FROM Scores s1
LEFT JOIN Scores s2 ON s1.score <= s2.score
GROUP BY s1.score
ORDER BY s1.score DESC;
```


**Method 2**: Rank() equivalent -- skipping after ties

- Self Join + (>=) sign + **Without Distinct**
 
```sql
SELECT
    s1.score,
    COUNT(*) AS rank
FROM scores s1
JOIN scores s2
    ON s2.score >= s1.score
GROUP BY s1.score
ORDER BY s1.score DESC;
```

- Correlated Subquery + **(>) sign** + Add 1 to count()
    
    - count how many rows have a *strictly greater* score, then add 1.

```sql
SELECT
    s1.score,
    1 + (
        SELECT COUNT(*)
        FROM scores s2
        WHERE s2.score > s1.score
    ) AS rank
FROM scores s1
ORDER BY s1.score DESC;
```


**Method 3** : ROW_NUMBER() equivalent
 
- Every row gets a unique, sequential number — ties are broken by a
deterministic tiebreaker (here, `id` ascending).
 

- Self-join 
 
```sql
SELECT
    s1.score,
    COUNT(*) AS row_num
FROM scores s1
JOIN scores s2
    ON s2.score > s1.score
    OR (s2.score = s1.score AND s2.id <= s1.id)
GROUP BY s1.score
ORDER BY s1.score DESC;
```
 
- Correlated subquery 
 
```sql
SELECT
    s1.score,
    (
        SELECT COUNT(*)
        FROM scores s2
        WHERE s2.score > s1.score
           OR (s2.score = s1.score AND s2.id <= s1.id)
    ) AS row_num
FROM scores s1
ORDER BY s1.score DESC;
```
 
[(Back to topic)](#leetcode-178){: .back-to-list }
[(Back to list)](#sql-revision-list){: .back-to-list }

### Consecutive Numbers

New Concept : GAPS AND ISLANDS


## Tricks

1. ### Print NULL in SELECT

    ```sql
    SELECT ( main_query ) as SEcondHighestSalary
    ```
    - If we want to print NULL if the query returns NULL then 
    bound it in a outer SELECT clause.


2. ### Using rank keyword as alias

    ```sql
    -- ❌ This gives error can't use rank keyword as alias
    select dense_rank() over(....) as rank
   
    -- ✅ Instead use commas or use any other name
    select dense_rank() over(....) as 'rank'
    ```



??? note "Rank Scores"
    <a id="leetcode-178"></a>

    **Implement Rankings without using Window()**

    A rank of a value is just: *"how many distinct/total values are greater than or equal to it?"*

    **Given Table:**

    | id | score |
    |---|---|
    | 1 | 3.50 |
    | 2 | 3.65 |
    | 3 | 4.00 |
    | 4 | 3.85 |
    | 5 | 4.00 |
    | 6 | 3.65 |

    | Method | Ties Behavior | Comparison Sign | Needs DISTINCT |
    |---|---|---|---|
    | DENSE_RANK() equiv | Ties share rank, no gaps | `>=` | ✅ Yes |
    | RANK() equiv | Ties share rank, gaps after | `>=` or `>` (+1) | ❌ No |
    | ROW_NUMBER() equiv | Every row unique, tiebreak by `id` | `>` or `=` with `id` tiebreak | ❌ No |

    === "**Method 1**: DENSE_RANK() equivalent"

        **Technique A — Correlated Subquery** (no `GROUP BY`, `>=` sign)

        ```sql
        SELECT s1.score, 
               (SELECT COUNT(DISTINCT s2.score) 
                FROM Scores s2 
                WHERE s2.score >= s1.score) AS denserank
        FROM Scores s1
        ORDER BY s1.score DESC;
        ```
    
        **Technique B — Self JOIN** (with `GROUP BY`, `>=` sign, `DISTINCT`)
    
        ```sql
        SELECT s1.score
            , COUNT(DISTINCT s2.score) AS denserank
        FROM Scores s1
        LEFT JOIN Scores s2 ON s1.score <= s2.score
        GROUP BY s1.score
        ORDER BY s1.score DESC;
        ```
    
        !!! tip "Core idea"
            Count how many *distinct* scores are ≥ this one — `DISTINCT`
            collapses ties into one rank.

    === "**Method 2**: RANK() equivalent (skips after ties)"

        **Technique A — Self Join** (`>=` sign, no `DISTINCT`)

        ```sql
        SELECT
            s1.score,
            COUNT(*) AS rank
        FROM scores s1
        JOIN scores s2
            ON s2.score >= s1.score
        GROUP BY s1.score
        ORDER BY s1.score DESC;
        ```

        **Technique B — Correlated Subquery** (`>` sign, `+1`)

        ```sql
        SELECT
            s1.score,
            1 + (
                SELECT COUNT(*)
                FROM scores s2
                WHERE s2.score > s1.score
            ) AS rank
        FROM scores s1
        ORDER BY s1.score DESC;
        ```

        !!! tip "Core idea"
            Count rows *strictly greater*, then add 1 — no `DISTINCT`
                needed since ties naturally get the same rank.

    === "**Method 3**: ROW_NUMBER() equivalent"

        Every row gets a unique, sequential number — ties are 
            broken by a deterministic tiebreaker (here, `id` ascending).

        **Technique A — Self Join**
        
        ```sql
        SELECT
            s1.score,
            COUNT(*) AS row_num
        FROM scores s1
        JOIN scores s2
            ON s2.score > s1.score
            OR (s2.score = s1.score AND s2.id <= s1.id)
        GROUP BY s1.score
        ORDER BY s1.score DESC;
        ```

        **Technique B — Correlated Subquery**

        ```sql
        SELECT
            s1.score,
            (
                SELECT COUNT(*)
                FROM scores s2
                WHERE s2.score > s1.score
                   OR (s2.score = s1.score AND s2.id <= s1.id)
            ) AS row_num
        FROM scores s1
        ORDER BY s1.score DESC;
        ```

        !!! tip "Core idea"
            The `id` tiebreaker is what forces uniqueness — without it,
            tied scores would get the same "count," which isn't a true ROW_NUMBER().