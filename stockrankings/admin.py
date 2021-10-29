from django.contrib import admin
from .models import Stockrankings, Tenbaggers

# Register your models here.
@admin.register(Stockrankings)
class PostAdmin(admin.ModelAdmin):
    list_display = ['stockname', 'marketcap']
    
