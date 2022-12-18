from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.apps import apps



class HomeListView(ListView):
    model = apps.get_model("html_generator", "HtmlModel")
    template_name = "home.html"
    
def page_create_view(request):
    return HttpResponseRedirect(reverse("html_generator:html_gen"))
def page_view(request, page_id):

    HtmlModel = apps.get_model("html_generator", "HtmlModel")
    html_object = get_object_or_404(HtmlModel,pk=page_id)
    context = { "html_page": html_object.page }
    return render(request, "page.html", context)