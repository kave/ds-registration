from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.base import View, ContextMixin
from django.views.generic import TemplateView
from core.forms import RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse


def home(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


class RegisterView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        pass

    def post(self, request):
        context = RequestContext(request)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')