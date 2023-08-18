from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("uslugi", views.Services.as_view(), name="services"),
    path("cennik", views.Prices.as_view(), name="prices"),
    path("floty", views.Fleets.as_view(), name="fleets"),
    path("kontakt", views.Contact.as_view(), name="contact"),
    path("onas", views.About.as_view(), name="about"),
]
