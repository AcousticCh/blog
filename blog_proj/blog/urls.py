from django.urls import path
from .views import HomeListView
from . import views

app_name = "blog"
urlpatterns = [
    path("create_test/", views.create_test_pages, name="create_test"),
    path("", HomeListView.as_view(), name="home"),
    path("create/", views.page_create_view, name="create"),
    path("<slug:slug>/", views.page_view, name="page"),
    path("search/", views.search_view, name="search"),
]
# PAGE ID CHANGED TO SLUG