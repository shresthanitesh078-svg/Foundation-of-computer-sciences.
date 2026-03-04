# ST4015CMD — Foundation of Computer Science
## Investigation and Analysis of Computing Data for Data Management

**Softwarica College of IT & E-Commerce | In collaboration with Coventry University**  
**Module Code:** ST4015CMD  
**Due Date:** 5th March 2026  

---

## Repository Contents

| File | Description |
|------|-------------|
| `schema.sql` | SQL to create all 3 normalised tables (Student, Club, Membership) |
| `seed_data.sql` | SQL to insert all original data from the assignment brief |
| `queries.sql` | All required SQL queries including INSERT, SELECT, and JOIN |
| `seating_solver.py` | Python script demonstrating Brute Force vs Heuristic seating solver |
| `README.md` | This file — explains how to interpret and run all work |

---

## Task 1: Encoding Formats and Protocol Integration

This task is covered fully in the written report. Key concepts include:

- **Base64** — converts binary to ASCII text for safe transmission over SMTP/HTTP
- **URL Encoding** — percent-encodes special characters in URLs and query strings  
- **ASCII** — the foundational 128-character encoding for text-based protocols
- **TLS/HTTPS** — encrypts encoded payloads to provide confidentiality
- **Security risks** — Base64 obfuscation used to bypass antivirus and WAFs

See Figure 1 in the report for the full encoding/protocol data flow diagram.

---

## Task 2: Seating Arrangement — P vs NP

### How to Run the Seating Solver

**Requirements:** Python 3.x (no external libraries needed)

```bash
python seating_solver.py
```

### What the Script Does

1. **Complexity Demo** — shows how n! grows and why brute force fails for large n
2. **Brute Force** — generates all permutations, checks each against constraints
3. **Heuristic** — greedy placement (most-constrained first) + local swap improvement

### Sample Output
```
n= 5  | n! = 120              | ~0.0000 seconds   (feasible)
n=10  | n! = 3,628,800        | ~0.0036 seconds   (OK)
n=15  | n! = 1,307,674,368,000| ~21.79 minutes    (slow)
n=20  | n! = 2.4 quintillion  | ~77 years         (impossible)

Brute Force: ['Alice', 'Eve', 'Charlie', 'Diana', 'Bob'] — Valid: True
Heuristic:   ['Bob', 'Diana', 'Charlie', 'Eve', 'Alice'] — Valid: True
```

---

## Task 3: College Club Database — SQL

### How to Run the SQL Files

Using any SQL client (MySQL, PostgreSQL, SQLite, or DB Browser):

```sql
-- Step 1: Create tables
source schema.sql

-- Step 2: Insert data  
source seed_data.sql

-- Step 3: Run queries
source queries.sql
```

### Database Schema (3NF)

```
Student        Club           Membership
-----------    -----------    ------------------
StudentID PK   ClubID    PK   MembershipID PK
StudentName    ClubName       StudentID    FK → Student
Email          ClubRoom       ClubID       FK → Club
               ClubMentor     JoinDate
```

### Key SQL Queries Explained

**INSERT new student:**
```sql
INSERT INTO Student VALUES (8, 'Priya', 'priya@email.com');
```

**SELECT all students:**
```sql
SELECT * FROM Student ORDER BY StudentID;
```

**Three-table JOIN (Student + Club + Membership):**
```sql
SELECT s.StudentName, c.ClubName, m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club    c ON m.ClubID    = c.ClubID
ORDER BY s.StudentName;
```

**Why JOIN is needed after normalisation:**  
After normalisation, related data lives in separate tables. JOIN reunites the data at query time using foreign key relationships, giving us complete meaningful results without storing redundant copies of data.

---

## Normalisation Summary

| Stage | Description | Tables |
|-------|-------------|--------|
| UNF | All data in one flat table | 1 table — redundancy and anomalies |
| 1NF | Atomic values, composite PK | 1 table — (StudentID + ClubName) key |
| 2NF | Remove partial dependencies | 3 tables — Student, Club, Membership |
| 3NF | Remove transitive dependencies | 3 tables — fully clean schema |

---

## References

- Cormen et al. (2009) *Introduction to Algorithms*. MIT Press.
- Elmasri & Navathe (2016) *Fundamentals of Database Systems*. Pearson.
- Stallings (2017) *Network Security Essentials*. Pearson.
- Sipser (2012) *Introduction to the Theory of Computation*. Cengage.
- OWASP (2021) *OWASP Testing Guide v4.2*. owasp.org
