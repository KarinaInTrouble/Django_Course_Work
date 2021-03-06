"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include,re_path
from dot_app import views

urlpatterns = [
    
    path('student/teachers/', views.student, name='student'),
    path('student/', views.departments, name='departments'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('siteadmin/',views.add_department, name="administration"),
    path('getbook/',views.give, name='getbook'),

    path('student/curriculum/',views.curr, name='curriculum'),
    re_path(r'^delete/(?P<id>\d+)/$',views.delete),
    re_path(r'^delete_1/(?P<id>\d+)/$',views.delete_1),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    
]