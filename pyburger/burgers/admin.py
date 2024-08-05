from django.contrib import admin

from burgers.models import Burger


# Register your models here.

# 관리자 계정 설정
# python manage.py createsuperuser
# http://localhost:8000/admin


@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass
