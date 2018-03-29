from django.urls import path
from assignment_2.fixtures import views_pass

urlpatterns = [path('', views_pass.home, name='home'),
               path('/newlist', views_pass.home, name='new_list')]