from django.shortcuts import render, get_object_or_404
from .forms import MarkdownForm
from .models import HtmlModel, MarkdownModel
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown
from django.contrib.auth import get_user_model

User = get_user_model()


def markdown_form_view(request):
    if str(request.method).upper() == "POST":

        if request.user.is_authenticated:
            form = MarkdownForm(request.POST)
            context = { "form": form }

            if form.is_valid():
                title = form.cleaned_data["title"]
                body = form.cleaned_data["body"]
                form.save()

                page = f"# {title}\n{body}"

                html = markdown.markdown(page)

                
                html_object = HtmlModel.objects.create(user=request.user, title=title, page=html)
                html_object.save()
                html_object.refresh_from_db()

                return HttpResponseRedirect(reverse("blog:page", args=[html_object.id]))


    else:
        form = MarkdownForm()
        context = { "form": form }
        return render(request, "page_form.html", context)

