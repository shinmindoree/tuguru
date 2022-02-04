from django.urls import path
from .views import ranking, tenbaggers, detail, comment_create, test

app_name = 'stockrankings'

urlpatterns = [
    path('ranking/', ranking, name="ranking"),
    path('tenbaggers/', tenbaggers, name="tenbaggers"),
    # path('', search, name="search"),
    path('<str:ticker>/', detail, name="detail"),
    path('<str:ticker>/comment_create/', comment_create, name="comment_create"),
    path('testhtml', test, name="test"),
    
]
