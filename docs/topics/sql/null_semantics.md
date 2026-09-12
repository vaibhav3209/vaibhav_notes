# NULL Semantics in SQL

SQL follows 3-valued logic:

- TRUE
- UNKNOWN
- FALSE

## Some Logical Operations


NOT UNKNOWN = UNKNOWN
UNKNOWN AND UNKNOWN = UNKNOWN
--- OR --- = ---


 
TRUE AND UNKNOWN = UNKNOWN
TRUE OR UNKNOWN = <Red>TRUE</Red>





## 1. NULL in WHERE

WHERE `only filters` rows that are 'TRUE'.

 
```sql
---
```


 
Improvement:
%sql
- - -




### **Laptop vs. Desktop**

| Feature | Laptop | Desktop |
| :--- | :--- | :--- |
| **Portability** | Highly portable and easy to carry. | Heavy and designed for a fixed location. |
| **Power Source** | Runs on a rechargeable internal battery. | Requires a constant wall outlet connection. |
| **Upgradability** | Limited to RAM and storage upgrades. | Highly customizable with easily swappable parts. |
| **Cost Efficiency** | More expensive for equivalent performance. | Offers higher performance per dollar spent. |


# single likhenge to poora ayega 
 
FALSE AND UNKNOWN = <Red>FALSE</Red>
FALSE OR UNKNOWN = UNKNOWN


## Flow chart



```mermaid
flowchart TD
    A[SQL commands] --> B[DML]
    A --> C[DQL]
    A --> D[DDL]
    A --> E[DQL]
    A --> F[TQL]
```



