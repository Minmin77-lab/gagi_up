from django.urls import path
from .views import page1, page2, page3, page4 

urlpatterns = [
    path('', page1, name='page1'),
    path('small/', page2, name='page2'),
    path('buy/', page4, name='page4'),
    path('logIn/', page3, name='page3'),
]