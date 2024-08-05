"""
URL configuration for pyburger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pyburger.views import main, main2, burger_list, lunch_list, burger_search

urlpatterns = [
    path('admin/', admin.site.urls),
    # main 이라는 건, views(컨트롤러 역할), main 함수를 의미함
    path('main/', main),
    path('main2/', main2),
    #목록 요소 조회 추가.
    path('list/', burger_list),

#목록 요소 조회 추가.
    path('lunchList/', lunch_list),

    #검색 화면 라우팅.
    path('search/', burger_search),
]
