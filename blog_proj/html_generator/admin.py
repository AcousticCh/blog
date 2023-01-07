from django.contrib import admin
from .models import MarkdownModel, HtmlModel, TopicModel

admin.site.register(MarkdownModel)
admin.site.register(HtmlModel)
admin.site.register(TopicModel)
