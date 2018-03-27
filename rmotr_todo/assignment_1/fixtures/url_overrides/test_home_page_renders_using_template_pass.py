from django.urls import path
from assignment_1.fixtures import views_pass

urlpatterns = [path('', views_pass.home, name='home')]