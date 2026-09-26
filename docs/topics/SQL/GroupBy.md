## GROUP BY Clause

### Definition

- Groups similar rows based on one or multiple columns so that aggregate functions (`agg()`) can be applied.

### Key Effects & Purpose

1. Changes the level of detail in the result set by shifting focus from individual rows to collective summaries.

2. Operates as a row/column level operation.

### GROUP BY without Aggregate Functions in SELECT

```sql
SELECT dept
FROM employees
GROUP BY dept;
```

- **Equivalent Query:**

```sql
    SELECT DISTINCT dept
    FROM employees;
```

- **Performance Note**: Using `GROUP BY` without an aggregate function is generally a more expensive query ($$) compared to `SELECT DISTINCT`, which is less expensive.

### GROUP BY with Multiple Columns

- Groups data based on the combination of values across all specified grouping columns.

### Selecting Columns with GROUP BY

- Columns in the `SELECT` list must either be grouped columns (listed in `GROUP BY`) or wrapped inside an aggregate function (`agg()`).

- Selecting non-aggregated columns directly creates ambiguity.

### Ambiguity of Non-Aggregated Columns

- **Problem Scenario:**

```sql
    -- Table Data:
    -- dept | name   | salary
    -- IT   | Rahul  | 50K
    -- IT   | Rahul2 | 30K
    -- IT   | Rahul3 | 60K

    SELECT dept, name
    FROM employees
    GROUP BY dept;
```

- **Explanation**:

    - The result set structure attempts to output `| dept | name |` where `dept = 'IT'` and `name = ??`.
    - SQL cannot determine which specific `name` row value to return for the grouped 'IT' department, leading to query ambiguity or errors.

- **Solution**: Wrap non-grouped columns in aggregate functions like `MAX(name)`, `MIN(name)`, etc.

### GROUP BY with NULL Values

- If the grouping column contains `NULL` values, all `NULL`s are gathered into a single group in SQL.

### Can GROUP BY Contain Expressions?

- **Answer**: Yes.

- **Example 1 (Date Function/Expression):**

```sql
    SELECT YEAR(order_date), COUNT(*)
    FROM orders
    GROUP BY YEAR(order_date);
```

    - Extracts the year from order dates and groups order totals accordingly.

- **Example 2 (String Expression):**

```sql
    SELECT LEFT(type, 1), COUNT(*)
    FROM customers
    GROUP BY type;
    -- Categorizes types like 'Consumer', 'Office', 'Home'
```

    - Grouping can incorporate string transformation functions or expressions.



### GROUP BY with CASE WHEN

- You can use conditional expressions like `CASE WHEN` inside a `GROUP BY` clause to form custom row groupings.

### Can we GROUP BY using Aggregate Functions `agg()`?

- **Answer**: No ✗.

- **Incorrect Example:**

```sql
    GROUP BY SUM(salary) -- ✗ Invalid
```

- **Explanation**: Aggregate functions calculate summaries across groups, so you cannot group by an aggregate function directly within the same `GROUP BY` clause.

### GROUP BY Before Join vs. GROUP BY After Join

- Performing a `GROUP BY` before a join versus after a join (standard approach) can yield different or mismatched result sets (Mismatch होता है - ध्यान रखना).

- **Key Takeaway**: Pay close attention to how join conditions can duplicate rows before aggregation.

### GROUP BY vs. Window Functions (`WINDOW()`)

- **GROUP BY**: Aggregates data and collapses multiple rows into single summary rows.

- **`WINDOW()` functions**: Calculate summary results while preserving row-level details without collapsing rows.

## Advanced GROUP BY: No GROUP BY Clause, But an Aggregate Function `agg()` Is Used

### 1. Querying an Entire Table

- SQL treats the entire table as 1 single group.

- **Example:**

```sql
    SELECT COUNT(*)
    FROM table;
```

### 2. Querying an Empty Table

- Returns 0 for counts.

- **Example:**

```sql
    SELECT COUNT(*)
    FROM table1; -- Output => 0
```

### 3. Selecting Non-Aggregated Columns without GROUP BY

- **Example:**

```sql
    SELECT dept, COUNT(*)
    FROM employees;
```

- **Result**: Error / Invalid Query (`There is no group`) because `dept` cannot be selected alongside an aggregate function when no `GROUP BY` clause is defined.