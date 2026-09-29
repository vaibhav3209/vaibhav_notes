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


## 2. 