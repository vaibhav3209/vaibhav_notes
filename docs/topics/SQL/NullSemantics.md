# NULL Semantics in SQL

## NULL logic

- SQL conditions can result in **3 outputs**, not 2.


- SQL uses **3-valued logic**: `TRUE` / `FALSE` / `UNKNOWN`.


- If SQL can't determine whether a statement is True or False, it marks it **UNKNOWN**.



| Expression            | Result                                                  |
|-----------------------|---------------------------------------------------------|
| True AND Unknown      | Unknown                                                 |
| Unknown AND Unknown   | Unknown                                                 |
| False OR Unknown      | Unknown                                                 |
| Unknown OR Unknown    | Unknown                                                 |
| Not Unknown           | Unknown                                                 |
| * True OR Unknown *   | **True** |
| * False AND Unknown * | **False**                                               |

---

## 1. NULLS in WHERE

!!! note "WHERE clause behavior"
    The `WHERE` clause only keeps rows where the condition evaluates to **TRUE**. Rows evaluating to `FALSE` or `UNKNOWN` are filtered out.

=== "A. city = NULL"
    
    ```sql
    SELECT city
    FROM table1
    WHERE city = NULL;
    
    -- Result:  Returns 0 rows (only column name/header shows up)
    -- Reason:      Where city = NULL 
        Becomes ->  Where Unknown        ==>> where only filter True
    -- Fix:     use IS NULL instead of = NULL
    
    SELECT city
    FROM table1
    WHERE city IS NULL;
    ```

=== "B. city = 'ABC'"

    ```sql
    SELECT city
    FROM table1
    WHERE city = 'ABC';
    
    -- Returns only non-NULL matches
    -- If a row's city is NULL, that row is skipped
    -- Reason: city = 'ABC' -> Unknown for NULL rows -> logic becomes Unknown, but only for that row
    
    /*
    Improvement: explicitly include the NULL-valued rows too, if needed
    */
    SELECT city
    FROM table1
    WHERE city = 'ABC'
       OR city IS NOT NULL;
    ```

---

## 2. NULL Progression

```sql
SELECT  
    col1
    , col2,
    , col1 + col2
FROM table_name;

-- If either col1 or col2 is NULL, the whole row's result becomes NULL
-- Examples:
--   1 + NULL       -> NULL
--   NULL + NULL    -> NULL

/*
Fix: use COALESCE to substitute a default value before adding
*/
SELECT 
    COALESCE(col1, 0) + COALESCE(col2, 0)
FROM table_name;
```

## 3. NULL in COUNT()

=== "Table1"


    | Salary |
    | :--- |
    | 50K |
    | 60K |
    | 0 |
    | 10K |
    | NULL |
    | NULL |

    ```sql
    SELECT COUNT(*)
    FROM salary;
    -- => 6   (counts all rows, regardless of NULL)
    
    SELECT COUNT(salary)
    FROM salary;
    -- => 4   (0 is counted since it's a real value, only NULLs are excluded)
    ```

=== "Table2"

    | Salary2 |
    | :--- |
    | NULL |
    | NULL |
    | NULL |

    ```sql
    SELECT COUNT(*)
    FROM salary2;
    -- => 3   (counts all rows including NULLs)
    
    SELECT COUNT(salary2)
    FROM salary2;
    -- => 0   (COUNT(column) only counts non-NULL values)
    
    SELECT COUNT(*)
    FROM salary2
    WHERE salary2 != 0;
    -- => 0   (NULL != 0 evaluates to Unknown, so no row passes WHERE)
    
    SELECT COUNT(salary2)
    FROM salary2
    WHERE salary2 != 0;
    -- => 0   (same reason: WHERE filters out all rows before COUNT runs)
    ```

=== "Table2 — IS NULL / IS NOT NULL"

    | Salary2 |
    | :--- |
    | NULL |
    | NULL |
    | NULL |

    ```sql
    SELECT COUNT(*)
    FROM salary2
    WHERE salary2 IS NULL;
    -- => 3   (all 3 rows satisfy the filter, COUNT(*) counts them all)
    
    SELECT COUNT(salary2)
    FROM salary2
    WHERE salary2 IS NULL;
    -- => 0   (rows pass the filter, but salary2 itself is NULL in each,
    --         and COUNT(column) never counts NULL values)
    
    SELECT COUNT(*)
    FROM salary2
    WHERE salary2 IS NOT NULL;
    -- => 0   (no row satisfies the filter, since every row is NULL)
    
    SELECT COUNT(salary2)
    FROM salary2
    WHERE salary2 IS NOT NULL;
    -- => 0   (no rows pass the filter, so nothing to count)
    ```

---

## 4. NULL in Other Aggregates (SUM / AVG / MIN / MAX)

- For `SUM`, `AVG`, `MIN`, `MAX` — any row where the value is `NULL` is simply **skipped**; 
    the result is computed only from the remaining (non-NULL) rows.


- Use `IFNULL` / `COALESCE` if you want NULLs treated as a value (e.g. `0`) instead of being skipped. 
    — this will **change** what `AVG()` (and the others) return, since skipped rows no longer reduce the divisor.

=== "Example 1"

    | Salary |
    | :--- |
    | NULL |
    | NULL |
    | NULL |
        
    ```sql
    
    SELECT COUNT(*)     FROM salary;  -- => 3
    SELECT COUNT(salary) FROM salary; -- => 0
    SELECT SUM(salary)  FROM salary;  -- => NULL
    SELECT AVG(salary)  FROM salary;  -- => NULL
    SELECT MIN(salary)  FROM salary;  -- => NULL
    SELECT MAX(salary)  FROM salary;  -- => NULL
    -- Reason: there are no non-NULL values left to aggregate over
    ```

=== "Example 2"

      
    | Salary |
    |:-------|
    | 500    |
    | 0      |
    | NULL   |
    | NULL   |

    
    ```sql
    SELECT COUNT(*)      FROM salary; -- => 4  (all rows, NULL included)
    SELECT COUNT(salary) FROM salary; -- => 2  (only the 0 and 500 rows)
    SELECT SUM(salary)   FROM salary; -- => 500   (0 + 500, NULLs skipped)
    SELECT AVG(salary)   FROM salary; -- => 250   (500 / 2, NOT 500 / 4)
    
    SELECT AVG(COALESCE(salary, 0)) FROM salary;
    -- => 125   (500 / 4, NOT 500 / 2 -> this is the actual behavior change)
    ```

---

## 5. NULL in GROUP BY

- Rows with `NULL` in the `GROUP BY` column are **not dropped** 
    — they get grouped together into their own single "NULL group".


- This matters for `COUNT()` and other aggregate corrections per group:
    don't forget the NULL group exists and will show up as its own row in the result set.


## 6. NULL in Case...When

    | emp | Output    |
    |-----|-----------|
    | A   | 50000      |
    | B   | 60000      |
    | C   | NULL   |

=== "A. CASE WHEN"

    ```sql
    SELECT emp,
        CASE
            WHEN salary > 50000 THEN 'High'
            WHEN salary < 50000 THEN 'Low'
            ELSE 'Unknown'
        END AS salary_band
    FROM emp;
    ```

    | emp | Output    |
    |-----|-----------|
    | A   | High      |
    | B   | High      |
    | C   | Unknown   |

=== "B. salary = NULL (wrong way)"

    ```sql
    SELECT emp,
        CASE
            WHEN salary = NULL THEN 'Missing'   -- ❌ never true
            ELSE 'Available'
        END AS salary_status
    FROM emp;
    
    -- salary = NULL always evaluates to Unknown,
    -- => the WHEN branch is never executed, for any row
    
    /*
    Fix: use IS NULL instead
    */
    SELECT emp,
        CASE
            WHEN salary IS NULL THEN 'Missing'
            ELSE 'Available'
        END AS salary_status
    FROM emp;
    ```

    | emp | Output (wrong version) | Output (fixed version) |
    |-----|-------------------------|--------------------------|
    | A   | Available               | Available                |
    | B   | Available               | Available                |
    | C   | Available               | Missing                  |


=== "C. CASE without ELSE"

    ```sql
    SELECT emp,
        CASE
            WHEN salary > 50000 THEN 'High'
        END AS salary_band
    FROM emp;

    -- Rows that don't satisfy any WHEN clause get NULL by default
    -- when there's no ELSE, i.e. it's equivalent to:

    /*
    BOTH QUERIES ARE SAME.
    */
    SELECT emp,
        CASE
            WHEN salary > 50000 THEN 'High'
            ELSE NULL
        END AS salary_band
    FROM emp;
    ```

    | emp | Output |
    |-----|--------|
    | A   | High   |
    | B   | High   |
    | C   | NULL   |

=== "D. CASE inside an aggregate"

    ```sql
    SELECT
        COUNT(
            CASE WHEN salary IS NULL THEN 1 END
        ) AS count_missing_salary
    FROM emp;
    
    -- Trace, row by row (A=50k, B=60k, C=NULL):
    --   A -> salary IS NULL is False -> CASE returns NULL (no ELSE)
    --   B -> salary IS NULL is False -> CASE returns NULL (no ELSE)
    --   C -> salary IS NULL is True  -> CASE returns 1
    
    
    -- => COUNT(NULL, NULL, 1)
    -- COUNT(column) ignores NULLs, so only the 1 is counted
    ```

    | count_missing_salary |
    |-----------------------|
    | 1                     |


    [See 2 difference between case...when vs Where](DifferenceBetween.md)


## 7. NULL in Subquery 

- `IN`: if the subquery returns `NULL` among its results, 
    rows that match one of the *other* (non-NULL) values are still selected fine 

    The `NULL` in the list doesn't block a `TRUE` match.


- `NOT IN`: **the main culprit** — if the subquery returns even a single `NULL`,
    rows that would otherwise be excluded correctly can end up excluded entirely (no rows returned)
     because the comparison chain turns `Unknown`.



|empid | dept_id|
|------|--------|
|1     | 10|
|2     | 20|
|3     | 30|
|4     | NULL|

| dept   |
|--------|
|10|
|20|
|NULL|


=== "IN"
    
    ```sql
    SELECT * FROM employees
    WHERE dept_id IN (
        SELECT dept FROM dept
    );
    
    -- Evaluates to: dept_id IN (10, 20, NULL)
    -- A NULL in the list doesn't stop a real match from being TRUE
    -- => Returns rows for empid = 1 and empid = 2
    
    /*
    Using EXISTS (safer)
    */

    SELECT e.* FROM employees e
    WHERE EXISTS (
        SELECT 1
        FROM dept d
        WHERE e.dept_id = d.dept
    );
    -- Same result: empid = 1 and empid = 2
    -- EXISTS just checks row existence, so a NULL in dept
    -- never even becomes part of the comparison
    ```

=== "NOT IN (the problem)"

    ```sql
    SELECT * FROM employees
    WHERE dept_id NOT IN (
        SELECT dept FROM dept
    );
    
    /*
    Step-by-step evaluation for empid = 3 (dept_id = 30):
      30 <> 10   -> False
      30 <> 20   -> False
      30 <> NULL -> Unknown
    
    NOT IN is really: (30<>10) AND (30<>20) AND (30<>NULL)
      => FALSE AND FALSE AND UNKNOWN
      => UNKNOWN
    
    Since WHERE only keeps TRUE rows, this row is dropped.
    The SAME thing happens for every other row too, because
    every comparison chain includes "<> NULL" => Unknown.
    
    Result: NO ROWS RETURNED AT ALL (not even empid = 3, 4)
    */
    ```

=== "NOT IN ->Solution"
    
    ```sql
    -- Solution 1: Exclude NULLs from the subquery
    SELECT * FROM employees
    WHERE dept_id NOT IN (
        SELECT dept FROM dept
        WHERE dept IS NOT NULL
    );

    -- Now the list is just (10, 20) -> no Unknown in the chain
    -- => Correctly returns empid = 3 (dept_id = 30)
    

    -- Solution 2: Use NOT EXISTS instead of NOT IN
    SELECT * FROM employees e
    WHERE NOT EXISTS (
        SELECT 1
        FROM dept d
        WHERE e.dept_id = d.dept
    );

    -- NOT EXISTS checks row-by-row existence directly,
    -- so a NULL sitting in dept never poisons the whole condition
    -- => Correctly returns empid = 3 (and empid = 4, since NULL dept_id
    --    also never matches any dept.dept value)
    ```