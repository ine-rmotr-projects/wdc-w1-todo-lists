from django.urls import path
from assignment_4.fixtures import views

urlpatterns = [path('', views.home, name='home'),
               path('lists/new', views.new_list_redirects_home, name='new_list'),
               path('lists/<list_id>/', views.view_list, name='view_list')]