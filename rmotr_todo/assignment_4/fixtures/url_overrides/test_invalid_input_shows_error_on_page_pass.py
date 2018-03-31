from django.urls import path
from assignment_4.fixtures import views

urlpatterns = [path('', views.show_errors, name='home'),
               path('lists/new', views.show_errors, name='new_list'),
               path('lists/<list_id>/', views.show_errors, name='view_list')]