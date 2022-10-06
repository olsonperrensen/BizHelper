from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Ticket
# Create your views here.


def tickets(req, uTicketID):
    uTicket = get_object_or_404(Ticket, mID=uTicketID)
    return render(req, "tickets/ticket.html", {
        "id": uTicket.mID,
        "type": uTicket.mType,
        "createdBy": uTicket.mCreatedBy,
        "date": uTicket.mDateOfCreation,
        "days": uTicket.mDaysPassed,
        "solved": uTicket.mSolved,
        "desc": uTicket.mComment, })


def tIndex(req):
    mCurrentTickets = Ticket.objects.all()
    return render(req, "tickets/tIndex.html", {"mCurrentTickets": mCurrentTickets})
