## 1. Tell difference between DBMS and RDBMS?

!!! tip "Keep your ans Short"

=== "DBMS"

    - A DBMS is software used to store, retrieve, and manage data — typically 
    in the form of individual files. 
    
    
    - These files are isolated, meaning there's no inherent relationship 
    between them, and no built-in mechanism to enforce data integrity or consistency
    across files.
    
    
    
    - Example, Storing data in flat files like text or CSV. 
    
    
    - Other examples include IBM's IMS (hierarchical DBMS) and network-model 
    databases like IDMS.
    
    
    **Disadvantage:** 
    
    Consider a school storing student data — one file for personal 
    details, one for class/academic records, and one for financial/fee records.
    
    Since these files are isolated, there's no way to enforce referential integrity .
    
    - We can have corrupted Records, mismatched Data
    
    
    - One change has to be manually propagated to multiple files
    
    
    - Retrieving combined information also requires manually opening and 
    referencing multiple files.
    
    
    - There's also no built-in concurrency control, so if two people edit 
    the same file simultaneously, data can get corrupted or overwritten.
    
    
    **Advantage:** 
    
    - DBMS is simple, lightweight, and low-overhead 
    
      - This makes it a reasonable choice for small-scale, single-user,
      or simple read/write use cases. 


=== "Relational DBMS "

    - RDBMS stores data in the form of tables (relations), where each table has rows
    and columns,
    
    
    - Tables can be linked to each other using keys — Primary Key (PK) to uniquely 
    identify a record, and Foreign Key (FK) to reference a record in another table,
    enforcing referential integrity.
    
    
    Other critical features:
    
    - **ACID compliance** — ensures transactions are processed reliably, even in 
    case of failures.
    
    
    - **Concurrency control** — multiple users can read/write data simultaneously
    without conflicts, using locking or MVCC (Multi-Version Concurrency Control).
    
    
    - **Security & authorization** — granular control over who can access or modify
    specific data (roles, permissions, grants).
    
    
    - **Data normalization** — reduces redundancy by organizing data efficiently 
    across related tables.
    
    
    - **Fast retrieval** — via indexing and optimized query engines (using SQL).
    
    
    Examples of RDBMS: MySQL, PostgreSQL, MS SQL Server, Oracle, SQLite.

---

## 2. Primary and Foreign Keys in SQL 

**What is a Key in a Database?**

- A **key** is a column (or set of columns) used to uniquely identify a row in a
table, or to establish a relationship between two tables. 

- Keys enforce data integrity 

- They are the basis for indexing and joins.


**Primary Key**

- Identifies each record in a table uniquely.

- Must be **UNIQUE**.

- Must be **NOT NULL**. 

- Automatically creates a **Clustered Index** in most engines 
(e.g., InnoDB) — the table's physical row storage is sorted by the PK.

  
- A table can have **only one PRIMARY KEY constraint**.
    That constraint can span **multiple columns** — called a **composite key**.


- **Column order matters** in a composite key:
  - The index is sorted by the first column, then the second within each first-column value.
  - A query filtering only on the *first* column uses the index efficiently.
  - A query filtering only on the *second* column generally **cannot** use the index efficiently.
  - Rule of thumb: put the higher-selectivity / most commonly filtered-alone column first.



`UNIQUE NOT NULL` Column vs Primary Key

| Aspect | Primary Key | `UNIQUE NOT NULL`                                                                            |
|---|---|----------------------------------------------------------------------------------------------|
| Count per table | Only one | Multiple allowed                                                                             |
| Index type (InnoDB) | Clustered — row data lives in the index leaf nodes | Secondary — leaf nodes store the value + PK, requiring a second lookup to fetch the full row |
| FK reference target | Yes | Yes — FKs *can* reference a UNIQUE column too.                                               |



**Foreign Key (FK)**
- A column in one table that references the PK (or a UNIQUE column) of another table, establishing a relationship.

- **Can a FK be null?** Yes — if the relationship is *optional*.
  - Example: `employees(employee_id PK, manager_id FK → employees.employee_id)`. The CEO has no manager, so `manager_id` is `NULL`.
  - Enforce `NOT NULL` on the FK only when the relationship is *mandatory* (e.g., every `order` must belong to a `customer`).
- Note: the column being *referenced* (the PK/UNIQUE column in the parent) must itself be NOT NULL — that's a separate rule about the parent key, not the FK.

---

## 6. What If a Table Has Zero Primary Keys?
- Valid SQL — a table can be created without a PK.
- Consequences:
  - No guaranteed unique row identifier.
  - `UPDATE` / `DELETE` statements can unintentionally affect **multiple duplicate-looking rows** if the `WHERE` clause isn't airtight, since there's nothing forcing row uniqueness.
  - Row-based replication (e.g., MySQL) performs worse — it must match full rows instead of doing a single index lookup.
- Best practice: every table should have a PK, even if it's just a surrogate auto-increment `id`.

---

## 7. Why Avoid an Updatable Primary Key (e.g., Email)
- A PK is meant to be a **stable, permanent identifier**.
- Natural keys like `email` can change (user updates their email) — updating a PK value:
  - Requires `ON UPDATE CASCADE` to propagate to every child table's FK, or it fails.
  - Risks breaking referential integrity if cascading isn't configured.
- **Surrogate keys** (auto-increment ID, UUID) are preferred because they have no business meaning and never need to change — the `email` itself can then be stored as a `UNIQUE` (alternate key) column instead.

---

## 8. Self-Referencing Foreign Key
A FK that references the **primary key of its own table**.

**Example:**
```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name        VARCHAR(100),
    manager_id  INT NULL,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
```
Models an org hierarchy — every employee's `manager_id` points to another row in the same table. `manager_id` is nullable for the top of the hierarchy (e.g., the CEO has no manager).

---

## 9. Creating Relationships Using Keys

### One-to-One
Put a FK in one table that is *also* marked `UNIQUE` (not just indexed) — this prevents more than one matching row on the child side.
```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name    VARCHAR(100)
);

CREATE TABLE user_profiles (
    profile_id INT PRIMARY KEY,
    user_id    INT UNIQUE,           -- UNIQUE enforces one-to-one
    bio        TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

### One-to-Many
A plain FK (no UNIQUE constraint) on the "many" side — allows multiple child rows to reference the same parent.
```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name        VARCHAR(100)
);

CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT,                 -- no UNIQUE — many orders per customer
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

### Many-to-Many
Requires a **junction / bridge table** with two FKs — one to each parent table — usually combined as a composite PK.
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name       VARCHAR(100)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    title     VARCHAR(100)
);

CREATE TABLE student_courses (        -- junction table
    student_id INT,
    course_id  INT,
    PRIMARY KEY (student_id, course_id),   -- composite key
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)
);
```