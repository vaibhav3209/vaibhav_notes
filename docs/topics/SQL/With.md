## WITH Clause

[Refer CTE later]()

### Overview

- Used to define a CTE (Common Table Expression).

- A CTE is a temporary, named result set that can be referenced within an SQL statement.

- Used to simplify complex SQL statements, making code easier to read, manage, and use.

### When to Use a CTE?

- **Sequential aggregations**: When you need to aggregate, then aggregate again and search/filter on those new results.

- **Reusing intermediate results**: Storing intermediate outputs returned by another subquery.

- **Window functions in WHERE clauses**: Since window functions (`WINDOW()`) cannot be used directly in `WHERE`, you must first define them inside a CTE.

- **Recursive problems**: Organizational hierarchies, tree structures, graph traversal, parent-child relationships, generating sequences etc

### Defining Multiple CTEs

- **Correct Syntax** ✔️ (Use `WITH` only once):

```sql
    WITH cte1 AS (
      ---
    ),
    cte2 AS (
      ---
    ),
    cte3 AS (
      ---
    );
```

- **Incorrect Syntax** ❌ (Do NOT repeat the `WITH` keyword):

```sql
    WITH cte1 AS (
      ---
    ),
    WITH cte2 AS (  -- Incorrect syntax!
      ---
    ),
    cte3 AS (
      ---
    );
```

!!! tip "Tip"
    A single `WITH` statement can define multiple CTEs, and all CTEs belong to the primary statement that immediately follows.

### Referencing CTEs Inside CTE

- Subsequent CTEs can directly query previously defined CTEs within the same `WITH` block:

```sql
    WITH cte1 AS (
      ---
    ),
    cte2 AS (
      SELECT ---
      FROM cte1  -- Referencing cte1
    ),
    cte3 AS (
      SELECT ---
      FROM cte2  -- Referencing cte2
    )
    SELECT *
    FROM cte3;   -- Final query referencing cte3
```

!!! tip "Key Takeaway"
    This hierarchical structure allows you to build **modular, step-by-step logic** where each virtual table builds upon the output of the preceding one.


## CTE vs Temporary Table

- They are not the same thing.

### CTE

```sql
WITH sales AS (
    SELECT ...
)
SELECT *
FROM sales;
```

- A CTE exists for the duration/scope of the SQL statement.

### Temporary Table

```sql
CREATE TEMP TABLE sales AS
SELECT ...;
```

- A temporary table is an actual temporary database object, with a lifetime defined by the database/session rules.

### Simplified Comparison

| CTE | Temporary Table |
|---|---|
| Exists for one statement | Can persist for a session/transaction depending on DB |
| Mainly improves query structure | Can be used across multiple statements |
| Usually no explicit creation/drop | Created as a database object |
| Great for multi-step query logic | Useful for intermediate datasets reused across queries |
| Can be recursive | Usually not the same mechanism |

## CTE vs VIEW

### CTE

- Temporary for the statement:

```sql
    WITH sales AS (...)
    SELECT ...
```

### View

- Saved database object:

```sql
    CREATE VIEW sales_view AS
    SELECT ...;
```

- A view can then be queried later:

```sql
    SELECT *
    FROM sales_view;
```

!!! note "Think of it this way"
    **CTE** → temporary query-level abstraction

    **VIEW** → persistent database-level abstraction

## Does CTE Improve Performance?

- This is a trick interview question.

- **Wrong answer**: "Yes, CTEs make queries faster."

- **Not necessarily.** A CTE is primarily a query organization/readability mechanism.

## Can CTEs Contain ORDER BY?

- This is database-specific and has an important conceptual point.

- A relational result does not inherently have an order unless the final result is ordered.

- So this:

```sql
    WITH data AS (
        SELECT *
        FROM employees
        ORDER BY salary DESC
    )

    SELECT *
    FROM data;
```

    should not be relied upon to produce an ordered final result.

- If you want the final output sorted:

```sql
    WITH data AS (
        SELECT *
        FROM employees
    )

    SELECT *
    FROM data
    ORDER BY salary DESC;
```

- The `ORDER BY` belongs to the result you actually want ordered.

- Some SQL dialects allow `ORDER BY` inside a CTE for specific constructs such as `LIMIT`, `TOP`, or similar operations, but don't confuse that with guaranteeing final output order.

## Can CTEs Be Used with INSERT, UPDATE, DELETE?

- Yes, depending on the database.

## Recursive CTE

- Now we get into a senior-level interview topic.

- A recursive CTE references itself.

- **General structure:**

```sql
    WITH RECURSIVE cte_name AS (

        -- Anchor query
        SELECT ...

        UNION ALL

        -- Recursive query
        SELECT ...
        FROM ...
        JOIN cte_name ...
    )
```

### Recursive CTE Example: Numbers

- Suppose we want numbers from 1 to 5.

```sql
    WITH RECURSIVE numbers AS (

        SELECT 1 AS n

        UNION ALL

        SELECT n + 1
        FROM numbers
        WHERE n < 5
    )

    SELECT *
    FROM numbers;
```