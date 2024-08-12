from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_view, name="blogs"),
    path("<int:id>/", views.blog_detail, name="blog_detail"),
    path("tag/<slug:tag>/", views.blog_tag, name="tag"),
    path("category/<slug:category>/", views.blog_category, name="category"),
    path("search/", views.search, name="search"),

]
