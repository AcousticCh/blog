from django import forms
from . import models

class MarkdownForm(forms.ModelForm):

    class Meta:
        model = models.MarkdownModel
        fields = ["title", "body"]
        widgets = {
            "body": forms.Textarea(attrs={"cols": 80, "rows": 30}),
        }
        