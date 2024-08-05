from django.contrib import admin
from lunchmenu.models import LunchMenu

# Register your models here.
@admin.register(LunchMenu)
class LunchMenuAdmin(admin.ModelAdmin):
    pass