from django.urls import path
from .views import PlaceView, CreatedPlaceView


urlpatterns = [
    path('', PlaceView.as_view(), name='home'),
    path('created/', CreatedPlaceView.as_view(), name='created'),
]