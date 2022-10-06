from django.urls import path
from . import views

urlpatterns = [
    path("<int:uTicketID>",views.tickets, name='ticket-detail'),
    path("",views.tIndex, name='tickets-overview')
]
