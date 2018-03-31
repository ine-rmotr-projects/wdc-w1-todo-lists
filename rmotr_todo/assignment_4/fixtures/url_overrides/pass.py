from django.urls import path
from assignment_4.fixtures import views

urlpatterns = [path('', views.home, name='home'),
               path('lists/new', views.new_list, name='new_list'),
               path('lists/<list_id>/', views.view_list, name='view_list'),
               path('lists/<list_id>/item/<item_id>/delete', views.delete_item, name='delete_item'),]