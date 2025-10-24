from django.urls import path
from .views import page1, page2, page3

urlpatterns = [
    path('', page1),
    path('small', page2),
    path('big', page3),
    
]