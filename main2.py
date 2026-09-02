
"""
EventSphere - Milestone 2 Demo
Simple console application for teaching:
- Attendee Registration
- Ticket Generation
- Attendance
- Vendor Management
- Vendor Assignment
"""

class Event:
    def __init__(self, event_id, name):
        self.id = event_id
        self.name = name
        self.attendees = []
        self.vendors = []

class Attendee:
    def __init__(self, reg_id, name, email, phone, ticket_id):
        self.reg_id = reg_id
        self.name = name
        self.email = email
        self.phone = phone
        self.ticket_id = ticket_id
        self.status = "Registered"

class Vendor:
    def __init__(self, vendor_id, name, service):
        self.id = vendor_id
        self.name = name
        self.service = service

events = [Event(1,"AI Workshop"), Event(2,"Python Bootcamp")]
vendors = []
ticket_number = 1001

def find_event(event_id):
    for e in events:
        if e.id == event_id:
            return e
    return None

def find_vendor(vendor_id):
    for v in vendors:
        if v.id == vendor_id:
            return v
    return None

def view_events():
    print("\nEvents")
    for e in events:
        print(e.id, e.name)

def register_attendee():
    global ticket_number
    view_events()
    try:
        event = find_event(int(input("Event ID: ")))
    except:
        print("Invalid Input"); return
    if event is None:
        print("Event Not Found"); return
    reg=input("Registration ID: ")
    name=input("Name: ")
    email=input("Email: ")
    phone=input("Phone: ")
    for a in event.attendees:
        if a.email==email:
            print("Already Registered"); return
    ticket="TKT"+str(ticket_number)
    ticket_number+=1
    event.attendees.append(Attendee(reg,name,email,phone,ticket))
    print("Registration Successful")
    print("Ticket:",ticket)

def view_attendees():
    view_events()
    try:
        event=find_event(int(input("Event ID: ")))
    except:
        return
    if event is None:
        print("Event Not Found"); return
    if not event.attendees:
        print("No Registrations"); return
    for a in event.attendees:
        print(a.name,a.ticket_id,a.status)

def mark_attendance():
    view_events()
    try:
        event=find_event(int(input("Event ID: ")))
    except:
        return
    if event is None:
        print("Event Not Found"); return
    ticket=input("Ticket ID: ")
    for a in event.attendees:
        if a.ticket_id==ticket:
            a.status="Checked In"
            print("Attendance Updated")
            return
    print("Invalid Ticket")

def add_vendor():
    try:
        vid=int(input("Vendor ID: "))
    except:
        print("Invalid"); return
    vendors.append(Vendor(vid,input("Vendor Name: "),input("Service: ")))
    print("Vendor Added")

def view_vendors():
    if not vendors:
        print("No Vendors"); return
    for v in vendors:
        print(v.id,v.name,v.service)

def assign_vendor():
    view_events()
    try:
        event=find_event(int(input("Event ID: ")))
    except:
        return
    if event is None:
        print("Event Not Found"); return
    view_vendors()
    try:
        vendor=find_vendor(int(input("Vendor ID: ")))
    except:
        return
    if vendor is None:
        print("Vendor Not Found"); return
    event.vendors.append(vendor)
    print("Vendor Assigned")

def report():
    print("\nREPORT")
    for e in events:
        print("\nEvent:",e.name)
        print("Registrations:",len(e.attendees))
        checked=sum(1 for a in e.attendees if a.status=="Checked In")
        print("Checked In:",checked)
        print("Vendors:")
        if not e.vendors:
            print("None")
        else:
            for v in e.vendors:
                print("-",v.name,"(",v.service,")")

while True:
    print("""
===== EVENTSPHERE MILESTONE 2 =====
1.Register Attendee
2.View Attendees
3.Mark Attendance
4.Add Vendor
5.View Vendors
6.Assign Vendor
7.Report
8.Exit
""")
    ch=input("Choice: ")
    if ch=="1":
        register_attendee()
    elif ch=="2":
        view_attendees()
    elif ch=="3":
        mark_attendance()
    elif ch=="4":
        add_vendor()
    elif ch=="5":
        view_vendors()
    elif ch=="6":
        assign_vendor()
    elif ch=="7":
        report()
    elif ch=="8":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
