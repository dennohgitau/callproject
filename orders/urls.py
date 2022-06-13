from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add_mofast', views.add_mofast, name="add_mofast"),
    path('add_2wtrade', views.add_2wtrade, name="add_2wtrade"),
    path('add_eglobal', views.add_eglobal, name="add_eglobal"),
    path('add_unateus', views.add_unateus, name="add_unateus"),
    path('add_halisi', views.add_halisi, name="add_halisi"),
    path('add_mainstream', views.add_mainstream, name="add_mainstream"),
    path('add_clinton', views.add_clinton, name="add_clinton"),
    path('add_ke', views.add_ke, name="add_ke"),
    path('add_adlat', views.add_adlat, name="add_adlat"),
    path('add_2b', views.add_2b, name="add_2b"),
    path('add_vital', views.add_vital, name="add_vital"),
    path('get_percentage_per_agent', views.get_percentage_per_agent, name="get_percentage_per_agent"),
    path('percentage_chart/', views.percentage_chart, name='percentage_chart'),



]

