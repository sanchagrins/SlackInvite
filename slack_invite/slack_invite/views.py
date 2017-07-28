# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import InviteForm

def home(request):
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
    else:
        form = InviteForm()

    return render(request, "slack_invite/index.html", {'form': form})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
