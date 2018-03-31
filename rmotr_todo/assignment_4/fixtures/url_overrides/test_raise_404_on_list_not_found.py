from django.urls import path
from assignment_4.fixtures import views

urlpatterns = [path('', views.home, name='home'),
               path('lists/new', views.new_list, name='new_list'),
               path('lists/<list_id>/', views.view_list_creates_new_on_404, name='view_list')]