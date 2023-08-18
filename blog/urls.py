from . import views
from django.urls import path

urlpatterns = [
    path("aktualnosci", views.PostList.as_view(), name="news"),
    path("aktualnosci/<slug:slug>/", views.PostDetail.as_view(), name="news_detail"),
]
