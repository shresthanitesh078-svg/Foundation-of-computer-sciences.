-- ============================================================
-- ST4015CMD Foundation of Computer Science
-- Task 3: College Club Management System
-- Database Schema — Third Normal Form (3NF)
-- ============================================================

-- Drop tables if they already exist (for re-running)
DROP TABLE IF EXISTS Membership;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Club;

-- ── Student Table ──────────────────────────────────────────
CREATE TABLE Student (
    StudentID   INT          PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    Email       VARCHAR(150) UNIQUE NOT NULL
);

-- ── Club Table ─────────────────────────────────────────────
CREATE TABLE Club (
    ClubID      INT          PRIMARY KEY,
    ClubName    VARCHAR(100) NOT NULL,
    ClubRoom    VARCHAR(50),
    ClubMentor  VARCHAR(100)
);

-- ── Membership Table (Junction / Bridge Table) ────────────
CREATE TABLE Membership (
    MembershipID INT  PRIMARY KEY,
    StudentID    INT  NOT NULL REFERENCES Student(StudentID) ON DELETE CASCADE,
    ClubID       INT  NOT NULL REFERENCES Club(ClubID)       ON DELETE CASCADE,
    JoinDate     DATE NOT NULL,
    UNIQUE (StudentID, ClubID)   -- A student can only join a club once
);
