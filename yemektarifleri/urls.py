from django.urls import path
from .views import hosgeldin, kayit_ol

urlpatterns = [
    path("kayit/", kayit_ol, name="kayit"),
    path("hosgeldin/", hosgeldin, name = "hosgeldin"),
]
