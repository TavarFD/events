"""
Project 2 - UTech Events Hub
Course: CNS1001 - Introduction to Programming
Date: April 17, 2026
Lecturer: Mr. Sheldon H. Gordon
Group Members:
    Tavar Foster-Davis  (2501913)
    Ajahni Thompson     (2503732)
    Kaden Faulkner      (2501970)
    Javon Morgan        (2506304)
"""


# IMPORT REQUIRED MODULES

import json
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box
from rich.align import Align

# GLOBAL VARIABLES
events = {}
console = Console()

# SAVE / LOAD
def save_data():
    try:
        with open("events_data.json", "w") as f:
            json.dump(events, f, indent=4)
    except Exception as e:
        console.print(f"[red]Error saving data: {e}[/red]")

def load_data():
    global events
    if os.path.exists("events_data.json"):
        try:
            with open("events_data.json", "r") as f:
                events = json.load(f)
            console.print("[green]Saved events loaded.[/green]")
        except Exception as e:
            console.print(f"[red]Error loading data: {e}[/red]")
            events = {}
    else:
        console.print("[dim]No saved data found.[/dim]")

# DEFAULT EVENT DATA
def load_mock_data():
    global events
    events = {
        "Career Fair": {
            "date": "20/04/2026",
            "time": "10:00",
            "location": "UTech Auditorium",
            "capacity": 200,
            "attendees": [],
            "checked_in": []
        }
    }

# DISPLAY
def print_header():
    title_text = "[bold blue]UTech Events Hub[/bold blue]"
    aligned_title = Align.center(title_text, vertical="middle")
    console.print(
        Panel(
            aligned_title,
            border_style="blue",
            padding=(1, 4),
            box=box.ROUNDED,
            expand=True
        )
    )

def view_dashboard():
    if not events:
        console.print("[yellow]No events available.[/yellow]")
        return

    today = datetime.now().date()

    # Sort events by date (soonest first)
    sorted_events = sorted(
        events.items(),
        key=lambda x: datetime.strptime(x[1]["date"], "%d/%m/%Y").date()
    )

    table = Table(
        title="Events Dashboard", 
        box=box.ROUNDED, 
        border_style="blue",
        expand=True,
        title_style="bold"
    )
    table.add_column("Event", style="bold", ratio=2)
    table.add_column("Date", ratio=1)
    table.add_column("Time", ratio=1)
    table.add_column("Location", style="dim", ratio=2)
    table.add_column("Capacity", justify="center", ratio=1)
    table.add_column("Registered", justify="center", ratio=1)
    table.add_column("Checked In", justify="center", ratio=1)
    table.add_column("Available", justify="center", ratio=1)
    table.add_column("Status", justify="center", ratio=1)

    for name, e in sorted_events:
        registered = len(e["attendees"])
        checked_in = len(e["checked_in"])
        cap = e["capacity"]
        event_date = datetime.strptime(e["date"], "%d/%m/%Y").date()

        capacity_show = str(cap) if cap else "∞"
        available = str(cap - registered) if cap else "∞"

        if event_date < today:
            status = "[dim]Past[/dim]"
        elif cap and registered >= cap:
            status = "[red]Full[/red]"
        else:
            status = "[green]Open[/green]"

        table.add_row(name, e["date"], e["time"], e["location"], 
                      capacity_show, str(registered), str(checked_in), 
                      available, status)

    console.print(table)

# EVENT MANAGEMENT
def create_event():
    console.print(Panel("[bold cyan]Add New Event[/bold cyan]", border_style="cyan", expand=True))
    
    name = Prompt.ask("[bold]Event name[/bold]").strip()
    if not name:
        console.print("[red]Name cannot be empty.[/red]")
        return
    if name in events:
        console.print("[red]Event already exists.[/red]")
        return

    while True:
        date = Prompt.ask("[bold]Date (DD/MM/YYYY)[/bold]").strip()
        try:
            d = datetime.strptime(date, "%d/%m/%Y").date()
            if d >= datetime.now().date():
                break
            console.print("[red]Date must be today or in the future.[/red]")
        except Exception:
            console.print("[red]Invalid date format. Use DD/MM/YYYY.[/red]")

    while True:
        time = Prompt.ask("[bold]Time (HH:MM)[/bold]").strip()
        if len(time) == 5 and time[2] == ":" and time[:2].isdigit() and time[3:].isdigit():
            break
        console.print("[red]Invalid time. Use HH:MM format.[/red]")

    location = Prompt.ask("[bold]Location[/bold]").strip()
    if not location:
        console.print("[red]Location cannot be empty.[/red]")
        return

    while True:
        cap_str = Prompt.ask("[bold]Capacity (0 = unlimited)[/bold]").strip()
        try:
            capacity = int(cap_str)
            if capacity >= 0:
                break
            console.print("[red]Capacity cannot be negative.[/red]")
        except Exception:
            console.print("[red]Please enter a valid number.[/red]")

    events[name] = {
        "date": date,
        "time": time,
        "location": location,
        "capacity": capacity,
        "attendees": [],
        "checked_in": []
    }
    save_data()
    console.print(f"[green]Event '{name}' created successfully.[/green]")

def edit_event():
    if not events:
        console.print("[yellow]No events to edit.[/yellow]")
        return

    console.print(Panel("[bold cyan]Edit Event[/bold cyan]", border_style="cyan", expand=True))
    name = Prompt.ask("[bold]Enter event name[/bold]").strip()
    if name not in events:
        console.print("[red]Event not found.[/red]")
        return

    e = events[name]
    console.print("[dim]Press Enter to keep current value[/dim]")

    new_name = Prompt.ask(f"New name (current: {name})", default=name).strip()
    if new_name and new_name != name:
        events[new_name] = events.pop(name)
        console.print(f"[green]Event '{name}' renamed to '{new_name}'[/green]")
        name = new_name
        e = events[name]          # Refresh reference after rename

    new_date = Prompt.ask(f"New date (current: {e['date']})", default="").strip()
    if new_date:
        try:
            d = datetime.strptime(new_date, "%d/%m/%Y").date()
            if d >= datetime.now().date():
                e["date"] = new_date
            else:
                console.print("[yellow]Invalid date - kept original.[/yellow]")
        except Exception:
            console.print("[yellow]Invalid date - kept original.[/yellow]")

    new_time = Prompt.ask(f"New time (current: {e['time']})", default="").strip()
    if new_time and len(new_time) == 5 and new_time[2] == ":" and new_time[:2].isdigit() and new_time[3:].isdigit():
        e["time"] = new_time
    elif new_time:
        console.print("[yellow]Invalid time - kept original.[/yellow]")

    new_loc = Prompt.ask(f"New location (current: {e['location']})", default="").strip()
    if new_loc:
        e["location"] = new_loc

    new_cap = Prompt.ask(f"New capacity (current: {e['capacity']})", default="").strip()
    if new_cap:
        try:
            cap = int(new_cap)
            if cap >= 0:
                e["capacity"] = cap
            else:
                console.print("[yellow]Invalid capacity - kept original.[/yellow]")
        except Exception:
            console.print("[yellow]Invalid capacity - kept original.[/yellow]")

    save_data()
    console.print("[green]Event updated.[/green]")

def delete_event():
    if not events:
        console.print("[yellow]No events available.[/yellow]")
        return

    console.print(Panel("[bold red]Delete Event[/bold red]", border_style="red", expand=True))
    name = Prompt.ask("[bold]Enter event name[/bold]").strip()
    if name not in events:
        console.print("[red]Event not found.[/red]")
        return

    confirm = Prompt.ask(f"Type YES to delete '{name}'", default="").strip()
    if confirm == "YES":
        del events[name]
        save_data()
        console.print("[green]Event deleted.[/green]")
    else:
        console.print("[dim]Cancelled.[/dim]")

def manage_events():
    while True:
        console.print(Panel("[bold]Manage Events[/bold]", border_style="cyan", expand=True))
        console.print("1. Add Event")
        console.print("2. Edit Event")
        console.print("3. Delete Event")
        console.print("4. Back to Main Menu")
        
        choice = Prompt.ask("[bold]Choice[/bold]").strip()
        
        if choice == "1":
            create_event()
        elif choice == "2":
            edit_event()
        elif choice == "3":
            delete_event()
        elif choice == "4":
            return
        else:
            console.print("[red]Invalid choice.[/red]")

# REGISTRATION
def register_attendee():
    if not events:
        console.print("[yellow]No events available.[/yellow]")
        return

    console.print(Panel("[bold cyan]Register for Event[/bold cyan]", border_style="cyan", expand=True))
    name = Prompt.ask("[bold]Event name[/bold]").strip()
    if name not in events:
        console.print("[red]Event not found.[/red]")
        return

    e = events[name]
    if e["capacity"] and len(e["attendees"]) >= e["capacity"]:
        console.print("[red]Event is full.[/red]")
        return

    attendee = Prompt.ask("[bold]Attendee name[/bold]").strip()
    if not attendee:
        console.print("[red]Name cannot be empty.[/red]")
        return
    if attendee in e["attendees"]:
        console.print("[yellow]Already registered.[/yellow]")
        return

    e["attendees"].append(attendee)
    save_data()
    console.print(f"[green]{attendee} registered for '{name}'.[/green]")

def cancel_registration():
    if not events:
        console.print("[yellow]No events available.[/yellow]")
        return

    console.print(Panel("[bold yellow]Cancel Registration[/bold yellow]", border_style="yellow", expand=True))
    event_name = Prompt.ask("[bold]Event name[/bold]").strip()
    if event_name not in events:
        console.print("[red]Event not found.[/red]")
        return

    attendee = Prompt.ask("[bold]Attendee name[/bold]").strip()
    if attendee in events[event_name]["attendees"]:
        events[event_name]["attendees"].remove(attendee)
        save_data()
        console.print(f"[green]Registration cancelled for {attendee}.[/green]")
    else:
        console.print("[red]Name not found.[/red]")

# CHECK-IN
def check_in_attendee():
    if not events:
        console.print("[yellow]No events available.[/yellow]")
        return

    console.print(Panel("[bold cyan]Check-In[/bold cyan]", border_style="cyan", expand=True))
    event_name = Prompt.ask("[bold]Event name[/bold]").strip()
    if event_name not in events:
        console.print("[red]Event not found.[/red]")
        return

    attendee = Prompt.ask("[bold]Attendee name[/bold]").strip()
    e = events[event_name]

    if attendee not in e["attendees"]:
        console.print("[red]Not registered for this event.[/red]")
    elif attendee in e["checked_in"]:
        console.print("[yellow]Already checked in.[/yellow]")
    else:
        e["checked_in"].append(attendee)
        save_data()
        console.print(f"[green]{attendee} checked in successfully.[/green]")

# EVENT REPORTS
def generate_event_report():
    if not events:
        console.print("[yellow]No events available.[/yellow]")
        return

    console.print(Panel("[bold cyan]Event Report[/bold cyan]", border_style="cyan", expand=True))
    name = Prompt.ask("[bold]Enter event name[/bold]").strip()
    if name not in events:
        console.print("[red]Event not found.[/red]")
        return

    e = events[name]
    registered = len(e["attendees"])
    checked = len(e["checked_in"])
    cap = e["capacity"]

    rate = (checked / registered * 100) if registered > 0 else 0
    usage = (registered / cap * 100) if cap > 0 else 0

    console.print(f"\n[bold]Report for: {name}[/bold]")
    console.print(f"Date: {e['date']}   Time: {e['time']}")
    console.print(f"Location: {e['location']}")
    console.print(f"Capacity: {cap if cap else 'Unlimited'}")
    console.print(f"Registered: {registered}   Checked In: {checked}")
    console.print(f"Attendance Rate: {rate:.1f}%")
    if cap:
        console.print(f"Capacity Usage: {usage:.1f}%")

    console.print("\n[bold]Attendees:[/bold]")
    if not e["attendees"]:
        console.print("No one registered yet.")
        return

    table = Table(show_lines=True, box=box.SIMPLE, expand=True)
    table.add_column("No.", ratio=1)
    table.add_column("Name", ratio=3)
    table.add_column("Status", justify="center", ratio=1)

    for i, person in enumerate(e["attendees"], 1):
        status = "[green]✓[/green]" if person in e["checked_in"] else "[red]✗[/red]"
        table.add_row(str(i), person, status)

    console.print(table)

# MAIN
def main():
    load_data()
    if not events:
        load_mock_data()
        save_data()

    while True:
        console.clear()
        print_header()
        view_dashboard()

        console.print(Panel("[bold]Main Menu[/bold]", border_style="blue", expand=True))
        console.print("1. Manage Events")
        console.print("2. Register Attendee")
        console.print("3. Cancel Registration")
        console.print("4. Check-In Attendee")
        console.print("5. View Event Report")
        console.print("6. Exit")

        choice = Prompt.ask("[bold]Enter your choice[/bold]").strip()

        if choice == "1":
            manage_events()
        elif choice == "2":
            register_attendee()
        elif choice == "3":
            cancel_registration()
        elif choice == "4":
            check_in_attendee()
        elif choice == "5":
            generate_event_report()
        elif choice == "6":
            save_data()
            console.print("[dim]Thank you for using UTech Events Hub![/dim]")
            break
        else:
            console.print("[red]Invalid choice.[/red]")

if __name__ == "__main__":
    main()