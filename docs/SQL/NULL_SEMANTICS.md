# NULL Semantics in SQL

SQL follows 3-valued logic:

- TRUE
- UNKNOWN
- FALSE

## Some Logical Operations

:::box left #page1_box1
NOT UNKNOWN = UNKNOWN
UNKNOWN AND UNKNOWN = UNKNOWN
--- OR --- = ---
:::

:::box mid #page1_box2
TRUE AND UNKNOWN = UNKNOWN
TRUE OR UNKNOWN = <Red>TRUE</Red>
:::

:::box right #page1_box3
FALSE AND UNKNOWN = <Red>FALSE</Red>
FALSE OR UNKNOWN = UNKNOWN
:::

## 1. NULL in WHERE

WHERE only filters rows that are 'TRUE'.

:::box left #page1_code1
%sql
- - -
:::

:::arrow:::

:::box right #page1_code2
Improvement:
%sql
- - -
:::

:::box full #page1_box4
Logic: - - -
:::