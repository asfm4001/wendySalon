from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("", views.index, name='index'),
]