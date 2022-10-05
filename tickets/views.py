from django.shortcuts import render
from django.http import Http404
# Create your views here.

mTickets = [2, 147, 483, 647]


def tickets(req, uTicketID):
    try:
        if (uTicketID in mTickets):
            mTicketID = uTicketID
        return render(req, "tickets/ticket.html", {"mTicketID": mTicketID})
    except:
        raise Http404()
