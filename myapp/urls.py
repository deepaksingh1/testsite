from django.urls import path
from . import views

urlpatterns=[

    path('', views.index, name='home'),
    #path('temp/', views.IndexView.as_view(), name='index'),
    #path('school_list/', views.SchoolListView.as_view(), name='school_list'),
]
