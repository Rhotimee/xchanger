from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.conf import settings

from .forms import ProfileForm, UserForm


def index_view(request):
    if request.user.is_authenticated():
        return render(request, 'core/dashboard.html')
    else:
        return render(request, 'index.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.dashboard)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect('/')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.dashboard)
    return render(request, 'core/update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
