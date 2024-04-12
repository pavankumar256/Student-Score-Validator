from django.urls import path

from studentscorevalidatorapp import views

urlpatterns = [
    path("",views.home),
    path("display",views.display_fun)
]