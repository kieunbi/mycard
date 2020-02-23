"""card URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import cardapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cardapp.views.main, name="main"),
    path('card_recommend/',cardapp.views.card_recommend, name="card_recommend"),
    path('card_result/',cardapp.views.card_result, name="card_result"),
    path('board/',cardapp.views.board, name="board"),
    path('board_detail/<int:blog_id>',cardapp.views.board_detail, name="board_detail"),
    path('board_update/<int:blog_id>',cardapp.views.board_update, name="board_update"),
    path('board_delete/<int:blog_id>',cardapp.views.board_delete, name="board_delete"),
    path('search/',cardapp.views.search, name="search"),
    path('board_search_result/',cardapp.views.board_search_result, name="board_search_result"),
    path('board_write/',cardapp.views.board_write, name="board_write"),
    path('write_create/',cardapp.views.write_create, name="write_create")
]
