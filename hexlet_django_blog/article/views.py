from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

class RootView(View):

    def get(self, request):
        return render(request, 'course.html')


class TemplatePageView(TemplateView):

    template_name = 'base.html'


def index(request):
    return render(request, 'course.html')
