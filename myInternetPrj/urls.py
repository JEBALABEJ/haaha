"""myInternetPrj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('blog/', include('blog.urls')), # 서버 IP/blog
    path('admin/', admin.site.urls),    # 서버IP/admin #두번째 인수를 지우고면, Page not found(404) 오류. url에 대한 함수가 없으니까(me)
    path('', include('single_pages.urls')), # 서버IP/ #프로젝트이면 서버 구동하자마자 볼 수 있는 페이지 그 자체.(me)
    path('accounts/', include('allauth.urls')),
    path('markdownx/', include('markdownx.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # 서버 IP/media/ #settings.py에 있는 MEDIA_URL(me)
                                        #document_root 매개변수가 다음이다. 좀 더 정확하게 표현 해주기 위해 docume...(me)


