from django.urls import path
from . import views

urlpatterns = [ # 서버IP/
    path('', views.langing), # 서버IP/ #대문 페이지에 대한. langing->landing(me)
    path('about_me/', views.about_me) # 서버IP/about_me/
]