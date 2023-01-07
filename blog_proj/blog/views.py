from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from django.utils import timezone
from django.apps import apps
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import markdown




class HomeListView(ListView):
    def __init__(self):
        super().__init__()
        self.model = apps.get_model("html_generator", "HtmlModel")
        self.template_name = "index.html"

    def get(self, request):
        search_string = request.GET.get("search")

        HtmlModel = apps.get_model("html_generator", "HtmlModel")
        TopicModel = apps.get_model("html_generator", "TopicModel")

        topic_list = TopicModel.objects.all()

        if search_string:
            filtered_list = HtmlModel.objects.filter(Q(title__icontains=search_string) | Q(description__icontains=search_string))
            context = { "filtered_list": filtered_list, "topic_list": topic_list }
            return render(request, "search.html", context)
        else:
            recommended_list = get_list_or_404(HtmlModel, featured=True)
            lastest_list = HtmlModel.objects.order_by('-pub_date')[:4]
            context = { "topic_list": topic_list, "recommended_list": recommended_list, "latest_post_list": lastest_list }
            return render(request, "index.html", context)
        

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
        HtmlModel = apps.get_model("html_generator", "HtmlModel")
        filtered_list = HtmlModel.objects.filter(Q(title__icontains=search_string) | Q(description__icontains=search_string))
        context = { "filtered_list": filtered_list }
        return render(request, "search.html", context)
    else:
        return HttpResponseRedirect(reverse("blog:index"))

def topic_list_view(request, slug):
    TopicModel = apps.get_model("html_generator", "TopicModel")
    HtmlModel = apps.get_model("html_generator", "HtmlModel")

    topic_page = get_object_or_404(TopicModel, slug=slug)
    topic_pages = HtmlModel.objects.filter(topics__in=[topic_page])

    context = { "topic_pages": topic_pages }

    return render(request, "topic_list.html", context)

def create_test_pages(request):
    titles = ["test t1", "test t2", "test t3", "test t4", "test t5", "test t6"]
    descriptions = ["test d1", "test d2", "test d3", "test d4", "test d5", "test d6"]
    bodys = ["## test b1\n- testing\n- testing", "## test b2\n- testing\n- testing", "## test b3\n- testing\n- testing", "## test b4\n- testing\n- testing", "## test b5\n- testing\n- testing", "## test b6\n- testing\n- testing", ]
    
    for c in range(6):
        title = titles[c]
        description= descriptions[c]
        body = bodys[c]

        MarkdownModel = apps.get_model("html_generator", "MarkdownModel")
        md_object = MarkdownModel.objects.create(user=request.user, title=title, description=description, body=body, pub_date=timezone.now())
        md_object.save()
        md_object.refresh_from_db()
        page = f"# {title}\n{body}"

        slug = str(title).replace(" ", "_")

        html = markdown.markdown(page)

        HtmlModel = apps.get_model("html_generator", "HtmlModel")
        html_object = HtmlModel.objects.create(user=request.user, mdModel=md_object, title=title, description=description, page=html, slug=slug, pub_date=timezone.now())
        html_object.save()
        html_object.refresh_from_db()
    return HttpResponse("View Ran Successfully")

def create_test_topics(request):
    TopicModel = apps.get_model("html_generator", "TopicModel")
    HtmlModel = apps.get_model("html_generator", "HtmlModel")


    linux_topic = TopicModel.objects.create(title="Linux", slug="Linux")
    fast_api_topic = TopicModel.objects.create(title="Fast API", slug="Fast Api")
    django_topic = TopicModel.objects.create(title="Django", slug="Django")

    linux_topic.save()
    fast_api_topic.save()
    django_topic.save()

    linux_topic.refresh_from_db()
    fast_api_topic.refresh_from_db()
    django_topic.refresh_from_db()

    page = get_object_or_404(HtmlModel, pk=1)

    page.topics.add(linux_topic, django_topic)

    return HttpResponse("View Ran Successfully")

