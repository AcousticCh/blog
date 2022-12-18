from django.urls import path
from .views import HomeListView
from . import views

app_name = "blog"
urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("create/", views.page_create_view, name="create"),
    path("<str:page_id>/", views.page_view, name="page"),
]