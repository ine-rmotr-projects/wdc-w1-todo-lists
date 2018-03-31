from django.urls import path
from assignment_4.fixtures import views

urlpatterns = [path('', views.home_wrong_form, name='home'),
               path('list/new', views.new_list, name='new_list')]