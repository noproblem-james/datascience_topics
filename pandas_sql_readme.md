# Review of SQL Joins

SQL is a common topic in data science interviews, so make sure you know your joins!!


## Overview

In SQL, the join is the mechanism to combine columns from multiple tables.  To join you must specify a primary key and a foreign key, which are then used to 'match' records between the two tables.

These are the types of joins we will discuss:

1. Inner Join
2. Left Join
3. Right Join
4. Outer Join

Each will be illustrated using a Venn diagram - an imperfect but useful illustration tool for this topic.

## 1. Inner Join

Returns only the records from Table A that have a corresponding record in Table B. 

![Inner join img](https://www.codeproject.com/KB/database/Visual_SQL_Joins/INNER_JOIN.png)

#### Syntax
  >SELECT A.col1, B.col2           
  >FROM table_A   
  >__INNER JOIN__ table_B  
  >ON table_A.key=table_b.key;
  
__Note: This is the default behavior when you query using 'JOIN'.__  Therefore this query will return the same result as the one above:
  
  >SELECT A.col1, B.col2  
  >FROM table_A  
  >__JOIN__ table_B  
  >ON table_A.key=table_b.key;
  
## 2. Left Join 
_AKA 'Left Outer Join'_

Returns all records from Table A plus all records from Table B that have a corresponding record in A.

![Left join img](https://www.codeproject.com/KB/database/Visual_SQL_Joins/LEFT_JOIN.png)

#### Syntax
  >SELECT A.col1, B.col2           
  >FROM table_A   
  >__LEFT JOIN__ table_B  
  >ON table_A.key=table_b.key;

_*So which table is left and which is right?*_

_The table in your 'FROM' statement is the left, and the table in your 'JOIN' statement is the right.  Think of it like writing; you start from the left and move to the right._

  
## 3. Right Join 
_AKA 'Right Outer Join'_

Returns all records from Table B plus all records from Table A that have a corresponding record in B.

![Right join img](https://www.codeproject.com/KB/database/Visual_SQL_Joins/RIGHT_JOIN.png)

#### Syntax
  >SELECT A.col1, B.col2           
  >FROM table_A   
  >__RIGHT JOIN__ table_B  
  >ON table_A.key=table_b.key;
  
  
## 4. Outer Join 
_AKA 'Full Outer Join'_

Returns all records from Table A and Table B.

![Outer join img](https://www.codeproject.com/KB/database/Visual_SQL_Joins/FULL_OUTER_JOIN.png)

#### Syntax
  >SELECT A.col1, B.col2           
  >FROM table_A   
  >__OUTER JOIN__ table_B  
  >ON table_A.key=table_b.key;
  
  
## Summary 
The graphic below shows visualizations of each of the four types covered, in addition to three more that are outside the scope of this review session.
![Visual Representation](https://www.codeproject.com/KB/database/Visual_SQL_Joins/Visual_SQL_JOINS_orig.jpg)

## Other
As indicated by the diagram, there are three other types of joins that are created by adding a 'WHERE __ IS NULL' statement to the end of a Left, Right, or Outer join query.  These are known as an __Excluding__ joins.

Finally, there is one last type of join that is not able to represented by a Venn diagram, which is the Cross Join.  The cross join is a specialized case that creates a Cartesian product of the two tables.

Credit to C.L. Moffatt for his excellent [page and graphics](https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins), which I used as source material for this presentation!
