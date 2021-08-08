from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
  path("create/<str:media_type>/<int:pk>", views.CreateReview.as_view(), name="create"),
  path("delete/<int:pk>", views.delete_review, name="delete"),
]
