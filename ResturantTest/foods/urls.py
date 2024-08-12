from django.urls import path
from .views import *

urlpatterns = [
    path('', FoodList, name='foods'),
    path('<int:id>/', FoodDetail, name='food'),
    path('menu/', menu_view, name='menu'),


]