### What is SQL?
`SQL stands for Structured Query Language.`

In the absolute simplest terms: SQL is the language used to talk to databases. Think of a database as a massive, super-powered collection of digital Excel spreadsheets stored on a server. If you want to build any modern app or website—like Netflix, Instagram, or an online store—you need a place to store user profiles, passwords, posts, and products. That’s the database.

SQL is the specific tool you use to ask that database questions or tell it what to do.

---

## MySQL (Relational)
`MySQL works with a relational database.` 

This means it organizes data into **tables** consisting of **rows** and **columns** (similar to how you handle rows and columns using lists and dictionaries in Python). 

* **Key concept:** Data is structured, and different tables connect (relate) to one another.

---

## NoSQL (Non-Relational)
`NoSQL is database software that works without traditional tables.`

Instead of rows and columns, NoSQL relies on **flexible data models**. 

* **Key concept:** Data can be stored as documents (which look a lot like Python dictionaries/JSON), key-value pairs, or graphs. It is ideal for unstructured data or when your data structure changes frequently. 

## MYSQL syntax: 
Think of a SQL database like an Excel spreadsheet. `It holds tables with rows and columns.` To talk to the database, we use simple English-like commands to Create, Insert, and Select data.

To start your file.sql, you need to call your HEAD line sql workflow first. By typing the type of sql sturcture you are intended to work with. 

<h1 style="color: green; text-align:center;">INNER JOIN - LEFT JOIN - RIGHT JOIN</h1>

<h2 style="color: white; text-align:left;">1. INNER JOIN</h2>
<p>Returns only the rows where there is a perfect, matching value in both tables. Rows without a match on either side are completely excluded.</p>

<h2 style="color: white; text-align:left;">2. LEFT JOIN</h2>
<p>Returns all rows from the left (first) table, plus any matching rows from the right table. If there is no match for a left row, the right side columns are filled with NULL.</p>

<h2 style="color: white; text-align:left;">3. RIGHT JOIN</h2>
<p>Returns all rows from the right (second) table, plus any matching rows from the left table. If there is no match for a right row, the left side columns are filled with NULL.</p>

<h1 style="color: white; text-align: center;">What is a Subquery?</h1>
<p>A subquery is simply a query inside another query.</p><br>
<p>Think of it like a math equation with parentheses, where you have to solve the inside part first before you can solve the outside part. SQL does the exact same thing: it runs the inner subquery first, gets the result, and then hands that result to the outer main query.</p>

<imp>A Quick Example (Using your GAMERlog Database)</imp>
<p>Imagine you want to find the username of the player who scored the highest score in your Progress table, but you don't know what that highest score actually is. You can use a subquery to find it!</p>

```sql
SELECT username 
FROM Users 
WHERE user_id = (
    -- This is the SUBCONSUlTA (Subquery)
    SELECT user_id 
    FROM Progress 
    ORDER BY score DESC 
    LIMIT 1
);
```
<h3 style="text-style: center;">How SQL executes this:</h3>
<h2 style="text-align: left;">Step 1 (The Inner Query):</h2>
<p>SQL runs the subquery inside the parentheses first to find the user_id with the highest score. Let's say it finds user_id = 2.</p>

<h3 style="text-style: center;">Step 2 (The Outer Query):</h3>
<p>SQL replaces the parentheses with that answer and runs the main query: SELECT username FROM Users WHERE user_id = 2;.</p>

<h1 style="text-align: center;">Joins vs. Subqueries</h1>
<br>
<p>Tutors often teach subqueries right after Joins because they can sometimes be used to solve the same problems.</p><br>

<imp>JOINS</imp><br>
<p>Smash tables together side-by-side so you can see columns from both tables at once.</p>

<imp>SUBQUERIES</imp><br>
<p>Act like a search filter, isolating a specific piece of data from one table to use as a condition for another table.</p>

<p style="text-align: right;" font-style: italic;.>For more information, ask Gemini.</p>
