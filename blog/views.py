from django.shortcuts import render
from .models import Post
from django.views import generic


# Create your views here.

class Index(generic.TemplateView):
    template_name = 'index.html'


class Services(generic.TemplateView):
    template_name = 'services.html'


class Prices(generic.TemplateView):
    template_name = 'prices.html'


class Fleets(generic.TemplateView):
    template_name = 'fleets.html'


class About(generic.TemplateView):
    template_name = 'about.html'


class Contact(generic.TemplateView):
    template_name = 'contact.html'


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'
    paginate_by = 5


class PostDetail(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'news_detail.html'
