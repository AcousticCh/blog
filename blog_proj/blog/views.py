from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.apps import apps
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from html_generator.models import HtmlModel



class HomeListView(ListView):
    def __init__(self):
        super().__init__()
        self.model = apps.get_model("html_generator", "HtmlModel")
        self.template_name = "index.html"
        self.context_object_name = 'latest_post_list'

    def get(self, request):
        search_string = request.GET.get("search")

        if search_string:
            filtered_list = HtmlModel.objects.filter(Q(title__icontains=search_string) | Q(description__icontains=search_string))
            context = { "filtered_list": filtered_list }
            return render(request, "search.html", context)
        else:
            context = { "latest_post_list": self.context_object_name }
            return render(request, "index.html", context)
        
    def get_queryset(self):
        """Return the last five published questions."""
        return HtmlModel.objects.order_by('-pk')[:5]

@login_required
def page_create_view(request):
    return HttpResponseRedirect(reverse("html_generator:html_gen"))

def page_view(request, slug):
    HtmlModel = apps.get_model("html_generator", "HtmlModel")
    html_object = get_object_or_404(HtmlModel,slug=slug)
    context = { "html_page": html_object.page }
    return render(request, "page.html", context)

def search_view(request):
    search_string = request.GET.get("search")

    if search_string:
        filtered_list = HtmlModel.objects.filter(Q(title__icontains=search_string) | Q(description__icontains=search_string))
        context = { "filtered_list": filtered_list }
        return render(request, "search.html", context)
    else:
        return HttpResponseRedirect(reverse("blog:index"))

