from django.urls import path
from .views import home
    # , RememberView


urlpatterns = [
    path('', home, name='home'),
    # path('', RememberView.as_view(), name='home'),
]