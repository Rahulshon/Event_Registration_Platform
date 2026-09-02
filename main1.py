
# ================================
# EventSphere - Milestone 1
# Simple Python Console Project
# ================================

class Event:
    def __init__(self, event_id, name, date, time):
        self.id = event_id
        self.name = name
        self.date = date
        self.time = time
        self.venue = "Not Assigned"
        self.resources = []
        self.status = "Planning"

events = []
venues = []
resources = {}

# ---------------- Utility ----------------

def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None

# ---------------- Event ----------------

def create_event():
    print("\n--- Create Event ---")
    event_id = len(events) + 1
    name = input("Event Name : ")
    date = input("Date (DD/MM/YYYY): ")
    time = input("Time : ")

    events.append(Event(event_id, name, date, time))
    print("Event Created Successfully!")

def view_events():
    print("\n--- Event List ---")
    if not events:
        print("No Events Available.")
        return

    for event in events:
        print(f"""
ID      : {event.id}
Name    : {event.name}
Date    : {event.date}
Time    : {event.time}
Venue   : {event.venue}
Status  : {event.status}
-----------------------------""")

def update_event():
    view_events()
    if not events:
        return

    try:
        event_id = int(input("Enter Event ID : "))
    except:
        print("Invalid Input")
        return

    event = find_event(event_id)

    if event is None:
        print("Event Not Found")
        return

    event.name = input("New Name : ")
    event.date = input("New Date : ")
    event.time = input("New Time : ")

    print("Event Updated Successfully!")

def delete_event():
    view_events()
    if not events:
        return

    try:
        event_id = int(input("Enter Event ID : "))
    except:
        print("Invalid Input")
        return

    event = find_event(event_id)

    if event:
        events.remove(event)
        print("Event Deleted Successfully!")
    else:
        print("Event Not Found")

# ---------------- Venue ----------------

def add_venue():
    venue = input("Venue Name : ")

    if venue in venues:
        print("Venue Already Exists")
    else:
        venues.append(venue)
        print("Venue Added Successfully!")

def view_venues():
    print("\n--- Venue List ---")

    if not venues:
        print("No Venues Available.")
        return

    for i, venue in enumerate(venues, 1):
        print(i, ".", venue)

def assign_venue():
    view_events()
    if not events:
        return

    try:
        event_id = int(input("Event ID : "))
    except:
        print("Invalid Input")
        return

    event = find_event(event_id)

    if event is None:
        print("Event Not Found")
        return

    view_venues()

    if not venues:
        return

    try:
        choice = int(input("Venue Number : ")) - 1
        venue = venues[choice]
    except:
        print("Invalid Venue")
        return

    for e in events:
        if e.id != event.id and e.venue == venue and e.date == event.date and e.time == event.time:
            print("Scheduling Conflict! Venue already booked.")
            return

    event.venue = venue
    print("Venue Assigned Successfully!")

# ---------------- Resource ----------------

def add_resource():
    name = input("Resource Name : ")

    try:
        quantity = int(input("Quantity : "))
    except:
        print("Invalid Quantity")
        return

    resources[name] = resources.get(name, 0) + quantity
    print("Resource Added Successfully!")

def view_resources():
    print("\n--- Resources ---")

    if not resources:
        print("No Resources Available.")
        return

    for name, quantity in resources.items():
        print(f"{name} : {quantity}")

def allocate_resource():
    view_events()

    if not events:
        return

    try:
        event_id = int(input("Event ID : "))
    except:
        print("Invalid Input")
        return

    event = find_event(event_id)

    if event is None:
        print("Event Not Found")
        return

    view_resources()

    resource = input("Resource Name : ")

    if resource not in resources:
        print("Resource Not Found")
        return

    try:
        quantity = int(input("Required Quantity : "))
    except:
        print("Invalid Quantity")
        return

    if quantity > resources[resource]:
        print("Not Enough Resources")
        return

    resources[resource] -= quantity
    event.resources.append((resource, quantity))

    print("Resource Allocated Successfully!")

# ---------------- Report ----------------

def event_report():
    print("\n========== EVENT REPORT ==========")

    if not events:
        print("No Events Available.")
        return

    for event in events:
        print(f"""
Event ID : {event.id}
Name     : {event.name}
Date     : {event.date}
Time     : {event.time}
Venue    : {event.venue}
Status   : {event.status}
Resources:""")

        if not event.resources:
            print("  None")
        else:
            for r, q in event.resources:
                print(f"  {r} - {q}")

        print("----------------------------------")

# ---------------- Main Menu ----------------

while True:

    print("""
==============================
 EVENTSPHERE - MILESTONE 1
==============================
1. Create Event
2. View Events
3. Update Event
4. Delete Event
5. Add Venue
6. View Venues
7. Assign Venue
8. Add Resource
9. View Resources
10. Allocate Resource
11. Event Report
12. Exit
==============================
""")

    choice = input("Enter Choice : ")

    if choice == "1":
        create_event()

    elif choice == "2":
        view_events()

    elif choice == "3":
        update_event()

    elif choice == "4":
        delete_event()

    elif choice == "5":
        add_venue()

    elif choice == "6":
        view_venues()

    elif choice == "7":
        assign_venue()

    elif choice == "8":
        add_resource()

    elif choice == "9":
        view_resources()

    elif choice == "10":
        allocate_resource()

    elif choice == "11":
        event_report()

    elif choice == "12":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
