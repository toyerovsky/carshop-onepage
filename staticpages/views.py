from django.views import generic

# Create your views here.


class Index(generic.TemplateView):
    template_name = "index.html"


class Services(generic.TemplateView):
    template_name = "services.html"


class Prices(generic.TemplateView):
    template_name = "prices.html"


class Fleets(generic.TemplateView):
    template_name = "fleets.html"


class About(generic.TemplateView):
    template_name = "about.html"
