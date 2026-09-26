## HAVING Clause

- Filter groups after aggregation.

- Primarily used to add `agg()` while filtering (Note: WHERE में नहीं कर सकते).

### Q1: Can we use GROUP BY w/o `HAVING`?

- **Ans**: Yes, when we don't want to filter after aggregation.

### Q2: Can we use `HAVING` w/o GROUP BY?

- **Ans**: Yes.

```sql
    SELECT COUNT(*)
    FROM employees
    HAVING COUNT(*) > 100
```

- Notes:
    - पूरा table result set का 1 group मानेगा.
    - Total rows > 100 ⇒ True.
    - Total rows < 100 ⇒ No rows.

### Q3: Can `HAVING` filter a non-agg. column? / Can `HAVING` be used w/o `agg()`?

- **Ans**: Yes (DB-dependent), but that defies the purpose of `HAVING` (फिर तो WHERE ही use करना).

### Q4: Can `HAVING`, `WHERE` be used together?

- Find employees having `Avg(Salary) > 50K` for "IT" department.

- (समझना)

### Tips

1. When using `COUNT(*)` in `HAVING`, पूरा NULL semantics का ध्यान रखना.

2. `HAVING` w/ Join ⇒ use `COUNT(col-name)`.

### Ques: Find customers who purchased at least 3 DISTINCT products

```sql
SELECT cust_id
FROM orders
GROUP BY cust_id
HAVING COUNT(DISTINCT prod_id) >= 3
```

### Alias in HAVING

- Can't be used (Query Exec. Order).

### HAVING with CASE WHEN AGG()

- Ques: Find customers who made at least 3 purchases & at least one above ₹1000

```sql
    SELECT cust_id
    FROM orders
    GROUP BY cust_id
    HAVING COUNT(*) >= 3
       AND COUNT(CASE WHEN amount > 1000 THEN 1 END) >= 1;
```


## Subqueries with HAVING (WHERE vs HAVING using Subqueries)

### Trick Question 1

```sql
SELECT dept, AVG(salary)
FROM employees
GROUP BY dept
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM employees
);
```

### Query Breakdown

- **Subquery**: Calculates the overall company-wide `AVG(salary)` across all employees and departments.

- **Main Query `AVG(salary)`**: Calculates the department-wise average salary after `GROUP BY dept`.

- **Meaning**: Finds departments whose average salary is greater than the overall company-wide average salary (Group Avg vs. Overall Avg).

### What NOT to do in HAVING

1. **Do not use Window Functions directly in HAVING**:

    - Solution: Use a CTE or subquery instead.

2. **Do not use non-aggregated columns in HAVING**:

    - Incorrect Example: `HAVING dept = 'IT'` or `HAVING salary > 10000`.

    - Correct Approach: Use `WHERE` instead, as non-aggregated conditions belong to the row-filtering stage.

    - Performance Benefit: Using `WHERE` provides better performance because it filters out rows early before grouping occurs.

### Query Execution & Optimization Doubt

- **Scenario:**

```sql
    SELECT dept, COUNT(*)
    FROM employees
    GROUP BY dept
    HAVING COUNT(*) > 10;
```

- **Question**: Is `COUNT(*)` calculated twice (once in `SELECT` and once in `HAVING`)?

- **Answer**: No.

    - The temporary result set is already calculated during the grouping phase with `COUNT(*)`.
    - `HAVING` only compares the already calculated value against `> 10`.
    - Note: The aggregated values are cached/stored in memory (e.g., hash tables) during execution.