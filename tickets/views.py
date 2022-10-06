from django.shortcuts import render
from django.http import Http404
from .models import Ticket
# Create your views here.


def tickets(req, uTicketID):
    try:
        uTicket = Ticket.objects.get(mID=uTicketID)
        return render(req, "tickets/ticket.html", {
            "id": uTicket.mID,
            "type": uTicket.mType,
            "createdBy": uTicket.mCreatedBy,
            "date": uTicket.mDateOfCreation,
            "days": uTicket.mDaysPassed,
            "solved": uTicket.mSolved,
            "desc": uTicket.mComment, })
    except:
        raise Http404()


def tIndex(req):
    mCurrentTickets = Ticket.objects.all()
    return render(req, "tickets/tIndex.html", {"mCurrentTickets": mCurrentTickets})
