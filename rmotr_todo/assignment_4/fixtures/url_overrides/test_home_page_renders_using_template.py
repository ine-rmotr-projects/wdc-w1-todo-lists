from django.urls import path
from assignment_4.fixtures import views

urlpatterns = [path('', views.no_template, name='home')]