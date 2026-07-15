from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "website/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Ana Sayfa"

        return context