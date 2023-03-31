from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<month>",views.challenges_text,name="monthly-challenge"),
]