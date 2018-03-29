from django.urls import path
from assignment_2.fixtures import views

urlpatterns = [path('', views.home, name='home'),
               path('lists/new', views.new_list, name='new_list'),
               path('lists/<list_id>/', views.view_list_doesnt_add_items, name='view_list')]