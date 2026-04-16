# Project 2 - UTech Events Hub
# Course: CNS1001 - Introduction to Programming
# Date: April 17, 2026
# Lecturer: Mr. Sheldon Gordon
# Group Members:
    Tavar Foster-Davis (2501913)
    Ajahni Thompson (2503732)
    Kaden Faulkner (2501970)
    Javon Morgan (2506304)
---

## Problem Statement

At the University of Technology, managing campus events such as career fairs, workshops, seminars, and student club activities is often done manually using spreadsheets, notice boards, or word-of-mouth. This approach often leads to confusion, missed events, inaccurate attendance records, and difficulty in tracking registrations and capacity limits. As a result, many students and staff miss valuable opportunities, while event organisers struggle to efficiently manage registrations and monitor actual attendance.

To address these challenges, this project introduces **UTech Events Hub**, a simple, centralised command-line application designed specifically for the university environment. The system allows users to create and manage events, register attendees, perform check-ins on the day of the event, view a real-time dashboard of upcoming events, and generate detailed attendance reports. All information is automatically saved and persists between sessions, ensuring reliability and ease of use.

The project focuses on event management functionalities that are practical and relevant to UTech students, lecturers, and administrators, providing a feasible and complete solution to improve event organisation and participation on campus.

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

We used Claude as an assistant while developing this project.

The AI was used for the following types of prompts and queries:
- "Explain syntax and help improve the structure of the event management code"
- "How to sort events by date in a dictionary and display them in a table"
- "Troubleshoot and assist with specific bugs, (example, where renaming an event breaks other edits in the same session)"
- "How to create tables for a dashboard using the rich library, and integrate rich methods/functions into existing code"
- "Explain how to save and load data using a JSON file"

We carefully reviewed every suggestion, tested the code, made necessary modifications, and ensured the logic worked correctly. For example, we manually verified the event renaming and editing functionality, adjusted the dashboard sorting, and confirmed all input validations. 

The final code, including the data structure, validation logic, file handling, and overall program flow, reflects our own understanding. We are able to explain the code during the demonstration. AI was used primarily as a learning and debugging assistant.

---

## Acknowledgement

Thank you for reviewing this project, we look forward to your feedback.
