from django.urls import path
from .views import PlaceView, CreatedPlaceView, DetailPlaceView


urlpatterns = [
    path('', PlaceView.as_view(), name='home'),
    path('created/', CreatedPlaceView.as_view(), name='created'),
    path('detail/<slug:detail_slug>', DetailPlaceView.as_view(), name='detail'),
]