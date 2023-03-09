from django.urls import path
from .views import InstitutionalHoldersAPIView

urlpatterns = [
    path('api/institutional-holders/', InstitutionalHoldersAPIView.as_view(), name='institutional-holders'),
    path('api/institutional-holders/<str:symbol>/', InstitutionalHoldersAPIView.as_view(), name='institutional-holders-symbol'),
]