from django.db import models
from core.models import CoreModel

class Review(CoreModel):

  """ Review Model """ 

  RATE_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
  )

  created_by = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
  text = models.TextField()
  movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
  book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
  rating = models.IntegerField(choices=RATE_CHOICES, default=5)

  def __str__(self):
    return self.text