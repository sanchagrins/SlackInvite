# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import InviteForm
from . import config 

def home(request):
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email_addr']
            url = 'https://' + config.slack_url + '/api/users.admin.invite'
            form = {'email' : email, 'token' : config.slack_token,
                    'set_active' : 'true'}
            r = requests.post(url, data=form)
            return HttpResponseRedirect('/thanks')
    else:
        form = InviteForm()
        community = config.slack_team
    return render(request, "slack_invite/index.html", {'form': form, 'community': community})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def thanks(request):
    community = config.slack_team
    return render(request, "slack_invite/thanks.html", {'community': community})

def handler404(request):
    reponse = render_to_response('404.html', {},
            context_instance=RequestContext(request))
    reponse.status_code = 404
    return reponse
