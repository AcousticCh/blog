from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# add descriptions to post models and place them in html post box instead of page

class MarkdownModel(models.Model):
    title = models.CharField(max_length=70, blank=True)
    body = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        return f"pk: {self.pk} | title: {self.title}"

class HtmlModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=True)
    page = models.CharField(max_length=8000)
    slug = models.SlugField(null=True)

    def __str__(self):
        return f"pk: {self.pk} | title: {self.title}"

    def get_absolute_url(self):
        return reverse("blog:page", kwargs={ "slug": self.slug})


# ADDED SLUG