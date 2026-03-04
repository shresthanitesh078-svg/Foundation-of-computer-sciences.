-- ============================================================
-- ST4015CMD -- SQL Queries for College Club Management System
-- ============================================================

-- 1. Insert a new student
INSERT INTO Student VALUES (8, 'Priya', 'priya@email.com');

-- 2. Insert a new club
INSERT INTO Club VALUES (5, 'Photography Club', 'Lab2', 'Ms. Kavya');

-- 3. Display all students
SELECT * FROM Student ORDER BY StudentID;

-- 4. Display all clubs
SELECT * FROM Club ORDER BY ClubID;

-- 5. Display all students with their clubs and join dates (JOIN query)
SELECT 
    s.StudentName,
    c.ClubName,
    m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club    c ON m.ClubID    = c.ClubID
ORDER BY s.StudentName, m.JoinDate;

-- 6. Count how many clubs each student has joined
SELECT 
    s.StudentName,
    COUNT(m.ClubID) AS TotalClubs
FROM Student s
LEFT JOIN Membership m ON s.StudentID = m.StudentID
GROUP BY s.StudentName
ORDER BY TotalClubs DESC;

-- 7. Find all members of the Music Club
SELECT s.StudentName, m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club    c ON m.ClubID    = c.ClubID
WHERE c.ClubName = 'Music Club'
ORDER BY m.JoinDate;

-- 8. Update a student email
UPDATE Student SET Email = 'asha.new@email.com' WHERE StudentID = 1;

-- 9. Delete a membership record
DELETE FROM Membership WHERE StudentID = 2 AND ClubID = 2;

-- 10. Display club membership count
SELECT 
    c.ClubName,
    c.ClubRoom,
    c.ClubMentor,
    COUNT(m.StudentID) AS MemberCount
FROM Club c
LEFT JOIN Membership m ON c.ClubID = m.ClubID
GROUP BY c.ClubName, c.ClubRoom, c.ClubMentor
ORDER BY MemberCount DESC;
