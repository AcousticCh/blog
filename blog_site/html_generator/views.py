from django.shortcuts import render, get_object_or_404
from .forms import MarkdownForm
from .models import HtmlModel, MarkdownModel
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils import timezone

User = get_user_model()

@login_required
def markdown_form_view(request):
    if str(request.method).upper() == "POST":

        if request.user.is_authenticated:
            form = MarkdownForm(request.POST)
            context = { "form": form }

            if form.is_valid():
                form.instance.user = request.user
                form.instance.pub_date = timezone.now()
                title = form.cleaned_data["title"]
                description = form.cleaned_data["description"]
                body = form.cleaned_data["body"]
                form.save()


                page = f"# {title}\n{body}"
                slug = str(title).replace(" ", "_")

                html = markdown.markdown(page, extensions=["fenced_code"])

                md = get_object_or_404(MarkdownModel, title=title)

                html_object = HtmlModel.objects.create(user=request.user, mdModel=md, title=title, description=description, page=html, slug=slug, pub_date = timezone.now())
                html_object.save()
                html_object.refresh_from_db()

                return HttpResponseRedirect(reverse("blog:page", kwargs={ "slug": html_object.slug}))


    else:
        form = MarkdownForm()
        context = { "form": form }
        return render(request, "markdown_form.html", context)

