from django.urls import path
from .views import create, list

app_name = 'photolog'

urlpatterns = [
    path('create/', create , name="create"),
    path('list/', list , name="list"),
]
