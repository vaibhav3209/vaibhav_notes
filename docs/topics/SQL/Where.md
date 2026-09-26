## WHERE Clause Overview

- Used to filter rows based on a condition.

- ONLY rows that evaluate to `TRUE` are returned.

- Allows:
    - Comparison operators
    - Logical operators (`AND`, `OR`, `NOT`)
    - `IN`, `BETWEEN`, `LIKE`
    - `IS` / `IS NOT NULL`
    - Subqueries, functions, expressions

- **WHERE**: Filters individual rows.

- **HAVING**: Filters groups.

## What Cannot Be Done in WHERE?

- No aggregate functions (`AGG()`).

- No window functions (`Window()`) directly → Use in `HAVING` or CTEs instead.

- Cannot use column aliases defined in the `SELECT` statement directly inside `WHERE`.

- Cannot use direct NULL comparisons (e.g., `= NULL`), 
because `WHERE` only keeps rows that evaluate to `TRUE`.

## Special Case: Possible Interview Question

=== "Join with Condition"
    
    ```sql
    SELECT * 
    FROM employee e
    JOIN dept d
      ON e.dept_id = d.dept_id 
     AND d.deptname = 'IT';
    ```

    - The `deptname = 'IT'` condition is applied **during the join itself**, before rows are combined.

    - Since this is an `INNER JOIN`, the practical result is the same as the WHERE approach here 
        only employees in the IT department come back.

    - The difference matters most with an **outer join** (e.g., `LEFT JOIN`). 
        With the condition inside `ON`, every employee row is still kept (matched or not), and department 
        columns are `NULL` for anyone not in IT. The filter only decides *which dept row to attach*,
        not *which employee rows survive*.

=== "Join with WHERE"
    
    ```sql
    SELECT * 
    FROM employee e
    JOIN dept d
      ON e.dept_id = d.dept_id
    WHERE d.deptname = 'IT';
    ```

    - Here the join happens first (matching every employee to their dept), 
        and `WHERE` filters the *combined result set* afterward.

    - With an `INNER JOIN`, this gives the same output as the ON-condition approach.

    - With a `LEFT JOIN`, this is where the difference shows up: any employee whose 
        dept didn't match (so `d.deptname` is `NULL`) gets **dropped** by the `WHERE` clause,
        since `NULL = 'IT'` isn't `TRUE`. This effectively turns your left join into an 
        inner join — a classic interview gotcha.

**Interview takeaway:** for `INNER JOIN`, condition placement (`ON` vs `WHERE`) doesn't change the result. For `LEFT`/`RIGHT JOIN`,
putting the filter in `ON` preserves unmatched rows, while putting it in `WHERE` silently filters them out.


## Joins & Index Efficiency

### Inner Join vs. Left Join Behavior

- An `INNER JOIN` and a `WHERE` filter may yield similar result sets, but a `LEFT JOIN` can produce **different results** because it retains all rows from the left table regardless of match.

### Writing Queries for Index Efficiency

- Filter conditions should be written so the database engine can **utilize pre-existing indexes**.

- **Efficient (Uses Index)** ✔️:

```sql
    WHERE date >= '2023-01-01' AND date < '2023-02-01'
```

- **Inefficient (Disables Index)** ❌:

```sql
    WHERE MONTH(date) = 'Jan'
    -- Function call on column prevents index usage!
```