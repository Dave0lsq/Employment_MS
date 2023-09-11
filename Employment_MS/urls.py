"""
URL configuration for Employment_MS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from chatbot import views as chatviews
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', chatviews.chatbot, name='chatbot'),
    path('add_question/', chatviews.add_question, name='add_question'),
    # path('login/', chatviews.login, name='login'),
    # path('register/', chatviews.register, name='register'),
    # path('logout/', chatviews.logout, name='logout'),

    #Department Manage
    path('department/list/', views.depart_list),
    path('department/add/', views.depart_add),
    path('department/delete/', views.depart_delete),
    path('department/<int:nid>/edit/', views.depart_edit),

    #User Manage
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/delete/', views.user_delete),
    path('user/<int:nid>/edit/', views.user_edit),

    #School Manage
    path('school/list/', views.school_list),
    path('school/add/', views.school_add),
    path('school/<int:nid>/edit/', views.school_edit)

]
