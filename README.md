# Class Attendance Tracker

## Project #3 - Daily Topic Project

A simple Python CLI (Command-Line Interface) program that tracks student attendance, counts absences, identifies students who need intervention, and calculates the average number of absences across all students.

---

## Problem Statement

Teachers and school administrators may need to manually check attendance records to determine which students have excessive absences.

This project provides a simple command-line tool that:

- Stores student names in a list.
- Stores attendance records for each student.
- Counts the number of absent days for every student.
- Flags students who have 3 or more absences.
- Displays each student's attendance summary.
- Displays the students who need intervention.
- Calculates the average number of absences across all students.

The project is designed to practice Python loops and basic programming concepts.

---

## Target Users

This tool is intended for:

- Teachers
- School administrators
- Anyone who wants a simple attendance tracking program

---

## Features

The program provides the following features:

1. Stores multiple students using a list.
2. Stores attendance records using nested lists.
3. Processes every student using a `for` loop.
4. Processes every attendance record using a nested `for` loop.
5. Uses `enumerate()` to work with indexes and numbering.
6. Uses `continue` to skip unexpected attendance values.
7. Counts absences for each student.
8. Flags students with 3 or more absences.
9. Stores student status separately.
10. Calculates the total number of absences using a loop-based accumulator.
11. Calculates the average number of absences.
12. Uses `for...else` to handle the case where no student needs intervention.
13. Displays a final list of students requiring intervention.

---

## Attendance Rules

Each attendance record must normally be one of the following:

```text
present
absent
