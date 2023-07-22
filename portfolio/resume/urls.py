
from django.urls import path
from .views import portfolio,home


urlpatterns = [
    path('portfolio/', portfolio, name='portfolio'),
    path("home/",home, name='home'),
]

