from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('uslugi', views.Services.as_view(), name='services'),
    path('cennik', views.Prices.as_view(), name='prices'),
    path('floty', views.Fleets.as_view(), name='fleets'),
    path('kontakt', views.Contact.as_view(), name='contact'),
    path('onas', views.About.as_view(), name='about'),
    path('aktualnosci', views.PostList.as_view(), name='news'),
    path('aktualnosci/<slug:slug>/', views.PostDetail.as_view(), name='news_detail')
]