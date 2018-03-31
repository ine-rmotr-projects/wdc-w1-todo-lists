from django.urls import path
from assignment_5.fixtures import views
from django.contrib.auth import views as auth_views

urlpatterns = [path('', views.home, name='home'),
               path('lists/new', views.new_list, name='new_list'),
               path('lists/<list_id>/', views.view_list_fake_form, name='view_list'),
               path('lists/<list_id>/item/<item_id>/delete', views.delete_item, name='delete_item'),
               path('login', auth_views.login, {'template_name': 'login.html'}, name='login'),]