from django.urls import path
from assignment_3.fixtures import views

urlpatterns = [path('', views.no_template, name='home'),
               path('list/new', views.no_template, name='new_list'),
               path('lists/<list_id>/', views.no_template, name='view_list')]