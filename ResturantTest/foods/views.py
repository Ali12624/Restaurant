from django.shortcuts import render, get_object_or_404
from .models import Food
# Create your views here.

def FoodList(request):
    
    foods = Food.objects.all()
    context = {
        'foods':foods
    }
    return render(request, 'foods/index.html', context)

def FoodDetail(request, id):
    # food = get_object_or_404(Food, id=id)
    food = Food.objects.get(id=id)
    return render(request, 'foods/detail.html', context={'food':food})

def menu_view(request):
    menu = Food.objects.all()
    context = {'menu':menu}

    return render(request, 'foods/menu.html', context)