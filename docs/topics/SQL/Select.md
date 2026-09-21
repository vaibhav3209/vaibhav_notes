## SELECT Clause

### 1. Basic Syntax

```sql
SELECT [col_name / expressions / constants / string literals / functions]
```

You can select any of the above in a `SELECT` statement.

### 2. Why not `SELECT *` ?

It's not used in production.

- Unnecessary columns can be transferred.


- Unnecessary columns can be present in the resultant table.


- Since production has many tables, `SELECT *` can produce a large, ambiguous result.


- There's an added cost of transferring non-required rows/columns.


### 3. Return Value of `SELECT`

| Select Returns  |  |
|-----------------|---------|
| Table           | ❌       |
| Result Set      | ✅       |


- It gives a result set containing the requested rows and columns.


- It can also include additional columns/expressions that were not present in the original table.

### 4. Relational Algebra Mapping

| SQL Clause | Relational Algebra |
|------------|---------------------|
| `SELECT` | **Projection** — selecting attributes from a relation |
| `WHERE` | **Selection** |


| Term       | Mapping |
|------------|---------|
| Degree      | number of columns.       |
| Cardinality | number of rows.       |


### 5. Key Notes on SELECT

- `SELECT` doesn't modify data.


- `SELECT` doesn't sort the result set.


- `SELECT` doesn't remove duplicates.


- Ordering of columns is important.


- Use of alias in `SELECT` vs. other clauses depends on order of execution.


!!! tip "`SELECT` doesn't require a `FROM` clause."


### 6. Tricky Questions(SELECT without FROM)

=== "Q1"

    ```sql
    SELECT 10;
    ```

    | 10 |
    |:---:|
    | 10 |


    ```sql
     SELECT 10.5, 'Hello';
    ```
    (String Columns have comma and result set Doesn;t )

    | 10.5 | `'Hello'` |
    |:---:|:---:|
    | 10.5 | Hello |



    ```sql
    SELECT TRUE;
    ```    

    *(DB-specific: `TRUE`/`FALSE` = `1`/`0`. )*

    | TRUE |
    |:---:|
    | 1 |



    ```sql
    SELECT NULL;
    ```

    | NULL |
    |:---:|
    | NULL |

=== "Q2"

    ```sql
    SELECT 10+20;
    ```

    | 10+20 |
    |:---:|
    | `30` |


    ```sql
    SELECT '10' + '20';
    ```
    *(MySQL: `+` coerces numeric strings → arithmetic. SQL Server: `+` between strings = concatenation → `'1020'`.)*

    | '10' + '20' |
    |:---:|
    | 30 (MySQL only) |


    ```sql
    SELECT 10 + 5 * 2;
    ```

    *(Operator precedence: `*` before `+`.)*

    | 10+5*2 |
    |:---:|
    | 20 |


=== "Q3"
    
    ```sql
    SELECT 10/2, 10.0/2;
    ```
    (Complete Division)

    | | Generic | MySQL |
    |---|:---:|:---:|
    | 10/2 | 5 | 5.0000 |
    | 10.0/2` | 5| 5.00000 |


    ```sql
    SELECT 10/3, 10.0/3;
    ```

    (Incomplete Division)    

    *(MySQL's `/` never truncates to an int — it always returns a decimal, with scale = operand's decimals + 4.)*

    | | Generic (SQL Server) | MySQL |
    |---|:---:|:---:|
    | `10/3` | `3` (int truncation) | `3.3333` |
    | `10.0/3` | `3.333...` (high precision) | `3.33333` |

