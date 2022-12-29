from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.apps import apps
from django.contrib.auth.decorators import login_required



class HomeListView(ListView):
    model = apps.get_model("html_generator", "HtmlModel")
    template_name = "index.html"

@login_required
def page_create_view(request):
    return HttpResponseRedirect(reverse("html_generator:html_gen"))

def page_view(request, slug):
    HtmlModel = apps.get_model("html_generator", "HtmlModel")
    html_object = get_object_or_404(HtmlModel,slug=slug)
    context = { "html_page": html_object.page }
    return render(request, "page.html", context)