from django.shortcuts import render
from .forms import ReserveForm
# Create your views here.


def reserve(request):

    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReserveForm()
    return render(request, 'reservation/reservation.html', {'form':form})

def customer_detail(rquest):
    pass