from django.urls import path
from . import views


urlpatterns = [
    path('', views.data_list, name='data_list'), # URL for the data list view
]