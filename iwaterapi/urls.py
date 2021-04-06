from django.urls import path
from .views import IwaterDriverView

app_name = "iwaterapi"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('driver/', IwaterDriverView.as_view()),
]
