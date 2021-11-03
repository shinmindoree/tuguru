from django.urls import path
from .views import ranking, tenbaggers, search, test


app_name = 'stockrankings'

urlpatterns = [
    path('ranking/', ranking, name="ranking"),
    path('tenbaggers/', tenbaggers, name="tenbaggers"),
    path('', search, name="search"),
    path('test', test, name="test"),
    
]