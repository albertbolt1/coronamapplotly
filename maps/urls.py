
from django.urls import path
from . import views
urlpatterns = [
    path('',views.some,name="default"),
]
