from django.shortcuts import render

# Create your views here.


def tickets(req, mTicketID):
    return render(req, "tickets/ticket.html", {"mTicketID": mTicketID})
