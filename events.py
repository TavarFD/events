# ============================================================
# CNS1001 Project 2 - UTech Events Tracker System
# Group #: ______
# Members: _______________________________
# ============================================================

# ===================== GROUP CONTRACT =====================

"""
IMPORTANT: ALL MEMBERS SHOULD FOLLOW THIS EXACT STRUCTURE

events = {
    "Event Name": {
        "date": "YYYY-MM-DD",
        "time": "HH:MM",
        "location": "String",
        "capacity": int,
        "attendees": [],       # list of names
        "checked_in": [],      # list of names
        "seats": {}            # {"Name": seat_number}
    }
}

RULES:
- DO NOT rename keys (e.g. attendees, checked_in, etc.)
- DO NOT change structure.
- ALL functions must use this structure
"""

# ===================== GLOBAL DATA =====================

events = {}

# ===================== MOCK DATA (FOR TESTING) =====================
# Each member can use this to test independently

def load_mock_data():
    global events
    events = {
        "Career Fair": {
            "date": "2026-04-20",
            "time": "10:00",
            "location": "UTech Auditorium",
            "capacity": 2,
            "attendees": [],
            "checked_in": [],
            "seats": {}
        }
    }

# ============================================================
# TAVAR — EVENT MANAGEMENT
# ============================================================

def create_event():
    """
    INPUT:
        User enters event details

    PROCESS:
        Create new event using contract structure

    OUTPUT:
        Event added to 'events' dictionary
    """
    pass


def view_all_events():
    """
    OUTPUT:
        Print all event names and basic info
    """
    pass


def view_event_details():
    """
    INPUT:
        event_name

    OUTPUT:
        Display full event details
    """
    pass


# ============================================================
# JAVON — REGISTRATION SYSTEM
# ============================================================

def register_attendee():
    """
    INPUT:
        event_name, attendee_name

    RULES:
        - Event must exist
        - No duplicate attendees
        - Must not exceed capacity

    OUTPUT:
        Adds attendee to events[event]["attendees"]
    """
    pass


def cancel_registration():
    """
    INPUT:
        event_name, attendee_name

    OUTPUT:
        Remove attendee from attendees list
    """
    pass


# ============================================================
# AJAHNI — CHECK-IN + SEAT ASSIGNMENT
# ============================================================

def check_in_attendee():
    """
    INPUT:
        event_name, attendee_name

    RULES:
        - Must be registered first
        - No duplicate check-in

    OUTPUT:
        Adds attendee to checked_in list
        Calls assign_seat()
    """
    pass


def assign_seat(event_name, attendee):
    """
    PROCESS:
        Assign next available seat number

    OUTPUT:
        events[event]["seats"][attendee] = seat_number
    """
    pass


# ============================================================
# KADEN — REPORTS & SUMMARY
# ============================================================

def generate_event_report():
    """
    INPUT:
        event_name

    OUTPUT:
        Display:
        - Date / Time / Location
        - Capacity
        - Total registered
        - Total checked-in
        - Available spots
        - Attendance rate (%)
    """
    pass


# ============================================================
# UTILITY FUNCTIONS (SHARED)
# ============================================================

def event_exists(event_name):
    return event_name in events


def get_event_choice():
    """
    PROMPT user for event name
    VALIDATE event exists
    RETURN valid event name
    """
    pass


# ============================================================
# MAIN MENU SYSTEM (INTEGRATION POINT)
# ============================================================

def main():
    # Optional: load mock data for testing
    # Comment out when using real input
    load_mock_data()

    while True:
        print("\n===== UTech Events Tracker =====")
        print("1. Create Event")
        print("2. View All Events")
        print("3. View Event Details")
        print("4. Register for Event")
        print("5. Cancel Registration")
        print("6. Check-In to Event")
        print("7. View Event Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_event()
        elif choice == "2":
            view_all_events()
        elif choice == "3":
            view_event_details()
        elif choice == "4":
            register_attendee()
        elif choice == "5":
            cancel_registration()
        elif choice == "6":
            check_in_attendee()
        elif choice == "7":
            generate_event_report()
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()