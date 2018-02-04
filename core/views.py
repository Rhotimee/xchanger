from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.conf import settings


def IndexView(request):
    if request.user.is_authenticated():
        return render(request, 'core/dashboard.html')
    else:
        return render(request, 'index.html')
