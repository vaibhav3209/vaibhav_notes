[← Back to list](List.md#linkedlist)

### 4.1 What are Linked Lists?

!!! danger "Don't Say"
    Linked Lists are linear Data Structures...... OR 
    Stored Linearly in memory.


!!! tip "Say"
    
    1. Linked Lists are Data structres that store data in form of Nodes,
        along with reference to the next node.

    2. It can only access data in sequential manner, forward for singly L.L.

    3. It has 2 components: 

        -> `val` : can store any data type [in PYTHON]

        -> `next` : pointer to next node



### 4.2 WHy was  Linked Lists developed ?

| Array limitation                                        | 	How linked list helps                              |
|---------------------------------------------------------|-----------------------------------------------------|
| Fixed size, or costly resizing (copy to a bigger block) | 	 Grows and shrinks one node at a time.             |
| Needs contiguous memory	                                | Nodes can be anywhere in memory, linked by pointers |
| Insert/delete in the middle shifts elements, O(n)       | 	O(1) once you have a reference to the position     |
| Wasted capacity from over-allocation                    | 	Allocates exactly what is needed                   |



### 4.3 Array vs Linked List (Python Specific)
| Arrays                                                                                                               | Linked List                                                           |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Elements stored in contigous memory locations and indexed access.                                                    | Elements stored in non contigous locations and accessed via pointers. |
| Linear and Binary Search possible.                                                                                   | Only linear search intuitively.                                       |
| Acessing : O(1)<br/>   Insert at end : O(1)<br/> Delete at end : O(1) <br/>Insert/Delete at start: O(n) [Ammortized] | O(1) if Position is known.<br/> O(n) from head pointer.               |
| Memory is allocated one time ==>> can need resizing                                                                  | Memory allocated upon creation ==>> No resiszing concept.             |
| Memory (per element) is **less**.                                                                                    | Memory (per element) is More.                                         |
| Bettter **Cache Locality**. ==>> Cache Friendly (since contigouus stored)                                            | Poor Cache locality. ==>> **Not** cache riendly.                      |


### 4.4 Applications of Linked List

- Implementing other Data structures like:

  - Queue / Deque(Doubly LL)

  - Hash table collision buckets.

  - Stacks

  - Adjacency Lists in Graphs

- Music Playback back and forth, Browser Navigation, File System
Navigation etc.

- Job Scheduling in OS.

