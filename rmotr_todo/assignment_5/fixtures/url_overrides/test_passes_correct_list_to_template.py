from django.urls import path
from assignment_5.fixtures import views

urlpatterns = [path('', views.home, name='home'),
               path('lists/new', views.new_list, name='new_list'),
               path('lists/<list_id>/', views.view_list_shows_wrong_list, name='view_list')]