from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from reviews.models import Review
from movies.models import Movie
from books.models import Book


class CreateReview(LoginRequiredMixin, View):

    login_url = reverse_lazy("users:login")

    def post(self, *args, **kwargs):

        text = self.request.POST.get("text", None)
        rating = self.request.POST.get("rating", None)
        pk = kwargs.get("pk")
        media_type = kwargs.get("media_type")

        if text is not None and rating is not None:
            if media_type == "movie":
                media = Movie.objects.get_or_none(pk=pk)
                if media is not None:
                    Review.objects.create(
                        created_by=self.request.user, text=text, movie=media, book=None, rating=rating
                    )
                return redirect(reverse("movies:movie", kwargs={"pk": pk}))

            elif media_type == "book":
                media = Book.objects.get_or_none(pk=pk)
                if media is not None:
                    Review.objects.create(
                        created_by=self.request.user, text=text, movie=None, book=media, rating=rating
                    )
                return redirect(reverse("books:book", kwargs={"pk": pk}))

        return redirect(reverse("core:home"))


def delete_review(request, pk):
  
    review = Review.objects.get_or_none(pk=pk)

    if review is not None:
        review.delete()

    return redirect(reverse("core:home"))
