from django.shortcuts import render, get_object_or_404
from .forms import MarkdownForm
from .models import HtmlModel
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown


def markdown_form_view(request):
    if str(request.method).upper() == "POST":

        if request.user.is_authenticated:
            form = MarkdownForm(request.POST)
            context = { "form": form }

            if form.is_valid():
                title = form.cleaned_data["title"]
                body = form.cleaned_data["body"]
                form.cleaned_data["slug"] = title
                form.save()

                page = f"# {title}\n{body}"

                html = markdown.markdown(page)

                
                html_object = HtmlModel.objects.create(author=, title=title, page=html)
                html_object.save()
                html_object.refresh_from_db()

                return HttpResponseRedirect(reverse("blog:page", args=[html_object.id]))


    else:
        form = MarkdownForm()
        context = { "form": form }
        return render(request, "page_form.html", context)

