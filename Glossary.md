### 1. Page Break

**Syntax**:

    ::page break::

Use:

- Splits content into separate paginated "pages".
- Put it wherever one physical page of notes should end.
- Page numbers are auto handled by javascript.


### 2. Colored Text

**Syntax**:

    <Red> For importatnt notes</Red>

    <Blue>For a casual / side note</Blue>

Use:
- Don't nest colors inside each other. 


### 3. Box

**Syntax**:

- Create a full box

        ::box
        [write anything, 
        any number of lines]
        ::

 
- Two box syntax used simultaneously , can lead to side by side boxes.

        ::box
        [box 1 content]
        ::

        [can only have new lines or empty spaces in between]

        ::box
        [box 2 content]
        ::



Use:

- A positioned callout box for a definition, a side-comment, or a highlighted snippet 
that should visually sit apart from the main flow of the page.



### 5. Diagrams — Mermaid

**Syntax**

        ```mermaid
            [specific syntax for chart]
        ``` 


Use:
- Anything that's actually a graph — flowcharts, decision trees, and classification charts.
- refer the documentation: https://mermaid.js.org/intro/


### 6. Images:

- Not a tag — just a convention. Keep images next to the markdown file that uses them:

```
docs/
  sql/
    joins.md
    images/
      image.png
```

- Reference with a relative path: `![Image text](images/image.png).` 



### 7. Comparision tables:

- Follow same format as markdown and rendered automatically in mkdocs Torillic theme. 