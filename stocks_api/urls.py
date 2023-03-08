from django.urls import path
from .views import InstitutionalHoldersView

urlpatterns = [
    path('api/institutional-holders/<str:ticker>/', InstitutionalHoldersView.as_view(), name='institutional-holders'),
]
