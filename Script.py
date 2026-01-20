#Lecture du ticket json
import json
from collections import Counter
from datetime import date
with open('ticket.json', 'r') as file:
    ticket_data = json.load(file)

def StatusCount ():
    status_counts = Counter(ticket["status"] for ticket in ticket_data)
    return status_counts

def TicketFilter(value):
    liste_tag=[]
    for ligne in ticket_data:
        if value in ligne["tags"]: 
            liste_tag.append(ligne)
    return liste_tag

def TicketSort():
    groups = {}
    for ticket in ticket_data:
        status = ticket.get("status")
        if status not in groups:
            groups[status]=[]
        groups[status].append(ticket)
    return groups

def TicketAdd (ticket_data,title,description,priority,status,tags):
    Newticket={ id:"unknown",
               title: "title",
         description : "description",
         priority: "priority",
         status : "status",
         tags : "tags",
         "createdAt":str(date.today()) }
    Newticket["id"]= ticket_data[-1]["id"]+1
    ticket_data.append(Newticket)
    with open('ticket.json', 'w') as file:
        ticket_data = json.dump(ticket_data,file,indent=4)

    







