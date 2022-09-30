from django.urls import path
from .views import home, newpost

urlpatterns = [
    path('', home, name='home'),
    path('newpost', newpost, name='newpost'),

]