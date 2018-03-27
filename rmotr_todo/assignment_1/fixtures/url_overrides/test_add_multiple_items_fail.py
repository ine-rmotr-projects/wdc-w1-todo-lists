from django.urls import path
from assignment_1.fixtures import views_fail

urlpatterns = [path('', views_fail.home, name='home')]