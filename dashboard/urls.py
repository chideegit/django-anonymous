from django.urls import path 
from .views import * 

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('leave-review/<str:username>/', leave_review, name='leave-review'),
    path('completed/', completed, name='completed')
]