from django.shortcuts import render
from django.http import Http404
from .models import Ticket
# Create your views here.

mTickets = [2, 147, 483, 647]


def tickets(req, uTicketID):
    try:
        if (uTicketID in mTickets):
            mTicketID = uTicketID
        return render(req, "tickets/ticket.html", {"mTicketID": mTicketID})
    except:
        raise Http404()

def tIndex(req):
    mCurrentTickets = Ticket.objects.all()
    return render(req,"tickets/tIndex.html")