from .models import Post
from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "news.html"
    paginate_by = 5


class PostDetail(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "news_detail.html"
