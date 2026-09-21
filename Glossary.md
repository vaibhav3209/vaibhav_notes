## Deploy:

1. See changes on LOCAL server once. 

     ```bash
     mkdocs serve
     ```

2. Open in GIT BASH in parent `Notes/` folder.


3. Use command in `Notes/` directory where `deploy.sh` file is present. 

    ```bash
    bash deploy.sh <remote-name> "commit message"
    ```
   
---

## Keywords For Mkdocs Styling 

- Tags For Leetcode Questions: 
   
  `<a id="leetcode-<questionnumber>"></a>`

   Usage in file: [docs/topics/sql/leetcode_sql.md](docs/topics/SQL/LeetcodeSQL.md)


- Using `Mermaid` library for flow charts, graphs, etc. 
   see [Mermaid Documentation](https://mermaid.js.org/intro/)


- **Admonitions**

   - `!!! note "texxt"`, `!!!question "texxt" `, `!!! tip "texxt"` etc make 

      special boxes when rendered in MKDocs. 

   - `??? note "texxt" ` makes **collapsible** sections.

   - `=== "tab name"` forms tab like GFG editorials
   
      for Multiple languages code. We can add different 
  
      methods for an ans.


- 