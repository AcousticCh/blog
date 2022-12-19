from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MarkdownModel(models.Model):
    title = models.CharField(max_length=70, blank=True)
    body = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        return f"pk: {self.pk} | title: {self.title}"

class HtmlModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=True)
    page = models.CharField(max_length=8000)

    def __str__(self):
        return f"pk: {self.pk} | title: {self.title}"