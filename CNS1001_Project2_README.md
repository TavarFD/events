# Project 2 - UTech Events Hub
# Course: CNS1001 - Introduction to Programming
# Date: April 17, 2026
# Lecturer: Mr. Sheldon Gordon
# Group Members:
    * Tavar Foster-Davis (2501913)
    * Ajahni Thompson (2503732)
    * Kaden Faulkner (2501970)
    * Javon Morgan (2506304)
---

## Problem Statement

Managing events manually can be inefficient and tedious, especially when tracking attendees, capacity, and check-ins. This project provides a command-line application that allows users to view, manage, and run reports for events.

The system is designed for students, staff, and administration, that need a simple tool to organize events, track registrations, and monitor attendance.

---

## Program Description

The UTech Events Hub is a console-based event management system that allows users to:

* Create, edit, and delete events
* Register and cancel attendees
* Check in attendees during events
* View a dashboard of all events
* Generate reports for each event

The program stores data using a JSON file so that event information is saved between sessions. 
The program includes default/mock data so the dashboard does not load blank, this also shows the user the correct input requirements and structure.

---

## Main Features

* Event creation with date, time, location, and capacity
* Edit and rename events
* Delete events
* Register attendees with duplicate prevention
* Cancel registrations
* Check-in system with validation
* Dashboard view sorted by date
* Event reports with attendance statistics
* Data persistence using JSON

---

## Programming Concepts Used

This project demonstrates the following programming concepts:

* Functions: Multiple user-defined functions are used to organize the program
* Conditionals: Used to control program flow and validate input
* Loops: Used for menus and repeated input handling
* Dictionaries and lists:

  * Dictionary is used to store events
  * Lists are used to store attendees and checked-in users
* File handling: JSON is used to save and load event data
* Input validation: Ensures correct formats for date, time, and capacity

---

## Required Libraries

Install the required library before running:

```
pip install rich
```

## How to Run the Program

1. Open a terminal or command prompt
2. Navigate to the project folder:

   ```
   cd events
   ```
3. Run the program:

   ```
   python3 CNS1001_Project2_project.py
   ```
---

## Sample Inputs and Outputs

### Example 1: Create Event

Input:

```
Event name: Tech Workshop  
Date: 18/04/2026  
Time: 14:00  
Location: Lecture Theatre 3  
Capacity: 50  
```

Output:

```
Event 'Tech Workshop' created successfully.
```

---

### Example 2: Dashboard View

The program displays a table showing:

* Event name
* Date
* Time
* Location
* Capacity
* Registered attendees
* Checked-in attendees
* Available spaces
* Status (Open, Full, or Past)

Events are sorted by the closest upcoming date.

---

### Example 3: Event Report

Input:

```
Event name: Career Fair
```

Output includes:

* Event details
* Number of registered attendees
* Number of checked-in attendees
* Attendance rate percentage
* List of attendees with check-in status

---

## Manual Testing and Validation

| Test Case | Description            | Input                                                                             | Expected Output                            | Actual Output                              | Result |
| --------- | ---------------------- | --------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------ | ------ |
| 1         | Valid event creation   | Name: Tech Seminar, Date: 18/04/2026, Time: 14:00, Location: LT3, Capacity: 50   | Event 'Tech Seminar' created successfully  | Event 'Tech Seminar' created successfully  | Pass   |
| 2         | Invalid date format    | 2026-04-18                                                                        | Error message displayed                    | Error message displayed                    | Pass   |
| 3         | Past date              | 01/01/2025                                                                        | Error message displayed                    | Error message displayed                    | Pass   |
| 4         | Event full             | Capacity 2, Register 3                                                    | Event is full                              | Event is full                              | Pass   |
| 5         | Duplicate registration | Same name twice                                                                   | Already registered                         | Already registered                         | Pass   |
| 6         | Check-in unregistered  | Unknown name                                                                      | Not registered for this event              | Not registered for this event              | Pass   |
| 7         | Dashboard sorting      | Multiple events added out of order                                                | Events sorted by soonest date              | Events sorted by soonest date              | Pass   |

## Challenges and Lessons Learned

Challenge 1: Designing a clean console interface:
Using basic print statements made the output difficult to read.

Solution:
The rich library was used to create structured tables and panels.

Lesson learned:
A clear interface improves usability.

Challenge 2: Renaming events while editing:
Renaming an event caused issues when updating other fields.

Solution:
The event reference was refreshed after renaming.

Lesson learned:
Careful handling of dictionary keys is necessary when modifying them.

---

## AI Assistance Disclosure

AI tools (Claude and ChatGPT) were used for:

* Understanding programming concepts
* Debugging issues
* Improving code structure
* Creating a clean user interface using the rich library

---

## Acknowledgement

Thank you for reviewing this project, we look forward to your feedback.
